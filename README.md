# 401 Review Repository Guide

这是一个用于复习 **ECE4010J / 401 概率统计相关内容** 的自用仓库。

本仓库的核心目标不是写教材，而是维护一份可以在考试中快速查阅的 **paper-based cheating sheet**。

---

## 1. 最重要的文件

当前主要维护文件是根目录下的：

```text
cheating_sheet.md
```

用户平时主要只看这个文件。其他文件只是辅助资料或归档材料。

---

## 2. 考试材料限制

非常重要：

```text
考试只能携带纸质材料。
```

因此，`cheating_sheet.md` 里虽然可以保留 Markdown 链接，例如：

```markdown
[C-RV-001](#c-rv-001)
[EX-JOINT-001](#ex-joint-001)
```

但不能依赖链接跳转作为主要索引方式。因为打印成纸质材料后，链接不会生效。

所以主索引必须依赖 **可打印、可肉眼查找的编号系统**：

```text
Concept ID: C-模块-编号
Example ID: EX-模块-编号
```

例如：

```text
C-RV-001      PMF / PDF / CDF
C-DIST-001    Discrete Distributions
C-TRANS-001   CDF Method
C-JOINT-001   Joint Distribution Workflow
C-REL-001     Reliability / Hazard

EX-RV-001     Continuous PDF Probability
EX-DIST-003   Hypergeometric Recognition
EX-JOINT-001  Joint Density Complete Workflow
EX-REL-002    Series and Parallel Systems
```

维护文档时要保证：

- 链接可以保留；
- 链接文字必须是清晰可打印的 ID；
- 表格中必须直接显示 Concept ID 和 Example ID；
- 不要只写“见这里”“点击这里”“跳转到本节”；
- 打印出来后，读者应该仍能通过编号找到对应内容。

---

## 3. 文档设计原则

`cheating_sheet.md` 必须遵循以下原则。

### 3.1 考试速查优先

这不是教材，也不是完整讲义。优先保留：

- 公式；
- 适用条件；
- 题型识别关键词；
- 解题模板；
- 常见陷阱；
- 结构化例题；
- Concept ID 与 Example ID 的映射关系。

不要写太长的背景故事、证明或大段解释，除非它能直接帮助考试做题。

### 3.2 概念和例题分离

概念区只放：

- 定义；
- 什么时候用；
- 公式；
- 考试模板；
- 常见陷阱。

完整例题必须放在 `Worked Examples` 区域。

不要把完整例题塞进概念区。

### 3.3 所有概念和例题必须有稳定 ID

Concept ID 格式：

```text
C-模块缩写-编号
```

Example ID 格式：

```text
EX-模块缩写-编号
```

常见模块缩写：

| Module | Meaning |
|---|---|
| `RV` | Random Variable basics |
| `DIST` | Distributions |
| `APPROX` | Approximation |
| `PP` | Poisson Process |
| `TRANS` | Transformation |
| `JOINT` | Joint Distribution |
| `COND` | Conditional Expectation |
| `COV` | Covariance / Correlation |
| `REL` | Reliability |
| `MGF` | Moment Generating Function |

### 3.4 不要轻易改已有 ID

已有 ID 一旦建立，后续不要因为重排章节而修改。

原因：

- 用户会在纸质材料上通过编号查找；
- Mapping 表依赖这些编号；
- 后续 AI 维护时也依赖这些编号；
- 改 ID 会破坏旧笔记和交叉引用。

如果必须重构，优先保留旧 ID，并只新增新 ID。

---

## 4. `cheating_sheet.md` 的固定结构

主文件建议保持以下结构：

```markdown
# ECE4010J Midterm Cheating Sheet

## 0. Quick Index
## 1. Concept-to-Example Map
## 2. Tag Index
## 3. How to Use This Sheet
## 4. Core Concepts
## 5. Exam Templates
## 6. Worked Examples
## 13. Common Traps
## 14. Final Self-check
```

说明：

- `Quick Index` 用于最快速定位题型；
- `Concept-to-Example Map` 用编号连接概念和例题；
- `Tag Index` 用于跨章节搜索；
- `Core Concepts` 放概念、公式、模板；
- `Worked Examples` 放完整例题；
- `Common Traps` 放考试常见错误。

---

## 5. 新增内容时的维护流程

如果接手的 AI 要继续维护，请按这个流程：

### Step 1：判断内容类型

先判断新内容属于哪类：

```text
概念 / 公式 / 解题模板 / 完整例题 / 常见陷阱 / 复习计划
```

### Step 2：分配或沿用 ID

- 新概念：分配新的 `C-...` 编号；
- 新例题：分配新的 `EX-...` 编号；
- 已有概念或例题：沿用原 ID，不要重命名。

### Step 3：放到正确位置

- 概念、公式、模板 → `Core Concepts`；
- 完整题目、解答过程 → `Worked Examples`；
- 常见错误 → `Common Traps`；
- 文档维护说明 → `README.md` 或 `materials/`。

### Step 4：同步更新索引

新增或修改后必须检查并更新：

1. `Quick Index`
2. `Concept-to-Example Map`
3. `Tag Index`
4. 相关概念中的 `Related Examples`
5. 相关例题中的 `Related Concepts`

### Step 5：纸质可读性检查

最后检查：

- 打印出来后是否还能靠 ID 找到内容；
- 表格里是否直接显示了编号；
- 是否有只依赖链接跳转的表达；
- 是否有过长段落影响考试速查；
- 是否遗漏 support / 条件 / 适用范围。

---

## 6. 写作风格

建议风格：

- 中文解释为主；
- 关键英文术语保留；
- 公式使用 LaTeX；
- 表格优先于长段落；
- 每个概念尽量短；
- 每个例题必须结构化；
- 重要提醒用 `> Warning:` 或 `> Exam Tip:`。

---

## 7. 当前资料文件夹

辅助资料在：

```text
materials/
```

其中包括：

```text
materials/cheating_sheet_document_design_guidelines.md
materials/ece4010j_two_day_review_guide.md
```

这些文件是归档和维护参考。真正考试复习主要看：

```text
cheating_sheet.md
```

---

## 8. 给下一位 AI 的一句话指令

如果一个新的 AI 接手，请直接遵守下面这句话：

```text
请维护根目录 cheating_sheet.md。它是只能打印成纸质材料使用的考试速查表，所以必须保留清晰的 Concept ID / Example ID / Mapping / Tag Index；Markdown 链接可以保留，但不能作为主要索引，主要索引必须靠打印后仍可见的编号完成。新增内容时，概念和例题分开写，并同步更新 Quick Index、Concept-to-Example Map 和 Tag Index。
```
