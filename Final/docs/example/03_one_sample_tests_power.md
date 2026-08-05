# 03 - One-Sample Tests, Errors, and Power

> 这一章训练统一假设检验模板、单侧/双侧判断、单总体方差检验、Type I/II error、power 和样本量。

---

## Example 1 - One-sample t test, right-tailed

### Problem

A manufacturer claims that the mean lifetime of a component is 100 hours. A random sample of \(n=25\) components has \(ar x=104\) and \(s=10\). Assuming normality, test whether the true mean lifetime is greater than 100 hours at \(\alpha=0.05\).

### 中文分析

总体标准差未知，单样本均值，使用 one-sample t。题目中的 “greater than” 决定右尾。

### Solution

Let \(\mu\) be the population mean lifetime.

\[
H_0:\mu=100,
\qquad
H_a:\mu>100.
\]

The test statistic is

\[
T=\frac{\bar X-\mu_0}{S/\sqrt n}\sim t_{n-1}
\quad	ext{under }H_0.
\]

Compute

\[
t=\frac{104-100}{10/\sqrt{25}}=\frac4{2}=2.00.
\]

The degrees of freedom are

\[
df=25-1=24.
\]

The right-tail critical value is

\[
t_{0.95,24}\approx1.711.
\]

Since

\[
2.00>1.711,
\]

reject \(H_0\). Equivalently, the one-sided p-value is approximately \(0.0285\).

**Conclusion:** There is sufficient evidence at the 5% level that the population mean lifetime exceeds 100 hours.

---

## Example 2 - Two-sided test using a confidence interval

### Problem

A 95% confidence interval for a population mean is \((48.2,53.7)\). Test

\[
H_0:\mu=55
\qquad	ext{versus}\qquad
H_a:\mu\ne55
\]

at \(\alpha=0.05\).

### 中文分析

双侧检验与同置信水平的双侧区间互为对偶。无需重新算统计量。

### Solution

The null value \(55\) is not contained in the 95% confidence interval \((48.2,53.7)\).

Therefore, reject \(H_0\) at the 5% significance level.

**Conclusion:** The data provide sufficient evidence that the population mean differs from 55.

### 易错点

这一对偶关系只直接对应同一个参数、同一个模型下的双侧检验和 \(100(1-\alpha)\%\) 双侧区间。

---

## Example 3 - Chi-square test for one variance

### Problem

A quality-control engineer wants to determine whether the population standard deviation exceeds 4 units. A normal-population sample of \(n=15\) has sample standard deviation \(s=6\). Test at \(\alpha=0.05\).

Use

\[
\chi^2_{0.95,14}=23.685.
\]

### 中文分析

检验对象是标准差，但统计量使用方差。题目是 “exceeds”，所以是右尾检验。

### Solution

Let \(\sigma\) be the population standard deviation.

\[
H_0:\sigma=4,
\qquad
H_a:\sigma>4.
\]

For a normal population,

\[
\chi^2=\frac{(n-1)S^2}{\sigma_0^2}
\sim\chi^2_{n-1}
\quad	ext{under }H_0.
\]

Compute

\[
\chi^2
=\frac{14(6^2)}{4^2}
=\frac{14(36)}{16}
=31.5.
\]

The degrees of freedom are \(14\). Since

\[
31.5>23.685,
\]

reject \(H_0\).

**Conclusion:** There is sufficient evidence that the population standard deviation exceeds 4 units.

### 易错点

单总体方差的精确 chi-square 检验强依赖总体正态性。

---

## Example 4 - Type I and Type II errors in context

### Problem

A hospital tests

\[
H_0:\text{a new treatment has no improvement}
\]

against

\[
H_a:\text{the new treatment improves outcomes}.
\]

Describe a Type I error and a Type II error in context.

### 中文分析

先用“真实状态”和“做出的决定”组织语言，不要只背定义。

### Solution

A Type I error occurs if the hospital concludes that the new treatment improves outcomes when, in fact, it does not improve outcomes.

A Type II error occurs if the hospital fails to detect an improvement when the new treatment truly improves outcomes.

The probability of a Type I error is \(\alpha\). The probability of a Type II error at a particular alternative value is \(eta\), and the power is \(1-eta\).

---

## Example 5 - Compute power for a one-sided Z test

### Problem

Suppose \(X_1,\ldots,X_{25}\) are sampled from a normal population with known \(\sigma=10\). Test

\[
H_0:\mu=100
\qquad	ext{versus}\qquad
H_a:\mu>100
\]

at \(\alpha=0.05\). Find the power when the true mean is \(\mu=105\).

### 中文分析

Power 的步骤是：先在 \(H_0\) 下求拒绝域，再在真实备择参数下计算落入该拒绝域的概率。

### Solution

Reject \(H_0\) when

\[
Z=\frac{\bar X-100}{10/\sqrt{25}}>z_{0.95}=1.645.
\]

Since \(10/\sqrt{25}=2\), this is equivalent to

\[
\bar X>100+1.645(2)=103.29.
\]

When the true mean is \(105\),

\[
\bar X\sim N\left(105,\frac{10^2}{25}\right)
=N(105,4).
\]

Therefore,

\[
\text{Power}
=P_{\mu=105}(\bar X>103.29).
\]

Standardize under \(\mu=105\):

\[
P\left(
Z>\frac{103.29-105}{2}
\right)
=P(Z>-0.855).
\]

Thus,

\[
\text{Power}=\Phi(0.855)\approx0.803.
\]

\[
\boxed{\text{Power}\approx0.803}.
\]

### 含义

若真实均值确实为 105，这个检验大约有 80.3% 的概率正确拒绝 \(H_0\)。

---

## Example 6 - Required sample size for target power

### Problem

For the same one-sided Z test, determine the minimum sample size needed to detect an increase from \(\mu_0=100\) to \(\mu_1=105\) with \(\alpha=0.05\), power \(0.90\), and known \(\sigma=10\).

Use

\[
z_{0.95}=1.645,
\qquad
z_{0.90}=1.282.
\]

### 中文分析

单侧已知方差均值检验的样本量公式来自令备择分布下拒绝概率达到目标 power。

### Solution

For a one-sided Z test,

\[
n
=\left[
\frac{(z_{1-\alpha}+z_{1-\beta})\sigma}{\mu_1-\mu_0}
\right]^2.
\]

Substitute the values:

\[
n
=\left[
\frac{(1.645+1.282)(10)}{5}
\right]^2.
\]

\[
n=(5.854)^2\approx34.27.
\]

The sample size must be rounded up:

\[
\boxed{n=35}.
\]

### 易错点

样本量永远向上取整；向下取整会使实际 power 低于目标。

---

## Example 7 - How design choices affect power

### Problem

Without calculation, state how each change affects power, holding all other quantities fixed:

1. Increase \(n\).
2. Decrease \(\alpha\).
3. Increase the true effect size \(|\mu-\mu_0|\).
4. Increase \(\sigma\).

### Solution

1. Increasing \(n\) increases power because the standard error decreases.
2. Decreasing \(\alpha\) decreases power because the rejection region becomes more difficult to reach.
3. Increasing the true effect size increases power because the alternative distribution moves farther from the null value.
4. Increasing \(\sigma\) decreases power because the sampling distribution becomes more variable.

---

## 章末速记

```text
Power calculation:
1. Find the rejection region under H0.
2. Recalculate its probability under the true alternative.

Right tail: statistic > upper critical value.
Left tail: statistic < lower critical value.
Two-sided: absolute statistic > two-sided critical value.
```
