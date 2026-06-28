# ECE4010J Midterm Cheating Sheet Draft

> Version: 初稿 v0.1  
> Purpose: 考试速查用。不是教材，不追求完整证明；优先保留公式、题型识别、解题模板、常见陷阱和例题索引。  
> Language: 中文解释为主，保留关键 English terms。

---

## 0. Quick Index

| What the problem asks | Go to | Main Template |
|---|---|---|
| 区分 PMF / PDF / CDF | [C-RV-001](#c-rv-001) | 离散求和，连续积分，CDF 通用 |
| 求期望 / 方差 / LOTUS | [C-RV-002](#c-rv-002) | 写 \(E[X]\)、\(E[X^2]\)，再 \(Var(X)=E[X^2]-E[X]^2\) |
| 看到题识别分布 | [C-DIST-000](#c-dist-000) | `Let X = ...` → `X follows ... because ...` |
| Binomial / Poisson / Exponential 等公式 | [Formula Table](#8-formula-tables) | 查 PMF/PDF, E, Var, MGF |
| Binomial 近似 | [C-APPROX-001](#c-approx-001) | Poisson approx 或 Normal + continuity correction |
| \(Y=g(X)\) 一维变换 | [C-TRANS-001](#c-trans-001) | CDF method / monotone inverse |
| \(Y=\max\) 或 \(Y=\min\) | [C-TRANS-002](#c-trans-002) | max 用 CDF，min 用 survival |
| 二维变量变换 | [C-TRANS-003](#c-trans-003) | inverse + support + Jacobian |
| 给 joint pdf/pmf | [C-JOINT-001](#c-joint-001) | support → marginal → conditional → expectation → independence |
| 求 \(E[X\mid Y]\) | [C-COND-001](#c-cond-001) | conditional density → integral → replace y by Y |
| 判断 independence / covariance | [C-COV-001](#c-cov-001) | joint = product of marginals；Cov 只看线性相关 |
| Reliability / hazard / Weibull | [C-REL-001](#c-rel-001) | \(R(t)=P(T>t)\), \(h(t)=f(t)/R(t)\) |
| MGF 求矩或独立和 | [C-MGF-001](#c-mgf-001) | \(M_X(t)=E[e^{tX}]\), independent sum → multiply |
| 常见坑 | [Common Traps](#7-common-traps) | PMF/PDF、independent/disjoint、support、continuity correction |

---

## 1. How to Use This Sheet

1. 先看题目关键词，确定题型和分布。
2. 写 `Let X = ...`，明确随机变量定义。
3. 如果是联合分布/变换题，先画或写 support。
4. 只把证明当作理解工具，考试时优先套模板。
5. 查例题时先看 Example ID，再回到对应 Concept ID。

> Exam Tip: 考试时最容易丢分的不是公式，而是 **support / 积分上下限 / 离散连续混用 / 条件事件翻译**。

---

## 2. Concept-to-Example Map

| Concept ID | Concept Name | Tags | Related Examples |
|---|---|---|---|
| [C-RV-001](#c-rv-001) | PMF / PDF / CDF | `#pmf` `#pdf` `#cdf` | [EX-RV-001](#ex-rv-001) |
| [C-RV-002](#c-rv-002) | Expectation / Variance / LOTUS | `#expectation` `#variance` `#lotus` | [EX-RV-002](#ex-rv-002) |
| [C-DIST-000](#c-dist-000) | Distribution Recognition | `#distribution-recognition` | [EX-DIST-001](#ex-dist-001) |
| [C-DIST-001](#c-dist-001) | Discrete Distributions | `#bernoulli` `#binomial` `#geometric` `#poisson` | [EX-DIST-001](#ex-dist-001), [EX-APPROX-001](#ex-approx-001) |
| [C-DIST-002](#c-dist-002) | Continuous Distributions | `#exponential` `#gamma` `#normal` `#weibull` | [EX-REL-001](#ex-rel-001) |
| [C-APPROX-001](#c-approx-001) | Binomial Approximation | `#poisson-approximation` `#normal-approximation` `#continuity-correction` | [EX-APPROX-001](#ex-approx-001) |
| [C-PP-001](#c-pp-001) | Poisson Process | `#poisson-process` `#independent-increments` `#memoryless` | [EX-PP-001](#ex-pp-001) |
| [C-TRANS-001](#c-trans-001) | CDF Method / One-dimensional Transformation | `#cdf-method` `#transformation` | [EX-TRANS-001](#ex-trans-001) |
| [C-TRANS-002](#c-trans-002) | Max / Min Transformation | `#max` `#min` | [EX-TRANS-002](#ex-trans-002) |
| [C-TRANS-003](#c-trans-003) | Jacobian Transformation | `#jacobian` `#multivariate-transformation` | [EX-TRANS-003](#ex-trans-003) |
| [C-JOINT-001](#c-joint-001) | Joint / Marginal / Conditional | `#joint-pdf` `#marginal` `#conditional-density` | [EX-JOINT-001](#ex-joint-001) |
| [C-COND-001](#c-cond-001) | Conditional Expectation | `#conditional-expectation` `#total-expectation` | [EX-JOINT-001](#ex-joint-001), [EX-COND-001](#ex-cond-001) |
| [C-COV-001](#c-cov-001) | Covariance / Correlation / Independence | `#covariance` `#correlation` `#independence` | [EX-COV-001](#ex-cov-001) |
| [C-REL-001](#c-rel-001) | Reliability / Hazard / Weibull | `#reliability` `#hazard-rate` `#weibull` | [EX-REL-001](#ex-rel-001) |
| [C-MGF-001](#c-mgf-001) | MGF Toolkit | `#mgf` `#independent-sums` | [EX-MGF-001](#ex-mgf-001) |

---

## 3. Tag Index

| Tag | Meaning | Related Concepts | Related Examples |
|---|---|---|---|
| `#pmf` | 离散随机变量点概率 | C-RV-001 | EX-RV-001 |
| `#pdf` | 连续随机变量密度 | C-RV-001 | EX-RV-001 |
| `#cdf` | \(F_X(x)=P(X\le x)\)，通用分布函数 | C-RV-001, C-TRANS-001 | EX-RV-001, EX-TRANS-001 |
| `#lotus` | 不求 \(Y=g(X)\) 分布直接求 \(E[g(X)]\) | C-RV-002 | EX-RV-002 |
| `#distribution-recognition` | 题目关键词识别分布 | C-DIST-000 | EX-DIST-001 |
| `#binomial` | 固定 \(n\) 次独立试验成功次数 | C-DIST-001 | EX-DIST-001, EX-APPROX-001 |
| `#poisson` | 固定时间/区域内事件数 | C-DIST-001 | EX-PP-001 |
| `#exponential` | 等下一次事件的时间 | C-DIST-002, C-PP-001 | EX-PP-001, EX-REL-001 |
| `#normal-approximation` | 用正态近似离散分布 | C-APPROX-001 | EX-APPROX-001 |
| `#continuity-correction` | 离散到连续近似时加减 0.5 | C-APPROX-001 | EX-APPROX-001 |
| `#cdf-method` | 变量变换通用方法 | C-TRANS-001 | EX-TRANS-001, EX-TRANS-002 |
| `#jacobian` | 二维变量变换 | C-TRANS-003 | EX-TRANS-003 |
| `#joint-pdf` | 两个随机变量联合密度 | C-JOINT-001 | EX-JOINT-001 |
| `#conditional-expectation` | 条件下的平均值 | C-COND-001 | EX-COND-001 |
| `#covariance` | 线性同向/反向变化趋势 | C-COV-001 | EX-COV-001 |
| `#reliability` | 生存概率 \(R(t)=P(T>t)\) | C-REL-001 | EX-REL-001 |
| `#mgf` | 矩母函数 | C-MGF-001 | EX-MGF-001 |

---

## 4. Core Concepts

<a id="c-rv-001"></a>

### C-RV-001 — PMF / PDF / CDF

**Tags:** `#pmf` `#pdf` `#cdf`  
**Related Examples:** [EX-RV-001](#ex-rv-001)  
**Depth Level:** Must Understand

#### One-line Definition

随机变量 \(X\) 把随机结果映射成数字；PMF/PDF/CDF 是描述 \(X\) 分布的三种方式。

#### When to Use

| Situation | Use |
|---|---|
| 离散变量，问 \(P(X=x)\) | PMF \(p_X(x)\) |
| 连续变量，问区间概率 | PDF 积分 |
| 任意变量，问 \(P(X\le x)\) | CDF \(F_X(x)\) |

#### Key Formulas

\[
p_X(x)=P(X=x)
\]

\[
P(a<X<b)=\int_a^b f_X(x)\,dx
\]

\[
F_X(x)=P(X\le x)
\]

Continuous case:

\[
f_X(x)=F_X'(x), \qquad P(X=x)=0
\]

#### Exam Template

1. 判断 \(X\) 是 discrete 还是 continuous。
2. Discrete → sum PMF。
3. Continuous → integrate PDF。
4. 不确定时先写 CDF，再看能否求导。

#### Common Traps

> Warning: PDF 不是概率，只有积分后才是概率。连续型随机变量 \(P(X=x)=0\)。

---

<a id="c-rv-002"></a>

### C-RV-002 — Expectation / Variance / LOTUS

**Tags:** `#expectation` `#variance` `#lotus`  
**Related Examples:** [EX-RV-002](#ex-rv-002)  
**Depth Level:** Must Understand

#### One-line Definition

Expectation 是长期平均值；Variance 是波动大小；LOTUS 用来直接求 \(E[g(X)]\)。

#### Key Formulas

Discrete:

\[
E[X]=\sum_x x p_X(x), \qquad E[g(X)]=\sum_x g(x)p_X(x)
\]

Continuous:

\[
E[X]=\int_{-\infty}^{\infty} x f_X(x)\,dx, \qquad E[g(X)]=\int_{-\infty}^{\infty} g(x)f_X(x)\,dx
\]

Variance:

\[
Var(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2
\]

Linear rules:

\[
E[aX+b]=aE[X]+b, \qquad Var(aX+b)=a^2Var(X)
\]

#### Exam Template

1. 求 \(E[X]\)。
2. 求 \(E[X^2]\)。
3. 套 \(Var(X)=E[X^2]-E[X]^2\)。
4. 如果问 \(E[g(X)]\)，优先 LOTUS，不一定先求 \(Y=g(X)\) 的分布。

#### Common Traps

> Warning: \(E[g(X)]\ne g(E[X])\) 一般不成立。

---

<a id="c-dist-000"></a>

### C-DIST-000 — Distribution Recognition

**Tags:** `#distribution-recognition`  
**Related Examples:** [EX-DIST-001](#ex-dist-001)  
**Depth Level:** Must Understand

#### One-line Definition

分布识别就是把文字题翻译成“哪个随机变量服从哪个分布”。

#### Recognition Table

| Problem keywords | Distribution | Fixed quantity | Random quantity |
|---|---|---|---|
| one success/failure trial | Bernoulli | one trial | success indicator |
| number of successes in fixed independent trials | Binomial | \(n\) trials | number of successes |
| first success occurs on which trial | Geometric | success probability \(p\) | waiting trial |
| r-th success occurs on which trial | Negative Binomial | \(r,p\) | trial count |
| sampling without replacement | Hypergeometric | population size | successes drawn |
| number of events in fixed interval | Poisson | interval/rate | event count |
| waiting time until next event | Exponential | rate | waiting time |
| waiting time until k-th event | Gamma | \(k\), rate/scale | waiting time |
| large-sample / error / approximation | Normal | mean/variance | continuous value |
| failure time / hazard / reliability | Exponential / Weibull | hazard pattern | lifetime |

#### Exam Template

```text
Let X = [quantity asked by the problem].
X follows [distribution] with parameter(s) [...]
because [keyword / fixed vs random explanation].
```

---

<a id="c-dist-001"></a>

### C-DIST-001 — Discrete Distributions

**Tags:** `#bernoulli` `#binomial` `#geometric` `#negative-binomial` `#hypergeometric` `#poisson`  
**Related Examples:** [EX-DIST-001](#ex-dist-001), [EX-APPROX-001](#ex-approx-001)  
**Depth Level:** Put on Paper + Must Understand recognition

#### Key Formulas

| Distribution | PMF | Mean | Variance |
|---|---|---|---|
| Bernoulli(\(p\)) | \(P(X=1)=p, P(X=0)=1-p\) | \(p\) | \(p(1-p)\) |
| Binomial(\(n,p\)) | \({n\choose k}p^k(1-p)^{n-k}\) | \(np\) | \(np(1-p)\) |
| Geometric(\(p\)) | \(P(X=k)=(1-p)^{k-1}p, k=1,2,...\) | \(1/p\) | \((1-p)/p^2\) |
| Negative Binomial(\(r,p\)) | \({k-1\choose r-1}p^r(1-p)^{k-r}, k=r,r+1,...\) | \(r/p\) | \(r(1-p)/p^2\) |
| Hypergeometric(\(N,K,n\)) | \(\frac{{K\choose k}{N-K\choose n-k}}{{N\choose n}}\) | \(nK/N\) | \(n\frac KN(1-\frac KN)\frac{N-n}{N-1}\) |
| Poisson(\(\lambda\)) | \(e^{-\lambda}\lambda^k/k!\) | \(\lambda\) | \(\lambda\) |

#### Common Traps

- Binomial: with replacement / independent / fixed \(n\)。
- Hypergeometric: without replacement。
- Geometric: first success。Negative Binomial: r-th success。
- Poisson: count in interval，不是等待时间。

---

<a id="c-dist-002"></a>

### C-DIST-002 — Continuous Distributions

**Tags:** `#uniform` `#exponential` `#gamma` `#normal` `#weibull`  
**Related Examples:** [EX-REL-001](#ex-rel-001)  
**Depth Level:** Put on Paper

#### Key Formulas

| Distribution | PDF / CDF | Mean | Variance |
|---|---|---|---|
| Uniform(\(a,b\)) | \(f(x)=1/(b-a), a<x<b\) | \((a+b)/2\) | \((b-a)^2/12\) |
| Exponential(rate \(\lambda\)) | \(f(x)=\lambda e^{-\lambda x}, F(x)=1-e^{-\lambda x}\) | \(1/\lambda\) | \(1/\lambda^2\) |
| Exponential(scale \(\beta\)) | \(f(x)=\frac1\beta e^{-x/\beta}\) | \(\beta\) | \(\beta^2\) |
| Gamma(shape \(\alpha\), rate \(\lambda\)) | \(f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}\) | \(\alpha/\lambda\) | \(\alpha/\lambda^2\) |
| Normal(\(\mu,\sigma^2\)) | \(f(x)=\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}\) | \(\mu\) | \(\sigma^2\) |
| Weibull with \(R(t)=e^{-\alpha t^\beta}\) | \(F(t)=1-e^{-\alpha t^\beta}\) | 查表/按参数 | 查表/按参数 |

#### Exam Template

1. 确认参数是 rate 还是 scale。
2. 写 support。
3. 求概率用 CDF 或积分。
4. Reliability 中优先写 \(R(t)=P(T>t)\)。

> Warning: Exponential 的 rate \(\lambda\) 和 scale \(\beta=1/\lambda\) 很容易混。

---

<a id="c-approx-001"></a>

### C-APPROX-001 — Binomial Approximation

**Tags:** `#poisson-approximation` `#normal-approximation` `#continuity-correction`  
**Related Examples:** [EX-APPROX-001](#ex-approx-001)  
**Depth Level:** Must Understand

#### When to Use

| Situation | Approximation |
|---|---|
| \(n\) large, \(p\) small, \(\lambda=np\) moderate | \(Bin(n,p)\approx Pois(np)\) |
| \(n\) large and \(np,n(1-p)\) large enough | \(Bin(n,p)\approx N(np,np(1-p))\) |

#### Key Formulas

If \(X\sim Bin(n,p)\):

\[
\mu=np, \qquad \sigma^2=np(1-p), \qquad \sigma=\sqrt{np(1-p)}
\]

Normal approximation with continuity correction:

\[
P(a\le X\le b)\approx \Phi\left(\frac{b+0.5-\mu}{\sigma}\right)-\Phi\left(\frac{a-0.5-\mu}{\sigma}\right)
\]

Common corrections:

| Discrete event | Normal interval |
|---|---|
| \(P(X\le b)\) | \(P(Y\le b+0.5)\) |
| \(P(X<b)\) | \(P(Y\le b-0.5)\) |
| \(P(X\ge a)\) | \(P(Y\ge a-0.5)\) |
| \(P(X>a)\) | \(P(Y\ge a+0.5)\) |

---

<a id="c-pp-001"></a>

### C-PP-001 — Poisson Process + Exponential

**Tags:** `#poisson-process` `#exponential` `#independent-increments` `#memoryless`  
**Related Examples:** [EX-PP-001](#ex-pp-001)  
**Depth Level:** Must Understand

#### One-line Definition

Poisson process 描述随机到达事件数；\(N_t\) 是 t 前事件数，相邻到达时间服从 Exponential。

#### Key Formulas

\[
N_t-N_s\sim Pois(\lambda(t-s))
\]

\[
P(N_t=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!}
\]

\[
P(N_t=0)=e^{-\lambda t}
\]

First waiting time \(W_1\sim Exp(rate=\lambda)\):

\[
P(W_1>t)=e^{-\lambda t}
\]

Memoryless:

\[
P(W>s+t\mid W>s)=P(W>t)
\]

#### Exam Template

1. Count in interval → Poisson with mean \(\lambda \times\) length。
2. Waiting time → Exponential。
3. No event in interval → \(P(N_t=0)\)。
4. Non-overlapping intervals → independent increments，可以相乘。

---

<a id="c-trans-001"></a>

### C-TRANS-001 — CDF Method / One-dimensional Transformation

**Tags:** `#cdf-method` `#transformation`  
**Related Examples:** [EX-TRANS-001](#ex-trans-001)  
**Depth Level:** Must Understand

#### When to Use

Use CDF method when \(Y=g(X)\) is non-monotone, piecewise, max/min, or direct inverse is awkward.

#### Key Template

\[
F_Y(y)=P(Y\le y)=P(g(X)\le y)
\]

Steps:

1. Fix \(y\)。
2. Solve x-region satisfying \(g(x)\le y\)。
3. Integrate/sum over that region。
4. If PDF is required, differentiate \(F_Y(y)\)。

#### Monotone Shortcut

If \(Y=g(X)\) is one-to-one and \(x=g^{-1}(y)\):

\[
f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|
\]

> Warning: 非单调函数不要直接套反函数公式，要拆分支或用 CDF method。

---

<a id="c-trans-002"></a>

### C-TRANS-002 — Max / Min Transformation

**Tags:** `#max` `#min` `#cdf-method`  
**Related Examples:** [EX-TRANS-002](#ex-trans-002)  
**Depth Level:** Must Understand

#### Max Template

If \(Y=\max(X_1,X_2)\):

\[
F_Y(y)=P(Y\le y)=P(X_1\le y, X_2\le y)
\]

If independent:

\[
F_Y(y)=F_{X_1}(y)F_{X_2}(y)
\]

#### Min Template

If \(Y=\min(X_1,X_2)\):

\[
P(Y>y)=P(X_1>y, X_2>y)
\]

If independent:

\[
F_Y(y)=1-[1-F_{X_1}(y)][1-F_{X_2}(y)]
\]

---

<a id="c-trans-003"></a>

### C-TRANS-003 — Multivariate Jacobian Transformation

**Tags:** `#jacobian` `#multivariate-transformation`  
**Related Examples:** [EX-TRANS-003](#ex-trans-003)  
**Depth Level:** Put on Paper + Must Understand workflow

#### Key Template

Given \(U=g_1(X,Y), V=g_2(X,Y)\):

1. Solve inverse:

\[
x=x(u,v), \qquad y=y(u,v)
\]

2. Find support of \((u,v)\)。
3. Compute Jacobian:

\[
J=\left|\frac{\partial(x,y)}{\partial(u,v)}\right|
\]

4. Then:

\[
f_{U,V}(u,v)=f_{X,Y}(x(u,v),y(u,v))J
\]

> Warning: Jacobian 最容易漏 support。没有 support，PDF 不完整。

---

<a id="c-joint-001"></a>

### C-JOINT-001 — Joint / Marginal / Conditional / Independence

**Tags:** `#joint-pdf` `#marginal` `#conditional-density` `#independence`  
**Related Examples:** [EX-JOINT-001](#ex-joint-001)  
**Depth Level:** Must Understand

#### Key Formulas

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

#### Joint Density Big Problem Template

```text
Given f_XY(x,y):
0. Find support.
1. Normalize if constant c exists: ∫∫ f_XY dxdy = 1.
2. Find marginal: f_Y(y)=∫ f_XY(x,y) dx.
3. Find conditional: f_X|Y(x|y)=f_XY(x,y)/f_Y(y).
4. Find E[X|Y=y]=∫ x f_X|Y(x|y) dx.
5. Use E[X]=E[E[X|Y]] if useful.
6. Check independence: f_XY ?= f_X f_Y.
```

#### Common Traps

- 积分上下限来自 support，不是永远 \(-\infty\) 到 \(\infty\)。
- 条件分布的 support 可能变。
- 判断 independence 要在整个 support 上成立。

---

<a id="c-cond-001"></a>

### C-COND-001 — Conditional Expectation

**Tags:** `#conditional-expectation` `#total-expectation` `#total-variance`  
**Related Examples:** [EX-JOINT-001](#ex-joint-001), [EX-COND-001](#ex-cond-001)  
**Depth Level:** Must Understand

#### One-line Definition

\(E[X\mid Y=y]\) 是固定 \(y\) 后的数字；\(E[X\mid Y]\) 是把 \(y\) 换成随机变量 \(Y\) 后得到的随机变量。

#### Key Formulas

\[
E[X\mid Y=y]=\int x f_{X\mid Y}(x\mid y)\,dx
\]

\[
E[X\mid Y]=g(Y)
\]

Total expectation:

\[
E[X]=E[E[X\mid Y]]
\]

Total variance:

\[
Var(X)=E[Var(X\mid Y)]+Var(E[X\mid Y])
\]

#### Exam Template

1. Find \(f_{X\mid Y}(x\mid y)\)。
2. Compute \(E[X\mid Y=y]\)。
3. Replace \(y\) by \(Y\)。
4. Use total expectation if it simplifies calculation。

---

<a id="c-cov-001"></a>

### C-COV-001 — Covariance / Correlation / Independence

**Tags:** `#covariance` `#correlation` `#independence` `#uncorrelated`  
**Related Examples:** [EX-COV-001](#ex-cov-001)  
**Depth Level:** Must Understand

#### Key Formulas

\[
Cov(X,Y)=E[(X-E[X])(Y-E[Y])]
\]

\[
Cov(X,Y)=E[XY]-E[X]E[Y]
\]

\[
\rho_{X,Y}=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
\]

#### Important Logic

\[
X,Y\text{ independent} \Rightarrow Cov(X,Y)=0
\]

\[
Cov(X,Y)=0 \nRightarrow X,Y\text{ independent}
\]

For jointly Gaussian random variables:

\[
Cov(X,Y)=0 \iff X,Y\text{ independent}
\]

#### Exam Template

- Check independence: use joint = product of marginals。
- Compute covariance: use \(E[XY]-E[X]E[Y]\)。
- Do not conclude independent only from covariance zero unless jointly Gaussian is given。

---

<a id="c-rel-001"></a>

### C-REL-001 — Reliability / Hazard / Weibull

**Tags:** `#reliability` `#hazard-rate` `#weibull` `#series-system` `#parallel-system`  
**Related Examples:** [EX-REL-001](#ex-rel-001)  
**Depth Level:** Must Understand

#### One-line Definition

Reliability studies failure time \(T\): \(R(t)\) means still working after time \(t\)。

#### Key Formulas

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

Weibull form in notes:

\[
R(t)=e^{-\alpha t^\beta}, \qquad h(t)=\alpha\beta t^{\beta-1}
\]

\[
\beta>1: \text{increasing hazard}, \quad \beta=1: \text{constant hazard}, \quad 0<\beta<1: \text{decreasing hazard}
\]

#### Event Translation

| English phrase | Event |
|---|---|
| still working at time \(t\) | \(T>t\) |
| failed by time \(t\) | \(T\le t\) |
| failed between \(a\) and \(b\) | \(a<T\le b\) |
| still working at \(a\) given failed by \(b\) | \(P(a<T\le b\mid T\le b)\) |

\[
P(T>a\mid T\le b)=\frac{P(a<T\le b)}{P(T\le b)}=\frac{R(a)-R(b)}{1-R(b)}, \quad a<b
\]

---

<a id="c-mgf-001"></a>

### C-MGF-001 — MGF Toolkit

**Tags:** `#mgf` `#moment-extraction` `#independent-sums`  
**Related Examples:** [EX-MGF-001](#ex-mgf-001)  
**Depth Level:** Put on Paper

#### One-line Definition

MGF \(M_X(t)=E[e^{tX}]\) can generate moments and identify distributions.

#### Key Formulas

\[
M_X(t)=E[e^{tX}]
\]

\[
E[X^k]=M_X^{(k)}(0)
\]

\[
E[X]=M_X'(0), \qquad Var(X)=M_X''(0)-[M_X'(0)]^2
\]

If \(X,Y\) independent:

\[
M_{X+Y}(t)=M_X(t)M_Y(t)
\]

If \(M_X(t)=M_Y(t)\) near \(0\), then \(X,Y\) have the same distribution.

---

## 5. Exam Templates

### T1 — Distribution Recognition

```text
Let X = [the random quantity].
Fixed quantity = [...]
Random quantity = [...]
Keyword = [...]
Therefore X ~ [Distribution]([parameters]).
Use [PMF/PDF/CDF] to compute [...].
```

### T2 — Probability from PMF/PDF/CDF

```text
Discrete: P(a≤X≤b)=Σ p_X(x) over valid x.
Continuous: P(a<X<b)=∫_a^b f_X(x)dx.
CDF: P(a<X≤b)=F_X(b)-F_X(a).
```

### T3 — Joint Density Big Problem

```text
1. Write support.
2. Normalize if needed.
3. Marginalize by integrating out the other variable.
4. Conditional = joint / marginal.
5. Conditional expectation = integral of x times conditional density.
6. Independence check = joint ? product of marginals.
```

### T4 — Reliability Conditional Probability

```text
Translate words:
still working at t → T>t
failed by t → T≤t
failed between a,b → a<T≤b
Then use conditional probability: P(A|B)=P(A∩B)/P(B).
```

---

## 6. Worked Examples

<a id="ex-rv-001"></a>

### EX-RV-001 — PMF / PDF / CDF 区分

**Concept Tags:** `#pmf` `#pdf` `#cdf`  
**Related Concepts:** [C-RV-001](#c-rv-001)  
**Problem Pattern:** 判断该求和、积分还是用 CDF。

#### Given Information

A random variable \(X\) is continuous with PDF \(f_X(x)=2x\), \(0<x<1\). Find \(P(0.2<X<0.5)\).

#### Solution Steps

\[
P(0.2<X<0.5)=\int_{0.2}^{0.5}2x\,dx=x^2\big|_{0.2}^{0.5}=0.25-0.04=0.21
\]

#### Final Answer

\[
P(0.2<X<0.5)=0.21
\]

#### What This Example Tests

Continuous probability = area under PDF, not \(f_X(0.5)\)。

---

<a id="ex-rv-002"></a>

### EX-RV-002 — LOTUS 求 \(E[g(X)]\)

**Concept Tags:** `#lotus` `#expectation`  
**Related Concepts:** [C-RV-002](#c-rv-002)  
**Problem Pattern:** 不求新分布，直接求函数期望。

#### Given Information

\(X\sim Uniform(0,1)\). Find \(E[X^2]\).

#### Solution Steps

\[
E[X^2]=\int_0^1 x^2\cdot 1\,dx=\frac13
\]

#### Final Answer

\[
E[X^2]=\frac13
\]

#### Mistakes to Avoid

不要先令 \(Y=X^2\) 再求 \(Y\) 的 PDF；LOTUS 更快。

---

<a id="ex-dist-001"></a>

### EX-DIST-001 — Distribution Recognition Mini Set

**Concept Tags:** `#distribution-recognition` `#binomial` `#poisson` `#exponential`  
**Related Concepts:** [C-DIST-000](#c-dist-000), [C-DIST-001](#c-dist-001), [C-DIST-002](#c-dist-002)

| Problem Pattern | Let X = | Distribution | Reason |
|---|---|---|---|
| 100 independent products, each defective with prob 0.02. Count defectives. | number of defectives | \(Bin(100,0.02)\) | fixed independent trials |
| Calls arrive at rate 3/hour. Count calls in 2 hours. | number of calls in 2h | \(Pois(6)\) | count in interval, mean \(\lambda t\) |
| Same calls. Wait for next call. | waiting time | \(Exp(rate=3)\) | waiting time until next event |
| Draw 5 cards without replacement. Count aces. | number of aces | Hypergeometric | without replacement |

#### What This Example Tests

先判断 fixed quantity 和 random quantity。

---

<a id="ex-approx-001"></a>

### EX-APPROX-001 — Normal Approximation with Continuity Correction

**Concept Tags:** `#normal-approximation` `#continuity-correction` `#binomial`  
**Related Concepts:** [C-APPROX-001](#c-approx-001)

#### Given Information

\(X\sim Bin(100,0.3)\). Approximate \(P(25\le X\le 35)\).

#### Solution Steps

\[
\mu=np=30, \qquad \sigma=\sqrt{np(1-p)}=\sqrt{21}
\]

Continuity correction:

\[
P(25\le X\le 35)\approx P(24.5\le Y\le 35.5)
\]

\[
=\Phi\left(\frac{35.5-30}{\sqrt{21}}\right)-\Phi\left(\frac{24.5-30}{\sqrt{21}}\right)
\]

#### Final Answer

\[
\Phi(1.20)-\Phi(-1.20)
\]

#### Mistakes to Avoid

不要写成 \(25\) 到 \(35\)，要改成 \(24.5\) 到 \(35.5\)。

---

<a id="ex-pp-001"></a>

### EX-PP-001 — Poisson Process Count and Waiting Time

**Concept Tags:** `#poisson-process` `#poisson` `#exponential`  
**Related Concepts:** [C-PP-001](#c-pp-001)

#### Given Information

Events arrive at rate \(\lambda=2\) per hour.

#### Solution Steps

Number in 3 hours:

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

#### What This Example Tests

Count → Poisson；waiting time → Exponential。

---

<a id="ex-trans-001"></a>

### EX-TRANS-001 — CDF Method for \(Y=X^2\)

**Concept Tags:** `#cdf-method` `#transformation`  
**Related Concepts:** [C-TRANS-001](#c-trans-001)

#### Given Information

\(X\sim Uniform(-1,1)\), \(Y=X^2\). Find \(F_Y(y)\).

#### Solution Steps

For \(0\le y\le 1\):

\[
F_Y(y)=P(Y\le y)=P(X^2\le y)=P(-\sqrt y\le X\le \sqrt y)
\]

Since \(X\sim Uniform(-1,1)\):

\[
F_Y(y)=\frac{2\sqrt y}{2}=\sqrt y
\]

#### Final Answer

\[
F_Y(y)=
\begin{cases}
0, & y<0,\\
\sqrt y, & 0\le y\le 1,\\
1, & y>1.
\end{cases}
\]

#### Mistakes to Avoid

\(X^2\) 非 one-to-one，不要直接用单一反函数。

---

<a id="ex-trans-002"></a>

### EX-TRANS-002 — Maximum of Two Independent Variables

**Concept Tags:** `#max` `#cdf-method`  
**Related Concepts:** [C-TRANS-002](#c-trans-002)

#### Given Information

\(X_1,X_2\) are independent with common CDF \(F_X(x)\). Let \(Y=\max(X_1,X_2)\).

#### Solution Steps

\[
F_Y(y)=P(Y\le y)=P(X_1\le y,X_2\le y)
\]

By independence:

\[
F_Y(y)=F_X(y)^2
\]

If PDF exists:

\[
f_Y(y)=2F_X(y)f_X(y)
\]

#### What This Example Tests

max 用 \(Y\le y\)，min 常用 \(Y>y\)。

---

<a id="ex-trans-003"></a>

### EX-TRANS-003 — Jacobian Skeleton Example

**Concept Tags:** `#jacobian` `#multivariate-transformation`  
**Related Concepts:** [C-TRANS-003](#c-trans-003)

#### Problem Pattern

Given \(U=X+Y, V=Y\), find \(f_{U,V}(u,v)\).

#### Solution Steps

Inverse:

\[
x=u-v, \qquad y=v
\]

Jacobian:

\[
J=\left|\frac{\partial(x,y)}{\partial(u,v)}\right|=
\left|\begin{matrix}1&-1\\0&1\end{matrix}\right|=1
\]

Therefore:

\[
f_{U,V}(u,v)=f_{X,Y}(u-v,v)\cdot 1
\]

#### Mistakes to Avoid

Final answer must include transformed support.

---

<a id="ex-joint-001"></a>

### EX-JOINT-001 — Joint Density Complete Workflow

**Concept Tags:** `#joint-pdf` `#marginal` `#conditional-density` `#conditional-expectation`  
**Related Concepts:** [C-JOINT-001](#c-joint-001), [C-COND-001](#c-cond-001)

#### Given Information

Suppose \(f_{X,Y}(x,y)=2\), for \(0<x<y<1\), and \(0\) otherwise.

#### Solution Steps

Support:

\[
0<x<y<1
\]

Marginal of \(Y\): for \(0<y<1\), \(x\in(0,y)\):

\[
f_Y(y)=\int_0^y 2\,dx=2y
\]

Conditional density:

\[
f_{X\mid Y}(x\mid y)=\frac{2}{2y}=\frac1y, \qquad 0<x<y
\]

Conditional expectation:

\[
E[X\mid Y=y]=\int_0^y x\frac1y\,dx=\frac{y}{2}
\]

Then:

\[
E[X\mid Y]=\frac{Y}{2}
\]

Independence check: support is triangular, not rectangular, so not independent.

#### Final Answer

\[
f_Y(y)=2y, \quad f_{X\mid Y}(x\mid y)=1/y, \quad E[X\mid Y=y]=y/2
\]

#### Mistakes to Avoid

不要把 \(x\) 的积分范围写成 \(0\) 到 \(1\)。固定 \(y\) 后，\(x\in(0,y)\)。

---

<a id="ex-cond-001"></a>

### EX-COND-001 — Total Expectation Template

**Concept Tags:** `#conditional-expectation` `#total-expectation`  
**Related Concepts:** [C-COND-001](#c-cond-001)

#### Problem Pattern

If \(E[X\mid Y]=g(Y)\), then compute \(E[X]\).

#### Solution Steps

\[
E[X]=E[E[X\mid Y]]=E[g(Y)]
\]

Use LOTUS on \(Y\):

\[
E[g(Y)]=\int g(y)f_Y(y)dy
\]

#### What This Example Tests

Total expectation can turn a hard \(E[X]\) into an easier expectation over \(Y\)。

---

<a id="ex-cov-001"></a>

### EX-COV-001 — Covariance Does Not Prove Independence

**Concept Tags:** `#covariance` `#independence` `#uncorrelated`  
**Related Concepts:** [C-COV-001](#c-cov-001)

#### Key Result

\[
Cov(X,Y)=0
\]

only means uncorrelated. It does not generally imply independent.

#### Exam Use

If the question asks independence, use:

\[
f_{X,Y}(x,y)=f_X(x)f_Y(y)
\]

not just covariance.

#### Exception

If jointly Gaussian is given:

\[
Cov(X,Y)=0 \iff X,Y \text{ independent}
\]

---

<a id="ex-rel-001"></a>

### EX-REL-001 — Reliability Event Translation

**Concept Tags:** `#reliability` `#hazard-rate` `#weibull`  
**Related Concepts:** [C-REL-001](#c-rel-001)

#### Given Information

A device failure time is \(T\). Find probability that it is still working at time \(a\), given that it failed by time \(b\), where \(a<b\).

#### Solution Steps

Translate:

\[
\text{still working at }a \Rightarrow T>a
\]

\[
\text{failed by }b \Rightarrow T\le b
\]

Given \(T\le b\), the event \(T>a\) becomes \(a<T\le b\):

\[
P(T>a\mid T\le b)=\frac{P(a<T\le b)}{P(T\le b)}
\]

Use reliability:

\[
P(a<T\le b)=F(b)-F(a)=R(a)-R(b)
\]

\[
P(T\le b)=1-R(b)
\]

#### Final Answer

\[
P(T>a\mid T\le b)=\frac{R(a)-R(b)}{1-R(b)}
\]

---

<a id="ex-mgf-001"></a>

### EX-MGF-001 — Independent Poisson Sum by MGF

**Concept Tags:** `#mgf` `#poisson` `#independent-sums`  
**Related Concepts:** [C-MGF-001](#c-mgf-001)

#### Given Information

\(X\sim Pois(\lambda)\), \(Y\sim Pois(\mu)\), independent.

#### Solution Steps

Poisson MGF:

\[
M_X(t)=e^{\lambda(e^t-1)}, \qquad M_Y(t)=e^{\mu(e^t-1)}
\]

Independent sum:

\[
M_{X+Y}(t)=M_X(t)M_Y(t)=e^{(\lambda+\mu)(e^t-1)}
\]

This is the MGF of \(Pois(\lambda+\mu)\).

#### Final Answer

\[
X+Y\sim Pois(\lambda+\mu)
\]

---

## 7. Common Traps

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
| Confuse \(E[X\mid Y=y]\) and \(E[X\mid Y]\) | first is number/function of y; second is random variable |
| Mix exponential rate and scale | rate \(\lambda\): mean \(1/\lambda\); scale \(\beta\): mean \(\beta\) |

---

## 8. Formula Tables

### 8.1 PMF / PDF / CDF / Expectation

| Concept | Formula |
|---|---|
| PMF | \(p_X(x)=P(X=x)\) |
| PDF probability | \(P(a<X<b)=\int_a^b f_X(x)dx\) |
| CDF | \(F_X(x)=P(X\le x)\) |
| Continuous PDF from CDF | \(f_X(x)=F_X'(x)\) |
| Discrete expectation | \(E[X]=\sum_x xp_X(x)\) |
| Continuous expectation | \(E[X]=\int x f_X(x)dx\) |
| LOTUS discrete | \(E[g(X)]=\sum_x g(x)p_X(x)\) |
| LOTUS continuous | \(E[g(X)]=\int g(x)f_X(x)dx\) |
| Variance | \(Var(X)=E[X^2]-E[X]^2\) |

### 8.2 Common Distribution Table

| Distribution | Support | PMF/PDF | \(E[X]\) | \(Var(X)\) |
|---|---:|---|---:|---:|
| Bernoulli(\(p\)) | \(0,1\) | \(p^x(1-p)^{1-x}\) | \(p\) | \(p(1-p)\) |
| Binomial(\(n,p\)) | \(0,...,n\) | \({n\choose k}p^k(1-p)^{n-k}\) | \(np\) | \(np(1-p)\) |
| Geometric(\(p\)) | \(1,2,...\) | \((1-p)^{k-1}p\) | \(1/p\) | \((1-p)/p^2\) |
| Poisson(\(\lambda\)) | \(0,1,...\) | \(e^{-\lambda}\lambda^k/k!\) | \(\lambda\) | \(\lambda\) |
| Exponential(rate \(\lambda\)) | \(x>0\) | \(\lambda e^{-\lambda x}\) | \(1/\lambda\) | \(1/\lambda^2\) |
| Normal(\(\mu,\sigma^2\)) | \(\mathbb R\) | \(\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}\) | \(\mu\) | \(\sigma^2\) |

### 8.3 Joint Distribution Formulas

| Task | Formula |
|---|---|
| Marginal \(X\), continuous | \(f_X(x)=\int f_{X,Y}(x,y)dy\) |
| Marginal \(Y\), continuous | \(f_Y(y)=\int f_{X,Y}(x,y)dx\) |
| Conditional density | \(f_{X\mid Y}(x\mid y)=f_{X,Y}(x,y)/f_Y(y)\) |
| Conditional expectation | \(E[X\mid Y=y]=\int x f_{X\mid Y}(x\mid y)dx\) |
| Independence | \(f_{X,Y}(x,y)=f_X(x)f_Y(y)\) |

### 8.4 Reliability Formulas

| Concept | Formula |
|---|---|
| CDF of failure time | \(F(t)=P(T\le t)\) |
| Reliability | \(R(t)=P(T>t)=1-F(t)\) |
| Hazard | \(h(t)=f(t)/R(t)\) |
| Reliability from hazard | \(R(t)=\exp(-\int_0^t h(s)ds)\) |
| Series system | \(R_s(t)=\prod_i R_i(t)\) |
| Parallel system | \(R_p(t)=1-\prod_i[1-R_i(t)]\) |
| Weibull reliability | \(R(t)=e^{-\alpha t^\beta}\) |
| Weibull hazard | \(h(t)=\alpha\beta t^{\beta-1}\) |

---

## 9. Appendix / Low-Priority Concepts

These are useful to include on paper, but do not spend too much time proving them during short review.

### Inequalities

\[
P(X\ge a)\le \frac{E[X]}{a}, \quad X\ge 0 \quad \text{Markov}
\]

\[
P(|X-\mu|\ge k\sigma)\le \frac1{k^2} \quad \text{Chebyshev}
\]

### LLN / CLT

LLN: sample average converges to true mean.

\[
\bar X_n \to \mu
\]

CLT: for large \(n\), standardized sum/sample mean is approximately normal.

\[
\frac{\bar X_n-\mu}{\sigma/\sqrt n}\approx N(0,1)
\]

---

## 10. Final Self-check List

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
