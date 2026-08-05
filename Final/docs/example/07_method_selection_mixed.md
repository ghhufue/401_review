# 07 - Method Selection and Mixed Drills

> 这一章不按公式分类，而是模拟考试时从题目描述中识别方法。先自己回答，再展开答案。

---

## Drill 1 - Known population standard deviation

### Problem

A machine fills bottles. The historical population standard deviation is known to be 2 mL. A random sample of 40 bottles is used to test whether the mean fill differs from 500 mL.

State the method, hypotheses, reference distribution, and tail direction.

### 中文分析

一个总体均值，\(\sigma\) 已知，关键词 “differs” 表示双侧。

### Answer

Use a one-sample Z test.

\[
H_0:\mu=500,
\qquad
H_a:\mu\ne500.
\]

\[
Z=\frac{\bar X-500}{2/\sqrt{40}}\sim N(0,1)
\quad	ext{under }H_0.
\]

This is a two-sided test.

---

## Drill 2 - Unknown sigma, small normal sample

### Problem

Twelve observations are sampled from an approximately normal population. The population standard deviation is unknown. Test whether the population mean is below 30.

### Answer

Use a one-sample t test.

\[
H_0:\mu=30,
\qquad
H_a:\mu<30.
\]

\[
T=\frac{\bar X-30}{S/\sqrt{12}}\sim t_{11}.
\]

This is a left-tailed test.

---

## Drill 3 - One population variance

### Problem

A process is assumed normal. Determine whether its variance exceeds \(16\) using a sample of 20 observations.

### Answer

Use a one-sample chi-square variance test.

\[
H_0:\sigma^2=16,
\qquad
H_a:\sigma^2>16.
\]

\[
\chi^2=\frac{19S^2}{16}\sim\chi^2_{19}.
\]

This is a right-tailed test.

---

## Drill 4 - Two independent means with equal variances

### Problem

Two random samples come from independent normal populations. Previous process knowledge supports the equal-variance assumption. Compare the two population means.

### Answer

Use a pooled two-sample t test.

\[
H_0:\mu_1-\mu_2=0.
\]

The statistic is

\[
T=
\frac{\bar X_1-\bar X_2}
{S_p\sqrt{1/n_1+1/n_2}}
\sim t_{n_1+n_2-2}.
\]

### 中文提醒

“独立”决定不是 paired；“方差相等”决定 pooled，而不是 Welch。

---

## Drill 5 - Two independent means with unequal variances

### Problem

Two independent groups have strongly different sample variances and unequal sample sizes. Both groups are approximately normal. Compare their means.

### Answer

Use Welch's two-sample t test.

\[
T=
\frac{(\bar X_1-\bar X_2)-\Delta_0}
{\sqrt{S_1^2/n_1+S_2^2/n_2}}.
\]

Use Welch-Satterthwaite degrees of freedom. Do not pool the sample variances.

---

## Drill 6 - Same subjects before and after

### Problem

Fifteen patients have cholesterol measured before and after treatment. The differences are approximately normal. Test whether treatment lowers mean cholesterol.

### 中文分析

定义差值方向时要与备择假设一致。例如 \(D=	ext{before}-	ext{after}\)，降低对应 \(D>0\)。

### Answer

Define

\[
D_i=\text{before}_i-\text{after}_i.
\]

Use a paired t test:

\[
H_0:\mu_D=0,
\qquad
H_a:\mu_D>0.
\]

\[
T=\frac{\bar D}{S_D/\sqrt{15}}\sim t_{14}.
\]

---

## Drill 7 - Paired data, direction only

### Problem

The same customers rate a service before and after a change. Ratings are highly irregular, and only whether each rating increased or decreased is considered reliable.

### Answer

Use the sign test. Delete zero differences and let \(Q_+\) be the number of positive differences.

Under \(H_0\),

\[
Q_+\sim\operatorname{Binomial}(n,0.5).
\]

---

## Drill 8 - Paired, nonnormal but symmetric differences

### Problem

Matched-pair differences are nonnormal but roughly symmetric, and their magnitudes can be ranked meaningfully.

### Answer

Use the Wilcoxon signed-rank test.

Compute differences, remove zeros, rank absolute differences, restore signs, and calculate \(W_+\) and \(W_-\).

---

## Drill 9 - Independent ordinal groups

### Problem

Two independent teaching methods are compared using satisfaction ratings from 1 to 5. The ratings are ordinal and heavily tied.

### Answer

Use the Wilcoxon rank-sum / Mann-Whitney U test, with the appropriate tie correction if a normal approximation is used.

### 中文提醒

不是 signed-rank，因为两组学生不是一一配对的。

---

## Drill 10 - Categorical counts

### Problem

Researchers record political-news source preference (TV, website, social media) and age category (young, middle, older) for one random sample. Determine whether the variables are associated.

### Answer

Use a chi-square test of independence.

\[
E_{ij}=\frac{(\text{row total})(\text{column total})}{N},
\]

\[
\chi^2=\sum\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\qquad
df=(r-1)(c-1).
\]

The conclusion should state association, not causation.

---

## Drill 11 - Regression mean response or new observation?

### Problem

A fitted regression model is used at \(x_0\). Determine which interval is required:

1. Estimate the average response of all units with \(x=x_0\).
2. Predict the response of one new unit with \(x=x_0\).

### Answer

1. Use the mean-response confidence interval:
   \[
   \hat y_0\pm t^*s
   \sqrt{\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}.
   \]

2. Use the prediction interval:
   \[
   \hat y_0\pm t^*s
   \sqrt{1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}.
   \]

The prediction interval is wider because it includes individual random error.

---

## Drill 12 - Correlation versus slope

### Problem

In simple linear regression with an intercept, compare the tests

\[
H_0:\beta_1=0
\]

and

\[
H_0:\rho=0.
\]

### Answer

The tests are equivalent in simple linear regression with an intercept. They have the same two-sided t statistic and \(n-2\) degrees of freedom.

Also,

\[
R^2=r^2.
\]

However, neither a significant slope nor significant correlation establishes causation.

---

# Mixed Problem A - From an F test to a mean test

### Problem

Two independent normal samples have

\[
n_1=12,\quad \bar x_1=48,\quad s_1^2=36,
\]

\[
n_2=10,\quad \bar x_2=43,\quad s_2^2=9.
\]

A two-sided F test at \(\alpha=0.05\) rejects equal variances. State the correct next procedure for testing whether the means differ, and write its statistic.

### 中文分析

F 检验结果不是最终研究问题的答案；它帮助决定均值比较时是否可 pooled。

### Solution

Because the equal-variance assumption is rejected, use Welch's two-sample t test:

\[
H_0:\mu_1-\mu_2=0,
\qquad
H_a:\mu_1-\mu_2\ne0.
\]

\[
T
=\frac{48-43}
{\sqrt{36/12+9/10}}.
\]

The reference distribution is approximately t with Welch-Satterthwaite degrees of freedom.

Do not use

\[
S_p^2
=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}.
\]

---

# Mixed Problem B - Full method identification

### Problem

A researcher compares two pain treatments. Patients are randomly assigned to treatment A or B. Pain scores are strongly right-skewed, sample sizes are 9 and 11, and the scores are ordinal. The researcher asks whether treatment A tends to produce lower pain scores.

State the data relationship, method, alternative direction, and conclusion form.

### Solution

The two samples are independent because different patients receive the two treatments.

Use a one-sided Wilcoxon rank-sum / Mann-Whitney U test.

The alternative should be defined so that treatment A tends to have smaller observations than treatment B.

A proper conclusion is:

> There is sufficient/insufficient evidence that the distribution of pain scores under treatment A tends to be lower than under treatment B.

### 中文提醒

不要写成 paired test；也不要在没有位置平移/形状相似假设时直接把结果表述为“两个总体均值不同”。

---

# Mixed Problem C - Assumption failure in regression

### Problem

A scatterplot is curved, and a residual plot shows a U-shaped pattern. A fitted straight-line slope is statistically significant. Should the straight-line model be accepted as adequate?

### Solution

No. A significant slope does not guarantee that the linear model is adequate. The curved scatterplot and U-shaped residual pattern indicate a violation of the linearity assumption.

A model with a nonlinear term, such as a polynomial term, may be considered, followed by another residual check.

---

## 最终方法选择口诀

```text
First ask:
1. What is the response type: quantitative or categorical?
2. One sample, two independent samples, or paired data?
3. Mean, variance, distribution, association, or regression?
4. Are normality/equal-variance assumptions reasonable?
5. One-sided or two-sided research question?

Only then choose the formula.
```
