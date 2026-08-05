# ECE4010J Final 例题集索引

> 本例题集依据 `Final/docs/material`、`Final/docs/README.md` 中的期末考点以及仓库已有 homework 的题面风格整理。题目均为重新设计或改写，不复制公开题库原文。
>
> **语言规则：**题目与解题步骤使用 English；方法识别、易错点、补充分析使用中文。

## 1. 文件目录

| 文件 | 主要内容 | 题量 |
|---|---|---:|
| [`01_estimators_mom_mle.md`](01_estimators_mom_mle.md) | Statistic, Bias, Variance, MSE, Consistency, MOM, MLE | 8 |
| [`02_reference_distributions_ci.md`](02_reference_distributions_ci.md) | Z / t / chi-square / F，均值与方差置信区间 | 7 |
| [`03_one_sample_tests_power.md`](03_one_sample_tests_power.md) | 单样本均值/方差检验，Type I/II error，Power，样本量 | 7 |
| [`04_two_sample_and_paired.md`](04_two_sample_and_paired.md) | F test, pooled t, Welch t, paired t，均值差区间 | 7 |
| [`05_nonparametric_and_categorical.md`](05_nonparametric_and_categorical.md) | Sign, signed-rank, rank-sum, chi-square GOF/independence | 8 |
| [`06_regression_and_correlation.md`](06_regression_and_correlation.md) | OLS, SSE, coefficient inference, prediction, correlation, diagnostics | 8 |
| [`07_method_selection_mixed.md`](07_method_selection_mixed.md) | 检验方法选择与综合题 | 15 |

总计 **60 道例题、方法选择小题与综合题**。其中计算题给出完整但压缩的步骤；方法选择题重点训练“看到题目就知道用什么”。

---

## 2. 建议使用顺序

1. 先做 `01`：保证会从随机样本走到估计量。
2. 再做 `02`：把 Z、t、chi-square、F 和自由度绑定起来。
3. 做 `03`、`04`：练固定的假设检验书写模板。
4. 做 `05`：重点区分 paired/independent 与 parametric/nonparametric。
5. 做 `06`：至少完整手算一次回归全流程。
6. 最后做 `07`：不看公式，只判断方法、假设、尾部和自由度。

---

## 3. 考场统一解题模板

### 3.1 Estimation

```text
1. State the parameter space.
2. Write the population moment or likelihood.
3. Solve for the estimator.
4. Check bias/variance/MSE or verify the maximum when requested.
5. State the final estimator clearly.
```

### 3.2 Hypothesis testing

```text
1. Define the parameter.
2. State H0 and Ha.
3. State assumptions.
4. Write the test statistic and its null distribution.
5. Compute the statistic and degrees of freedom.
6. Compare with a critical value or report the p-value.
7. Make the statistical decision.
8. State the conclusion in context.
```

### 3.3 Regression

```text
1. Compute x-bar, y-bar, Sxx, Sxy, and Syy.
2. Find b1 and b0.
3. Compute fitted values, residuals, SSE, and s^2.
4. Use t_{n-2} for coefficient inference.
5. Distinguish a mean-response interval from a prediction interval.
6. Interpret the result in context and check model assumptions.
```

---

## 4. 一眼选方法

| 题目结构 | 首选方法 | Reference distribution / df |
|---|---|---|
| One mean, known population SD | One-sample Z | Standard normal |
| One mean, unknown population SD | One-sample t | `n-1` |
| One normal-population variance | Chi-square test/CI | `n-1` |
| Two independent means, equal variances | Pooled two-sample t | `n1+n2-2` |
| Two independent means, unequal variances | Welch t | Welch-Satterthwaite df |
| Same subjects measured twice | Paired t on differences | `n-1` pairs |
| Two independent normal variances | F test | `(n1-1, n2-1)` |
| Paired, nonnormal, only directions reliable | Sign test | Binomial `(n, 1/2)` |
| Paired, symmetric differences, ranks usable | Wilcoxon signed-rank | Exact/table/normal approx. |
| Two independent nonnormal/ordinal groups | Wilcoxon rank-sum | Exact/table/normal approx. |
| Categorical counts in a table | Chi-square independence/homogeneity | `(r-1)(c-1)` |
| Fit a straight-line mean relationship | Simple linear regression | Coefficient tests use `t_{n-2}` |
| Test linear correlation | Pearson correlation t-test | `n-2` |

---

## 5. 最常见失分点

- 把 `fail to reject H0` 写成 `accept/prove H0`。
- 配对数据仍使用 two-sample t-test。
- `sigma` unknown 却使用 Z；或总体方差题忘记正态假设。
- pooled t 的合并方差写错，或方差明显不等仍强行 pooled。
- chi-square/F 的左右临界值和分子、分母自由度写反。
- 非参数检验忘记删除 zero differences、处理 ties。
- 列联表输入百分比而不是 counts。
- prediction interval 忘记根号内额外的 `1`。
- 相关显著就宣称因果关系。

---

## 6. 临界值记号

本例题集使用左侧分位数记号：

\[
P(Z\le z_q)=q,\qquad P(T_\nu\le t_{q,\nu})=q.
\]

因此，右尾显著性水平为 `alpha` 时使用 `z_{1-alpha}` 或 `t_{1-alpha,nu}`；双尾时使用 `1-alpha/2`。

---

## 7. 补充题型来源

仓库样卷对 Welch t、单总体方差、power、signed-rank、sign test、回归 mean-response interval 等覆盖较少，因此这些题型参照以下官方公开资料的标准定义与解题结构重新设计：

- NIST/SEMATECH, Chi-Square Test for the Variance: https://www.itl.nist.gov/div898/handbook/eda/section3/eda358.htm
- NIST/SEMATECH, Regression Prediction: https://itl.nist.gov/div898/handbook/pmd/section1/pmd132.htm
- Penn State STAT 415, Tests of Equality of Two Means: https://online.stat.psu.edu/stat415/lesson/11
- Penn State STAT 415, Wilcoxon Tests: https://online.stat.psu.edu/stat415/lesson/20
- Penn State STAT ONLINE, Power Analysis: https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/power-analysis

---

## 8. 最终目标

```text
Recognize the data structure
-> choose the method
-> check assumptions
-> write statistic and reference distribution
-> compute and decide
-> interpret in context.
```
