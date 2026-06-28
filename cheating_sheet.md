# ECE4010J Midterm Cheating Sheet

> Version: v0.3  
> 用途：考试速查 + 做题模板。中文解释为主，保留关键英文术语。  
> 原则：所有概念和例题都保留稳定 ID；概念区和例题区分开，通过 Mapping 表互相引用。

---

## 0. Quick Index

| 题目问什么 | Go to Concept | Main Template | Related Examples |
|---|---|---|---|
| PMF / PDF / CDF 区分 | [C-RV-001](#c-rv-001) | 离散求和，连续积分，CDF 通用 | [EX-RV-001](#ex-rv-001) |
| 求 \(E[X]\)、\(Var(X)\)、\(E[g(X)]\) | [C-RV-002](#c-rv-002) | 先 \(E[X]\)、\(E[X^2]\)，再方差；LOTUS 直接求 \(E[g(X)]\) | [EX-RV-002](#ex-rv-002) |
| 根据文字判断分布 | [C-DIST-000](#c-dist-000) | `Let X = ...` → `X follows ... because ...` | [EX-DIST-001](#ex-dist-001) |
| 常见离散分布 | [C-DIST-001](#c-dist-001) | 查 PMF、support、mean、variance | [EX-DIST-002](#ex-dist-002), [EX-DIST-003](#ex-dist-003), [EX-DIST-004](#ex-dist-004) |
| 常见连续分布 | [C-DIST-002](#c-dist-002) | 查 PDF/CDF、rate/scale、mean/variance | [EX-PP-002](#ex-pp-002), [EX-REL-003](#ex-rel-003) |
| Binomial 近似 | [C-APPROX-001](#c-approx-001) | Poisson approx / Normal + continuity correction | [EX-APPROX-001](#ex-approx-001), [EX-APPROX-002](#ex-approx-002) |
| Poisson Process | [C-PP-001](#c-pp-001) | count → Poisson，waiting time → Exponential | [EX-PP-001](#ex-pp-001), [EX-PP-002](#ex-pp-002) |
| \(Y=g(X)\) 变换 | [C-TRANS-001](#c-trans-001) | CDF method / inverse formula | [EX-TRANS-001](#ex-trans-001) |
| \(Y=\max\)、\(Y=\min\) | [C-TRANS-002](#c-trans-002) | max 用 CDF，min 用 survival | [EX-TRANS-002](#ex-trans-002), [EX-TRANS-003](#ex-trans-003) |
| 二维变换 / 和分布 | [C-TRANS-003](#c-trans-003), [C-TRANS-004](#c-trans-004) | inverse → support → Jacobian；sum → convolution | [EX-TRANS-004](#ex-trans-004), [EX-TRANS-005](#ex-trans-005) |
| Joint pdf 大题 | [C-JOINT-001](#c-joint-001) | support → marginal → conditional → expectation → independence | [EX-JOINT-001](#ex-joint-001), [EX-JOINT-002](#ex-joint-002), [EX-JOINT-003](#ex-joint-003) |
| Conditional expectation | [C-COND-001](#c-cond-001) | \(f_{X|Y}\) → \(E[X|Y=y]\) → \(E[X|Y]\) | [EX-COND-001](#ex-cond-001) |
| Covariance / correlation / independence | [C-COV-001](#c-cov-001) | \(Cov=E[XY]-E[X]E[Y]\)，独立看 joint 是否可拆 | [EX-COV-001](#ex-cov-001), [EX-COV-002](#ex-cov-002) |
| Reliability / hazard / Weibull | [C-REL-001](#c-rel-001) | \(R(t)=P(T>t)\)，\(h(t)=f(t)/R(t)\) | [EX-REL-001](#ex-rel-001), [EX-REL-002](#ex-rel-002), [EX-REL-003](#ex-rel-003) |
| MGF | [C-MGF-001](#c-mgf-001) | 求矩、独立和、识别分布 | [EX-MGF-001](#ex-mgf-001), [EX-MGF-002](#ex-mgf-002) |
| 常见坑 | [13. Common Traps](#13-common-traps) | PDF 不是概率；support 不能漏 | all examples |

---

## 1. Concept-to-Example Map

| Concept ID | Concept Name | Tags | Related Examples |
|---|---|---|---|
| [C-RV-001](#c-rv-001) | PMF / PDF / CDF | `#pmf` `#pdf` `#cdf` | [EX-RV-001](#ex-rv-001) |
| [C-RV-002](#c-rv-002) | Expectation / Variance / LOTUS | `#expectation` `#variance` `#lotus` | [EX-RV-002](#ex-rv-002) |
| [C-DIST-000](#c-dist-000) | Distribution Recognition | `#distribution-recognition` | [EX-DIST-001](#ex-dist-001) |
| [C-DIST-001](#c-dist-001) | Discrete Distributions | `#bernoulli` `#binomial` `#geometric` `#negative-binomial` `#hypergeometric` `#poisson` | [EX-DIST-002](#ex-dist-002), [EX-DIST-003](#ex-dist-003), [EX-DIST-004](#ex-dist-004) |
| [C-DIST-002](#c-dist-002) | Continuous Distributions | `#uniform` `#exponential` `#gamma` `#normal` `#weibull` | [EX-PP-002](#ex-pp-002), [EX-REL-003](#ex-rel-003) |
| [C-APPROX-001](#c-approx-001) | Binomial Approximation | `#poisson-approximation` `#normal-approximation` `#continuity-correction` | [EX-APPROX-001](#ex-approx-001), [EX-APPROX-002](#ex-approx-002) |
| [C-PP-001](#c-pp-001) | Poisson Process + Exponential Waiting Time | `#poisson-process` `#exponential` `#memoryless` | [EX-PP-001](#ex-pp-001), [EX-PP-002](#ex-pp-002) |
| [C-TRANS-001](#c-trans-001) | CDF Method / One-dimensional Transformation | `#cdf-method` `#transformation` | [EX-TRANS-001](#ex-trans-001) |
| [C-TRANS-002](#c-trans-002) | Max / Min Transformation | `#max` `#min` | [EX-TRANS-002](#ex-trans-002), [EX-TRANS-003](#ex-trans-003) |
| [C-TRANS-003](#c-trans-003) | Jacobian Transformation | `#jacobian` `#multivariate-transformation` | [EX-TRANS-004](#ex-trans-004) |
| [C-TRANS-004](#c-trans-004) | Sum / Convolution | `#convolution` `#sum-of-rv` | [EX-TRANS-005](#ex-trans-005) |
| [C-JOINT-001](#c-joint-001) | Joint / Marginal / Conditional / Independence | `#joint-pdf` `#marginal` `#conditional-density` `#independence` | [EX-JOINT-001](#ex-joint-001), [EX-JOINT-002](#ex-joint-002), [EX-JOINT-003](#ex-joint-003) |
| [C-COND-001](#c-cond-001) | Conditional Expectation | `#conditional-expectation` `#total-expectation` `#total-variance` | [EX-JOINT-001](#ex-joint-001), [EX-COND-001](#ex-cond-001) |
| [C-COV-001](#c-cov-001) | Covariance / Correlation / Independence | `#covariance` `#correlation` `#uncorrelated` | [EX-COV-001](#ex-cov-001), [EX-COV-002](#ex-cov-002) |
| [C-REL-001](#c-rel-001) | Reliability / Hazard / Weibull | `#reliability` `#hazard-rate` `#weibull` `#series-system` `#parallel-system` | [EX-REL-001](#ex-rel-001), [EX-REL-002](#ex-rel-002), [EX-REL-003](#ex-rel-003) |
| [C-MGF-001](#c-mgf-001) | MGF Toolkit | `#mgf` `#moment-extraction` `#independent-sums` | [EX-MGF-001](#ex-mgf-001), [EX-MGF-002](#ex-mgf-002) |

---

## 2. Tag Index

| Tag | Meaning | Related Concepts | Related Examples |
|---|---|---|---|
| `#pmf` | 离散随机变量点概率 | C-RV-001 | EX-RV-001 |
| `#pdf` | 连续随机变量密度 | C-RV-001 | EX-RV-001 |
| `#cdf` | \(F_X(x)=P(X\le x)\)，通用分布函数 | C-RV-001, C-TRANS-001 | EX-RV-001, EX-TRANS-001 |
| `#lotus` | 不求 \(Y=g(X)\) 分布直接求 \(E[g(X)]\) | C-RV-002 | EX-RV-002 |
| `#distribution-recognition` | 根据题目关键词识别分布 | C-DIST-000 | EX-DIST-001 |
| `#binomial` | 固定 \(n\) 次独立试验成功次数 | C-DIST-001 | EX-DIST-002, EX-APPROX-001 |
| `#hypergeometric` | 不放回抽样 | C-DIST-001 | EX-DIST-003 |
| `#geometric` | 第一次成功等待试验数 | C-DIST-001 | EX-DIST-004 |
| `#negative-binomial` | 第 r 次成功等待试验数 | C-DIST-001 | EX-DIST-004 |
| `#poisson` | 固定时间/区域内事件数 | C-DIST-001, C-PP-001 | EX-PP-001, EX-APPROX-002, EX-MGF-001 |
| `#exponential` | 等下一次事件的时间 | C-DIST-002, C-PP-001 | EX-PP-002 |
| `#normal-approximation` | 用正态近似离散分布 | C-APPROX-001 | EX-APPROX-001 |
| `#continuity-correction` | 离散到连续近似时加减 0.5 | C-APPROX-001 | EX-APPROX-001 |
| `#cdf-method` | 变量变换通用方法 | C-TRANS-001, C-TRANS-002 | EX-TRANS-001, EX-TRANS-002, EX-TRANS-003 |
| `#jacobian` | 二维变量变换 | C-TRANS-003 | EX-TRANS-004 |
| `#convolution` | 独立随机变量求和 | C-TRANS-004 | EX-TRANS-005 |
| `#joint-pdf` | 两个随机变量联合密度 | C-JOINT-001 | EX-JOINT-001, EX-JOINT-002, EX-JOINT-003 |
| `#conditional-expectation` | 条件下的平均值 | C-COND-001 | EX-JOINT-001, EX-COND-001 |
| `#covariance` | 线性同向/反向变化趋势 | C-COV-001 | EX-COV-001, EX-COV-002 |
| `#reliability` | 生存概率 \(R(t)=P(T>t)\) | C-REL-001 | EX-REL-001, EX-REL-002, EX-REL-003 |
| `#mgf` | 矩母函数 | C-MGF-001 | EX-MGF-001, EX-MGF-002 |

---

## 3. How to Use This Sheet

1. 先用 Quick Index 找题型。
2. 查 Concept ID 看公式和模板。
3. 如果题目像某个例题，跳到 Example ID。
4. 做完后回到 Common Traps 检查 support、条件、连续/离散是否写错。

> Exam Tip: 不要只背公式。考试得分关键是：**识别题型 → 定义随机变量 → 找 support → 套正确模板**。

---

## 4. Core Concepts

<a id="c-rv-001"></a>

### C-RV-001 — PMF / PDF / CDF

**Tags:** `#pmf` `#pdf` `#cdf`  
**Related Examples:** [EX-RV-001](#ex-rv-001)  
**Depth Level:** Must Understand

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

---

<a id="c-rv-002"></a>

### C-RV-002 — Expectation / Variance / LOTUS

**Tags:** `#expectation` `#variance` `#lotus`  
**Related Examples:** [EX-RV-002](#ex-rv-002)  
**Depth Level:** Must Understand

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

<a id="c-dist-000"></a>

### C-DIST-000 — Distribution Recognition

**Tags:** `#distribution-recognition`  
**Related Examples:** [EX-DIST-001](#ex-dist-001)  
**Depth Level:** Must Understand

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

<a id="c-dist-001"></a>

### C-DIST-001 — Discrete Distributions

**Tags:** `#bernoulli` `#binomial` `#geometric` `#negative-binomial` `#hypergeometric` `#poisson`  
**Related Examples:** [EX-DIST-002](#ex-dist-002), [EX-DIST-003](#ex-dist-003), [EX-DIST-004](#ex-dist-004), [EX-APPROX-002](#ex-approx-002)  
**Depth Level:** Put on Paper + Must Understand recognition

| Distribution | Support | PMF | Mean | Variance |
|---|---|---|---|---|
| Bernoulli(\(p\)) | \(0,1\) | \(P(X=1)=p\) | \(p\) | \(p(1-p)\) |
| Binomial(\(n,p\)) | \(0,1,...,n\) | \({n\choose k}p^k(1-p)^{n-k}\) | \(np\) | \(np(1-p)\) |
| Geometric(\(p\)) | \(1,2,...\) | \((1-p)^{k-1}p\) | \(1/p\) | \((1-p)/p^2\) |
| Negative Binomial(\(r,p\)) | \(r,r+1,...\) | \({k-1\choose r-1}p^r(1-p)^{k-r}\) | \(r/p\) | \(r(1-p)/p^2\) |
| Hypergeometric(\(N,K,n\)) | valid \(k\) | \(rac{{K\choose k}{N-K\choose n-k}}{{N\choose n}}\) | \(nK/N\) | \(n\frac KN(1-\frac KN)\frac{N-n}{N-1}\) |
| Poisson(\(\lambda\)) | \(0,1,2,...\) | \(e^{-\lambda}\lambda^k/k!\) | \(\lambda\) | \(\lambda\) |

---

<a id="c-dist-002"></a>

### C-DIST-002 — Continuous Distributions

**Tags:** `#uniform` `#exponential` `#gamma` `#normal` `#weibull`  
**Related Examples:** [EX-PP-002](#ex-pp-002), [EX-REL-003](#ex-rel-003), [EX-MGF-002](#ex-mgf-002)  
**Depth Level:** Put on Paper

| Distribution | Support | PDF / CDF | Mean | Variance |
|---|---|---|---|---|
| Uniform(\(a,b\)) | \(a<x<b\) | \(f(x)=1/(b-a)\) | \((a+b)/2\) | \((b-a)^2/12\) |
| Exponential(rate \(\lambda\)) | \(x>0\) | \(f(x)=\lambda e^{-\lambda x}\), \(F(x)=1-e^{-\lambda x}\) | \(1/\lambda\) | \(1/\lambda^2\) |
| Exponential(scale \(\beta\)) | \(x>0\) | \(f(x)=\frac1\beta e^{-x/\beta}\) | \(\beta\) | \(\beta^2\) |
| Gamma(shape \(\alpha\), rate \(\lambda\)) | \(x>0\) | \(f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}\) | \(\alpha/\lambda\) | \(\alpha/\lambda^2\) |
| Normal(\(\mu,\sigma^2\)) | \(\mathbb R\) | \(f(x)=\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}\) | \(\mu\) | \(\sigma^2\) |
| Weibull via reliability | \(t>0\) | \(R(t)=e^{-\alpha t^\beta}\) | usually table | usually table |

> Warning: Exponential 的 rate \(\lambda\) 和 scale \(\beta=1/\lambda\) 很容易混。

---

<a id="c-approx-001"></a>

### C-APPROX-001 — Binomial Approximation

**Tags:** `#poisson-approximation` `#normal-approximation` `#continuity-correction`  
**Related Examples:** [EX-APPROX-001](#ex-approx-001), [EX-APPROX-002](#ex-approx-002)  
**Depth Level:** Must Understand

If \(X\sim Bin(n,p)\), \(n\) large and \(p\) small:

\[
X\approx Pois(\lambda=np)
\]

If \(X\sim Bin(n,p)\) and \(np,n(1-p)\) are large enough:

\[
\mu=np, \qquad \sigma^2=np(1-p), \qquad X\approx N(np,np(1-p))
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

<a id="c-pp-001"></a>

### C-PP-001 — Poisson Process + Exponential

**Tags:** `#poisson-process` `#poisson` `#exponential` `#memoryless`  
**Related Examples:** [EX-PP-001](#ex-pp-001), [EX-PP-002](#ex-pp-002)  
**Depth Level:** Must Understand

If events arrive at rate \(\lambda\), \(N_t\) is the number of events by time \(t\)。

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

Waiting time \(W\sim Exp(rate=\lambda)\):

\[
P(W>t)=e^{-\lambda t}
\]

Memoryless:

\[
P(W>s+t\mid W>s)=P(W>t)
\]

---

<a id="c-trans-001"></a>

### C-TRANS-001 — CDF Method / One-dimensional Transformation

**Tags:** `#cdf-method` `#transformation`  
**Related Examples:** [EX-TRANS-001](#ex-trans-001)  
**Depth Level:** Must Understand

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

---

<a id="c-trans-002"></a>

### C-TRANS-002 — Max / Min Transformation

**Tags:** `#max` `#min` `#cdf-method`  
**Related Examples:** [EX-TRANS-002](#ex-trans-002), [EX-TRANS-003](#ex-trans-003)  
**Depth Level:** Must Understand

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

---

<a id="c-trans-003"></a>

### C-TRANS-003 — Jacobian Transformation

**Tags:** `#jacobian` `#multivariate-transformation`  
**Related Examples:** [EX-TRANS-004](#ex-trans-004)  
**Depth Level:** Put on Paper + Must Understand workflow

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

> Warning: Formula without transformed support is incomplete.

---

<a id="c-trans-004"></a>

### C-TRANS-004 — Sum / Convolution

**Tags:** `#convolution` `#sum-of-rv`  
**Related Examples:** [EX-TRANS-005](#ex-trans-005)  
**Depth Level:** Put on Paper

If \(Z=X+Y\) and \(X,Y\) independent continuous RVs:

\[
f_Z(z)=\int_{-\infty}^{\infty} f_X(x)f_Y(z-x)\,dx
\]

The real work is finding the valid integration interval from support.

---

<a id="c-joint-001"></a>

### C-JOINT-001 — Joint / Marginal / Conditional / Independence

**Tags:** `#joint-pdf` `#marginal` `#conditional-density` `#independence`  
**Related Examples:** [EX-JOINT-001](#ex-joint-001), [EX-JOINT-002](#ex-joint-002), [EX-JOINT-003](#ex-joint-003)  
**Depth Level:** Must Understand

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

Joint density big problem template:

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

---

<a id="c-cond-001"></a>

### C-COND-001 — Conditional Expectation

**Tags:** `#conditional-expectation` `#total-expectation` `#total-variance`  
**Related Examples:** [EX-JOINT-001](#ex-joint-001), [EX-COND-001](#ex-cond-001)  
**Depth Level:** Must Understand

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

| Expression | Meaning |
|---|---|
| \(E[X\mid Y=y]\) | 固定 \(y\) 后的数字 / function of \(y\) |
| \(E[X\mid Y]\) | 把 \(y\) 替换成随机变量 \(Y\)，所以本身是 random variable |

---

<a id="c-cov-001"></a>

### C-COV-001 — Covariance / Correlation / Independence

**Tags:** `#covariance` `#correlation` `#uncorrelated` `#independence`  
**Related Examples:** [EX-COV-001](#ex-cov-001), [EX-COV-002](#ex-cov-002)  
**Depth Level:** Must Understand

\[
Cov(X,Y)=E[(X-E[X])(Y-E[Y])]
\]

\[
Cov(X,Y)=E[XY]-E[X]E[Y]
\]

\[
\rho_{X,Y}=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
\]

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

<a id="c-rel-001"></a>

### C-REL-001 — Reliability / Hazard / Weibull

**Tags:** `#reliability` `#hazard-rate` `#weibull` `#series-system` `#parallel-system`  
**Related Examples:** [EX-REL-001](#ex-rel-001), [EX-REL-002](#ex-rel-002), [EX-REL-003](#ex-rel-003)  
**Depth Level:** Must Understand

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

<a id="c-mgf-001"></a>

### C-MGF-001 — MGF Toolkit

**Tags:** `#mgf` `#moment-extraction` `#independent-sums`  
**Related Examples:** [EX-MGF-001](#ex-mgf-001), [EX-MGF-002](#ex-mgf-002)  
**Depth Level:** Put on Paper

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

Common MGFs:

| Distribution | MGF |
|---|---|
| Bernoulli(\(p\)) | \(1-p+pe^t\) |
| Binomial(\(n,p\)) | \((1-p+pe^t)^n\) |
| Poisson(\(\lambda\)) | \(e^{\lambda(e^t-1)}\) |
| Exponential(rate \(\lambda\)) | \(rac{\lambda}{\lambda-t}, t<\lambda\) |
| Normal(\(\mu,\sigma^2\)) | \(e^{\mu t+\frac12\sigma^2t^2}\) |

---

## 5. Exam Templates

### T-DIST — Distribution Recognition

```text
Let X = [the random quantity].
Fixed quantity = [...]
Random quantity = [...]
Keyword = [...]
Therefore X ~ [Distribution]([parameters]).
Use [PMF/PDF/CDF] to compute [...].
```

### T-PROB — Probability from PMF/PDF/CDF

```text
Discrete: P(a≤X≤b)=Σ p_X(x) over valid x.
Continuous: P(a<X<b)=∫_a^b f_X(x)dx.
CDF: P(a<X≤b)=F_X(b)-F_X(a).
```

### T-JOINT — Joint Density Big Problem

```text
1. Write support.
2. Normalize if needed.
3. Marginalize by integrating out the other variable.
4. Conditional = joint / marginal.
5. Conditional expectation = integral of x times conditional density.
6. Independence check = joint ? product of marginals.
```

### T-REL — Reliability Conditional Probability

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

### EX-RV-001 — Continuous PDF Probability

**Concept Tags:** `#pdf` `#cdf`  
**Related Concepts:** [C-RV-001](#c-rv-001)  
**Problem Pattern:** Given PDF, find interval probability.

Given \(f_X(x)=2x\), \(0<x<1\). Find \(P(0.2<X<0.5)\).

\[
P(0.2<X<0.5)=\int_{0.2}^{0.5}2x\,dx=x^2\big|_{0.2}^{0.5}=0.25-0.04=0.21
\]

**Final Answer:** \(0.21\)

---

<a id="ex-rv-002"></a>

### EX-RV-002 — LOTUS

**Concept Tags:** `#lotus` `#expectation`  
**Related Concepts:** [C-RV-002](#c-rv-002)  
**Problem Pattern:** Find \(E[g(X)]\) directly.

Given \(X\sim Uniform(0,1)\). Find \(E[X^2]\).

\[
E[X^2]=\int_0^1 x^2\cdot 1\,dx=\frac13
\]

**Final Answer:** \(1/3\)

---

<a id="ex-dist-001"></a>

### EX-DIST-001 — Distribution Recognition Mini Table

**Concept Tags:** `#distribution-recognition`  
**Related Concepts:** [C-DIST-000](#c-dist-000)

| Problem Pattern | Let X = | Distribution | Reason |
|---|---|---|---|
| 100 independent products, each defective with prob 0.02. | number defective | \(Bin(100,0.02)\) | fixed independent trials |
| Calls arrive at rate 3/hour. Count calls in 2 hours. | calls in 2h | \(Pois(6)\) | count in interval, mean \(\lambda t\) |
| Same calls. Wait for next call. | waiting time | \(Exp(rate=3)\) | waiting time until next event |
| Draw 5 cards without replacement. Count aces. | aces drawn | Hypergeometric | without replacement |

---

<a id="ex-dist-002"></a>

### EX-DIST-002 — Binomial Recognition

**Concept Tags:** `#binomial`  
**Related Concepts:** [C-DIST-001](#c-dist-001)

100 products are independently defective with probability \(0.02\). Let \(X\) be the number of defective products.

\[
X\sim Bin(100,0.02)
\]

Probability exactly 3 defective:

\[
P(X=3)={100\choose 3}(0.02)^3(0.98)^{97}
\]

---

<a id="ex-dist-003"></a>

### EX-DIST-003 — Hypergeometric Recognition

**Concept Tags:** `#hypergeometric`  
**Related Concepts:** [C-DIST-001](#c-dist-001)

A box has 20 items, 5 defective. Draw 4 without replacement. Let \(X\) be defective items drawn.

\[
X\sim Hypergeometric(N=20,K=5,n=4)
\]

\[
P(X=2)=\frac{{5\choose 2}{15\choose 2}}{{20\choose 4}}
\]

**Mistake to Avoid:** without replacement → Hypergeometric, not Binomial.

---

<a id="ex-dist-004"></a>

### EX-DIST-004 — Geometric vs Negative Binomial

**Concept Tags:** `#geometric` `#negative-binomial`  
**Related Concepts:** [C-DIST-001](#c-dist-001)

If \(X\) is the trial number of the first success:

\[
X\sim Geometric(p), \qquad P(X=k)=(1-p)^{k-1}p
\]

If \(Y\) is the trial number of the 3rd success:

\[
Y\sim NegativeBinomial(r=3,p), \qquad P(Y=k)={k-1\choose 2}p^3(1-p)^{k-3}
\]

---

<a id="ex-approx-001"></a>

### EX-APPROX-001 — Normal Approximation with Continuity Correction

**Concept Tags:** `#normal-approximation` `#continuity-correction` `#binomial`  
**Related Concepts:** [C-APPROX-001](#c-approx-001)

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

<a id="ex-approx-002"></a>

### EX-APPROX-002 — Poisson Approximation to Binomial

**Concept Tags:** `#poisson-approximation` `#binomial` `#poisson`  
**Related Concepts:** [C-APPROX-001](#c-approx-001), [C-DIST-001](#c-dist-001)

\(X\sim Bin(1000,0.002)\). Approximate \(P(X=3)\).

\[
\lambda=np=2, \qquad X\approx Pois(2)
\]

\[
P(X=3)\approx e^{-2}\frac{2^3}{3!}
\]

---

<a id="ex-pp-001"></a>

### EX-PP-001 — Poisson Process Count

**Concept Tags:** `#poisson-process` `#poisson`  
**Related Concepts:** [C-PP-001](#c-pp-001)

Events arrive at rate \(\lambda=2\) per hour. Number of events in 3 hours:

\[
N_3\sim Pois(6)
\]

No event in 3 hours:

\[
P(N_3=0)=e^{-6}
\]

---

<a id="ex-pp-002"></a>

### EX-PP-002 — Exponential Waiting Time and Memoryless

**Concept Tags:** `#exponential` `#memoryless`  
**Related Concepts:** [C-PP-001](#c-pp-001), [C-DIST-002](#c-dist-002)

Let \(W\sim Exp(rate=\lambda)\). Find \(P(W>8\mid W>5)\).

\[
P(W>8\mid W>5)=P(W>5+3\mid W>5)=P(W>3)=e^{-3\lambda}
\]

---

<a id="ex-trans-001"></a>

### EX-TRANS-001 — CDF Method: \(Y=X^2\)

**Concept Tags:** `#cdf-method` `#transformation`  
**Related Concepts:** [C-TRANS-001](#c-trans-001)

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

<a id="ex-trans-002"></a>

### EX-TRANS-002 — Max of Two Independent Uniform Variables

**Concept Tags:** `#max` `#cdf-method`  
**Related Concepts:** [C-TRANS-002](#c-trans-002)

Let \(X_1,X_2\sim Uniform(0,1)\) independent, \(Y=\max(X_1,X_2)\).

For \(0<y<1\):

\[
F_Y(y)=P(X_1\le y,X_2\le y)=y^2
\]

\[
f_Y(y)=2y, \qquad 0<y<1
\]

---

<a id="ex-trans-003"></a>

### EX-TRANS-003 — Min of Two Independent Uniform Variables

**Concept Tags:** `#min` `#cdf-method`  
**Related Concepts:** [C-TRANS-002](#c-trans-002)

Let \(X_1,X_2\sim Uniform(0,1)\) independent, \(Y=\min(X_1,X_2)\).

\[
P(Y>y)=P(X_1>y,X_2>y)=(1-y)^2
\]

\[
F_Y(y)=1-(1-y)^2, \qquad f_Y(y)=2(1-y)
\]

---

<a id="ex-trans-004"></a>

### EX-TRANS-004 — Jacobian Skeleton

**Concept Tags:** `#jacobian`  
**Related Concepts:** [C-TRANS-003](#c-trans-003)

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

<a id="ex-trans-005"></a>

### EX-TRANS-005 — Convolution: Sum of Two Uniform(0,1)

**Concept Tags:** `#convolution` `#sum-of-rv`  
**Related Concepts:** [C-TRANS-004](#c-trans-004)

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

<a id="ex-joint-001"></a>

### EX-JOINT-001 — Joint Density Complete Workflow

**Concept Tags:** `#joint-pdf` `#marginal` `#conditional-density` `#conditional-expectation`  
**Related Concepts:** [C-JOINT-001](#c-joint-001), [C-COND-001](#c-cond-001)

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

<a id="ex-joint-002"></a>

### EX-JOINT-002 — Normalizing Constant in Joint PDF

**Concept Tags:** `#joint-pdf` `#normalization`  
**Related Concepts:** [C-JOINT-001](#c-joint-001)

Suppose \(f_{X,Y}(x,y)=c(x+y)\), \(0<x<1,0<y<1\). Find \(c\).

\[
1=\int_0^1\int_0^1 c(x+y)\,dxdy
\]

\[
= c\left(\frac12+\frac12\right)=c
\]

\[
c=1
\]

---

<a id="ex-joint-003"></a>

### EX-JOINT-003 — Independence Check from Joint PDF

**Concept Tags:** `#joint-pdf` `#independence`  
**Related Concepts:** [C-JOINT-001](#c-joint-001)

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

<a id="ex-cond-001"></a>

### EX-COND-001 — Conditional Expectation by Total Expectation

**Concept Tags:** `#conditional-expectation` `#total-expectation`  
**Related Concepts:** [C-COND-001](#c-cond-001)

If \(E[X\mid Y]=Y^2\) and \(Y\sim Uniform(0,1)\), then

\[
E[X]=E[E[X\mid Y]]=E[Y^2]=\int_0^1 y^2dy=\frac13
\]

---

<a id="ex-cov-001"></a>

### EX-COV-001 — Covariance Calculation

**Concept Tags:** `#covariance`  
**Related Concepts:** [C-COV-001](#c-cov-001)

Given \(E[X]=2\), \(E[Y]=3\), \(E[XY]=7\):

\[
Cov(X,Y)=E[XY]-E[X]E[Y]=7-2\cdot 3=1
\]

---

<a id="ex-cov-002"></a>

### EX-COV-002 — Covariance Zero Does Not Mean Independent

**Concept Tags:** `#covariance` `#independence` `#uncorrelated`  
**Related Concepts:** [C-COV-001](#c-cov-001)

If \(Cov(X,Y)=0\), then \(X,Y\) are uncorrelated. Do not conclude independent unless jointly Gaussian or joint distribution factorization is given.

For independence, check:

\[
f_{X,Y}(x,y)=f_X(x)f_Y(y)
\]

---

<a id="ex-rel-001"></a>

### EX-REL-001 — Reliability Conditional Probability

**Concept Tags:** `#reliability`  
**Related Concepts:** [C-REL-001](#c-rel-001)

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

<a id="ex-rel-002"></a>

### EX-REL-002 — Series and Parallel Systems

**Concept Tags:** `#reliability` `#series-system` `#parallel-system`  
**Related Concepts:** [C-REL-001](#c-rel-001)

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

<a id="ex-rel-003"></a>

### EX-REL-003 — Weibull Hazard

**Concept Tags:** `#weibull` `#hazard-rate`  
**Related Concepts:** [C-REL-001](#c-rel-001), [C-DIST-002](#c-dist-002)

If \(R(t)=e^{-\alpha t^\beta}\), then

\[
h(t)=\alpha\beta t^{\beta-1}
\]

- \(\beta>1\): hazard increases with time.
- \(\beta=1\): constant hazard, same as exponential form.
- \(0<\beta<1\): hazard decreases with time.

---

<a id="ex-mgf-001"></a>

### EX-MGF-001 — MGF: Sum of Independent Poisson

**Concept Tags:** `#mgf` `#poisson` `#independent-sums`  
**Related Concepts:** [C-MGF-001](#c-mgf-001)

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

<a id="ex-mgf-002"></a>

### EX-MGF-002 — MGF Moment / Distribution Recognition

**Concept Tags:** `#mgf` `#normal`  
**Related Concepts:** [C-MGF-001](#c-mgf-001), [C-DIST-002](#c-dist-002)

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
