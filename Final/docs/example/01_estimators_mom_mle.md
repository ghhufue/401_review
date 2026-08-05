# 01 - Estimators, MOM, and MLE

> 这一章对应随机样本、统计量、Bias/Variance/MSE、一致性、矩估计和最大似然估计。

---

## Example 1 - Is it a statistic?

### 题目

Let \(X_1,\ldots,X_n\) be a random sample from a distribution with unknown mean \(\mu\) and variance \(\sigma^2\). Determine which of the following are statistics:

1. \(ar X\)
2. \(ar X-\mu\)
3. \(S^2\)
4. \(\max_i X_i/\sigma\)

### 中文分析

统计量只能由样本和已知常数组成，表达式中不能出现未知参数。

### Solution

1. \(ar X\) is a statistic because it is a function of the sample only.
2. \(ar X-\mu\) is not a statistic because it contains the unknown parameter \(\mu\).
3. \(S^2\) is a statistic because it is computed entirely from the sample.
4. \(\max_i X_i/\sigma\) is not a statistic because it contains the unknown parameter \(\sigma\).

**Answer:** Only \(ar X\) and \(S^2\) are statistics.

### 易错点

“统计量的分布可以依赖未知参数”和“统计量的表达式不能含未知参数”不是一回事。例如 \(ar X\) 是统计量，但它的分布通常仍与 \(\mu,\sigma^2\) 有关。

---

## Example 2 - Expectation and variance of an estimator

### Problem

Suppose \(X_1,\ldots,X_n\overset{iid}{\sim}\operatorname{Poisson}(\lambda)\). Let

\[
T=2\bar X+1.
\]

Find \(E[T]\), \(\operatorname{Var}(T)\), and determine which parameter \(T\) estimates without bias.

### 中文分析

只需要使用 \(E[ar X]=\lambda\) 和 \(\operatorname{Var}(ar X)=\lambda/n\)。

### Solution

Since \(E[X_i]=\lambda\) and \(\operatorname{Var}(X_i)=\lambda\),

\[
E[\bar X]=\lambda,
\qquad
\operatorname{Var}(\bar X)=\frac{\lambda}{n}.
\]

Therefore,

\[
E[T]=E[2\bar X+1]=2\lambda+1,
\]

and

\[
\operatorname{Var}(T)=4\operatorname{Var}(\bar X)
=\frac{4\lambda}{n}.
\]

Thus, \(T\) is an unbiased estimator of

\[
\theta=2\lambda+1.
\]

---

## Example 3 - Bias, variance, and MSE comparison

### Problem

Let \(X_1,\ldots,X_{10}\overset{iid}{\sim}N(\mu,4)\). Consider

\[
T_1=\bar X,
\qquad
T_2=\frac{9}{10}\bar X.
\]

At \(\mu=2\), compare the MSEs of \(T_1\) and \(T_2\).

### 中文分析

无偏不一定代表 MSE 最小。这里 \(T_2\) 有偏，但缩小系数也降低了方差。

### Solution

For \(T_1\),

\[
E[T_1]=\mu,
\qquad
\operatorname{Bias}(T_1)=0,
\]

and

\[
\operatorname{Var}(T_1)=\frac{4}{10}=0.4.
\]

Hence,

\[
\operatorname{MSE}(T_1)=0.4.
\]

For \(T_2\),

\[
E[T_2]=\frac{9}{10}\mu,
\]

so at \(\mu=2\),

\[
\operatorname{Bias}(T_2)=\frac{9}{10}(2)-2=-0.2.
\]

Also,

\[
\operatorname{Var}(T_2)
=\left(\frac{9}{10}\right)^2\frac{4}{10}
=0.324.
\]

Therefore,

\[
\operatorname{MSE}(T_2)
=0.324+(-0.2)^2
=0.364.
\]

Since \(0.364<0.4\), \(T_2\) has the smaller MSE at \(\mu=2\).

### 易错点

MSE 比较可能依赖真实参数值。不能只根据“是否无偏”判断哪个估计量更好。

---

## Example 4 - Method of moments for one parameter

### Problem

Let \(X_1,\ldots,X_n\overset{iid}{\sim}\operatorname{Uniform}(0,	heta)\), where \(	heta>0\). Find the method-of-moments estimator of \(	heta\), and compute its bias and variance.

### 中文分析

单参数 MOM 通常令第一样本矩等于第一总体矩。

### Solution

For \(X\sim\operatorname{Uniform}(0,	heta)\),

\[
E[X]=\frac{\theta}{2}.
\]

Set the sample first moment equal to the population first moment:

\[
\bar X=\frac{\theta}{2}.
\]

Solving for \(	heta\),

\[
\hat\theta_{	ext{MOM}}=2\bar X.
\]

Its expectation is

\[
E[\hat\theta_{	ext{MOM}}]
=2E[\bar X]
=2\cdot\frac{\theta}{2}
=\theta,
\]

so it is unbiased.

Since \(\operatorname{Var}(X)=	heta^2/12\),

\[
\operatorname{Var}(\hat\theta_{	ext{MOM}})
=4\operatorname{Var}(\bar X)
=4\frac{\theta^2}{12n}
=\frac{\theta^2}{3n}.
\]

---

## Example 5 - Method of moments for two parameters

### Problem

Assume \(X_1,\ldots,X_n\) follow a Gamma distribution with shape \(\alpha\) and scale \(eta\), so that

\[
E[X]=\alpha\beta,
\qquad
\operatorname{Var}(X)=\alpha\beta^2.
\]

Suppose the observed sample moments are

\[
m_1'=\frac1n\sum X_i=6,
\qquad
m_2'=\frac1n\sum X_i^2=54.
\]

Find the MOM estimates of \(\alpha\) and \(eta\).

### 中文分析

已知的是原点二阶样本矩 \(m_2'\)，要先得到方差型矩 \(m_2'-(m_1')^2\)。

### Solution

The sample variance based on raw moments is

\[
m_2'-(m_1')^2=54-6^2=18.
\]

Match the first two population moments:

\[
\alpha\beta=6,
\qquad
\alpha\beta^2=18.
\]

Divide the second equation by the first:

\[
\beta=\frac{18}{6}=3.
\]

Then

\[
\alpha=\frac{6}{3}=2.
\]

Therefore,

\[
\hat\alpha_{	ext{MOM}}=2,
\qquad
\hat\beta_{	ext{MOM}}=3.
\]

---

## Example 6 - Interior MLE: Poisson parameter

### Problem

Let \(X_1,\ldots,X_n\overset{iid}{\sim}\operatorname{Poisson}(\lambda)\). For the sample

\[
2,1,0,3,4,
\]

find the MLE of \(\lambda\).

### 中文分析

这是最标准的 log-likelihood 求导题。最后必须说明二阶导为负或似然函数在解处最大。

### Solution

The likelihood is

\[
L(\lambda)
=\prod_{i=1}^n\frac{e^{-\lambda}\lambda^{x_i}}{x_i!}
=e^{-n\lambda}\lambda^{\sum x_i}\prod_{i=1}^n\frac1{x_i!}.
\]

The log-likelihood is

\[
\ell(\lambda)
=-n\lambda+\left(\sum x_i\right)\log\lambda+C.
\]

Differentiate:

\[
\ell'(\lambda)
=-n+\frac{\sum x_i}{\lambda}.
\]

Set \(\ell'(\lambda)=0\):

\[
\hat\lambda=\frac1n\sum x_i=\bar x.
\]

For the given sample,

\[
\hat\lambda=\frac{2+1+0+3+4}{5}=2.
\]

Also,

\[
\ell''(\lambda)=-\frac{\sum x_i}{\lambda^2}<0,
\]

so the solution is a maximum.

---

## Example 7 - Boundary MLE and parameter-dependent support

### Problem

Let \(X_1,\ldots,X_n\overset{iid}{\sim}\operatorname{Uniform}(0,	heta)\), where \(	heta>0\). Find the MLE of \(	heta\).

### 中文分析

这里不能只做普通求导，因为 support 依赖 \(	heta\)。likelihood 中必须保留 indicator。

### Solution

The density is

\[
f(x;\theta)=\frac1\theta I(0\le x\le\theta).
\]

Thus,

\[
L(\theta)
=\theta^{-n}I(\theta\ge X_{(n)}),
\]

where

\[
X_{(n)}=\max(X_1,\ldots,X_n).
\]

For all feasible values \(	heta\ge X_{(n)}\), the factor \(	heta^{-n}\) decreases as \(	heta\) increases. Therefore the likelihood is maximized at the smallest feasible value:

\[
\boxed{\hat\theta_{	ext{MLE}}=X_{(n)}}.
\]

### 易错点

若直接写 \(\ell(	heta)=-n\log	heta\) 后求导，会发现没有驻点。真正的最大值在参数空间边界，由 indicator 决定。

---

## Example 8 - Rayleigh-type MLE matching the sample-exam form

### Problem

Suppose \(X_1,\ldots,X_n\) are i.i.d. with density

\[
f(x;\theta)=\frac{x}{\theta^2}
\exp\left(-\frac{x^2}{2\theta^2}\right),
\qquad x>0,\ \theta>0.
\]

Find the MLE of \(	heta\). Then evaluate it for the sample \(1,2,3,4\).

### 中文分析

这类题的关键是 log-likelihood 中同时有 \(-2n\log	heta\) 和 \(-\sum x_i^2/(2	heta^2)\)。

### Solution

The likelihood is

\[
L(\theta)
=\prod_{i=1}^n
\frac{x_i}{\theta^2}
\exp\left(-\frac{x_i^2}{2\theta^2}\right).
\]

The log-likelihood is

\[
\ell(\theta)
=\sum_{i=1}^n\log x_i
-2n\log\theta
-\frac1{2\theta^2}\sum_{i=1}^n x_i^2.
\]

Differentiate:

\[
\ell'(\theta)
=-\frac{2n}{\theta}
+\frac{1}{\theta^3}\sum_{i=1}^n x_i^2.
\]

Set the derivative equal to zero:

\[
-2n\theta^2+\sum_{i=1}^n x_i^2=0.
\]

Hence,

\[
\hat\theta^2_{	ext{MLE}}
=\frac1{2n}\sum_{i=1}^n x_i^2,
\]

and

\[
\boxed{
\hat\theta_{	ext{MLE}}
=\sqrt{\frac1{2n}\sum_{i=1}^n x_i^2}
}.
\]

For \(1,2,3,4\),

\[
\sum x_i^2=1+4+9+16=30,
\]

so

\[
\hat\theta
=\sqrt{\frac{30}{8}}
\approx1.936.
\]

---

## 章末速记

```text
MOM: population moments = sample moments.
MLE: write support -> likelihood -> log -> derivative/boundary -> verify maximum.
MSE = variance + bias^2.
A statistic contains no unknown parameter.
```
