#!/usr/bin/env python3
"""Validate eval fixture structure, not tutoring behavior or learning efficacy."""

import argparse
from collections import Counter
import json
from pathlib import Path
import sys


TASK_FAMILIES = {
    "formal_quantitative", "mechanistic_explanation", "empirical_inquiry",
    "textual_argument", "language_communication", "design_implementation",
    "creative_performance", "learning_orientation",
}
LEARNER_STARTS = {"novice", "partial", "practiced", "unknown"}
COVERAGE = {
    "unit_progression", "diagnosis", "transfer", "unlabeled_selection",
    "user_control", "continuity", "beginner_entry", "unclear_goal",
    "task_adaptation", "evidence_limits", "source_grounding", "open_ended",
}
REVIEW_FIELDS = {
    "expected_behaviors", "unacceptable_behaviors", "reference_checks",
    "alternative_valid_approaches", "independence_notes",
}


class FixtureError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise FixtureError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"重复 JSON 键：{key}")
        result[key] = value
    return result


def object_keys(value, keys, location):
    require(isinstance(value, dict), f"{location} 必须是对象")
    require(set(value) == keys, f"{location} 字段应为 {sorted(keys)}")


def nonempty_text(value, location):
    require(isinstance(value, str) and bool(value.strip()), f"{location} 必须是非空文本")


def text_list(value, location):
    require(isinstance(value, list) and bool(value), f"{location} 必须是非空列表")
    for index, item in enumerate(value):
        nonempty_text(item, f"{location}[{index}]")


def validate(data):
    object_keys(data, {"schema_version", "purpose", "visibility", "cases"}, "root")
    require(type(data["schema_version"]) is int and data["schema_version"] == 2,
            "schema_version 必须为整数 2")
    nonempty_text(data["purpose"], "purpose")
    nonempty_text(data["visibility"], "visibility")
    cases = data["cases"]
    require(isinstance(cases, list) and bool(cases), "cases 必须是非空列表")
    ids = set()
    covered = set()
    domain_counts = Counter()
    family_counts = Counter()
    start_counts = Counter()
    held_out = []
    for index, case in enumerate(cases):
        location = f"cases[{index}]"
        object_keys(case, {"id", "domain", "task_families", "learner_start", "coverage", "held_out_from_runtime_examples",
                           "tutor_visible", "reviewer_only"}, location)
        nonempty_text(case["id"], location + ".id")
        require(case["id"] not in ids, f"重复案例 id：{case['id']}")
        ids.add(case["id"])
        nonempty_text(case["domain"], location + ".domain")
        # Domain names are intentionally open: adding a subject needs no whitelist edit.
        text_list(case["task_families"], location + ".task_families")
        require(len(set(case["task_families"])) == len(case["task_families"]),
                f"{location}.task_families 不应重复")
        require(set(case["task_families"]) <= TASK_FAMILIES,
                f"{location}.task_families 含未知标签")
        family_counts.update(case["task_families"])
        nonempty_text(case["learner_start"], location + ".learner_start")
        require(case["learner_start"] in LEARNER_STARTS,
                f"{location}.learner_start 含未知标签")
        start_counts[case["learner_start"]] += 1
        domain_counts[case["domain"]] += 1
        text_list(case["coverage"], location + ".coverage")
        require(len(set(case["coverage"])) == len(case["coverage"]),
                f"{location}.coverage 不应重复")
        require(set(case["coverage"]) <= COVERAGE, f"{location}.coverage 含未知标签")
        covered.update(case["coverage"])
        require(type(case["held_out_from_runtime_examples"]) is bool,
                f"{location}.held_out_from_runtime_examples 必须是布尔值")
        if case["held_out_from_runtime_examples"]:
            held_out.append(case)

        tutor = case["tutor_visible"]
        object_keys(tutor, {"initial_user", "followups"}, location + ".tutor_visible")
        nonempty_text(tutor["initial_user"], location + ".tutor_visible.initial_user")
        require(isinstance(tutor["followups"], list), f"{location}.followups 必须是列表")
        for turn, followup in enumerate(tutor["followups"]):
            turn_location = f"{location}.followups[{turn}]"
            object_keys(followup, {"user", "send_when"}, turn_location)
            nonempty_text(followup["user"], turn_location + ".user")
            nonempty_text(followup["send_when"], turn_location + ".send_when")

        reviewer = case["reviewer_only"]
        object_keys(reviewer, REVIEW_FIELDS, location + ".reviewer_only")
        for field in sorted(REVIEW_FIELDS):
            text_list(reviewer[field], location + ".reviewer_only." + field)

    require(covered == COVERAGE, f"缺少覆盖标签：{sorted(COVERAGE - covered)}")
    require(set(family_counts) == TASK_FAMILIES,
            f"缺少任务类型：{sorted(TASK_FAMILIES - set(family_counts))}")
    require(set(start_counts) == LEARNER_STARTS,
            f"缺少学习起点：{sorted(LEARNER_STARTS - set(start_counts))}")
    require(bool(held_out), "应有标记为运行时没有具体教学示例的案例")
    require(any("beginner_entry" in case["coverage"] and "unclear_goal" in case["coverage"]
                for case in cases), "应有零基础且目标未明确的启动案例")
    require(any("evidence_limits" in case["coverage"] for case in held_out),
            "示例外案例应包含观察证据限制的检查")
    return cases, domain_counts, covered, held_out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, default=Path(__file__).with_name("cases.json"))
    parser.add_argument("--case", help="只打印此案例的当前学生消息，不打印评审字段")
    parser.add_argument("--followup", type=int, help="与 --case 配合，后续消息从 1 开始编号")
    args = parser.parse_args()
    if args.followup is not None and args.case is None:
        parser.error("--followup 需要 --case")
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        cases, counts, covered, held_out = validate(data)
        if args.case is not None:
            matches = [case for case in cases if case["id"] == args.case]
            require(bool(matches), f"未知案例：{args.case}")
            tutor = matches[0]["tutor_visible"]
            if args.followup is None:
                print(tutor["initial_user"])
            else:
                require(1 <= args.followup <= len(tutor["followups"]),
                        "后续消息编号超出范围")
                print(tutor["followups"][args.followup - 1]["user"])
        else:
            print("结构检查通过；不代表教学行为或学习效果通过。")
            print(f"案例数：{len(cases)}")
            print("学科分布：" + ", ".join(f"{key}={counts[key]}" for key in sorted(counts)))
            print("覆盖标签：" + ", ".join(sorted(covered)))
            families = Counter(family for case in cases for family in case["task_families"])
            starts = Counter(case["learner_start"] for case in cases)
            print("任务分布：" + ", ".join(f"{key}={families[key]}" for key in sorted(families)))
            print("学习起点：" + ", ".join(f"{key}={starts[key]}" for key in sorted(starts)))
            print("运行时示例外标签：" + ", ".join(case["id"] for case in held_out))
            print("仍需人工核查参考答案、运行时示例划分、上下文隔离及实际行为。")
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, FixtureError) as error:
        print(f"结构检查失败：{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
