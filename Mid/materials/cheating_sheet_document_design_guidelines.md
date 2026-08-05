# Cheating Sheet 文档设计准则

> 这个文件用于保存 cheating sheet 的维护规则。平时主要编辑根目录的 `cheating_sheet.md`。

## 1. 文档定位

- 这是 ECE4010J / 概率统计类考试用的纸质或电子 cheating sheet。
- 内容目标是考试速查，不是教材式长篇解释。
- 优先保留：公式、适用条件、题型识别、解题模板、常见陷阱、例题标签。
- 证明、背景故事、严格推导只在能直接帮助做题时保留。

## 2. 推荐结构

主文档建议使用以下结构：

```markdown
# ECE4010J Midterm Cheating Sheet

## 0. Quick Index
## 1. Random Variable Basics
## 2. Distribution Recognition
## 3. Common Distributions
## 4. Approximation
## 5. Poisson Process
## 6. Transformation
## 7. Joint Distribution
## 8. Conditional Expectation
## 9. Covariance and Independence
## 10. Reliability
## 11. MGF Toolkit
## 12. Worked Examples
## 13. Common Traps
## 14. Final Self-check
```

## 3. 内容维护规则

### Concept Block

每个概念尽量包含：

- Concept name
- Tags
- One-line definition
- When to use
- Key formulas
- Exam template
- Common traps

### Example Block

每个例题尽量包含：

- Example ID
- Problem pattern
- Given information
- Solution steps
- Final answer
- What this example tests
- Mistakes to avoid

## 4. 标签规则

标签统一小写，用反引号包裹：

```text
`#pmf`
`#pdf`
`#cdf`
`#binomial`
`#poisson`
`#normal-approximation`
`#continuity-correction`
`#cdf-method`
`#jacobian`
`#joint-pdf`
`#conditional-expectation`
`#covariance`
`#independence`
`#reliability`
`#hazard-rate`
`#mgf`
```

## 5. 修改原则

新增内容时：

1. 先判断是概念、公式、模板还是例题。
2. 概念放到对应章节。
3. 完整题目放到 Worked Examples，不塞进概念解释里。
4. 如果新增例题，更新 Quick Index 或相应章节的提醒。
5. 不要为了重排而频繁改已有 Example ID。

## 6. 风格要求

- 中文解释为主，关键英文术语保留。
- 公式使用 LaTeX。
- 表格优先于长段落。
- 每个知识点应适合考试时快速扫描。
- 重要提醒用 `> Warning:` 或 `> Exam Tip:`。

## 7. 当前主文件

当前主要维护文件：

```text
/cheating_sheet.md
```

其他文件只作为资料归档。