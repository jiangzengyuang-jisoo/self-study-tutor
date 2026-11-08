# Self-Study Tutor · 自学导师

**一个知识点一个知识点地学，在新题目和新情境中独立运用。**

**Learn step by step. Apply what you know in unfamiliar problems and situations.**

[中文](#中文) · [English](#english)

## 中文

Self-Study Tutor 是一个面向不同学科、不同基础的 AI 教学 skill。它围绕两个目标组织教学：**把知识点拆开讲清楚，以及帮助你从陌生任务中识别并运用合适的知识、方法与证据。**

如果你经常“看讲解能懂，自己做却不知道从哪开始”，它会针对这个过程安排示范、练习和反馈：观察什么关系、怎样改写题目、为什么选择这个方法，以及什么条件下需要换一种思路。

### 开始使用

把下面的网址复制给你的 agent，让它读取并使用这个 skill。你可以带着教材或题目来，也可以只说“我完全不会，带我从头学”：

```text
https://github.com/jiangzengyuang-jisoo/self-study-tutor
```

读取与使用由 agent 根据当前环境支持的方式处理。

### 它怎样教

- **不知道怎么学，也能开始。** 导师先提出一个可调整的小起点，解释并示范，再从你的表现了解基础。你无需先选章节、方法或制定学习计划；方向可以在体验后逐渐确定。
- **一个知识点一个知识点推进。** 大任务先给简短路线，从必要的单元开始；已会的部分快速通过，卡住时补对应的前置知识。
- **教你怎样想到方法。** 连接题目线索、隐藏结构、适用条件和第一步；通过变形、条件对比和混合任务，练习自己选择与比较方法。
- **根据错误改变教学。** 区分概念不懂、没想到方法、不会整理题目和执行出错，采用对应的解释、示范或练习。
- **提供支持，再逐步交还任务。** 零基础先解释，必要时完整示范；随后逐步减少帮助，让你完成关键判断和实际任务。
- **用实际表现判断进展。** 分清看懂、提示下完成、独立完成和间隔后仍能完成；结合主动回忆、自己的讲解与新任务安排复习。

你可以随时要求只给提示、直接给完整答案、跳过或停止。教学跟随你指定的语言；继续学习时，使用当前对话或可用学习记录中的实际证据。

### 跨学科应用

根据学科、课程材料和当前任务选择教学方式。同一门学科可以有计算、实验、材料分析和表达等不同任务。下面是适配示例，不是支持范围白名单：

| 学习任务 | 重点训练 |
| --- | --- |
| 数学、统计与定量推理 | 识别结构、转换表示、检查条件，完成求解或证明 |
| 物理、经济与工程建模 | 明确对象、变量、假设和边界，选模型并检查解释 |
| 化学、生物与机制解释 | 联系现象、粒子或系统过程与符号，解释变化并作预测 |
| 实验、地理与数据分析 | 检查变量、对照、测量和图表，判断证据支持什么 |
| 历史、文学、哲学与论证 | 分析来源、语境和文本，让解释与证据相称 |
| 语言学习 | 根据意图和情境理解、表达、修改，逐步减少示范 |
| 会计、编程与规则应用 | 依据实际情境判断规则适用性，执行并检查结果 |
| 艺术、设计、音乐与实践 | 围绕目标、约束和实际作品或表现，反馈并改进 |

遇到没有专门示例的领域，导师会依据材料和学习目的，确定当前的小目标、必要前置、合适表示与评价依据，再开始教学。没有正式课程标准时，使用明确标为自拟的学习目标。

实际技能按可观察的证据评价：文字交流可以帮助理解演奏、发音或动作原理，实际表现仍需要相应音频、视频、作品或操作结果。

### 可以这样开始学

> 我想学物理，但完全没基础，也不知道想学到什么程度。你先带我学一点。

> 我想学这一章，请一个知识点一个知识点地教，根据我的回答决定下一步。

> 我记得公式，但题目一变就不知道怎么用。请教我应该观察什么，再让我自己判断。

> 我会画供需图，但文字题总判断错。请根据我的解释找出卡点。

> 帮我检查这段论证的证据是否足够，让我自己修改关键部分。

> 我看得懂英语，但说不出来。请用具体情境带我练表达。

> 这是我这门课的材料，领域可能比较冷门。请先帮我找到起点，再根据我的表现调整。

### 当前验证

评测集现有 27 个案例。本轮实际检查 8 种场景，包含零基础、目标未定、物理与化学、地学材料、设计、节奏和数学回归；加上两组旧版比较，共 10 段对话、20 条导师回复。见[本轮行为报告](evals/results/2026-11-09-cross-subject/REPORT.md)。

[首轮记录](evals/results/2026-11-09/REPORT.md)另有默认模型和简短提示比较。这些检查尚未证明全学科效果、稳定优于其他配置或真人学习增益；案例数量也不代表全部案例已实际运行。

## English

Self-Study Tutor is an AI skill for independent learning across subjects and starting levels. It focuses on two goals: **teaching one meaningful unit at a time, and helping you recognize and apply suitable concepts, methods, and evidence in an unfamiliar task.**

If you understand explanations but struggle to begin on your own, the tutor works on that gap: what relationships to notice, how to represent the task, why an approach fits, and when its conditions require a different choice.

### Get started

Copy this URL to your agent and ask it to read and use the skill. Bring course materials or a problem, or simply say, “I am a complete beginner; help me get started”:

```text
https://github.com/jiangzengyuang-jisoo/self-study-tutor
```

Your agent handles reading and using the skill through the capabilities its environment supports.

### How it teaches

- **Start even without a clear goal.** The tutor proposes a small, adjustable starting point, explains and demonstrates, then learns about your foundation through your work. You do not need to choose chapters, methods, or a complete learning plan first.
- **Progress one useful unit at a time.** Start with a short route, move quickly through demonstrated skills, and repair missing prerequisites where needed.
- **Learn how an approach comes to mind.** Connect visible clues, hidden relationships, conditions, and the first step. Practise selecting and comparing approaches through changed representations, contrasting conditions, and mixed tasks.
- **Adapt to the reason for an error.** Distinguish missing concepts, missed approaches, difficulty reorganizing a task, and execution mistakes; choose feedback accordingly.
- **Provide support, then hand back responsibility.** Explain unfamiliar ideas and demonstrate when needed, then gradually let you make the key decisions and complete the task.
- **Use performance as evidence.** Distinguish understanding an explanation, assisted completion, independent performance, and retention. Use recall, learner explanations, and new tasks to guide review.

You can request a hint, a full answer, a skip, or an end to the session at any time. The tutor follows your preferred language and uses evidence from the current conversation or accessible learning records when continuing.

### Across subjects

Teaching adapts to the subject, course materials, and current task. A single subject may involve calculation, experiments, source analysis, and expression. These are examples, not a whitelist:

| Learning task | Focus |
| --- | --- |
| Mathematics, statistics, and quantitative reasoning | Recognize structure, transform representations, check conditions, solve or prove |
| Physics, economics, and engineering models | Define systems, variables, assumptions, and limits; choose and check a model |
| Chemistry, biology, and mechanisms | Connect observations, particles or system processes, and symbols; explain and predict |
| Experiments, geography, and data analysis | Examine variables, controls, measurements, and charts; judge what evidence supports |
| History, literature, philosophy, and argument | Analyze sources, context, and text; support interpretations with evidence |
| Language learning | Understand, produce, and revise language for a purpose and context with fading support |
| Accounting, programming, and rule application | Check when a rule fits, apply it, and verify the result |
| Art, design, music, and practical skills | Improve actual work or performance against its goals and constraints |

For a field without a dedicated example, the tutor uses the materials and learning purpose to establish a small objective, prerequisites, suitable representations, and assessment criteria. Self-designed objectives are identified as such when no official course criteria are available.

Practical skills require observable evidence. Text can support understanding of performance, pronunciation, or movement, while judging execution requires suitable audio, video, work samples, or operation results.

### Example requests

> I want to learn physics from scratch, but I do not know what level to aim for. Start with something small.

> Teach me this chapter one useful unit at a time, and choose the next step based on my answers.

> I remember the formula but cannot recognize when to use it in a changed problem. Help me learn what to notice, then let me decide.

> I can draw supply and demand curves but misread word problems. Use my explanation to find where I go wrong.

> Help me check whether this paragraph has enough evidence, then let me revise the key part.

> I understand English when I read it but struggle to speak. Help me practise with concrete situations.

> Here are materials for a specialized course. Help me find a starting point and adjust the route based on my work.

### Current evidence

The fixture set now contains 27 cases. This round ran eight revised scenarios covering beginner entry, unclear goals, physics, chemistry, supplied geology materials, design, rhythm, and a mathematics regression. Two previous-version comparisons bring the total to 10 conversations and 20 tutor replies. See the [current behavioral report](evals/results/2026-11-09-cross-subject/REPORT.md).

The [earlier report](evals/results/2026-11-09/REPORT.md) also includes default-model and short-prompt comparisons. These checks do not establish effectiveness in every subject, stable superiority, or gains in human learning. Fixture counts do not mean every case has been run.

## 设计参考 · Design references

本项目借鉴以下流程设计，教学规则与示例按本项目目标编写。The following projects informed the workflow; the teaching rules and examples are written for this project.

- [Think Before Code](https://github.com/Far-200/think-before-code) — 结构提取与迁移 / structure and transfer.
- [Course Creator](https://github.com/ShivamGupta42/course-creator) — 方法线索与选择练习 / selection cues and practice.
- [LearnLM-Inspired Tutor](https://github.com/unix2dos/skills/tree/main/learnlm-inspired-tutor) — 先修关系与教学调整 / prerequisites and adaptive teaching.
- [Book Tutor](https://github.com/xixiaofinland/agent-skills/tree/main/skills/book-tutor) — 课程材料与进度衔接 / course materials and continuity.
- [Teacher_skill](https://github.com/BTHawake/Teacher_skill) — 学科模块与具体教学动作 / subject modules and teaching actions.
- [Learning Commons agent-skills](https://github.com/learning-commons-org/agent-skills) — 共同要求与学科教学参考 / shared requirements and subject pedagogy.
- [School Skills](https://github.com/Jellypod-Inc/school-skills) — 误解诊断与任务评价标准 / misconception diagnosis and task-specific criteria.
- [Tutor MCP](https://github.com/ArnaudGuiovanna/tutor-mcp) — 区分学习估计、实际表现、保持与迁移 / separate estimates, demonstrated performance, retention, and transfer.
