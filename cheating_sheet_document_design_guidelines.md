# Cheating Sheet 文档设计准则与维护 Prompt

> 适用场景：ECE4010J / 概率统计类期中考试 cheating sheet。  
> 目标：让文档既能考试速查，又能持续扩展；概念解释和例题分离，但通过标签和链接保持清晰映射。

---

## 0. 给 AI 使用的总 Prompt

把下面这段作为你以后让 AI 帮你维护 cheating sheet 时的固定提示词。

```text
你现在是我的 ECE4010J 期中考试 cheating sheet 文档编辑器。

请严格按照以下规则维护我的 Markdown 文档：

1. 文档定位
   - 这是考试允许携带的纸质 cheating sheet。
   - 内容必须适合考试速查，而不是教材式长篇解释。
   - 优先保留：公式、适用条件、题型识别、解题模板、常见陷阱、例题标签。
   - 不要写太长的背景故事和证明，除非它能直接帮助考试做题。

2. 排版结构
   - 使用清晰的大标题、小标题。
   - 每个大模块使用二级标题 `##`。
   - 每个概念使用三级标题 `###`。
   - 每个例题使用三级标题 `###`。
   - 每个概念和例题都必须有唯一 ID，方便互相引用。
   - 概念解释和例题必须分开，不要把完整例题塞进概念区。

3. 概念区要求
   每个概念必须尽量包含：
   - Concept ID
   - Tags
   - Related Examples
   - One-line Definition
   - When to Use
   - Key Formulas
   - Exam Template
   - Common Traps
   - Depth Level: Must Understand / Put on Paper / Optional

4. 例题区要求
   每个例题必须尽量包含：
   - Example ID
   - Concept Tags
   - Related Concepts
   - Problem Pattern
   - Given Information
   - Solution Steps
   - Final Answer
   - What This Example Tests
   - Mistakes to Avoid

5. 概念和例题的映射方式
   - 不使用页码作为主要索引。
   - 使用 `Concept ID`、`Example ID`、`Tags` 和 Markdown anchor 链接。
   - 概念处必须标注相关例题。
   - 例题处必须标注涉及的概念标签。
   - 如果一个概念对应多个例题，要列出所有 Example ID。
   - 如果一个例题涉及多个概念，要列出所有 Concept ID。

6. 内容风格
   - 中文解释为主，关键英文术语必须保留。
   - 公式使用 LaTeX。
   - 表格优先于长段落。
   - 每个概念尽量控制在半页以内。
   - 每个例题可以稍长，但必须结构化。
   - 重要提醒用 `> Warning:` 或 `> Exam Tip:`。

7. 可扩展性
   - 新增概念时，先分配 Concept ID。
   - 新增例题时，先分配 Example ID。
   - 新增内容后，必须更新：
     1. Quick Index
     2. Concept-to-Example Map
     3. Tag Index
   - 不要破坏已有 ID。
   - 不要因为重排文档而改 ID。

8. 修改输出要求
   当我给你新内容、截图、PDF 或 git diff 时，请你：
   - 判断应该放入哪个模块；
   - 如果是概念，整理成 Concept Block；
   - 如果是题目，整理成 Example Block；
   - 如果同时包含概念和题目，则拆成两个部分，并建立映射；
   - 最后给出需要更新的 mapping 表。
```

---

## 1. 文档总体结构

推荐整个 cheating sheet 使用下面的固定结构。

```markdown
# ECE4010J Midterm Cheat Sheet

## 0. Quick Index

## 1. How to Use This Sheet

## 2. Concept-to-Example Map

## 3. Tag Index

## 4. Core Concepts

### 4.1 Basic Probability

### 4.2 Random Variables

### 4.3 Common Distributions

### 4.4 Approximation Methods

### 4.5 Random Variable Transformation

### 4.6 Joint Distributions

### 4.7 Conditional Expectation

### 4.8 Covariance and Correlation

### 4.9 Reliability

### 4.10 MGF Toolkit

## 5. Exam Templates

## 6. Worked Examples

### 6.1 Distribution Examples

### 6.2 Transformation Examples

### 6.3 Joint Distribution Examples

### 6.4 Reliability Examples

### 6.5 Approximation Examples

## 7. Common Traps

## 8. Formula Tables

## 9. Appendix / Low-Priority Concepts
```

---

## 2. 命名与 ID 规则

### 2.1 Concept ID

概念 ID 格式：

```text
C-模块缩写-编号
```

例如：

| Concept ID | Meaning |
|---|---|
| `C-RV-001` | PMF / PDF / CDF |
| `C-DIST-001` | Binomial Distribution |
| `C-DIST-002` | Poisson Distribution |
| `C-TRANS-001` | CDF Method |
| `C-JOINT-001` | Marginal Distribution |
| `C-COND-001` | Conditional Expectation |
| `C-REL-001` | Reliability Function |
| `C-MGF-001` | MGF Definition |

---

### 2.2 Example ID

例题 ID 格式：

```text
EX-模块缩写-编号
```

例如：

| Example ID | Meaning |
|---|---|
| `EX-DIST-001` | Binomial / Poisson / Normal approximation 例题 |
| `EX-TRANS-001` | \(Y=\max(X_1,X_2)\) 例题 |
| `EX-JOINT-001` | Joint density 完整流程例题 |
| `EX-REL-001` | Reliability 条件概率例题 |
| `EX-MGF-001` | MGF 证明独立和分布例题 |

---

### 2.3 Tag 规则

标签统一小写，使用反引号包裹。

格式：

```text
`#topic-subtopic`
```

例子：

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
`#marginal`
`#conditional-density`
`#conditional-expectation`
`#covariance`
`#independence`
`#reliability`
`#hazard-rate`
`#weibull`
`#mgf`
```

---

## 3. Quick Index 设计

Quick Index 放在文档最前面，用于考试时快速跳转。

模板：

```markdown
## 0. Quick Index

| What the problem asks | Go to | Main Template |
|---|---|---|
| Identify a distribution | [Distribution Recognition](#distribution-recognition) | Define X → choose distribution |
| Approximate Binomial | [Approximation Methods](#approximation-methods) | Normal + continuity correction |
| Find PDF of Y=g(X) | [Transformation](#random-variable-transformation) | CDF method |
| Given joint PDF | [Joint Distributions](#joint-distributions) | marginal → conditional → expectation |
| Find E[X\|Y] | [Conditional Expectation](#conditional-expectation) | conditional density → integral |
| Check independence | [Independence](#independence) | joint = product of marginals |
| System failure | [Reliability](#reliability) | R(t), hazard, series/parallel |
| Use MGF | [MGF Toolkit](#mgf-toolkit) | multiply MGFs / take derivatives |
```

---

## 4. Concept-to-Example Map 设计

这是本文档的核心：**概念和例题分开，但通过映射表连接**。

模板：

```markdown
## 2. Concept-to-Example Map

| Concept ID | Concept Name | Tags | Related Examples |
|---|---|---|---|
| C-DIST-001 | Binomial Distribution | `#binomial` | [EX-DIST-001](#ex-dist-001), [EX-APPROX-001](#ex-approx-001) |
| C-DIST-002 | Poisson Distribution | `#poisson` | [EX-DIST-002](#ex-dist-002), [EX-MGF-001](#ex-mgf-001) |
| C-TRANS-001 | CDF Method | `#cdf-method` | [EX-TRANS-001](#ex-trans-001), [EX-TRANS-002](#ex-trans-002) |
| C-JOINT-001 | Marginal Density | `#marginal` | [EX-JOINT-001](#ex-joint-001) |
| C-COND-001 | Conditional Expectation | `#conditional-expectation` | [EX-JOINT-001](#ex-joint-001), [EX-COND-001](#ex-cond-001) |
| C-REL-001 | Reliability Function | `#reliability` | [EX-REL-001](#ex-rel-001) |
```

---

## 5. Tag Index 设计

Tag Index 用于跨章节搜索。

模板：

```markdown
## 3. Tag Index

| Tag | Meaning | Related Concepts | Related Examples |
|---|---|---|---|
| `#binomial` | Fixed number of independent trials | C-DIST-001 | EX-DIST-001 |
| `#normal-approximation` | Approximate Binomial by Normal | C-APPROX-001 | EX-APPROX-001 |
| `#cdf-method` | Use CDF to transform RV | C-TRANS-001 | EX-TRANS-001, EX-TRANS-002 |
| `#joint-pdf` | Joint density of continuous random variables | C-JOINT-001 | EX-JOINT-001 |
| `#conditional-expectation` | Expected value after conditioning | C-COND-001 | EX-JOINT-001 |
| `#reliability` | Survival probability \(R(t)=P(T>t)\) | C-REL-001 | EX-REL-001 |
```

---

## 6. 概念区模板

每个概念都使用下面格式。不要把完整例题放进概念区，只放最小示例或模板。

```markdown
<a id="c-dist-001"></a>

### C-DIST-001 — Binomial Distribution

**Tags:** `#binomial` `#discrete-rv` `#independent-trials`  
**Related Examples:** [EX-DIST-001](#ex-dist-001), [EX-APPROX-001](#ex-approx-001)  
**Depth Level:** Must Understand

#### One-line Definition

Counts the number of successes in a fixed number of independent Bernoulli trials.

#### When to Use

Use Binomial when:

- the number of trials \(n\) is fixed;
- each trial has only success/failure;
- success probability \(p\) is the same;
- trials are independent.

#### Key Formulas

If \(X \sim \mathrm{Binomial}(n,p)\),

\[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}, \quad k=0,1,\dots,n
\]

\[
E[X]=np, \qquad Var(X)=np(1-p)
\]

#### Exam Template

```text
Let X = number of successes.
Since there are n independent trials and each has success probability p,
X ~ Binomial(n,p).
Then plug into the PMF/CDF/approximation formula.
```

#### Common Traps

> Warning: Binomial assumes independent trials or sampling with replacement.  
> If the problem says “without replacement”, consider Hypergeometric.

#### Paper-only or Must Understand?

- Formula: Put on paper.
- Distribution recognition: Must understand.
- Derivation of PMF: Optional.
```

---

## 7. 例题区模板

每个例题使用下面格式。例题可以对应多个概念。

```markdown
<a id="ex-joint-001"></a>

### EX-JOINT-001 — Joint PDF Full Workflow

**Concept Tags:** `#joint-pdf` `#marginal` `#conditional-density` `#conditional-expectation` `#independence`  
**Related Concepts:** [C-JOINT-001](#c-joint-001), [C-COND-001](#c-cond-001), [C-INDEP-001](#c-indep-001)  
**Difficulty:** Core Exam Template

#### Problem Pattern

Given a joint density \(f_{X,Y}(x,y)\), find:

1. marginal density;
2. conditional density;
3. \(E[X|Y]\);
4. \(E[X]\);
5. whether \(X,Y\) are independent.

#### Given Information

```text
f_XY(x,y) = ...
support = ...
```

#### Solution Steps

1. **Find support.**
2. **Find marginal density.**

\[
f_Y(y)=\int f_{X,Y}(x,y)\,dx
\]

3. **Find conditional density.**

\[
f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
\]

4. **Find conditional expectation.**

\[
E[X|Y=y]=\int x f_{X|Y}(x|y)\,dx
\]

5. **Use total expectation.**

\[
E[X]=E[E[X|Y]]
\]

6. **Check independence.**

\[
f_{X,Y}(x,y) \stackrel{?}{=} f_X(x)f_Y(y)
\]

#### Final Answer

```text
Write final results here.
```

#### What This Example Tests

- support recognition;
- marginalization;
- conditioning;
- total expectation;
- independence check.

#### Mistakes to Avoid

> Warning: Do not integrate over \(-\infty\) to \(\infty\) blindly.  
> The true limits come from the support.
```

---

## 8. 大模块排版规则

### 8.1 每个大模块开头必须有 overview

模板：

```markdown
## 4.5 Random Variable Transformation

### Overview

This module is used when the problem defines a new random variable from old ones.

| Problem Type | Method |
|---|---|
| \(Y=g(X)\), monotone | inverse function |
| \(Y=g(X)\), non-monotone | CDF method |
| \(Y=\max(X_1,X_2)\) | CDF method |
| \(Y=\min(X_1,X_2)\) | survival method |
| \((U,V)=g(X,Y)\) | Jacobian |
```

---

### 8.2 每个模块结尾必须有 mini checklist

模板：

```markdown
### Mini Checklist

- [ ] Can I identify this problem type?
- [ ] Do I know which formula/template to use?
- [ ] Do I know what goes into the cheating sheet?
- [ ] Do I know the common traps?
- [ ] Do I have at least one related example?
```

---

## 9. 内容深度等级

每个概念都标记一个深度等级。

| Depth Level | Meaning | How to Study |
|---|---|---|
| Must Understand | 必须真正理解 | 需要练题 |
| Template Skill | 必须会套模板 | 需要做例题 |
| Put on Paper | 放纸上即可 | 考试时查 |
| Optional | 低优先级 | 有时间再看 |

示例：

```markdown
**Depth Level:** Must Understand
```

或者：

```markdown
**Depth Level:** Put on Paper
```

---

## 10. 概念和例题的映射规范

### 10.1 概念处必须写 Related Examples

```markdown
**Related Examples:** [EX-TRANS-001](#ex-trans-001), [EX-TRANS-002](#ex-trans-002)
```

### 10.2 例题处必须写 Concept Tags 和 Related Concepts

```markdown
**Concept Tags:** `#cdf-method` `#max-rv` `#independence`  
**Related Concepts:** [C-TRANS-001](#c-trans-001), [C-INDEP-001](#c-indep-001)
```

### 10.3 一对多关系

一个概念对应多个例题：

```markdown
C-COND-001 Conditional Expectation
→ EX-JOINT-001, EX-COND-001, EX-GAUSS-001
```

### 10.4 多对一关系

一个例题涉及多个概念：

```markdown
EX-JOINT-001
→ C-JOINT-001, C-MARG-001, C-COND-001, C-INDEP-001
```

---

## 11. 推荐标签库

### 11.1 Basic Probability

```text
#sample-space
#event
#conditional-probability
#bayes
#independence
#partition
#counting
```

### 11.2 Random Variables

```text
#random-variable
#pmf
#pdf
#cdf
#expectation
#variance
#lotus
```

### 11.3 Distributions

```text
#bernoulli
#binomial
#geometric
#negative-binomial
#hypergeometric
#poisson
#exponential
#gamma
#chi-square
#normal
#weibull
```

### 11.4 Approximation

```text
#poisson-approximation
#normal-approximation
#continuity-correction
#clt
#lln
```

### 11.5 Transformation

```text
#cdf-method
#monotone-transform
#piecewise-transform
#max-rv
#min-rv
#jacobian
#convolution
#polar-transform
```

### 11.6 Joint Distribution

```text
#joint-pmf
#joint-pdf
#marginal
#conditional-density
#support
#independence
```

### 11.7 Dependence

```text
#covariance
#correlation
#uncorrelated
#covariance-matrix
```

### 11.8 Conditional Expectation

```text
#conditional-expectation
#total-expectation
#conditional-variance
#total-variance
#regression
```

### 11.9 Reliability

```text
#failure-time
#reliability
#survival-function
#hazard-rate
#series-system
#parallel-system
#weibull
#memoryless
```

### 11.10 MGF

```text
#mgf
#moment-extraction
#independent-sum
#uniqueness
#random-sum
```

---

## 12. 新增内容时的操作流程

每次加入新内容时，按下面顺序处理：

```text
Step 1: 判断内容类型
- 是概念？
- 是例题？
- 是公式？
- 是 common trap？
- 是 exam template？

Step 2: 分配 ID
- 概念 → C-XXX-编号
- 例题 → EX-XXX-编号

Step 3: 添加标签
- 至少 1 个主标签
- 最多 5 个核心标签
- 不要堆太多标签

Step 4: 放入对应模块
- 概念进 Core Concepts
- 例题进 Worked Examples
- 公式进 Formula Tables
- 陷阱进 Common Traps

Step 5: 更新映射
- 更新 Concept-to-Example Map
- 更新 Tag Index
- 在概念处写 Related Examples
- 在例题处写 Related Concepts

Step 6: 检查排版
- 是否有标题？
- 是否有公式？
- 是否有考试模板？
- 是否太长？
- 是否适合打印？
```

---

## 13. Markdown 风格规范

### 13.1 标题层级

```markdown
# 文档标题

## 大模块

### 概念或例题

#### 子部分
```

不要跳级，例如不要从 `##` 直接跳到 `####`。

---

### 13.2 表格优先

推荐：

```markdown
| Situation | Method |
|---|---|
| fixed n, independent trials | Binomial |
| without replacement | Hypergeometric |
```

不推荐：

```markdown
当有固定 n 次独立试验的时候我们用 Binomial，而如果是不放回抽样则用 Hypergeometric……
```

---

### 13.3 公式格式

独立公式用：

```markdown
\[
E[X]=\int x f_X(x)\,dx
\]
```

行内公式用：

```markdown
\(X \sim \mathrm{Binomial}(n,p)\)
```

---

### 13.4 警告和考试提示

```markdown
> Warning: Continuous PDF is not probability. \(P(X=x)=0\).

> Exam Tip: Always determine the support before integrating.
```

---

### 13.5 代码块用于模板

```markdown
```text
Step 1: Define X
Step 2: Identify distribution
Step 3: Plug into formula
```
```

---

## 14. 示例：一个完整概念块

```markdown
<a id="c-trans-001"></a>

### C-TRANS-001 — CDF Method

**Tags:** `#cdf-method` `#transformation` `#piecewise-transform`  
**Related Examples:** [EX-TRANS-001](#ex-trans-001), [EX-TRANS-002](#ex-trans-002)  
**Depth Level:** Must Understand

#### One-line Definition

CDF method finds the distribution of \(Y=g(X)\) by directly computing \(F_Y(y)=P(Y\le y)\).

#### When to Use

Use CDF method when:

- \(g(X)\) is not one-to-one;
- \(g(X)\) is piecewise;
- \(Y=\max(X_1,X_2)\);
- \(Y=\min(X_1,X_2)\);
- direct PDF transformation is messy.

#### Key Formula

\[
F_Y(y)=P(Y\le y)=P(g(X)\le y)
\]

#### Exam Template

```text
1. Write F_Y(y)=P(Y≤y).
2. Replace Y by g(X).
3. Solve the x-region satisfying g(X)≤y.
4. Integrate f_X over that region.
5. Differentiate if f_Y is required.
```

#### Common Traps

> Warning: If \(g\) is not one-to-one, do not blindly use the inverse function formula.

#### Paper-only or Must Understand?

- Formula: Put on paper.
- Region solving: Must understand.
```

---

## 15. 示例：一个完整例题块

```markdown
<a id="ex-trans-001"></a>

### EX-TRANS-001 — Maximum of Two Exponential Random Variables

**Concept Tags:** `#cdf-method` `#max-rv` `#exponential` `#independence`  
**Related Concepts:** [C-TRANS-001](#c-trans-001), [C-DIST-EXP](#c-dist-exp), [C-INDEP-001](#c-indep-001)  
**Difficulty:** Core

#### Problem Pattern

Let \(X_1,X_2\) be iid exponential random variables. Find the PDF of

\[
Y=\max(X_1,X_2).
\]

#### Given Information

\[
F_X(x)=1-e^{-\lambda x}, \quad x>0
\]

#### Solution Steps

1. Start from the CDF.

\[
F_Y(y)=P(Y\le y)
\]

2. Substitute \(Y=\max(X_1,X_2)\).

\[
F_Y(y)=P(X_1\le y, X_2\le y)
\]

3. Use independence.

\[
F_Y(y)=F_X(y)^2=(1-e^{-\lambda y})^2
\]

4. Differentiate.

\[
f_Y(y)=2\lambda e^{-\lambda y}-2\lambda e^{-2\lambda y}, \quad y>0
\]

#### Final Answer

\[
f_Y(y)=
\begin{cases}
2\lambda e^{-\lambda y}-2\lambda e^{-2\lambda y}, & y>0,\\
0, & otherwise.
\end{cases}
\]

#### What This Example Tests

- CDF method;
- max random variable;
- independence;
- exponential CDF;
- differentiation from CDF to PDF.

#### Mistakes to Avoid

> Warning: \(Y\le y\) for a maximum means both \(X_1\le y\) and \(X_2\le y\).
```

---

## 16. 文档质量检查清单

每次更新后检查：

```markdown
## Update Checklist

- [ ] 新概念是否有 Concept ID？
- [ ] 新例题是否有 Example ID？
- [ ] 是否添加了 Tags？
- [ ] 概念处是否写了 Related Examples？
- [ ] 例题处是否写了 Related Concepts？
- [ ] Concept-to-Example Map 是否更新？
- [ ] Tag Index 是否更新？
- [ ] 是否有考试模板？
- [ ] 是否有 Common Traps？
- [ ] 是否太长，能否压缩？
- [ ] 是否适合打印？
```

---

## 17. 最终原则

这份 cheating sheet 不是百科全书。

它应该服务于考试中的三个动作：

```text
1. 识别题型
2. 找到模板
3. 快速代入
```

因此每个板块都应该回答：

```text
这是什么？
什么时候用？
公式是什么？
怎么做题？
容易错在哪里？
对应哪些例题？
```
