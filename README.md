# Self-Study Tutor · 自学导师

**Learn to choose a method, explain why it works, and solve new problems independently.**

**从必要示范走向独立思考：学会选方法、解释依据，并解决未见过的问题。**

[中文](#中文) · [English](#english)

## 中文

### 这是什么

Self-Study Tutor 是一个可复用的 AI 教学技能，用于概念学习、引导练习、闭卷检测、费曼讲解、迁移训练和延迟复习。

它会根据基础提供解释和示范，再逐步减少帮助；区分“看懂答案”“提示下完成”“独立完成”“间隔后仍能完成”和“能迁移到新情境”。你可以随时要求直接答案、完整讲解、切换模式或结束学习。

**语言不限。** 教学跟随你指定的语言或当前对话语言。技能规则文件目前使用中文，界面元数据使用英文，这不限制实际回复语言。

### 核心优势

**把“为什么想到这个方法”纳入教学，让练习逐步走向撤去提示后的独立作答。** 以下是项目的主要设计及其面向学习者的价值：

| 优势 | 具体设计 | 对学习者的价值 |
| --- | --- | --- |
| 学会选方法 | 连接题目线索、适用条件和选择理由，比较合理解法，并讨论方法的失效边界。 | 练习看到新题时如何起步，而不只是照着已指定的方法计算。 |
| 帮助随能力逐步减少 | 基础不足时先解释和示范；卡住时按需提供方向、线索、局部步骤或完整解答，再将思考交还给学习者。 | 初学者有足够的起点，也有机会在支持减少后检验自己的能力。 |
| 掌握判断有依据 | 分开记录提示下完成、无提示完成、延迟保持与迁移表现；用新题验证，不把“听懂了”或同题重做正确当成掌握。 | 更清楚哪些已经能独立完成，哪些仍依赖帮助，哪些尚未验证。 |
| 训练解释、迁移与保持 | 结合闭卷讲解、反例、条件变化题、无方法标签的混合题和延迟复测。 | 检查知识能否经得起换问法、换情境与时间间隔，为后续复习提供依据。 |
| 反馈指出具体卡点 | 优先定位最早的实质错误，保留正确步骤，区分概念、审题、方法选择、推理、计算和表达问题。 | 知道下一步该补概念、练选法还是修正执行，避免把所有错误都归结为“不会”。 |
| 节奏灵活，学习者保有选择权 | 根据表现调整深度，熟练内容快速推进；允许随时要求直接答案、完整讲解、切换模式或停止。 | 把时间用在当前最需要的环节，不必每次完成整套教学流程。 |
| 轻量、通用、可复用 | 以技能文件提供教学流程，无需额外运行时；不绑定学科或教学语言，可按支持平台的方式安装并匹配学习请求。 | 同一套学习原则可用于不同主题与项目，减少重复粘贴长提示词的负担。 |

这些优势描述的是技能的教学设计与使用价值，不代表已经证明能提高分数；实际效果应通过撤去帮助后的独立表现和延迟复测来评估。

### 安装

以下步骤以支持本地技能的 Codex 环境为例。其他支持 Agent Skills 的工具，请使用其自己的安装器或技能目录。教学流程本身无需 Python、Node.js 或额外依赖。

#### 方法一：让 Codex 安装

在提供内置 `skill-installer` 的 Codex 中发送：

```text
请使用 $skill-installer 安装这个 GitHub 仓库中的技能：
https://github.com/jiangzengyuang-jisoo/self-study-tutor

SKILL.md 位于仓库根目录，仓库内路径为 .，安装名称为 self-study-tutor。
请保留 references 和 agents 目录。
```

这里的 `.` 表示仓库根目录，不是仓库中的同名子目录。安装器会选择它支持的安装位置；如果发现已有版本，应先检查现有内容，避免覆盖自己的修改。

#### 方法二：手动安装

当前 Codex 官方文档使用 `~/.agents/skills/` 作为个人技能目录。以下命令需要已安装 Git，且目标目录尚不存在。[目录说明](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

**macOS / Linux：**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/jiangzengyuang-jisoo/self-study-tutor.git "$HOME/.agents/skills/self-study-tutor"
```

**Windows PowerShell：**

```powershell
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
git clone https://github.com/jiangzengyuang-jisoo/self-study-tutor.git (Join-Path $skillRoot 'self-study-tutor')
```

**没有 Git：** 在仓库页面选择 **Code → Download ZIP**，解压后将包含 `SKILL.md` 的文件夹重命名为 `self-study-tutor`，放入上述技能目录。不要多嵌套一层文件夹。

**只在一个项目中使用：** 将同一个完整文件夹放入该项目的 `.agents/skills/self-study-tutor/`。个人安装和项目安装通常选一种即可。

部分版本或内置安装器使用 `$CODEX_HOME/skills`（默认 `~/.codex/skills`）。以当前环境实际支持的位置为准；已经能被发现的安装不需要搬迁，也不要为了兼容路径重复安装。

安装后的文件结构应为：

```text
self-study-tutor/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    └── assessment-and-review.md
```

### 自动调用：不用每次手动点名

安装并被 Codex 发现后，直接提出学习需求即可，例如“从零教我导数”或“出题检查我是否掌握”。Codex 会根据请求与技能描述的匹配情况决定是否选用。[自动调用说明](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)

本仓库没有设置 `allow_implicit_invocation: false`，沿用允许自动调用的默认值 `true`，因此无需额外打开该开关。[调用设置](https://learn.chatgpt.com/docs/build-skills#optional-metadata)

- **适合自动选用：** 学习概念、引导练习、解释自己的理解、测试掌握程度、复习和迁移训练。
- **不会刻意强制教学：** 单纯查事实、索取答案、制作讲义或代办任务；明确要求其他技能时也不叠加本技能。
- **自动匹配并非每次必定触发。** 它依赖技能是否被发现、是否启用及对请求的理解；这也不是后台运行或自动提醒功能。

如果没有触发，先确认技能列表中能找到 `self-study-tutor`，或让助手检查是否可用；安装后仍未出现时重启 Codex。需要明确指定时，在对话中输入：

```text
请使用 $self-study-tutor，从零教我导数，先解释概念，再让我尝试。
```

这是聊天指令，不是终端命令。更换工具时，其技能选择语法可能不同。

### 使用示例

以下请求都可以直接发送；除最后一项外，无需包含技能名。

| 场景 | 可以这样说 |
| --- | --- |
| 零基础入门 | 我没有学过机会成本，请用生活例子从头教我，先不要考试。 |
| 只给提示 | 我卡在这一步了。先给一个方向提示，等我尝试后再继续。题目和我的过程如下：…… |
| 方法选择 | 我学过因式分解和求根公式。给我几道混合题，不提示用哪种方法，让我先解释怎么选。 |
| 费曼讲解 | 我来向零基础学生解释边际成本。请根据我的解释追问，并指出概念错误。 |
| 闭卷检测 | 根据我们刚学的内容出三道无提示新题，建议限时十分钟，等我提交后再评分。我会自行计时。 |
| 延迟复习 | 帮我复习三天前学的内容。先让我回忆，再用一道新题检查；记录如下：…… |
| 直接讲解 | 这道题我暂时不练了，请直接给完整解法并说明关键依据。 |
| 明确调用 | 请使用 $self-study-tutor，帮助我理解这段代码，重点练习如何定位问题。 |

### 检测与能力边界

讲得流畅、重复刚看过的解法或提示后做对，都不能单独证明独立掌握。考试中主动询问“这个方向对吗”也属于索要提示：导师会先说明该题转为有帮助的练习，再提供反馈。

这是教学工作流，不是监考系统，也不保证提高成绩。文件读取、计时、跨会话记录和提醒取决于宿主能力与授权；复习建议不等于提醒已创建。新对话如果缺少历史，请提供之前的学习摘要。

### 文件说明

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 启用范围、模式选择、教学循环与掌握证据 |
| [references/assessment-and-review.md](references/assessment-and-review.md) | 出题、评分、迁移训练、延迟复习与可选记录 |
| [agents/openai.yaml](agents/openai.yaml) | 支持该格式的宿主使用的可选界面元数据 |

---

## English

### What this is

Self-Study Tutor is a reusable AI tutoring skill for concept learning, guided practice, independent assessment, learner explanations, transfer practice, and delayed review.

It explains and demonstrates when prerequisites are missing, then gradually reduces assistance. It distinguishes understanding an explanation, completing a task with help, solving it independently, retaining it over time, and transferring it to a new situation. You can request a direct answer, a full explanation, a mode change, or an end to the session at any time.

**There is no fixed teaching language.** The tutor follows your preferred language or the language of the conversation. The instruction files are currently in Chinese and the interface metadata is in English; neither determines the language of tutoring responses.

### Why use it

**Practice why a method comes to mind, then work toward solving problems without hints.** The skill connects each teaching choice to a practical learner need:

| Advantage | How it works | Value for the learner |
| --- | --- | --- |
| Learn to choose a method | Connects problem clues to applicable conditions and selection reasons, compares valid approaches, and discusses where a method stops working. | Practices how to start an unfamiliar problem, beyond executing a method already named by the tutor. |
| Support gradually fades | Explains and demonstrates when foundations are missing; offers direction, clues, partial steps, or a full solution as needed, then returns the thinking to the learner. | Gives beginners a usable starting point and opportunities to check their ability as assistance is reduced. |
| Mastery claims require evidence | Separates assisted completion, independent performance, retention, and transfer; checks new problems instead of treating “I understand” or a repeated answer as mastery. | Makes it clearer what you can do alone, what still depends on help, and what has not been assessed. |
| Practice explanation, transfer, and retention | Combines closed-book explanations, counterexamples, changed conditions, mixed problems without method labels, and delayed checks. | Tests whether knowledge survives new wording, new situations, and time away, informing what to review next. |
| Feedback identifies the obstacle | Locates the first substantive error, preserves correct work, and distinguishes conceptual, reading, method-selection, reasoning, calculation, and expression issues. | Clarifies whether to revisit a concept, practice choosing an approach, or fix execution. |
| Flexible pacing and learner control | Adjusts depth to performance, moves quickly through familiar content, and accepts requests for direct answers, full explanations, mode changes, or stopping. | Focuses time on the current need without requiring a full teaching checklist every session. |
| Lightweight and reusable | Delivers the workflow as skill files without extra runtimes; does not bind teaching to one subject or language, and supports installation and learning-request matching through compatible hosts. | Reuses the same learning principles across topics and projects with less repeated prompt setup. |

These advantages describe the skill’s design and intended value, not a demonstrated improvement in grades. Evaluate its usefulness through independent performance after help is removed and through delayed checks.

### Installation

These instructions target Codex environments that support local skills. For other Agent Skills-compatible tools, use their installer or skill directory. The tutoring workflow itself requires no Python, Node.js, or additional dependencies.

#### Option 1: Ask Codex to install it

In a Codex environment with the built-in `skill-installer`, send:

```text
Use $skill-installer to install the skill from this GitHub repository:
https://github.com/jiangzengyuang-jisoo/self-study-tutor

SKILL.md is at the repository root. Use repository path . and install it as self-study-tutor.
Keep the references and agents directories.
```

The `.` means the repository root, not a nested directory with the same name. The installer selects a location it supports. If an installation already exists, inspect it before replacing it so local changes are preserved.

#### Option 2: Install manually

Current Codex documentation lists `~/.agents/skills/` for personal skills. The commands below require Git and a destination that does not already exist. [Skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

**macOS / Linux:**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/jiangzengyuang-jisoo/self-study-tutor.git "$HOME/.agents/skills/self-study-tutor"
```

**Windows PowerShell:**

```powershell
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
git clone https://github.com/jiangzengyuang-jisoo/self-study-tutor.git (Join-Path $skillRoot 'self-study-tutor')
```

**Without Git:** Select **Code → Download ZIP** on the repository page. Extract it, rename the folder containing `SKILL.md` to `self-study-tutor`, and place it in the skill directory above. Avoid an extra nested folder.

**For one project only:** Place the same complete folder at `.agents/skills/self-study-tutor/` inside that project. Usually choose either personal or project installation.

Some versions or bundled installers use `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`. Follow the location supported by your environment. An installation that is already discovered does not need to be moved or duplicated.

The installed folder should contain:

```text
self-study-tutor/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    └── assessment-and-review.md
```

### Automatic invocation

Once the skill is installed and discovered, make an ordinary learning request, such as “Teach me derivatives from scratch” or “Test whether I understand this.” Codex selects skills by matching the request to their descriptions. [Implicit invocation](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)

This repository does not set `allow_implicit_invocation: false`, so it retains the default `true`. No additional switch is required to allow automatic selection. [Invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata)

- **Intended matches:** Learning concepts, guided practice, explaining your understanding, checking mastery, review, and transfer practice.
- **No forced tutoring:** Simple factual lookups, requests for answers, study-material creation, or delegated tasks. An explicitly requested different skill takes precedence.
- **Automatic selection is not guaranteed on every request.** It depends on discovery, enablement, and task interpretation. It does not mean background execution or automatic reminders.

If it does not activate, check whether `self-study-tutor` appears in the available skills, or ask the assistant to check availability. Restart Codex if a new installation does not appear. To select it explicitly, send:

```text
Use $self-study-tutor to teach me derivatives from scratch. Explain the concept first, then let me try.
```

This is a chat instruction, not a terminal command. Other tools may use different skill-selection syntax.

### Examples

Send these requests directly. Only the last example explicitly names the skill.

| Situation | Example request |
| --- | --- |
| Starting from zero | I have never studied opportunity cost. Teach me with everyday examples; do not test me yet. |
| Getting a hint | I am stuck here. Give me one directional hint and wait for my attempt. Here is the problem and my work: … |
| Choosing a method | I know factorization and the quadratic formula. Give me mixed problems without naming the method, and let me explain my choice first. |
| Explaining to a beginner | I will explain marginal cost to a beginner. Ask follow-up questions based on my explanation and point out conceptual errors. |
| Independent assessment | Give me three new problems on what we just studied, without hints. Suggest a ten-minute limit and grade after I submit. I will time myself. |
| Delayed review | Help me review what I studied three days ago. Start with recall, then check with a new problem. Here are my notes: … |
| Direct explanation | I do not want to practise this problem right now. Give me the full solution and explain the key decisions. |
| Explicit invocation | Use $self-study-tutor to help me understand this code, focusing on how to locate a problem. |

### Assessment and capability boundaries

A fluent explanation, immediate repetition of a demonstrated solution, or success after a hint does not by itself establish independent mastery. Asking “Is this the right approach?” during an assessment also requests a hint: the tutor identifies that item as assisted practice before providing feedback.

This is a teaching workflow, not a proctoring system or a guarantee of improved grades. File access, timing, persistent records, and reminders depend on host capabilities and authorization. A review suggestion is not a scheduled reminder. Provide a previous learning summary when a new conversation lacks that context.

### Files

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Scope, mode selection, tutoring loop, and mastery evidence |
| [references/assessment-and-review.md](references/assessment-and-review.md) | Assessment, scoring, transfer practice, delayed review, and optional records |
| [agents/openai.yaml](agents/openai.yaml) | Optional interface metadata for supporting hosts |
