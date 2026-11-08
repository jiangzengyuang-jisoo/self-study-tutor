# Self-Study Tutor · 自学导师

**一个知识点一个知识点地学，在新题目和新情境中独立运用。**

**Learn step by step. Apply what you know in unfamiliar problems and situations.**

[中文](#中文) · [English](#english)

## 中文

Self-Study Tutor 是一个面向自主学习的 AI 教学 skill。它围绕两个目标组织教学：**把知识点拆开讲清楚，以及帮助你从陌生题目中识别应该使用的知识与方法。**

如果你经常“看讲解能懂，自己做却不知道从哪开始”，它会针对这个过程安排示范、练习和反馈：观察什么关系、怎样改写题目、为什么选择这个方法，以及什么条件下需要换一种思路。

### 开始使用

把下面的网址复制给你的 agent，让它读取并使用这个 skill，再告诉它你想学什么：

```text
https://github.com/jiangzengyuang-jisoo/self-study-tutor
```

读取与使用由 agent 根据当前环境支持的方式处理。

### 它怎样教

- **一个知识点一个知识点推进。** 大任务先给简短路线，从必要的单元开始；已会的部分快速通过，卡住时补对应的前置知识。
- **教你怎样想到方法。** 连接题目线索、隐藏结构、适用条件和第一步；通过变形、条件对比和混合任务，练习自己选择与比较方法。
- **根据错误改变教学。** 区分概念不懂、没想到方法、不会整理题目和执行出错，采用对应的解释、示范或练习。
- **提供支持，再逐步交还任务。** 零基础先解释，必要时完整示范；随后逐步减少帮助，让你完成关键判断和实际任务。
- **用实际表现判断进展。** 分清看懂、提示下完成、独立完成和间隔后仍能完成；结合主动回忆、自己的讲解与新任务安排复习。

你可以随时要求只给提示、直接给完整答案、跳过或停止。教学跟随你指定的语言；继续学习时，使用当前对话或可用学习记录中的实际证据。

### 跨学科应用

不同任务采用相应的教学方式和评价标准：

| 学习任务 | 重点训练 |
| --- | --- |
| 数学 | 识别结构、完成变形、检查条件，并独立选法求解 |
| 经济学 | 从情境提取变量与假设，选择模型并解释因果关系 |
| 会计 | 根据业务实质判断账户、确认时点与报表影响 |
| 论证与阅读 | 区分材料和推断，让证据支持恰当范围的主张 |
| 语言 | 根据沟通对象、目的和语境，独立组织表达 |
| 编程与操作 | 根据要求形成方案，实际执行、调试并检查结果 |

### 可以这样开始学

> 我想学这一章，请一个知识点一个知识点地教，根据我的回答决定下一步。

> 我记得公式，但题目一变就不知道怎么用。请教我应该观察什么，再让我自己判断。

> 我会画供需图，但文字题总判断错。请根据我的解释找出卡点。

> 帮我检查这段论证的证据是否足够，让我自己修改关键部分。

> 我看得懂英语，但说不出来。请用具体情境带我练表达。

### 当前验证

已完成覆盖六类学科的首轮行为检查，并在两个场景比较了默认模型、简短提示、旧版与改版。检查记录见[评测报告](evals/results/2026-11-09/REPORT.md)；目前尚未证明稳定优于旧版或简短提示，也未验证真人学习增益。

## English

Self-Study Tutor is an AI skill for independent learning. It focuses on two goals: **teaching one meaningful unit at a time, and helping you recognize which concepts or methods to use in an unfamiliar task.**

If you understand explanations but struggle to begin on your own, the tutor works on that gap: what relationships to notice, how to represent the task, why an approach fits, and when its conditions require a different choice.

### Get started

Copy this URL to your agent, ask it to read and use the skill, and tell it what you want to learn:

```text
https://github.com/jiangzengyuang-jisoo/self-study-tutor
```

Your agent handles reading and using the skill through the capabilities its environment supports.

### How it teaches

- **Progress one useful unit at a time.** Start with a short route, move quickly through demonstrated skills, and repair missing prerequisites where needed.
- **Learn how an approach comes to mind.** Connect visible clues, hidden relationships, conditions, and the first step. Practise selecting and comparing approaches through changed representations, contrasting conditions, and mixed tasks.
- **Adapt to the reason for an error.** Distinguish missing concepts, missed approaches, difficulty reorganizing a task, and execution mistakes; choose feedback accordingly.
- **Provide support, then hand back responsibility.** Explain unfamiliar ideas and demonstrate when needed, then gradually let you make the key decisions and complete the task.
- **Use performance as evidence.** Distinguish understanding an explanation, assisted completion, independent performance, and retention. Use recall, learner explanations, and new tasks to guide review.

You can request a hint, a full answer, a skip, or an end to the session at any time. The tutor follows your preferred language and uses evidence from the current conversation or accessible learning records when continuing.

### Across subjects

Tasks and assessment criteria adapt to the subject:

| Learning task | Focus |
| --- | --- |
| Mathematics | Recognize structure, transform expressions, check conditions, and choose and execute a method |
| Economics | Identify variables and assumptions, select a model, and explain causal relationships |
| Accounting | Interpret the transaction, recognition timing, accounts, and financial statement effects |
| Argument and reading | Separate evidence from inference and match the scope of a claim to its support |
| Language | Produce appropriate expressions for an audience, purpose, and context |
| Programming and procedures | Develop an approach, implement it, debug, and verify the result |

### Example requests

> Teach me this chapter one useful unit at a time, and choose the next step based on my answers.

> I remember the formula but cannot recognize when to use it in a changed problem. Help me learn what to notice, then let me decide.

> I can draw supply and demand curves but misread word problems. Use my explanation to find where I go wrong.

> Help me check whether this paragraph has enough evidence, then let me revise the key part.

> I understand English when I read it but struggle to speak. Help me practise with concrete situations.

### Current evidence

Initial behavioral checks cover six subject areas, with default-model, short-prompt, previous-skill, and revised-skill comparisons on two scenarios. See the [evaluation report](evals/results/2026-11-09/REPORT.md). Stable superiority over the previous skill or a short prompt, and improvements in human learning, have not yet been established.

## 设计参考 · Design references

本项目借鉴以下流程设计，教学规则与示例按本项目目标编写。The following projects informed the workflow; the teaching rules and examples are written for this project.

- [Think Before Code](https://github.com/Far-200/think-before-code) — 结构提取与迁移 / structure and transfer.
- [Course Creator](https://github.com/ShivamGupta42/course-creator) — 方法线索与选择练习 / selection cues and practice.
- [LearnLM-Inspired Tutor](https://github.com/unix2dos/skills/tree/main/learnlm-inspired-tutor) — 先修关系与教学调整 / prerequisites and adaptive teaching.
- [Book Tutor](https://github.com/xixiaofinland/agent-skills/tree/main/skills/book-tutor) — 课程材料与进度衔接 / course materials and continuity.
