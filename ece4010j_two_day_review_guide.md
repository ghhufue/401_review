# ECE4010J Midterm 两天速成路线指南

> 目标：这份文档不是完整教材，而是一个 **两天全天复习路线 + 概念清单 + 逐个问 AI 的提示词模板**。  
> 使用方法：按时间块推进；每学一个概念，就复制对应问题问 AI；每做一类题，就把最终模板补进你的 cheating sheet。

---

## 0. 总目标

这次复习不要追求“完全理解概率论”，目标是：

1. **看题识别题型**
2. **知道该查 cheating sheet 哪一页**
3. **知道该用哪个模板**
4. **能把文字条件翻译成概率事件**
5. **能确定积分区域 / support**
6. **能完成常见大题流程**

---

## 1. 两天复习总览

### Day 1：分布 + 一维随机变量 + 变换

| 时间 | 内容 | 目标 |
|---|---|---|
| 09:00-10:00 | PMF / PDF / CDF / E / Var / LOTUS | 建立随机变量基础 |
| 10:00-12:00 | 常见分布识别 | 看到题知道用什么分布 |
| 12:00-13:00 | 午饭 + 整理分布表 | 做 cheating sheet 第 1-2 页 |
| 13:00-14:30 | Binomial / Poisson / Normal Approximation | 会做近似题 |
| 14:30-16:30 | Random Variable Transformation | 会做 max/min/g(X)/Jacobian |
| 16:30-17:00 | 休息 | 不学新内容 |
| 17:00-19:00 | Poisson Process + Exponential | 会处理计数过程和等待时间 |
| 19:00-20:00 | 晚饭 | 休息 |
| 20:00-22:30 | Day 1 题型训练 + 整理模板 | 每类题整理一个模板 |

---

### Day 2：联合分布 + 条件期望 + Reliability

| 时间 | 内容 | 目标 |
|---|---|---|
| 09:00-10:30 | Joint Distribution 基础 | 会 marginal / conditional / independence |
| 10:30-12:30 | Joint Density 大题模板 | 练完整流程题 |
| 12:30-13:30 | 午饭 + 整理 joint 模板 | 做 cheating sheet 联合分布页 |
| 13:30-15:00 | Covariance / Correlation / Independence | 会判断独立、相关、不相关 |
| 15:00-17:00 | Conditional Expectation | 会算 E[X\|Y] 和 total expectation |
| 17:00-17:30 | 休息 | 不学新内容 |
| 17:30-19:30 | Reliability / Hazard / Weibull | 会做寿命和系统可靠性题 |
| 19:30-20:30 | 晚饭 | 休息 |
| 20:30-21:30 | MGF 快速掌握 | 会查 MGF、乘 MGF、识别分布 |
| 21:30-23:00 | 最终整理 + 模板复盘 | 完成纸质材料索引 |

---

## 2. 必须真正掌握的方法

这些内容不能只放纸上，因为考试时必须现场判断。

| 方法 | 为什么必须掌握 |
|---|---|
| 分布识别 | 题目不会直接告诉你用什么分布 |
| PMF / PDF / CDF 区分 | 连续型和离散型做法完全不同 |
| Support / 积分范围判断 | 联合分布和变换题最容易错 |
| CDF method | 非单调变换和 max/min 常用 |
| Jacobian 变换 | 二维随机变量变换题需要 |
| Conditional density | 联合分布大题核心 |
| Conditional expectation | 期望题、回归题、total expectation 核心 |
| Independence 判断 | 要会看 joint 是否能拆成 marginal 乘积 |
| Reliability 事件翻译 | 要会把 “still working / failed by” 翻译成 T 的事件 |
| Normal approximation 加 continuity correction | 近似题常见 |

---

## 3. 可以放进纸质材料，不用深入理解的内容

这些内容要放进 cheating sheet，但两天内不建议深挖证明。

| 内容 | 处理方式 |
|---|---|
| 所有分布 PMF/PDF/CDF/E/Var/MGF | 放表格 |
| Gamma function 性质 | 放公式 |
| Weibull mean / variance | 放公式 |
| MGF 推导过程 | 放结论和例子即可 |
| Markov / Chebyshev / Cantelli | 放公式和适用条件 |
| LLN / CLT 严格表述 | 放文字解释和公式 |
| σ-algebra 严格定义 | 放定义，不深挖 |
| Probability philosophy / Dutch book | 放概念解释 |
| Covariance matrix 正半定证明 | 不深挖 |
| Multivariate Gaussian 完整公式 | 放公式，重点会查 |
| Buffon's needle | 如果材料中出现，放结论和模板 |

---

# Day 1 详细路线

---

## 4. Day 1 - Part 1：随机变量基础

### 时间

**09:00-10:00**

### 需要搞懂的概念

| 概念 | 英文 | 你要会说什么 |
|---|---|---|
| 随机变量 | Random Variable | 把随机结果映射成数字 |
| 概率质量函数 | PMF | 离散变量的点概率 |
| 概率密度函数 | PDF | 连续变量的密度，概率是面积 |
| 累积分布函数 | CDF | \(F_X(x)=P(X\le x)\) |
| 期望 | Expectation | 长期平均值 |
| 方差 | Variance | 波动大小 |
| LOTUS | Law of the Unconscious Statistician | 求 \(E[g(X)]\) 不一定先求 \(Y=g(X)\) 分布 |

### 必须掌握的方法

1. 离散变量：概率用求和
2. 连续变量：概率用积分
3. 连续变量的单点概率为 0
4. CDF 可以用于所有随机变量

### 放到 cheating sheet

```text
PMF:
p_X(x)=P(X=x)

PDF:
P(a<X<b)=∫_a^b f_X(x)dx

CDF:
F_X(x)=P(X≤x)

Expectation:
Discrete: E[X]=Σx p_X(x)
Continuous: E[X]=∫x f_X(x)dx

Variance:
Var(X)=E[X²]-E[X]²

LOTUS:
E[g(X)] = Σg(x)p_X(x)
E[g(X)] = ∫g(x)f_X(x)dx
```

### 复制问 AI

```text
请用考试题的角度讲清楚 PMF、PDF、CDF 的区别。
要求：
1. 用中文解释；
2. 每个概念给一个最简单例子；
3. 说明考试中怎么判断该用求和还是积分；
4. 最后给我一段可以放进 cheating sheet 的英文说明。
```

---

## 5. Day 1 - Part 2：常见分布识别

### 时间

**10:00-12:00**

### 必须搞懂的分布

| 分布 | 英文 | 题目关键词 |
|---|---|---|
| Bernoulli | Bernoulli Distribution | 一次成功/失败 |
| Binomial | Binomial Distribution | 固定 n 次独立试验，成功几次 |
| Geometric | Geometric Distribution | 第一次成功在第几次 |
| Negative Binomial | Negative Binomial Distribution | 第 r 次成功在第几次 |
| Hypergeometric | Hypergeometric Distribution | 不放回抽样 |
| Poisson | Poisson Distribution | 固定时间/区域内事件次数 |
| Exponential | Exponential Distribution | 等下一次事件多久 |
| Gamma | Gamma Distribution | 等第 k 次事件多久 |
| Normal | Normal Distribution | 正态近似、大样本、误差 |
| Weibull | Weibull Distribution | 寿命、失效率、可靠性 |

### 必须掌握的方法

看到题后，先写三行：

```text
Let X = ...
X follows ...
because ...
```

### 放到 cheating sheet

```text
Distribution Recognition:

fixed number of independent trials → Binomial
first success waiting trial → Geometric
r-th success waiting trial → Negative Binomial
without replacement → Hypergeometric
rare events in interval → Poisson
waiting time until next event → Exponential
waiting time until k-th event → Gamma
failure time with hazard → Exponential / Weibull
large n approximation → Normal
```

### 复制问 AI

```text
请帮我区分 Bernoulli、Binomial、Geometric、Negative Binomial、Hypergeometric、Poisson、Exponential、Gamma、Normal、Weibull。
要求：
1. 用“题目关键词 → 分布”的方式解释；
2. 每个分布给一个考试例子；
3. 说明 fixed quantity 和 random quantity 分别是什么；
4. 最后给一张 cheating sheet 表格。
```

---

## 6. Day 1 - Part 3：近似方法

### 时间

**13:00-14:30**

### 需要搞懂的概念

| 概念 | 作用 |
|---|---|
| Binomial exact calculation | 精确二项计算 |
| Poisson approximation | \(n\) 大、\(p\) 小，\(\lambda=np\) |
| Normal approximation | \(n\) 大，\(np\)、\(n(1-p)\) 足够大 |
| Continuity correction | 离散变量用连续正态近似时加减 0.5 |

### 必须掌握模板

```text
If X ~ Binomial(n,p):

μ = np
σ² = np(1-p)
σ = sqrt(np(1-p))

X ≈ N(μ, σ²)

P(a ≤ X ≤ b)
≈ Φ((b+0.5-μ)/σ) - Φ((a-0.5-μ)/σ)
```

### 放到 cheating sheet

1. Poisson approximation 条件
2. Normal approximation 条件
3. Continuity correction 模板
4. 常见 \(\Phi\) 值或 standard normal table

### 复制问 AI

```text
请讲清楚 Binomial 分布什么时候可以用 Poisson approximation，什么时候可以用 Normal approximation。
要求：
1. 说明直觉；
2. 给出公式；
3. 重点解释 continuity correction 为什么要加 0.5；
4. 给我一个完整考试模板。
```

---

## 7. Day 1 - Part 4：随机变量变换

### 时间

**14:30-16:30**

### 必须搞懂的题型

| 题型 | 方法 |
|---|---|
| \(Y=g(X)\)，单调 | 反函数 + derivative |
| \(Y=g(X)\)，非单调/分段 | CDF method |
| \(Y=\max(X_1,X_2)\) | CDF method |
| \(Y=\min(X_1,X_2)\) | Survival method |
| \((U,V)=g(X,Y)\) | Jacobian |
| \(Z=X+Y\) | Convolution |

### 核心模板 1：CDF method

```text
F_Y(y)=P(Y≤y)=P(g(X)≤y)

Step 1: Fix y
Step 2: Solve the x-region satisfying g(x)≤y
Step 3: Integrate f_X(x) over that region
Step 4: Differentiate if f_Y(y) is required
```

### 核心模板 2：max

```text
Y=max(X1,X2)

F_Y(y)=P(Y≤y)
=P(X1≤y, X2≤y)

If independent:
F_Y(y)=F_X1(y)F_X2(y)

f_Y(y)=dF_Y(y)/dy
```

### 核心模板 3：Jacobian

```text
U=g1(X,Y), V=g2(X,Y)

1. Solve inverse:
   x=x(u,v), y=y(u,v)

2. Find support of (u,v)

3. Compute:
   J = |∂(x,y)/∂(u,v)|

4. Then:
   f_{U,V}(u,v)=f_{X,Y}(x(u,v),y(u,v))J
```

### 必须掌握的方法

1. 先看 \(g\) 是否 one-to-one
2. 非单调一定优先用 CDF
3. 二维变换一定先反解
4. support 不能忘

### 复制问 AI

```text
请用考试角度讲随机变量变换。
要求：
1. 区分 CDF method、反函数法、Jacobian 法；
2. 解释什么时候用哪一种；
3. 讲 Y=max(X1,X2) 的固定模板；
4. 讲 Y=g(X) 分段函数时怎么找区间；
5. 最后给 cheating sheet 模板。
```

---

## 8. Day 1 - Part 5：Poisson Process + Exponential

### 时间

**17:00-19:00**

### 需要搞懂的概念

| 概念 | 说明 |
|---|---|
| Poisson Process | 按固定 rate 随机到达的事件流 |
| Counting Process | \(N_t\) 表示 t 前事件数 |
| Independent increments | 不重叠时间段内事件数独立 |
| Interarrival time | 相邻事件之间的等待时间 |
| Memoryless | 已等时间不影响未来等待时间 |

### 核心公式

```text
N_t - N_s ~ Poisson(λ(t-s))

P(N_t=k)=e^{-λt}(λt)^k/k!

P(N_t=0)=e^{-λt}

W_1 ~ Exponential(scale=1/λ)

P(W>t)=e^{-λt}
```

### 必须掌握的方法

1. 把时间长度变成 \(λt\)
2. “没有事件”就是 \(P(N_t=0)\)
3. “等待超过 t”就是 \(P(W>t)\)
4. 不重叠时间段可以独立相乘

### 复制问 AI

```text
请用考试题方式讲 Poisson Process 和 Exponential Distribution 的关系。
要求：
1. 解释 N_t 是什么；
2. 解释为什么等待时间是 Exponential；
3. 给出常见题型：某时间内至少几个事件、等待超过多久、两个时间段是否独立；
4. 最后给 cheating sheet 模板。
```

---

# Day 2 详细路线

---

## 9. Day 2 - Part 1：Joint Distribution 基础

### 时间

**09:00-10:30**

### 需要搞懂的概念

| 概念 | 英文 | 你要会什么 |
|---|---|---|
| 联合分布 | Joint Distribution | 两个变量一起的分布 |
| 边缘分布 | Marginal Distribution | 把另一个变量加掉/积分掉 |
| 条件分布 | Conditional Distribution | 已知一个变量后的分布 |
| 独立 | Independence | joint 能否拆成 marginals 相乘 |
| 支撑区域 | Support | 哪些 \((x,y)\) 可能出现 |

### 核心公式

```text
Discrete:
p_X(x)=Σ_y p_XY(x,y)
p_Y(y)=Σ_x p_XY(x,y)

Continuous:
f_X(x)=∫ f_XY(x,y)dy
f_Y(y)=∫ f_XY(x,y)dx

Conditional:
f_X|Y(x|y)=f_XY(x,y)/f_Y(y)

Independence:
f_XY(x,y)=f_X(x)f_Y(y)
```

### 必须掌握的方法

1. 先画 support
2. 固定一个变量，看另一个变量范围
3. 积分上下限来自 support，不是永远 \(-\infty\) 到 \(\infty\)
4. 条件后 support 可能改变

### 复制问 AI

```text
请用考试角度讲 joint distribution。
要求：
1. 讲 joint pdf、marginal pdf、conditional pdf；
2. 用一个二维区域例子说明怎么找积分上下限；
3. 解释 support 为什么重要；
4. 给我一套 joint density 大题模板。
```

---

## 10. Day 2 - Part 2：Joint Density 大题完整模板

### 时间

**10:30-12:30**

### 必须练熟的流程

```text
Given f_XY(x,y):

Step 0: Find support

Step 1: Normalize if unknown constant exists:
∫∫ f_XY(x,y) dxdy = 1

Step 2: Find marginal:
f_Y(y)=∫f_XY(x,y)dx

Step 3: Find conditional:
f_X|Y(x|y)=f_XY(x,y)/f_Y(y)

Step 4: Find conditional expectation:
E[X|Y=y]=∫x f_X|Y(x|y)dx

Step 5: Use total expectation:
E[X]=E[E[X|Y]]

Step 6: Check independence:
f_XY ?= f_X f_Y
```

### 复制问 AI

```text
请带我完整做一类 joint density 大题。
题型是：给 f_XY(x,y)，要求 marginal density、conditional density、E[X|Y]、E[X]、判断 independence。
要求：
1. 先给通用模板；
2. 再给一个简单例子；
3. 特别强调 support 和积分上下限；
4. 最后总结成 cheating sheet 版本。
```

---

## 11. Day 2 - Part 3：Covariance / Correlation / Independence

### 时间

**13:30-15:00**

### 需要搞懂的概念

| 概念 | 说明 |
|---|---|
| Covariance | 两个变量线性同向/反向变化趋势 |
| Correlation | 标准化后的 covariance |
| Uncorrelated | 协方差为 0 |
| Independent | 一个变量不给另一个变量信息 |

### 核心公式

```text
Cov(X,Y)=E[(X-E[X])(Y-E[Y])]

Cov(X,Y)=E[XY]-E[X]E[Y]

ρ_XY = Cov(X,Y)/(σ_Xσ_Y)
```

### 必须记住

```text
Independent ⇒ Cov(X,Y)=0

Cov(X,Y)=0 does NOT imply independent

For jointly Gaussian random variables:
Cov(X,Y)=0 ⇔ independent
```

### 放到 cheating sheet

1. Cov 计算公式
2. Correlation 公式
3. 独立与不相关区别
4. Gaussian 特殊情况

### 复制问 AI

```text
请讲清楚 covariance、correlation、independence、uncorrelated 的区别。
要求：
1. 用直觉解释；
2. 给公式；
3. 举一个 Cov=0 但不 independent 的例子；
4. 告诉我考试中怎么判断 independence。
```

---

## 12. Day 2 - Part 4：Conditional Expectation

### 时间

**15:00-17:00**

### 需要搞懂的概念

| 概念 | 说明 |
|---|---|
| \(E[X|Y=y]\) | 固定 y 后的一个数字 |
| \(E[X|Y]\) | 把 y 换成 Y 后的随机变量 |
| Total expectation | \(E[E[X|Y]]=E[X]\) |
| Total variance | \(Var(X)=E[Var(X|Y)]+Var(E[X|Y])\) |
| Regression curve | 条件期望作为预测函数 |

### 核心模板

```text
1. Find f_X|Y(x|y)

2. Compute:
E[X|Y=y]=∫x f_X|Y(x|y)dx

3. Replace y by Y:
E[X|Y]=g(Y)

4. Use:
E[X]=E[E[X|Y]]
```

### 必须掌握的方法

1. 先求 conditional density
2. 再求 conditional expectation
3. \(E[X|Y=y]\) 是数字
4. \(E[X|Y]\) 是随机变量
5. total expectation 可以减少二重积分

### 复制问 AI

```text
请讲清楚 conditional expectation。
要求：
1. 区分 E[X|Y=y] 和 E[X|Y]；
2. 解释它为什么是 joint density 题的后半部分；
3. 用一个例子说明怎么从 f_XY 求 E[X|Y]；
4. 讲 total expectation 怎么用来简化计算；
5. 最后给 cheating sheet 模板。
```

---

## 13. Day 2 - Part 5：Reliability / Hazard / Weibull

### 时间

**17:30-19:30**

### 需要搞懂的概念

| 概念 | 英文 | 说明 |
|---|---|---|
| 失效时间 | Failure Time | 设备坏掉的时间 \(T\) |
| 可靠性函数 | Reliability Function | \(R(t)=P(T>t)\) |
| 失效密度 | Failure Density | \(f(t)=F'(t)\) |
| 风险率 | Hazard Rate | 活到 t 后马上坏的风险 |
| 串联系统 | Series System | 一个坏就全坏 |
| 并联系统 | Parallel System | 全部坏才全坏 |
| Weibull | Weibull Distribution | 可描述 increasing/decreasing hazard |

### 核心公式

```text
F(t)=P(T≤t)

R(t)=P(T>t)=1-F(t)

ρ(t)=f(t)/R(t)

R(t)=exp(-∫_0^t ρ(s)ds)

Series:
R_series(t)=Π_i R_i(t)

Parallel:
R_parallel(t)=1-Π_i[1-R_i(t)]
```

### Weibull

```text
R(t)=e^{-αt^β}

ρ(t)=αβt^{β-1}

β>1: increasing hazard
β=1: constant hazard
0<β<1: decreasing hazard
```

### 必须掌握的方法

把文字翻译成事件：

```text
still working at time t → T>t

failed by time t → T≤t

failed between a and b → a<T≤b

P(still working at a | failed by b)
= P(a<T≤b)/P(T≤b)
= [R(a)-R(b)]/[1-R(b)]
```

### 复制问 AI

```text
请用考试角度讲 Reliability。
要求：
1. 解释 F(t)、R(t)、f(t)、hazard rate 的关系；
2. 讲 series system 和 parallel system；
3. 讲 Exponential 和 Weibull 在 reliability 里的区别；
4. 重点讲如何把 still working / failed by 翻译成条件概率；
5. 给 cheating sheet 模板。
```

---

## 14. Day 2 - Part 6：MGF 快速掌握

### 时间

**20:30-21:30**

### 需要搞懂的概念

| 概念 | 说明 |
|---|---|
| MGF | \(m_X(t)=E[e^{tX}]\) |
| Moment extraction | 用导数求矩 |
| Independent sums | 独立和的 MGF 相乘 |
| Uniqueness | MGF 相同则分布相同 |

### 核心公式

```text
m_X(t)=E[e^{tX}]

E[X^k]=m_X^(k)(0)

If X,Y independent:
m_X+Y(t)=m_X(t)m_Y(t)

If m_X(t)=m_Y(t) near 0:
X and Y have the same distribution
```

### 必须掌握的方法

1. 会查分布 MGF
2. 独立和时把 MGF 相乘
3. 识别乘完以后是什么分布
4. 会用一阶、二阶导数求均值方差

### 复制问 AI

```text
请用考试角度讲 MGF。
要求：
1. 解释 MGF 是什么；
2. 讲怎么用 MGF 求 E[X] 和 Var(X)；
3. 讲独立随机变量相加为什么 MGF 相乘；
4. 用 Poisson+Poisson 或 Gamma+Gamma 做例子；
5. 最后给 cheating sheet 模板。
```

---

# 15. 最终 cheating sheet 目录建议

你最终在线文档或纸质材料建议按这个顺序组织：

```text
0. Quick Index

1. Distribution Recognition Table
   - 题目关键词 → 分布
   - fixed quantity / random quantity

2. Common Distributions
   - Bernoulli
   - Binomial
   - Geometric
   - Negative Binomial
   - Hypergeometric
   - Poisson
   - Exponential
   - Gamma
   - Normal
   - Weibull

3. Approximation
   - Binomial exact
   - Poisson approximation
   - Normal approximation
   - Continuity correction

4. Poisson Process
   - N_t
   - independent increments
   - interarrival time
   - memoryless

5. One-dimensional Transformation
   - CDF method
   - monotone transformation
   - max
   - min
   - piecewise g(X)

6. Multivariate Transformation
   - Jacobian
   - sum/convolution
   - product/ratio if needed
   - polar coordinates if needed

7. Joint Distribution Workflow
   - joint pmf/pdf
   - marginal
   - conditional
   - support
   - independence

8. Conditional Expectation
   - E[X|Y=y]
   - E[X|Y]
   - total expectation
   - total variance
   - regression curve

9. Covariance and Correlation
   - Cov formula
   - rho formula
   - independent vs uncorrelated
   - covariance matrix

10. Reliability
   - F(t), f(t), R(t), hazard
   - Exponential reliability
   - Weibull reliability
   - series system
   - parallel system

11. MGF Toolkit
   - definition
   - moment extraction
   - independent sums
   - uniqueness
   - common MGF table

12. Inequalities / LLN / CLT
   - Markov
   - Chebyshev
   - Cantelli
   - LLN
   - CLT

13. Common Traps
   - PMF vs PDF
   - independent vs disjoint
   - independent vs uncorrelated
   - expectation vs probability
   - Binomial vs Hypergeometric
   - Geometric vs Negative Binomial
   - CDF method vs Jacobian
```

---

# 16. 每个概念问 AI 的统一提示词模板

你可以每次把下面模板中的 `[概念名]` 替换掉。

```text
我正在复习 ECE4010J 期中考试，现在要学 [概念名]。

请你按考试导向讲解：
1. 这个概念是什么，用中文直观解释；
2. 它在题目里通常怎么出现；
3. 我需要掌握到什么程度；
4. 哪些公式应该放进 cheating sheet；
5. 哪些细节可以不深入理解；
6. 给一个最小例题，并完整解答；
7. 最后给我一段英文版 cheating sheet note。
```

---

# 17. 每类题问 AI 的统一提示词模板

```text
我正在复习 ECE4010J 期中考试，现在要掌握 [题型名]。

请你按以下结构教我：
1. 先说明这类题的识别关键词；
2. 给出通用解题步骤；
3. 给出必须写在 cheating sheet 上的模板；
4. 给一个简单例题；
5. 给一个接近考试难度的例题；
6. 总结常见陷阱；
7. 最后问我一道小题确认我是否理解。
```

---

# 18. 最后一天晚上自测清单

考试前一晚，逐项检查：

## 分布识别

- [ ] 我能区分 Binomial / Geometric / Negative Binomial
- [ ] 我能区分 Binomial / Hypergeometric
- [ ] 我知道 Poisson 什么时候用
- [ ] 我知道 Exponential 是等待时间
- [ ] 我知道 Gamma 是多个 Exponential 等待时间之和
- [ ] 我知道 Weibull 用于 reliability

## 变换

- [ ] 我会用 CDF method
- [ ] 我会做 \(Y=\max(X_1,X_2)\)
- [ ] 我知道非单调函数不能随便用反函数公式
- [ ] 我知道二维变换要用 Jacobian
- [ ] 我会先找 support

## 联合分布

- [ ] 我会从 joint pdf 求 marginal
- [ ] 我会从 joint pdf 求 conditional pdf
- [ ] 我会求 \(E[X|Y=y]\)
- [ ] 我知道 \(E[X|Y]\) 是随机变量
- [ ] 我会用 total expectation
- [ ] 我会判断 independence

## 可靠性

- [ ] 我知道 \(R(t)=P(T>t)\)
- [ ] 我知道 hazard rate 是 \(f(t)/R(t)\)
- [ ] 我会做 series system
- [ ] 我会做 parallel system
- [ ] 我会把 still working / failed by 翻译成条件概率
- [ ] 我知道 Weibull 的 hazard 由 \(\beta\) 决定

## MGF / 近似

- [ ] 我知道 MGF 定义
- [ ] 我知道独立和的 MGF 相乘
- [ ] 我会用 normal approximation
- [ ] 我会 continuity correction
- [ ] 我知道 CLT 的基本用途

---

# 19. 两天复习的最低完成标准

如果时间不够，最低要完成这些：

```text
1. 分布识别表
2. 常见分布公式表
3. Normal approximation 模板
4. CDF method / max / min 模板
5. Joint density 完整流程模板
6. Conditional expectation 模板
7. Reliability / hazard / series / parallel 模板
8. Common traps 表
```

只要这 8 个内容能熟练查和套，考试就有基本战斗力。

---

# 20. 最重要的一句话

不要把时间花在“把所有公式背下来”。

你真正要练的是：

```text
看到题目 → 判断类型 → 找对应模板 → 翻译事件/区域 → 套公式
```

公式可以放纸上，**题型判断和 support 判断必须靠你自己练**。
