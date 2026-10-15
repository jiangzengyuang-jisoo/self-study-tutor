# Self-Study Tutor

An adaptive tutoring skill for independent understanding, method selection, retention, and transfer to unfamiliar problems.

The tutor can explain and demonstrate when prerequisites are missing, then gradually reduce assistance. It distinguishes following an explanation from solving a new problem independently.

## What it does

- Builds foundations with concrete explanations and worked examples.
- Teaches how to select a method, why it works, and when it stops applying.
- Gives graded hints without turning every task into a sequence of leading questions.
- Supports guided practice, independent assessment, review, and direct explanations.
- Uses learner explanations, new problems, and delayed checks as separate sources of evidence.
- Respects requests for an answer, a different mode, or an end to the session.

## Use

Install this repository folder through your agent's supported skill installer or configured local skill directory. Keep `SKILL.md` and `references/` together. The optional `agents/openai.yaml` provides interface metadata for hosts that support it.

Where the host supports named skill invocation, use:

```text
Use $self-study-tutor to help me understand derivatives from the beginning.
```

Where automatic skill selection is supported and enabled, ordinary learning requests can also match the skill description:

```text
Teach me this concept from scratch.
Give me one hint, then let me try the next step.
Test whether I can choose a method without being told which one to use.
Help me review what I studied last week.
```

The skill follows the learner's preferred language or the language of the conversation. Its instruction documents are written in Chinese; this does not require Chinese teaching responses. No particular school, curriculum, model, operating system, memory system, or external service is required by the tutoring workflow. Actual file access, persistence, reminders, and skill discovery depend on the host.

## Files

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Scope, mode selection, tutoring loop, and mastery evidence |
| [references/assessment-and-review.md](references/assessment-and-review.md) | Assessment, scoring, transfer practice, and delayed review |
| [agents/openai.yaml](agents/openai.yaml) | Optional interface metadata |

## Assessment boundaries

Receiving a hint, confirming a method, or immediately repeating a demonstrated solution does not count as an unaided result. During an assessment, a learner can request help; the tutor then marks that item as assisted practice before providing it.

This is an instruction-based workflow, not a proctoring system or a guarantee of improved grades. Reported timing, closed-book conditions, and learning outcomes should be limited to the evidence actually available.

## 中文简介

自学导师帮助学习者从必要示范逐步过渡到独立选择方法和解决问题，支持分级提示、费曼讲解、无提示检测、迁移训练与延迟复习。教学语言跟随学习者；普通查事实、索取答案或制作资料不会被强行转成教学。完整规则见 [SKILL.md](SKILL.md)。
