# 02 — Distribution Recognition + Discrete Distributions

> 覆盖范围：C-DIST-000, C-DIST-001

## 考试识别模板

```text
Bernoulli: one yes/no trial.
Binomial: fixed n independent trials with same p.
Hypergeometric: sampling without replacement.
Geometric: wait until first success.
Negative binomial: wait until r-th success.
Poisson: count events in a fixed interval.
```

## 典型例题

### EX-DIST-101 — Bernoulli：一次 0/1 试验

**题目**

一次检测到故障的概率为 \(0.03\)。令 \(X=1\) 表示检测到故障，\(X=0\) 表示没有故障。写出分布、均值、方差。

**解法 / 可抄步骤**

\[
X\sim Bern(0.03).
\]
\[
P(X=1)=0.03,\quad P(X=0)=0.97.
\]
\[
E[X]=p=0.03,\quad Var(X)=p(1-p)=0.03(0.97)=0.0291.
\]

---

### EX-DIST-102 — Binomial：固定次数成功数

**题目**

20 个芯片独立测试，每个通过概率 \(0.9\)。令 \(X\) 为通过个数。求 \(P(X=18)\)、均值、方差。

**解法 / 可抄步骤**

固定 \(n=20\)，独立，同一个 \(p=0.9\)：
\[
X\sim Bin(20,0.9).
\]
\[
P(X=18)=\binom{20}{18}(0.9)^{18}(0.1)^2.
\]
\[
E[X]=np=18,\quad Var(X)=np(1-p)=1.8.
\]

---

### EX-DIST-103 — Hypergeometric：不放回

**题目**

50 个零件中 8 个不合格。不放回抽 5 个。令 \(X\) 为不合格数。求 \(P(X=2)\)。

**解法 / 可抄步骤**

不放回：
\[
X\sim Hypergeom(N=50,K=8,n=5).
\]
\[
P(X=2)=\frac{\binom82\binom{42}{3}}{\binom{50}{5}}\approx0.1517.
\]

---

### EX-DIST-104 — Geometric：第一次成功

**题目**

每次启动成功概率 \(0.2\)。令 \(X\) 为第一次成功所需尝试次数。求 \(P(X=4)\)、\(P(X>5)\)。

**解法 / 可抄步骤**

\[
X\sim Geom(0.2),\quad x=1,2,\dots
\]
\[
P(X=4)=(0.8)^3(0.2)=0.1024.
\]
\[
P(X>5)=(0.8)^5=0.32768.
\]

---

### EX-DIST-105 — Negative Binomial：第 r 次成功

**题目**

每次成功概率 \(p=0.2\)。令 \(X\) 为第 3 次成功发生在第几次。求 \(P(X=10)\)。

**解法 / 可抄步骤**

第 10 次必须成功，前 9 次恰好有 2 次成功：
\[
P(X=10)=\binom92p^3(1-p)^7
=\binom92(0.2)^3(0.8)^7\approx0.0604.
\]

---

### EX-DIST-106 — Poisson：固定区间计数

**题目**

网站平均每分钟收到 4 个请求。令 \(X\) 为下一分钟请求数。求 \(P(X=6)\)。

**解法 / 可抄步骤**

固定区间内事件数：
\[
X\sim Pois(4).
\]
\[
P(X=6)=e^{-4}\frac{4^6}{6!}.
\]

---

### EX-DIST-107 — Binomial vs Poisson

**题目**

100 个独立请求中失败个数，失败概率 \(0.01\)；以及一分钟内请求个数，平均每分钟 80 次。分别是什么分布？

**解法 / 可抄步骤**

固定 100 次试验：
\[
X\sim Bin(100,0.01).
\]

固定时间内随机计数：
\[
Y\sim Pois(80).
\]

口诀：
```text
Binomial has fixed n.
Poisson has fixed interval, count is random.
```

---

### EX-DIST-108 — Binomial vs Hypergeometric

**题目**

20 个球中 5 个红球，抽 4 个。放回和不放回分别是什么分布？

**解法 / 可抄步骤**

放回：每次概率不变且独立，
\[
X\sim Bin(4,5/20).
\]

不放回：概率变化，
\[
X\sim Hypergeom(20,5,4).
\]

---

### EX-DIST-109 — 不是 Binomial 的陷阱

**题目**

射击 10 次，但第 \(i\) 次命中概率为 \(0.9-0.02i\)。命中次数是否服从 Binomial？

**解法 / 可抄步骤**

不是。Binomial 要求每次成功概率相同，这里 \(p_i\) 随 \(i\) 改变。

---

### EX-DIST-110 — Poisson 可加性

**题目**

上午故障数 \(Pois(5)\)，下午故障数 \(Pois(7)\)，独立。全天故障数分布？

**解法 / 可抄步骤**

独立 Poisson 相加：
\[
X+Y\sim Pois(5+7)=Pois(12).
\]

---

## 参考资料

- OpenStax discrete distributions: https://openstax.org/books/introductory-business-statistics/pages/4-formula-review
- OpenStax Poisson examples: https://openstax.org/books/introductory-statistics-2e/pages/4-6-poisson-distribution
