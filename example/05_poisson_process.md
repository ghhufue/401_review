# 05 — Poisson Process + Exponential Waiting Time

> 覆盖范围：C-PP-001

## 考试识别模板

```text
Poisson process with rate λ:
N(t)~Pois(λt).
Time to first event ~ Exp(λ).
Time to kth event ~ Gamma(k,λ).
Independent increments: disjoint intervals independent.
```

## 典型例题

### EX-PP-101 — Count in interval

**题目**

报警平均每小时 3 次。求 2 小时内恰好 4 次报警概率。

**解法 / 可抄步骤**

\[
N(2)\sim Pois(3\cdot2)=Pois(6).
\]
\[
P(N(2)=4)=e^{-6}\frac{6^4}{4!}.
\]

---

### EX-PP-102 — Waiting to first event

**题目**

平均每 10 分钟 1 个电话。求下一通电话等待超过 15 分钟的概率。

**解法 / 可抄步骤**

\[
\lambda=1/10\ \text{per minute},\quad T\sim Exp(1/10).
\]
\[
P(T>15)=e^{-15/10}=e^{-1.5}.
\]

---

### EX-PP-103 — 第 3 次事件在 10 小时内发生

**题目**

Poisson process rate \(0.2\)/hour。求第 3 次故障在 10 小时内发生的概率。

**解法 / 可抄步骤**

\[
P(T_3\le10)=P(N(10)\ge3).
\]
\[
N(10)\sim Pois(2).
\]
\[
P(N(10)\ge3)=1-e^{-2}\left(1+2+\frac{2^2}{2!}\right)=1-5e^{-2}.
\]

---

### EX-PP-104 — Independent increments

**题目**

错误到达 rate 4/hour。求第 1 小时有 2 个错误，接下来 2 小时有 5 个错误的概率。

**解法 / 可抄步骤**

\[
P=\left(e^{-4}\frac{4^2}{2!}\right)\left(e^{-8}\frac{8^5}{5!}\right).
\]
因为 \(N(1)\sim Pois(4)\)，\(N(3)-N(1)\sim Pois(8)\)，且独立。

---

### EX-PP-105 — Memoryless residual time

**题目**

电话到达 rate 6/hour。已经 10 分钟没电话了，求还要再等超过 5 分钟概率。

**解法 / 可抄步骤**

\[
P(T>15\text{ min}\mid T>10\text{ min})=P(T>5\text{ min})
=e^{-6(1/12)}=e^{-0.5}.
\]

---

### EX-PP-106 — Thinning

**题目**

请求到达 rate 20/min，每个请求有 10% 是错误请求。求一分钟内错误请求数分布。

**解法 / 可抄步骤**

\[
N_{\text{error}}\sim Pois(20\cdot0.1)=Pois(2).
\]

---

### EX-PP-107 — Superposition

**题目**

A 错误 rate 2/hour，B 错误 rate 3/hour，独立。合并过程分布？

**解法 / 可抄步骤**

合并后的 Poisson process rate：
\[
\lambda=2+3=5.
\]
\[
N(t)\sim Pois(5t).
\]

---

### EX-PP-108 — 给定总数后的分配

**题目**

一小时平均 12 个请求。已知这一小时一共 6 个请求，求前 20 分钟有 2 个的概率。

**解法 / 可抄步骤**

给定 \(N(1)=6\)，前 20 分钟占 \(1/3\)。
\[
N_{\text{first}}\mid N(1)=6\sim Bin(6,1/3).
\]
\[
P=\binom62(1/3)^2(2/3)^4.
\]

---

## 参考资料

- OpenStax Poisson examples: https://openstax.org/books/introductory-statistics-2e/pages/4-6-poisson-distribution
- Penn State STAT 414 exponential/gamma: https://online.stat.psu.edu/stat414/Lesson15
