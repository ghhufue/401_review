# ECE4010J Midterm Cheating Sheet

> Version: v0.2  
> 用途：考试速查 + 做题模板。中文解释为主，保留关键英文术语。  
> 原则：先识别题型，再套公式；联合分布和变换题永远先写 support。

---

## 0. Quick Index

| 题目问什么 | 去哪里看 | 主模板 |
|---|---|---|
| PMF / PDF / CDF 区分 | [1. Random Variable Basics](#1-random-variable-basics) | 离散求和，连续积分，CDF 通用 |
| 求 \(E[X]\)、\(Var(X)\)、\(E[g(X)]\) | [1.2 Expectation / Variance / LOTUS](#12-expectation--variance--lotus) | 先 \(E[X]\)、\(E[X^2]\)，再方差 |
| 根据文字判断分布 | [2. Distribution Recognition](#2-distribution-recognition) | `Let X = ...` → `X follows ... because ...` |
| 常见分布公式 | [3. Common Distributions](#3-common-distributions) | 查 PMF/PDF、support、mean、variance |
| Binomial 近似 | [4. Approximation](#4-approximation) | Poisson approx / Normal + continuity correction |
| Poisson Process | [5. Poisson Process](#5-poisson-process) | count → Poisson，waiting time → Exponential |
| \(Y=g(X)\) 变换 | [6. Transformation](#6-transformation) | CDF method / inverse formula |
| \(Y=\max\)、\(Y=\min\) | [6.2 Max / Min](#62-max--min) | max 用 CDF，min 用 survival |
| 二维变换 | [6.3 Jacobian](#63-jacobian) | inverse → support → Jacobian |
| Joint pdf 大题 | [7. Joint Distribution](#7-joint-distribution) | support → marginal → conditional → expectation → independence |
| Conditional expectation | [8. Conditional Expectation](#8-conditional-expectation) | \(f_{X|Y}\) → \(E[X|Y=y]\) → \(E[X|Y]\) |
| Covariance / correlation / independence | [9. Covariance and Independence](#9-covariance-and-independence) | \(Cov=E[XY]-E[X]E[Y]\)，独立看 joint 是否可拆 |
| Reliability / hazard / Weibull | [10. Reliability](#10-reliability) | \(R(t)=P(T>t)\)，\(h(t)=f(t)/R(t)\) |
| MGF | [11. MGF Toolkit](#11-mgf-toolkit) | 求矩、独立和、识别分布 |
| 常见坑 | [13. Common Traps](#13-common-traps) | PDF 不是概率；support 不能漏 |

---

## 1. Random Variable Basics

### 1.1 PMF / PDF / CDF

| 名称 | English | 适用 | 含义 | 求概率方式 |
|---|---|---|---|---|
| PMF | probability mass function | discrete | \(p_X(x)=P(X=x)\) | 求和 |
| PDF | probability density function | continuous | 密度，不是点概率 | 积分 |
| CDF | cumulative distribution function | all RVs | \(F_X(x)=P(X\le x)\) | 相减或求导 |

Key formulas:

\[
p_X(x)=P(X=x)
\]

\[
P(a<X<b)=\int_a^b f_X(x)\,dx
\]

\[
F_X(x)=P(X\le x), \qquad f_X(x)=F_X'(x) \text{ for continuous RV}
\]

> Warning: 连续型随机变量 \(P(X=x)=0\)。PDF 的某个点的值不是概率。

### 1.2 Expectation / Variance / LOTUS

Discrete:

\[
E[X]=\sum_x x p_X(x), \qquad E[g(X)]=\sum_x g(x)p_X(x)
\]

Continuous:

\[
E[X]=\int x f_X(x)\,dx, \qquad E[g(X)]=\int g(x)f_X(x)\,dx
\]

Variance:

\[
Var(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2
\]

Linear rules:

\[
E[aX+b]=aE[X]+b, \qquad Var(aX+b)=a^2Var(X)
\]

LOTUS means: 求 \(E[g(X)]\) 时，不一定要先求 \(Y=g(X)\) 的分布。

---

## 2. Distribution Recognition

考试中先写三行：

```text
Let X = [the random quantity].
X follows [distribution] with parameter(s) [...]
because [fixed quantity / random quantity / keyword].
```

| 题目关键词 | Distribution | Fixed quantity | Random quantity |
|---|---|---|---|
| one success/failure trial | Bernoulli(\(p\)) | one trial | 0/1 result |
| number of successes in fixed independent trials | Binomial(\(n,p\)) | \(n,p\) | number of successes |
| first success on which trial | Geometric(\(p\)) | \(p\) | trial number |
| r-th success on which trial | Negative Binomial(\(r,p\)) | \(r,p\) | trial number |
| sampling without replacement | Hypergeometric(\(N,K,n\)) | population and draw size | successes in draw |
| number of events in interval | Poisson(\(\lambda t\)) | rate and time length | event count |
| waiting time until next event | Exponential(rate \(\lambda\)) | rate | waiting time |
| waiting time until k-th event | Gamma | \(k\), rate/scale | waiting time |
| measurement error / large sample | Normal | mean/variance | value |
| lifetime / hazard / reliability | Exponential / Weibull | hazard pattern | failure time |

> Exam Tip: Binomial 和 Hypergeometric 的核心区别是是否 independent / replacement。Poisson 和 Exponential 的核心区别是 count vs waiting time。

---

## 3. Common Distributions

### 3.1 Discrete Distribution Table

| Distribution | Support | PMF | Mean | Variance |
|---|---|---|---|---|
| Bernoulli(\(p\)) | \(0,1\) | \(P(X=1)=p\) | \(p\) | \(p(1-p)\) |
| Binomial(\(n,p\)) | \(0,1,...,n\) | \({n\choose k}p^k(1-p)^{n-k}\) | \(np\) | \(np(1-p)\) |
| Geometric(\(p\)) | \(1,2,...\) | \((1-p)^{k-1}p\) | \(1/p\) | \((1-p)/p^2\) |
| Negative Binomial(\(r,p\)) | \(r,r+1,...\) | \({k-1\choose r-1}p^r(1-p)^{k-r}\) | \(r/p\) | \(r(1-p)/p^2\) |
| Hypergeometric(\(N,K,n\)) | valid \(k\) | \(rac{{K\choose k}{N-K\choose n-k}}{{N\choose n}}\) | \(nK/N\) | \(n\frac KN(1-\frac KN)\frac{N-n}{N-1}\) |
| Poisson(\(\lambda\)) | \(0,1,2,...\) | \(e^{-\lambda}\lambda^k/k!\) | \(\lambda\) | \(\lambda\) |

### 3.2 Continuous Distribution Table

| Distribution | Support | PDF / CDF | Mean | Variance |
|---|---|---|---|---|
| Uniform(\(a,b\)) | \(a<x<b\) | \(f(x)=1/(b-a)\) | \((a+b)/2\) | \((b-a)^2/12\) |
| Exponential(rate \(\lambda\)) | \(x>0\) | \(f(x)=\lambda e^{-\lambda x}\), \(F(x)=1-e^{-\lambda x}\) | \(1/\lambda\) | \(1/\lambda^2\) |
| Exponential(scale \(\beta\)) | \(x>0\) | \(f(x)=\frac1\beta e^{-x/\beta}\) | \(\beta\) | \(\beta^2\) |
| Gamma(shape \(\alpha\), rate \(\lambda\)) | \(x>0\) | \(f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}\) | \(\alpha/\lambda\) | \(\alpha/\lambda^2\) |
| Normal(\(\mu,\sigma^2\)) | \(\mathbb R\) | \(f(x)=\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}\) | \(\mu\) | \(\sigma^2\) |
| Weibull via reliability | \(t>0\) | \(R(t)=e^{-\alpha t^\beta}\) | usually table | usually table |

---

## 4. Approximation

### 4.1 Binomial to Poisson

If \(X\sim Bin(n,p)\), \(n\) large and \(p\) small:

\[
X\approx Pois(\lambda=np)
\]

Use when the problem says rare events / small defect rate / many trials.

### 4.2 Binomial to Normal

If \(X\sim Bin(n,p)\):

\[
\mu=np, \qquad \sigma^2=np(1-p), \qquad \sigma=\sqrt{np(1-p)}
\]

\[
X\approx N(np,np(1-p))
\]

Continuity correction:

\[
P(a\le X\le b)\approx \Phi\left(\frac{b+0.5-\mu}{\sigma}\right)-\Phi\left(\frac{a-0.5-\mu}{\sigma}\right)
\]

| Discrete event | Continuous normal event |
|---|---|
| \(P(X\le b)\) | \(P(Y\le b+0.5)\) |
| \(P(X<b)\) | \(P(Y\le b-0.5)\) |
| \(P(X\ge a)\) | \(P(Y\ge a-0.5)\) |
| \(P(X>a)\) | \(P(Y\ge a+0.5)\) |

---

## 5. Poisson Process

If events arrive at rate \(\lambda\), then \(N_t\) is the number of events by time \(t\)。

\[
N_t-N_s\sim Pois(\lambda(t-s))
\]

\[
P(N_t=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!}
\]

No event:

\[
P(N_t=0)=e^{-\lambda t}
\]

Waiting time until next event \(W\sim Exp(rate=\lambda)\):

\[
P(W>t)=e^{-\lambda t}
\]

Memoryless:

\[
P(W>s+t\mid W>s)=P(W>t)
\]

> Exam Tip: “at least one event in time \(t\)” = \(1-P(N_t=0)=1-e^{-\lambda t}\)。

---

## 6. Transformation

### 6.1 CDF Method / One-dimensional Transformation

Use CDF method when \(Y=g(X)\) is not one-to-one, is piecewise, or has max/min.

\[
F_Y(y)=P(Y\le y)=P(g(X)\le y)
\]

Steps:

1. Fix \(y\)。
2. Solve the x-region satisfying \(g(x)\le y\)。
3. Integrate/sum over that region。
4. Differentiate if \(f_Y(y)\) is required。

If \(Y=g(X)\) is monotone and \(x=g^{-1}(y)\):

\[
f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|
\]

### 6.2 Max / Min

For \(Y=\max(X_1,X_2)\):

\[
F_Y(y)=P(Y\le y)=P(X_1\le y,X_2\le y)
\]

If independent:

\[
F_Y(y)=F_{X_1}(y)F_{X_2}(y)
\]

For \(Y=\min(X_1,X_2)\):

\[
P(Y>y)=P(X_1>y,X_2>y)
\]

If independent:

\[
F_Y(y)=1-[1-F_{X_1}(y)][1-F_{X_2}(y)]
\]

### 6.3 Jacobian

Given \(U=g_1(X,Y), V=g_2(X,Y)\):

1. Solve inverse:

\[
x=x(u,v), \qquad y=y(u,v)
\]

2. Find support of \((u,v)\)。
3. Compute:

\[
J=\left|\frac{\partial(x,y)}{\partial(u,v)}\right|
\]

4. Then:

\[
f_{U,V}(u,v)=f_{X,Y}(x(u,v),y(u,v))J
\]

### 6.4 Sum / Convolution

If \(Z=X+Y\) and \(X,Y\) independent continuous RVs:

\[
f_Z(z)=\int_{-\infty}^{\infty} f_X(x)f_Y(z-x)\,dx
\]

The real work is finding the valid integration interval from support.

---

## 7. Joint Distribution

### 7.1 Marginal / Conditional / Independence

Discrete:

\[
p_X(x)=\sum_y p_{X,Y}(x,y), \qquad p_Y(y)=\sum_x p_{X,Y}(x,y)
\]

Continuous:

\[
f_X(x)=\int f_{X,Y}(x,y)\,dy, \qquad f_Y(y)=\int f_{X,Y}(x,y)\,dx
\]

Conditional:

\[
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
\]

Independence:

\[
f_{X,Y}(x,y)=f_X(x)f_Y(y)
\]

### 7.2 Joint Density Big Problem Template

```text
Given f_XY(x,y):
0. Find support.
1. Normalize if unknown constant c exists: ∫∫ f_XY dxdy = 1.
2. Find marginal: f_Y(y)=∫ f_XY(x,y) dx.
3. Find conditional: f_X|Y(x|y)=f_XY(x,y)/f_Y(y).
4. Find E[X|Y=y]=∫ x f_X|Y(x|y) dx.
5. Use E[X]=E[E[X|Y]] if useful.
6. Check independence: f_XY ?= f_X f_Y.
```

> Warning: 积分上下限来自 support，不是永远 \(-\infty\) 到 \(\infty\)。

---

## 8. Conditional Expectation

\[
E[X\mid Y=y]=\int x f_{X\mid Y}(x\mid y)\,dx
\]

\[
E[X\mid Y]=g(Y)
\]

\[
E[X]=E[E[X\mid Y]]
\]

\[
Var(X)=E[Var(X\mid Y)]+Var(E[X\mid Y])
\]

Difference:

| Expression | Meaning |
|---|---|
| \(E[X\mid Y=y]\) | 固定 \(y\) 后的数字 / function of \(y\) |
| \(E[X\mid Y]\) | 把 \(y\) 替换成随机变量 \(Y\)，所以本身是 random variable |

---

## 9. Covariance and Independence

\[
Cov(X,Y)=E[(X-E[X])(Y-E[Y])]
\]

\[
Cov(X,Y)=E[XY]-E[X]E[Y]
\]

\[
\rho_{X,Y}=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
\]

Logic:

\[
X,Y \text{ independent} \Rightarrow Cov(X,Y)=0
\]

\[
Cov(X,Y)=0 \nRightarrow X,Y \text{ independent}
\]

For jointly Gaussian:

\[
Cov(X,Y)=0 \iff X,Y \text{ independent}
\]

---

## 10. Reliability

Let \(T\) be failure time.

\[
F(t)=P(T\le t), \qquad R(t)=P(T>t)=1-F(t)
\]

\[
h(t)=\rho(t)=\frac{f(t)}{R(t)}
\]

\[
R(t)=\exp\left(-\int_0^t h(s)\,ds\right)
\]

Series system:

\[
R_{series}(t)=\prod_i R_i(t)
\]

Parallel system:

\[
R_{parallel}(t)=1-\prod_i[1-R_i(t)]
\]

Weibull reliability form:

\[
R(t)=e^{-\alpha t^\beta}, \qquad h(t)=\alpha\beta t^{\beta-1}
\]

\[
\beta>1: \text{increasing hazard}, \quad \beta=1: \text{constant hazard}, \quad 0<\beta<1: \text{decreasing hazard}
\]

Event translation:

| English phrase | Event |
|---|---|
| still working at \(t\) | \(T>t\) |
| failed by \(t\) | \(T\le t\) |
| failed between \(a,b\) | \(a<T\le b\) |

---

## 11. MGF Toolkit

\[
M_X(t)=E[e^{tX}]
\]

\[
E[X]=M_X'(0), \qquad E[X^2]=M_X''(0)
\]

\[
Var(X)=M_X''(0)-[M_X'(0)]^2
\]

If \(X,Y\) independent:

\[
M_{X+Y}(t)=M_X(t)M_Y(t)
\]

If two MGFs are the same near \(0\), the distributions are the same.

Common MGFs:

| Distribution | MGF |
|---|---|
| Bernoulli(\(p\)) | \(1-p+pe^t\) |
| Binomial(\(n,p\)) | \((1-p+pe^t)^n\) |
| Poisson(\(\lambda\)) | \(e^{\lambda(e^t-1)}\) |
| Exponential(rate \(\lambda\)) | \(rac{\lambda}{\lambda-t}, t<\lambda\) |
| Normal(\(\mu,\sigma^2\)) | \(e^{\mu t+\frac12\sigma^2t^2}\) |

---

## 12. Worked Examples

### EX-001 — Continuous PDF Probability

**Pattern:** Given PDF, find interval probability.  
**Related:** PMF/PDF/CDF

Given \(f_X(x)=2x\), \(0<x<1\). Find \(P(0.2<X<0.5)\).

\[
P(0.2<X<0.5)=\int_{0.2}^{0.5}2x\,dx=x^2\big|_{0.2}^{0.5}=0.25-0.04=0.21
\]

**Answer:** \(0.21\)

---

### EX-002 — LOTUS

**Pattern:** Find \(E[g(X)]\) directly.  
Given \(X\sim Uniform(0,1)\). Find \(E[X^2]\).

\[
E[X^2]=\int_0^1 x^2\cdot 1\,dx=\frac13
\]

**Answer:** \(1/3\)

---

### EX-003 — Binomial Recognition

100 products are independently defective with probability \(0.02\). Let \(X\) be the number of defective products.

\[
X\sim Bin(100,0.02)
\]

because there are fixed independent trials and each trial has success/failure.

Probability exactly 3 defective:

\[
P(X=3)={100\choose 3}(0.02)^3(0.98)^{97}
\]

---

### EX-004 — Hypergeometric Recognition

A box has 20 items, 5 defective. Draw 4 without replacement. Let \(X\) be defective items drawn.

\[
X\sim Hypergeometric(N=20,K=5,n=4)
\]

\[
P(X=2)=\frac{{5\choose 2}{15\choose 2}}{{20\choose 4}}
\]

**Key:** without replacement → Hypergeometric, not Binomial.

---

### EX-005 — Geometric vs Negative Binomial

If \(X\) is the trial number of the first success:

\[
X\sim Geometric(p), \qquad P(X=k)=(1-p)^{k-1}p
\]

If \(Y\) is the trial number of the 3rd success:

\[
Y\sim NegativeBinomial(r=3,p), \qquad P(Y=k)={k-1\choose 2}p^3(1-p)^{k-3}
\]

---

### EX-006 — Normal Approximation with Continuity Correction

\(X\sim Bin(100,0.3)\). Approximate \(P(25\le X\le 35)\).

\[
\mu=30, \qquad \sigma=\sqrt{100(0.3)(0.7)}=\sqrt{21}
\]

\[
P(25\le X\le 35)\approx P(24.5\le Y\le 35.5)
\]

\[
=\Phi\left(\frac{35.5-30}{\sqrt{21}}\right)-\Phi\left(\frac{24.5-30}{\sqrt{21}}\right)
\]

---

### EX-007 — Poisson Approximation to Binomial

\(X\sim Bin(1000,0.002)\). Approximate \(P(X=3)\).

\[
\lambda=np=2
\]

\[
X\approx Pois(2)
\]

\[
P(X=3)\approx e^{-2}\frac{2^3}{3!}
\]

---

### EX-008 — Poisson Process Count and Waiting Time

Events arrive at rate \(\lambda=2\) per hour.

Number of events in 3 hours:

\[
N_3\sim Pois(6)
\]

No event in 3 hours:

\[
P(N_3=0)=e^{-6}
\]

Wait more than 1 hour for next event:

\[
P(W>1)=e^{-2}
\]

---

### EX-009 — Exponential Memoryless

Let \(W\sim Exp(rate=\lambda)\). Find \(P(W>8\mid W>5)\).

\[
P(W>8\mid W>5)=P(W>5+3\mid W>5)=P(W>3)=e^{-3\lambda}
\]

---

### EX-010 — CDF Method: \(Y=X^2\)

\(X\sim Uniform(-1,1)\), \(Y=X^2\). Find \(F_Y(y)\).

For \(0\le y\le 1\):

\[
F_Y(y)=P(X^2\le y)=P(-\sqrt y\le X\le \sqrt y)=\frac{2\sqrt y}{2}=\sqrt y
\]

\[
F_Y(y)=
\begin{cases}
0, & y<0,\\
\sqrt y, & 0\le y\le 1,\\
1, & y>1.
\end{cases}
\]

---

### EX-011 — Max of Two Independent Uniform Variables

Let \(X_1,X_2\sim Uniform(0,1)\) independent, \(Y=\max(X_1,X_2)\).

For \(0<y<1\):

\[
F_Y(y)=P(X_1\le y,X_2\le y)=y^2
\]

\[
f_Y(y)=2y, \qquad 0<y<1
\]

---

### EX-012 — Min of Two Independent Uniform Variables

Let \(X_1,X_2\sim Uniform(0,1)\) independent, \(Y=\min(X_1,X_2)\).

\[
P(Y>y)=P(X_1>y,X_2>y)=(1-y)^2
\]

\[
F_Y(y)=1-(1-y)^2, \qquad 0<y<1
\]

\[
f_Y(y)=2(1-y)
\]

---

### EX-013 — Jacobian Skeleton

Given \(U=X+Y, V=Y\). Inverse:

\[
x=u-v, \qquad y=v
\]

Jacobian:

\[
J=\left|\frac{\partial(x,y)}{\partial(u,v)}\right|=
\left|\begin{matrix}1&-1\\0&1\end{matrix}\right|=1
\]

\[
f_{U,V}(u,v)=f_{X,Y}(u-v,v)
\]

Final answer must include transformed support.

---

### EX-014 — Convolution: Sum of Two Uniform(0,1)

Let \(X,Y\sim Uniform(0,1)\) independent, \(Z=X+Y\).

\[
f_Z(z)=\int f_X(x)f_Y(z-x)dx
\]

Need \(0<x<1\) and \(0<z-x<1\), so \(z-1<x<z\). Intersect with \(0<x<1\):

For \(0<z<1\): \(0<x<z\), length \(z\), so \(f_Z(z)=z\)。

For \(1\le z<2\): \(z-1<x<1\), length \(2-z\), so \(f_Z(z)=2-z\)。

\[
f_Z(z)=
\begin{cases}
z, & 0<z<1,\\
2-z, & 1\le z<2,\\
0, & otherwise.
\end{cases}
\]

---

### EX-015 — Joint Density Complete Workflow

Suppose \(f_{X,Y}(x,y)=2\), for \(0<x<y<1\), and \(0\) otherwise.

Support:

\[
0<x<y<1
\]

Marginal of \(Y\): for fixed \(y\), \(0<x<y\):

\[
f_Y(y)=\int_0^y 2\,dx=2y, \qquad 0<y<1
\]

Conditional density:

\[
f_{X\mid Y}(x\mid y)=\frac{2}{2y}=\frac1y, \qquad 0<x<y
\]

Conditional expectation:

\[
E[X\mid Y=y]=\int_0^y x\frac1y\,dx=\frac{y}{2}
\]

\[
E[X\mid Y]=\frac{Y}{2}
\]

Independence: not independent because support is triangular, not rectangular.

---

### EX-016 — Normalizing Constant in Joint PDF

Suppose \(f_{X,Y}(x,y)=c(x+y)\), \(0<x<1,0<y<1\). Find \(c\).

\[
1=\int_0^1\int_0^1 c(x+y)\,dxdy
\]

\[
= c\left(\int_0^1\int_0^1 x\,dxdy+\int_0^1\int_0^1 y\,dxdy\right)=c\left(\frac12+\frac12\right)=c
\]

\[
c=1
\]

---

### EX-017 — Independence Check from Joint PDF

Suppose \(f_{X,Y}(x,y)=4xy\), \(0<x<1,0<y<1\).

\[
f_X(x)=\int_0^1 4xy\,dy=2x
\]

\[
f_Y(y)=\int_0^1 4xy\,dx=2y
\]

\[
f_X(x)f_Y(y)=4xy=f_{X,Y}(x,y)
\]

So \(X,Y\) are independent.

---

### EX-018 — Conditional Expectation by Total Expectation

If \(E[X\mid Y]=Y^2\) and \(Y\sim Uniform(0,1)\), then

\[
E[X]=E[E[X\mid Y]]=E[Y^2]=\int_0^1 y^2dy=\frac13
\]

---

### EX-019 — Covariance Calculation

Given \(E[X]=2\), \(E[Y]=3\), \(E[XY]=7\):

\[
Cov(X,Y)=E[XY]-E[X]E[Y]=7-2\cdot 3=1
\]

---

### EX-020 — Covariance Zero Does Not Mean Independent

If \(Cov(X,Y)=0\), then \(X,Y\) are uncorrelated. Do not conclude independent unless jointly Gaussian or joint distribution factorization is given.

For independence, check:

\[
f_{X,Y}(x,y)=f_X(x)f_Y(y)
\]

---

### EX-021 — Reliability Conditional Probability

A device failure time is \(T\). Find probability that it is still working at time \(a\), given that it failed by time \(b\), where \(a<b\).

\[
P(T>a\mid T\le b)=\frac{P(a<T\le b)}{P(T\le b)}
\]

\[
P(a<T\le b)=F(b)-F(a)=R(a)-R(b)
\]

\[
P(T\le b)=1-R(b)
\]

\[
P(T>a\mid T\le b)=\frac{R(a)-R(b)}{1-R(b)}
\]

---

### EX-022 — Series and Parallel Systems

Two independent components have reliabilities \(R_1(t)\), \(R_2(t)\).

Series system works only if both work:

\[
R_s(t)=R_1(t)R_2(t)
\]

Parallel system fails only if both fail:

\[
R_p(t)=1-[1-R_1(t)][1-R_2(t)]
\]

If \(R_1=e^{-\lambda_1 t}\), \(R_2=e^{-\lambda_2 t}\), then series:

\[
R_s(t)=e^{-(\lambda_1+\lambda_2)t}
\]

---

### EX-023 — Weibull Hazard

If \(R(t)=e^{-\alpha t^\beta}\), then

\[
h(t)=\alpha\beta t^{\beta-1}
\]

- \(\beta>1\): hazard increases with time.
- \(\beta=1\): constant hazard, same as exponential form.
- \(0<\beta<1\): hazard decreases with time.

---

### EX-024 — MGF: Sum of Independent Poisson

If \(X\sim Pois(\lambda)\), \(Y\sim Pois(\mu)\), independent:

\[
M_X(t)=e^{\lambda(e^t-1)}, \qquad M_Y(t)=e^{\mu(e^t-1)}
\]

\[
M_{X+Y}(t)=M_X(t)M_Y(t)=e^{(\lambda+\mu)(e^t-1)}
\]

So:

\[
X+Y\sim Pois(\lambda+\mu)
\]

---

### EX-025 — MGF Moment Extraction

Given \(M_X(t)=e^{3t+2t^2}\). Compare with normal MGF \(e^{\mu t+\frac12\sigma^2t^2}\).

\[
\mu=3, \qquad \frac12\sigma^2=2 \Rightarrow \sigma^2=4
\]

So:

\[
X\sim N(3,4)
\]

---

## 13. Common Traps

| Trap | Correct Thinking |
|---|---|
| Treat PDF value as probability | Continuous probability must integrate PDF |
| Forget \(P(X=x)=0\) for continuous RV | Single point probability is zero |
| Confuse independent and disjoint | Independent: \(P(A\cap B)=P(A)P(B)\); disjoint: \(A\cap B=\varnothing\) |
| Covariance zero means independent | False unless jointly Gaussian is given |
| Use Binomial for without replacement | Without replacement → Hypergeometric |
| Forget continuity correction | \(P(a\le X\le b)\) → \(a-0.5\) to \(b+0.5\) |
| Ignore support in joint PDF | Always draw/write support first |
| Conditional density uses wrong denominator | \(f_{X\mid Y}=f_{X,Y}/f_Y\), not divide by \(f_X\) |
| Confuse \(E[X\mid Y=y]\) and \(E[X\mid Y]\) | first is function of \(y\); second is random variable |
| Mix exponential rate and scale | rate \(\lambda\): mean \(1/\lambda\); scale \(\beta\): mean \(\beta\) |
| Use max/min wrong event | max: \(Y\le y\); min: \(Y>y\) often easier |
| Forget transformed support in Jacobian | Formula without support is incomplete |

---

## 14. Final Self-check

- [ ] I can distinguish PMF / PDF / CDF.
- [ ] I can choose sum vs integral.
- [ ] I can identify Binomial / Geometric / Negative Binomial / Hypergeometric.
- [ ] I can identify Poisson count vs Exponential waiting time.
- [ ] I can use normal approximation with continuity correction.
- [ ] I can use CDF method for non-one-to-one transformation.
- [ ] I can handle max/min templates.
- [ ] I remember Jacobian = inverse transform derivative absolute value.
- [ ] I always write support before joint distribution calculations.
- [ ] I can compute marginal, conditional, \(E[X\mid Y]\), and independence.
- [ ] I can translate reliability word problems into \(T\) events.
- [ ] I know independent implies zero covariance, but not conversely.
- [ ] I can use MGF multiplication for independent sums.
