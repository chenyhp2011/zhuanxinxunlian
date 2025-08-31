# zhuanxinxunlian
为了减少中学生因为粗心，审题不认真，开发的训练程序

# 数学思维训练营 (Math Mind Training Camp)

**一个基于认知科学原理，旨在从根本上提升计算细心度和审题能力的Python应用。**

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📖 项目简介

在数学学习中，“粗心”和“读题忘条件”是两个长期存在的痛点。传统的刷题训练往往治标不治本。本项目认为，这些问题的根源不在于数学知识本身，而在于学生底层的**认知能力**存在短板。

“数学思维训练营”不是一个普通的刷题工具，它是一个认知能力训练器。它通过两个核心模块，将认知科学的研究成果转化为可交互的训练任务，旨在锻炼学生的**执行功能**（特别是工作记忆和抑制控制）和**结构化思维能力**。

本项目完全开源，希望能为有同样困扰的学生、老师和家长提供一个科学、有效的训练工具。

## 🔬 核心原理与方法

本应用的设计深度融合了神经认知科学的理论。

### 🧠 **心算能力训练：从“算得快”到“算得对”**

传统的计算训练只关注速度和熟练度。本模块的核心目标是**减少因“冲动”导致的低级错误**。

* **执行功能训练:** 我们将“粗心”重新定义为大脑**执行功能**（Executive Functions）的短暂失效。
* **抑制控制 (Inhibitory Control):** 为了精准训练这一点，我们设计了独创的**“Stroop计数运算”**。例如，对于表达式 `(7 7 7)`，用户必须抑制住阅读数字“7”或“777”的自动化冲动，转而执行“计数”这一新规则，得到值“3”。这能极大地锻炼大脑前额叶皮层的抑制控制能力，即“三思而后行”的能力。
* **工作记忆 (Working Memory):** 训练任务从2个数的运算逐步升级到7个数的复合运算，持续挑战并拓展用户的工作记忆容量。

心算训练界面如下
<img width="1618" height="618" alt="image" src="https://github.com/user-attachments/assets/52c52a42-fdcd-437d-8436-1c9b0fd3ff9d" />



### ✍️ **审题能力训练：从“读文字”到“建模”**

许多学生能“读懂”题目的每一个字，但无法解题，这是因为他们未能将文字信息成功转化为结构化的“情境模型”（Situation Model），并且会在做题过程中，由于没有形成结构化记忆，很容易遗漏题目条件，最终导致错误。

* **结构化信息编码:** 本模块将一道复杂的应用题，强制“解剖”为四个标准步骤：
    1.  **目标诊断 (Goal):** 我要求解什么？
    2.  **要素提取 (Extraction):** 题目给了我哪些“棋子”（数值和条件）？
    3.  **规则识别 (Rule):** 这些“棋子”之间遵循什么“游戏规则”（公式和隐含关系）？
    4.  **策略规划 (Strategy):** 我的第一步应该怎么走？
* **思维过程显性化:** 通过引导式的问答，这个训练将优秀解题者内隐的、不可见的思维过程，转化为外在的、可操作的训练流程。通过反复练习，帮助用户将这套分析框架内化为自己的思维习惯，从而减少条件遗忘。

审题训练界面如下
<img width="1824" height="812" alt="image" src="https://github.com/user-attachments/assets/1b66fd67-4a50-441d-883c-4cc40adec50f" />


## ✨ 主要功能

* **两大训练模块:** “心算能力训练”与“审题能力训练”。
* **科学的认知训练:** 独创的“Stroop计数运算”，有效提升抑制控制能力。
* **结构化的审题流程:** 四步法引导学生深度理解和分析问题。
* **渐进式难度:** 每个模块都包含多个难度等级，适应不同水平的学习者。
* **实时交互与反馈:** 即时的计时器、得分反馈和答案解析，构成高效的学习闭环。
* **高度可定制化:** 审题训练的题库采用易于编辑的Markdown格式，方便用户添加自己的题目。

## 📂 应用结构

```
math_trainer/
│
├── app.py                   # 主程序入口，应用的首页
├── requirements.txt         # 项目依赖库文件
├── prompt.md                # 题目生成提示词
├── readme.md                # 应用说明
│
├── pages/                   # Streamlit多页面目录
│   ├── 1_心算能力训练.py      # “心算训练”任务页面
│   └── 2_审题能力训练.py      # “审题训练”任务页面
│
├── modules/                 # 核心逻辑模块
│   ├── calculator_logic.py  # 心算题目生成逻辑
│   └── comprehension_logic.py # 审题题库加载与解析逻辑
│
└── data/                    # 审题训练题库 (.md格式)
    ├── comprehension_level_1.md
    ├── comprehension_level_2.md
    └── comprehension_level_3.md
```

## 🚀 如何运行

请按照以下步骤在您的本地计算机上运行本应用。

### 1. 准备工作

* 确保您的电脑已经安装了 **Python 3.8** 或更高版本。
* 从 [Python官网](https://www.python.org/downloads/) 下载并安装。**（重要：安装时请务必勾选 "Add Python to PATH"）**

### 2. 下载项目

将本项目下载或克隆到您的本地。

```bash
git clone [https://github.com/your-username/math-trainer.git](https://github.com/your-username/math-trainer.git)
cd math-trainer
```

### 3. 创建虚拟环境并安装依赖

为了不污染您的全局Python环境，建议使用虚拟环境。

```bash
# 创建一个名为 venv 的虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
.\venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 安装所有必需的库
pip install -r requirements.txt
```

### 4. 运行应用

一切准备就绪！在终端中运行以下命令：

```bash
streamlit run app.py
```

您的默认浏览器将会自动打开一个新的标签页，显示应用界面。

## ✏️ 如何自定义题库

您可以非常方便地添加或修改“审题能力训练”的题目。

1.  进入 `data/` 文件夹。
2.  打开对应难度的 `.md` 文件（如 `comprehension_level_1.md`）。
3.  参照以下格式，在文件末尾添加您的新题目（注意用 `---` 与上一题隔开）。

**题目格式模板：**
```markdown
Problem_ID:: 103
Difficulty_Level:: 1
Problem_Text::
这里是你的题目描述，可以**加粗**，也可以换行。
例如：一个篮球`80`元，一个足球`60`元，各买一个需要多少钱？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 一个篮球的价格|B. 一个足球的价格|C. 总共需要的钱
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 篮球80元|B. 足球60元|C. 各买一个
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 总价 = 篮球价格 + 足球价格|B. 篮球比足球贵
Rule_Answer:: A
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 将两个价格相加|B. 将两个价格相减
Strategy_Answer:: A
Feedback_Column:: {"Strategy_B":"题目要求计算总价，相减是计算差价，审题错误。"}
```

**题目生成提示词：**
```markdown
可以从prompt.md中复制不同难度的提示词，可根据需求进行修改。
大模型生成后，将题库复制到不同难度的 comprehension_level_x.md文件中，供程序进行随机选择。
```

## 🤝 贡献

欢迎任何形式的贡献！如果您有任何想法、建议或发现了Bug，请随时通过 [GitHub Issues](https://github.com/your-username/math-trainer/issues) 提交。

## 📄 许可证

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 开源许可证。

---
*文档更新于 2025年8月30日*
