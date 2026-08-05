# 02 - Reference Distributions and Confidence Intervals

> 这一章训练 Z、t、chi-square、F 的识别，以及均值、方差和均值差置信区间。

---

## Example 1 - Choose the reference distribution

### Problem

For each setting, identify the appropriate reference distribution and degrees of freedom when applicable.

1. A normal population mean, known population standard deviation.
2. A normal population mean, unknown population standard deviation.
3. A normal population variance.
4. The ratio of two independent normal-population sample variances.

### 中文分析

这四个分布要与“参数类型 + 已知/未知条件 + 样本关系”绑定记忆。

### Solution

1. Use the standard normal distribution:
   \[
   Z=\frac{\bar X-\mu}{\sigma/\sqrt n}.
   \]

2. Use Student's t distribution with \(n-1\) degrees of freedom:
   \[
   T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}.
   \]

3. Use the chi-square distribution with \(n-1\) degrees of freedom:
   \[
   \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
   \]

4. Use the F distribution with numerator df \(n_1-1\) and denominator df \(n_2-1\):
   \[
   \frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}
   \sim F_{n_1-1,n_2-1}.
   \]

---

## Example 2 - Mean confidence interval with known sigma

### Problem

A process output is normally distributed with known standard deviation \(\sigma=12\). A sample of \(n=36\) observations has mean \(ar x=50\). Construct a 95% confidence interval for the population mean.

### 中文分析

总体标准差已知，因此用 Z interval。95% 双侧临界值为 \(z_{0.975}=1.96\)。

### Solution

The confidence interval is

\[
\bar x\pm z_{0.975}\frac{\sigma}{\sqrt n}.
\]

Substitute the values:

\[
50\pm1.96\frac{12}{\sqrt{36}}
=50\pm1.96(2)
=50\pm3.92.
\]

Therefore,

\[
\boxed{(46.08,53.92)}.
\]

We are 95% confident that the procedure used to construct the interval captures the true population mean.

### 易错点

不要写“\(\mu\) 有 95% 概率位于这个已经算出的区间内”。频率学派中参数是固定的，随机的是区间构造过程。

---

## Example 3 - Mean confidence interval with unknown sigma

### Problem

A normal-population sample has \(n=16\), \(ar x=82\), and \(s=8\). Construct a 95% confidence interval for \(\mu\).

### 中文分析

总体标准差未知，且样本量小，所以必须使用 \(t_{15}\)。

### Solution

Use

\[
\bar x\pm t_{0.975,15}\frac{s}{\sqrt n}.
\]

With \(t_{0.975,15}\approx2.131\),

\[
82\pm2.131\frac8{4}
=82\pm4.262.
\]

Thus,

\[
\boxed{(77.74,86.26)}.
\]

---

## Example 4 - Confidence interval for a normal-population variance

### Problem

A normal-population sample has \(n=20\) and sample variance \(s^2=25\). Construct a 95% confidence interval for \(\sigma^2\), and then for \(\sigma\).

Use

\[
\chi^2_{0.975,19}=32.852,
\qquad
\chi^2_{0.025,19}=8.907.
\]

### 中文分析

方差区间的上下界分母顺序非常容易写反。大的卡方分位数放在下界分母。

### Solution

For a normal population,

\[
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
\]

The 95% confidence interval for \(\sigma^2\) is

\[
\left(
\frac{(n-1)s^2}{\chi^2_{0.975,19}},
\frac{(n-1)s^2}{\chi^2_{0.025,19}}
\right).
\]

Since \((n-1)s^2=19(25)=475\),

\[
\left(
\frac{475}{32.852},
\frac{475}{8.907}
\right)
=(14.46,53.33).
\]

Therefore,

\[
\boxed{14.46<\sigma^2<53.33}.
\]

Taking square roots gives the interval for \(\sigma\):

\[
\boxed{3.80<\sigma<7.30}.
\]

---

## Example 5 - Pooled confidence interval for two means

### Problem

Two independent normal samples are assumed to have equal variances. The summary statistics are

\[
n_1=10,\quad \bar x_1=82,\quad s_1=6,
\]

\[
n_2=12,\quad \bar x_2=76,\quad s_2=5.
\]

Construct a 95% confidence interval for \(\mu_1-\mu_2\).

### 中文分析

方差相等且两样本独立，使用 pooled t interval，自由度为 \(10+12-2=20\)。

### Solution

First compute the pooled variance:

\[
s_p^2
=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}
\]

\[
=\frac{9(36)+11(25)}{20}
=29.95.
\]

Thus,

\[
s_p=5.473.
\]

The standard error is

\[
SE=s_p\sqrt{\frac1{n_1}+\frac1{n_2}}
=5.473\sqrt{\frac1{10}+\frac1{12}}
=2.343.
\]

Using \(t_{0.975,20}=2.086\),

\[
(\bar x_1-\bar x_2)
\pm t^*SE
=6\pm2.086(2.343).
\]

Therefore,

\[
\boxed{(1.11,10.89)}.
\]

Because 0 is not in the interval, the data indicate a difference between the two population means at the 5% level.

---

## Example 6 - Welch confidence interval

### Problem

Two independent samples have

\[
n_1=8,\quad \bar x_1=15,\quad s_1=4,
\]

\[
n_2=12,\quad \bar x_2=10,\quad s_2=2.
\]

The population variances should not be assumed equal. Construct a 95% confidence interval for \(\mu_1-\mu_2\).

### 中文分析

不合并方差。标准误直接使用 \(s_1^2/n_1+s_2^2/n_2\)，自由度用 Welch-Satterthwaite 近似。

### Solution

The standard error is

\[
SE=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
=\sqrt{\frac{16}{8}+\frac4{12}}
=1.528.
\]

The approximate degrees of freedom are

\[
\nu=
\frac{(s_1^2/n_1+s_2^2/n_2)^2}
{(s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)}
\approx9.36.
\]

Using \(t_{0.975,9.36}\approx2.249\),

\[
5\pm2.249(1.528).
\]

Therefore,

\[
\boxed{(1.56,8.44)}.
\]

---

## Example 7 - Derive a variance interval from the pivot

### Problem

Starting from

\[
P\left(
\chi^2_{\alpha/2,n-1}
\le
\frac{(n-1)S^2}{\sigma^2}
\le
\chi^2_{1-\alpha/2,n-1}
\right)=1-\alpha,
\]

derive the confidence interval for \(\sigma^2\).

### 中文分析

这是代数方向题。因为 \(\sigma^2\) 在分母中，取倒数时不等号方向会交换。

### Solution

Begin with

\[
\chi^2_{\alpha/2,n-1}
\le
\frac{(n-1)S^2}{\sigma^2}
\le
\chi^2_{1-\alpha/2,n-1}.
\]

Taking reciprocals reverses the inequalities:

\[
\frac1{\chi^2_{\alpha/2,n-1}}
\ge
\frac{\sigma^2}{(n-1)S^2}
\ge
\frac1{\chi^2_{1-\alpha/2,n-1}}.
\]

Reorder and multiply by \((n-1)S^2\):

\[
\frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}}
\le
\sigma^2
\le
\frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}}.
\]

Hence,

\[
\boxed{
\left(
\frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}},
\frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}}
\right)
}.
\]

---

## 章末速记

```text
Known sigma -> Z.
Unknown sigma -> t.
One normal variance -> chi-square.
Ratio of two independent normal variances -> F.
Large chi-square critical value goes in the lower-bound denominator.
```
