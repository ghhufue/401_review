# 04 - Two-Sample and Paired Procedures

> 这一章训练 F test、pooled t、Welch t、paired t，以及三类数据关系的辨别。

---

## Example 1 - Independent or paired?

### Problem

Identify whether each design produces independent samples or paired observations.

1. Compare exam scores from students in two different classes.
2. Compare blood pressure before and after treatment for the same patients.
3. Compare battery life for batteries randomly assigned to two brands.
4. Compare twins, assigning one twin to treatment A and the other to treatment B.

### 中文分析

判断标准不是“有两列数据”，而是一个观测能否与另一个观测形成自然的一一对应。

### Solution

1. Independent samples.
2. Paired observations.
3. Independent samples.
4. Paired observations because each twin pair forms a matched unit.

---

## Example 2 - F test for equal variances

### Problem

Two independent normal samples have

\[
n_1=12,\quad s_1^2=36,
\qquad
n_2=10,\quad s_2^2=9.
\]

Test

\[
H_0:\sigma_1^2=\sigma_2^2
\qquad	ext{versus}\qquad
H_a:\sigma_1^2\ne\sigma_2^2
\]

at \(\alpha=0.05\). Use

\[
F_{0.975,11,9}=3.912,
\qquad
F_{0.025,11,9}=0.279.
\]

### 中文分析

分子使用第一组方差，所以自由度顺序必须是 \((11,9)\)。双侧检验有上下两个拒绝域。

### Solution

The test statistic is

\[
F=\frac{s_1^2}{s_2^2}
=\frac{36}{9}=4.00.
\]

Under \(H_0\),

\[
F\sim F_{11,9}.
\]

Reject \(H_0\) if

\[
F<0.279
\quad	ext{or}\quad
F>3.912.
\]

Since

\[
4.00>3.912,
\]

reject \(H_0\).

**Conclusion:** There is sufficient evidence that the two population variances are different. A pooled t procedure is not appropriate; use Welch's t procedure for comparing means.

### 易错点

有些老师习惯把较大样本方差放分子，使 \(F\ge1\)，但此时仍要重新对应正确的分子/分母自由度和双侧临界值。

---

## Example 3 - Pooled two-sample t test

### Problem

Two independent normal populations are assumed to have equal variances. The sample summaries are

\[
n_1=10,\quad \bar x_1=82,\quad s_1=6,
\]

\[
n_2=12,\quad \bar x_2=76,\quad s_2=5.
\]

Test whether the population means differ at \(\alpha=0.05\).

### 中文分析

这是双侧 pooled t。前一章已计算过标准误，这里按完整检验格式书写。

### Solution

Let \(\mu_1\) and \(\mu_2\) be the population means.

\[
H_0:\mu_1-\mu_2=0,
\qquad
H_a:\mu_1-\mu_2\ne0.
\]

The pooled variance is

\[
s_p^2
=\frac{9(36)+11(25)}{20}
=29.95,
\qquad
s_p=5.473.
\]

The standard error is

\[
SE=s_p\sqrt{\frac1{10}+\frac1{12}}
=2.343.
\]

The test statistic is

\[
t=\frac{82-76}{2.343}=2.561.
\]

The degrees of freedom are

\[
df=10+12-2=20.
\]

Using \(t_{0.975,20}=2.086\),

\[
|2.561|>2.086.
\]

Reject \(H_0\). The two-sided p-value is approximately \(0.0186\).

**Conclusion:** There is sufficient evidence that the two population means differ.

---

## Example 4 - Welch two-sample t test

### Problem

Two independent samples have

\[
n_1=8,\quad \bar x_1=15,\quad s_1=4,
\]

\[
n_2=12,\quad \bar x_2=10,\quad s_2=2.
\]

Test \(H_0:\mu_1=\mu_2\) against \(H_a:\mu_1
e\mu_2\) at \(\alpha=0.05\), without assuming equal variances.

### 中文分析

Welch 的自由度通常不是整数。计算时可以保留小数或按课程规定向下取整查表。

### Solution

The standard error is

\[
SE=\sqrt{\frac{16}{8}+\frac4{12}}
=1.528.
\]

The test statistic is

\[
t=\frac{15-10}{1.528}=3.273.
\]

The Welch-Satterthwaite degrees of freedom are

\[
\nu\approx9.36.
\]

The two-sided critical value is approximately

\[
t_{0.975,9.36}=2.249.
\]

Since

\[
|3.273|>2.249,
\]

reject \(H_0\). The two-sided p-value is approximately \(0.0091\).

**Conclusion:** There is sufficient evidence that the two population means differ.

---

## Example 5 - Paired t test

### Problem

Eight subjects are measured before and after a training program. Define the improvement as

\[
D_i=\text{after}_i-\text{before}_i.
\]

The observed differences are

\[
2,3,1,4,0,2,3,1.
\]

Assuming the differences are approximately normal, test whether the mean improvement is positive at \(\alpha=0.05\).

### 中文分析

只分析差值这一列。样本量是 8 对，而不是 16 个独立观测。

### Solution

Let \(\mu_D\) be the population mean difference.

\[
H_0:\mu_D=0,
\qquad
H_a:\mu_D>0.
\]

From the differences,

\[
\bar d=2.000,
\qquad
s_D=1.309.
\]

The test statistic is

\[
t=\frac{\bar d-0}{s_D/\sqrt n}
=\frac{2}{1.309/\sqrt8}
=4.320.
\]

The degrees of freedom are

\[
df=8-1=7.
\]

The right-tail critical value is

\[
t_{0.95,7}=1.895.
\]

Since

\[
4.320>1.895,
\]

reject \(H_0\). The one-sided p-value is approximately \(0.0017\).

**Conclusion:** There is strong evidence that the program produces a positive mean improvement.

---

## Example 6 - Confidence interval for a paired mean difference

### Problem

Using the same paired differences, construct a 95% confidence interval for the population mean improvement.

Use \(t_{0.975,7}=2.365\).

### Solution

The standard error is

\[
SE=\frac{s_D}{\sqrt n}
=\frac{1.309}{\sqrt8}
=0.463.
\]

The confidence interval is

\[
\bar d\pm t^*SE
=2.000\pm2.365(0.463).
\]

Thus,

\[
\boxed{(0.905,3.095)}.
\]

Because the entire interval is positive, it agrees with the one-sided test conclusion that the mean improvement is positive.

---

## Example 7 - Why paired analysis may be more powerful

### Problem

Explain why pairing can reduce the standard error when the two measurements within a pair are positively correlated.

### 中文分析

这是一道理解题。核心是差值方差中的协方差项。

### Solution

For a paired difference \(D=X-Y\),

\[
\operatorname{Var}(D)
=\operatorname{Var}(X)+\operatorname{Var}(Y)
-2\operatorname{Cov}(X,Y).
\]

If \(X\) and \(Y\) are positively correlated, then

\[
\operatorname{Cov}(X,Y)>0,
\]

which reduces \(\operatorname{Var}(D)\). A smaller variance of the differences produces a smaller standard error and can increase test power.

### 易错点

只有存在合理配对关系时才能使用 paired analysis，不能为了获得更小标准误而人为乱配对。

---

## 章末速记

```text
Independent + equal variances -> pooled t.
Independent + unequal variances -> Welch t.
Natural one-to-one matching -> paired t on D_i.
F test requires two independent normal samples.
```
