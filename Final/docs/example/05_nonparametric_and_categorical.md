# 05 - Nonparametric and Categorical Tests

> 这一章训练 Sign test、Wilcoxon signed-rank、Wilcoxon rank-sum，以及 chi-square goodness-of-fit / independence / homogeneity。

---

## Example 1 - Select the nonparametric method

### Problem

Choose the most appropriate method for each situation.

1. The same 12 patients are measured before and after treatment. Only the direction of change is considered reliable.
2. The same 12 patients are measured before and after treatment. The differences are roughly symmetric, and their magnitudes are meaningful.
3. Two independent groups provide strongly skewed ordinal ratings.

### 中文分析

三个方法分别对应：配对只看符号、配对看符号与秩、独立两组比较秩。

### Solution

1. Use the sign test.
2. Use the Wilcoxon signed-rank test.
3. Use the Wilcoxon rank-sum test, also called the Mann-Whitney U test.

---

## Example 2 - Sign test

### Problem

Ten paired observations produce nine positive differences and one negative difference; there are no zero differences. Test whether the population median difference is zero against a two-sided alternative at \(\alpha=0.05\).

### 中文分析

在 \(H_0\) 下，正差数 \(Q_+\sim\operatorname{Binomial}(10,0.5)\)。双侧 p-value 要把同样极端的另一侧乘 2。

### Solution

Let \(Q_+\) be the number of positive differences.

Under \(H_0\),

\[
Q_+\sim\operatorname{Binomial}(10,0.5).
\]

The observed value is

\[
Q_+=9.
\]

For a two-sided test,

\[
p=2P(Q_+\ge9).
\]

By symmetry,

\[
p=2P(Q_+\le1).
\]

Thus,

\[
p
=2\left[
\binom{10}{0}\left(\frac12\right)^{10}
+\binom{10}{1}\left(\frac12\right)^{10}
\right]
\]

\[
=2\frac{1+10}{1024}
=0.0215.
\]

Since \(0.0215<0.05\), reject \(H_0\).

**Conclusion:** There is sufficient evidence that the population median difference is not zero.

### 易错点

Zero differences must be removed before determining the effective sample size \(n\).

---

## Example 3 - Wilcoxon signed-rank test

### Problem

The paired differences are

\[
1,2,3,4,5,6,7,8.
\]

Use the Wilcoxon signed-rank test to test whether the median difference is zero against a two-sided alternative.

### 中文分析

绝对值本身就是 1 到 8，因此秩也是 1 到 8。所有差值为正，负秩和为 0。

### Solution

There are no zero differences. Rank the absolute differences:

| Difference | Absolute value | Rank | Signed rank |
|---:|---:|---:|---:|
| 1 | 1 | 1 | +1 |
| 2 | 2 | 2 | +2 |
| 3 | 3 | 3 | +3 |
| 4 | 4 | 4 | +4 |
| 5 | 5 | 5 | +5 |
| 6 | 6 | 6 | +6 |
| 7 | 7 | 7 | +7 |
| 8 | 8 | 8 | +8 |

Therefore,

\[
W_+=1+2+\cdots+8=36,
\qquad
W_-=0.
\]

For a two-sided test, the usual small-sample statistic is

\[
T=\min(W_+,W_-)=0.
\]

The exact two-sided p-value is

\[
p=0.0078125.
\]

Reject \(H_0\) at the 5% level.

**Conclusion:** The paired differences provide strong evidence of a nonzero positive location shift.

### 易错点

Signed-rank 不只是数正负号；它使用绝对差值的秩，因此通常比 sign test 使用更多信息，但常要求差值分布近似对称。

---

## Example 4 - Wilcoxon rank-sum / Mann-Whitney U

### Problem

Two independent groups have observations

\[
A: 8,9,10,11,
\qquad
B: 1,2,3,4.
\]

Use a two-sided Wilcoxon rank-sum test.

### 中文分析

先合并排序再赋秩。这里没有 ties，A 占据最高四个秩。

### Solution

The combined ordered data are

\[
1_B,2_B,3_B,4_B,8_A,9_A,10_A,11_A.
\]

Thus, the rank sum for group A is

\[
R_A=5+6+7+8=26.
\]

The Mann-Whitney statistic for group A is

\[
U_A=R_A-\frac{n_A(n_A+1)}2
=26-\frac{4(5)}2
=16.
\]

Also,

\[
U_B=n_An_B-U_A=16-16=0.
\]

The exact two-sided p-value is

\[
p=\frac{2}{\binom84}
=\frac2{70}
=0.0286.
\]

Since \(p<0.05\), reject \(H_0\).

**Conclusion:** The distributions of the two groups differ; group A tends to have larger observations.

### 易错点

Rank-sum 的结论首先是“分布位置/随机排序倾向不同”。只有在两总体形状相近时，才常被解释为中位数位置差异。

---

## Example 5 - Chi-square goodness-of-fit

### Problem

A genetic model predicts four phenotype proportions in the ratio \(9:3:3:1\). In a sample of 100 offspring, the observed counts are

\[
58,18,20,4.
\]

Test whether the observed distribution is consistent with the model at \(\alpha=0.05\).

### 中文分析

这是一个总体与给定理论比例比较，属于 goodness-of-fit，不是 independence。没有估计参数时自由度为类别数减 1。

### Solution

The null proportions are

\[
\frac9{16},\frac3{16},\frac3{16},\frac1{16}.
\]

The expected counts are

\[
E=(56.25,18.75,18.75,6.25).
\]

The test statistic is

\[
\chi^2
=\sum_{i=1}^4\frac{(O_i-E_i)^2}{E_i}.
\]

Substitution gives

\[
\chi^2
=\frac{(58-56.25)^2}{56.25}
+\frac{(18-18.75)^2}{18.75}
\]

\[
+\frac{(20-18.75)^2}{18.75}
+\frac{(4-6.25)^2}{6.25}
=0.978.
\]

The degrees of freedom are

\[
df=4-1=3.
\]

The p-value is approximately

\[
p=0.807.
\]

Fail to reject \(H_0\).

**Conclusion:** The data are consistent with the proposed \(9:3:3:1\) distribution.

---

## Example 6 - Chi-square test of independence

### Problem

A survey records preferred product category for two age groups:

| Age group | Product A | Product B | Product C | Total |
|---|---:|---:|---:|---:|
| Younger | 34 | 18 | 8 | 60 |
| Older | 16 | 27 | 17 | 60 |
| Total | 50 | 45 | 25 | 120 |

Test whether age group and product preference are independent at \(\alpha=0.05\).

### 中文分析

期望频数由行总数乘列总数除以总样本量。两行总数相同，所以两行期望值相同。

### Solution

The hypotheses are

\[
H_0:\text{age group and product preference are independent},
\]

\[
H_a:\text{they are associated}.
\]

For each row, the expected counts are

\[
E=(25,22.5,12.5).
\]

The chi-square statistic is

\[
\chi^2
=2\left[
\frac{(34-25)^2}{25}
+\frac{(18-22.5)^2}{22.5}
+\frac{(8-12.5)^2}{12.5}
\right].
\]

Thus,

\[
\chi^2=11.52.
\]

The degrees of freedom are

\[
df=(2-1)(3-1)=2.
\]

The p-value is approximately

\[
p=0.00315.
\]

Reject \(H_0\).

**Conclusion:** There is significant evidence that age group and product preference are associated.

### 易错点

显著关联不等于年龄导致偏好变化。观察性数据通常不能直接给出因果结论。

---

## Example 7 - Independence versus homogeneity

### Problem

Explain the difference between a chi-square test of independence and a chi-square test of homogeneity.

### Solution

A test of independence uses one population and asks whether two categorical variables are associated within that population.

A test of homogeneity uses multiple populations or treatment groups and asks whether they have the same categorical distribution.

Both tests use

\[
\chi^2=\sum\frac{(O-E)^2}{E}
\]

and degrees of freedom

\[
(r-1)(c-1),
\]

but the sampling design and contextual conclusion are different.

---

## Example 8 - Expected-count condition

### Problem

A \(2\times3\) contingency table has expected counts

\[
12.0, 8.5, 1.5, 10.0, 7.0, 1.0.
\]

Should the ordinary chi-square approximation be trusted without modification?

### 中文分析

该课程材料要求检查期望频数不能过小。两个单元格明显低于 5。

### Solution

No. Several expected counts are too small for the ordinary chi-square approximation to be reliable. Categories may need to be combined when scientifically reasonable, or an exact method should be considered.

---

## 章末速记

```text
Paired + signs only -> sign test.
Paired + signed ranks -> Wilcoxon signed-rank.
Independent groups + ranks -> Wilcoxon rank-sum.
One categorical variable vs fixed proportions -> chi-square GOF.
Two categorical variables / several populations -> chi-square table test.
```
