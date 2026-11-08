# Self-Study Tutor · 自学导师

**从零建立理解，在陌生问题里找到思路。**

**Build understanding. Learn how to approach unfamiliar tasks.**

[中文](#中文) · [English](#english)

## 中文

Self-Study Tutor 是一套交给 AI agent 使用的自学教学流程。它关注两件事：**一个知识点一个知识点地学，以及遇到新题时，知道怎样找到可行的方法。**

如果你看讲解能懂，独立做题却不知道从哪开始，它会带你练习观察题目关系、转换表示、检查条件，再逐步把关键判断交给你。完全零基础、还不知道怎么学，也可以直接开始。

### 开始使用

把下面的网址复制给你的 agent，让它读取并使用这个 skill：

```text
https://github.com/jiangzengyuang-jisoo/self-study-tutor
```

接着告诉它你想学什么，或者直接带上教材、课件、题目或自己的尝试。不需要提前制定学习计划。

> 我想学物理，但完全没基础，也不知道想学到什么程度。你先带我学一点。

> 这是我这门课的材料。请一个知识点一个知识点地教，根据我的回答决定下一步。

> 我记得公式，但题目一变就不知道怎么用。请教我应该观察什么，再让我自己判断。

读取仓库、文件和其他材料的方式，取决于你的 agent 所支持的能力。

### 学习时会发生什么

- **先找到一个能开始的小单元。** 有课程材料就结合材料；目标还不明确，导师会提出可调整的起点，在教学中了解你的基础。
- **讲清关键选择。** 除了解释步骤，还会说明为什么想到这个方法、哪些条件支持它，以及换一种题面后怎样识别。
- **针对卡点改变教法。** 概念不懂就补概念，改写困难就示范转换，选法困难就比较条件，局部算错就修正对应步骤。
- **逐步交还任务。** 从必要的解释和示范，过渡到你自己判断、起步和完成任务；通过新情境检查是否能独立应用。

例如，你能在“提示使用换元”后算对，下一步就应该检查能否自己发现替换关系；如果方法已经选对，只是漏掉适用条件，就重点练条件判断。

教学会根据你的表现调整节奏。你可以随时说“讲慢一点”“只给提示”“直接给完整解答”“跳过”或“换个方向”。看懂讲解、受助完成与独立完成会分别看待。

### 不同学科，按任务来教

同一门学科也可能涉及计算、解释、实验和表达。下面是教学侧重点的例子，适用范围不限于这些领域：

| 学科与任务 | 教学侧重点 |
| --- | --- |
| 数学、统计 | 发现结构、转换表示、检查条件，完成求解或证明 |
| 物理、经济、工程 | 从情境明确对象与假设，选择模型并检查结果 |
| 化学、生物 | 联系现象、粒子或系统过程与符号，理解机制并作预测 |
| 地理、实验与数据分析 | 读懂图表，检查变量、测量和证据能支持什么 |
| 历史、文学、哲学 | 分析来源与语境，用材料支持解释和论证 |
| 中文、英语及其他语言 | 围绕理解与沟通目标，练习表达、语境和修改 |
| 会计、编程 | 判断规则何时适用，完成记录或实现，再检查结果 |
| 艺术、设计、音乐与实践 | 围绕目标、约束和具体作品或表现，反馈并改进 |

没有专门示例的领域，也可以从你的材料出发，确定一个小目标及相应的练习和评价依据。带上课程要求，有助于让教学贴近你实际要学的内容。

演奏、发音和动作等实际表现，需要相应的音频、视频或操作证据。只有文字时，可以先学习原理、分析步骤和做准备练习。

### 试用与反馈

欢迎直接用它学习你的真实课程。一次具体的使用经历就很有价值，不需要先完成正式测评。

可以在 [Issues](https://github.com/jiangzengyuang-jisoo/self-study-tutor/issues) 留下反馈：

- **你在学什么？** 学科、主题，以及大致基础。
- **哪里有帮助？** 原来卡在哪里，哪段解释或练习让你能继续？
- **哪里不顺？** 讲太多、提示太早、追问太久、重复已会内容，或其他具体问题。
- **之后自己能做了吗？** 如果试过一道新题或新任务，可以描述结果；对话和作答片段可选。

“用了与普通聊天区别不大”也欢迎反馈。附上对应片段，能帮助定位需要改进的地方。

## English

Self-Study Tutor is a learning workflow for an AI agent. It focuses on **learning one meaningful unit at a time, and finding a workable approach when a task is unfamiliar.**

If explanations make sense but you struggle to start on your own, it helps you notice relationships, change representations, check conditions, and gradually make the key decisions yourself. You can also start as a complete beginner without a clear learning plan.

### Get started

Copy this URL to your agent and ask it to read and use the skill:

```text
https://github.com/jiangzengyuang-jisoo/self-study-tutor
```

Then say what you want to learn, or bring course materials, a problem, or your own attempt. You do not need to plan the whole course first.

> I want to learn physics from scratch, but I do not know what level to aim for. Start with something small.

> Here are my course materials. Teach me one useful unit at a time and choose the next step based on my answers.

> I remember the formula but cannot recognize when to use it in a changed problem. Help me learn what to notice, then let me decide.

Access to the repository, files, and other materials depends on the capabilities of your agent.

### What learning looks like

- **Find a manageable starting point.** Use your course materials when available. If your goal is unclear, the tutor proposes an adjustable first step and learns about your foundation as you work.
- **Explain the key choices.** Learn why an approach comes to mind, which conditions support it, and how to recognize it in a different presentation.
- **Respond to the actual difficulty.** Repair missing concepts, demonstrate a difficult representation change, compare conditions when method selection is hard, or correct a local execution error.
- **Hand back responsibility gradually.** Move from necessary explanations and demonstrations to making decisions, starting, and completing tasks yourself. Use new situations to check independent application.

For example, if you can solve a problem after being told to substitute, the next useful check is whether you can identify a substitution yourself. If you already chose a valid method but missed a condition, the next task should focus on that condition.

The pace adjusts to your work. You can ask for a slower explanation, a hint, a full solution, a skip, or a change of direction at any time. Understanding an explanation, assisted completion, and independent performance are treated separately.

### Teaching across subjects

One subject can involve calculation, explanation, investigation, and expression. These are examples of teaching priorities, not a limit on the fields you can study:

| Subjects and tasks | Teaching focus |
| --- | --- |
| Mathematics and statistics | Recognize structure, change representations, check conditions, solve or prove |
| Physics, economics, and engineering | Identify systems and assumptions, choose models, and check results |
| Chemistry and biology | Connect observations, particles or system processes, and symbols; explain and predict |
| Geography, experiments, and data analysis | Read charts, examine variables and measurements, and judge what evidence supports |
| History, literature, and philosophy | Analyze sources and context; support interpretations and arguments with evidence |
| Chinese, English, and other languages | Practise comprehension, expression, context, and revision for a communication goal |
| Accounting and programming | Decide when rules apply, produce entries or implementations, and verify results |
| Art, design, music, and practical skills | Improve specific work or performance against its goals and constraints |

For a field without a dedicated example, the tutor can start from your materials and establish a small objective, practice task, and assessment criteria. Course requirements help align teaching with what you need to learn.

Assessing musical performance, pronunciation, or movement requires suitable audio, video, or direct observation of the task. With text alone, you can still work on principles, steps, and preparation.

### Try it and share feedback

Use it with a real course or learning task. A concrete experience is useful feedback; you do not need to complete a formal evaluation first.

You can leave feedback in [Issues](https://github.com/jiangzengyuang-jisoo/self-study-tutor/issues):

- **What were you learning?** Include the subject, topic, and approximate starting level.
- **What helped?** Where were you stuck, and which explanation or exercise helped you continue?
- **What got in the way?** Too much explanation, premature hints, prolonged questioning, repeated content, or another specific problem.
- **Could you apply it yourself afterward?** If you tried a new task, describe what happened. Conversation or work excerpts are optional.

“I could not see much difference from ordinary chat” is useful feedback too. An example makes it easier to identify what needs improvement.

## 项目进展 · Project status

当前欢迎真实使用反馈。已有检查主要针对模型的教学行为，尚未证明真人学习增益或各学科的稳定效果。

The project welcomes feedback from real use. Existing checks mainly assess model tutoring behavior; gains in human learning and consistent effectiveness across subjects have not yet been established.

<details>
<summary>评测记录 · Evaluation notes</summary>

目前有 27 个行为案例；最近一轮实际运行 8 种新版场景，加入两组旧版比较，共 10 段对话、20 条导师回复。学生消息为预写脚本，不能作为真实学习成果。

The fixture set contains 27 cases. The latest round ran eight revised scenarios plus two previous-version comparisons: 10 conversations and 20 tutor replies. Learner messages were scripted, so these are not human learning outcomes.

- [跨学科与零基础起步检查 · Cross-subject and beginner checks](evals/results/2026-11-09-cross-subject/REPORT.md)
- [首轮对照记录 · Initial comparisons](evals/results/2026-11-09/REPORT.md)
- [评测方法 · Evaluation approach](evals/README.md)

</details>

<details>
<summary>设计参考 · Design references</summary>

以下项目为流程设计提供了参考；本项目的教学规则与示例按自身目标编写。The following projects informed the workflow; teaching rules and examples are written for this project.

- [Think Before Code](https://github.com/Far-200/think-before-code) — 结构提取与迁移 / structure and transfer.
- [Course Creator](https://github.com/ShivamGupta42/course-creator) — 方法线索与选择练习 / selection cues and practice.
- [LearnLM-Inspired Tutor](https://github.com/unix2dos/skills/tree/main/learnlm-inspired-tutor) — 先修关系与教学调整 / prerequisites and adaptive teaching.
- [Book Tutor](https://github.com/xixiaofinland/agent-skills/tree/main/skills/book-tutor) — 课程材料与进度衔接 / course materials and continuity.
- [Teacher_skill](https://github.com/BTHawake/Teacher_skill) — 学科模块与具体教学动作 / subject modules and teaching actions.
- [Learning Commons agent-skills](https://github.com/learning-commons-org/agent-skills) — 共同要求与学科教学参考 / shared requirements and subject pedagogy.
- [School Skills](https://github.com/Jellypod-Inc/school-skills) — 误解诊断与任务评价标准 / misconception diagnosis and task-specific criteria.
- [Tutor MCP](https://github.com/ArnaudGuiovanna/tutor-mcp) — 区分学习估计、实际表现、保持与迁移 / separate estimates, demonstrated performance, retention, and transfer.

</details>
