# 04 — Binomial Approximation

> 覆盖范围：C-APPROX-001

## 考试识别模板

```text
Binomial -> Poisson: n large, p small, λ=np.
Binomial -> Normal: np and n(1-p) large, use μ=np, σ²=np(1-p).
Discrete -> continuous: use continuity correction ±0.5.
```

## 典型例题

### EX-APPROX-101 — Normal approximation：至少型

**题目**

\(X\sim Bin(300,0.53)\)。用正态近似求 \(P(X\ge150)\)。

**解法 / 可抄步骤**

\[
\mu=np=159,\quad \sigma=\sqrt{np(1-p)}=\sqrt{74.73}\approx8.6447.
\]
Continuity correction:
\[
P(X\ge150)\approx P(Y\ge149.5).
\]
\[
z=\frac{149.5-159}{8.6447}\approx-1.10.
\]
\[
P(Z\ge-1.10)\approx0.8641.
\]

---

### EX-APPROX-102 — Normal approximation：区间型

**题目**

\(X\sim Bin(100,0.5)\)。用正态近似求 \(P(45\le X\le55)\)。

**解法 / 可抄步骤**

\[
\mu=50,\quad \sigma=5.
\]
\[
P(45\le X\le55)\approx P(44.5<Y<55.5).
\]
\[
=P(-1.1<Z<1.1)\approx0.7287.
\]

---

### EX-APPROX-103 — Poisson approximation to Binomial

**题目**

100 个灯泡，每个损坏概率 \(0.03\)。令 \(X\) 为坏灯泡数。用 Poisson 近似求 \(P(X\le4)\)。

**解法 / 可抄步骤**

\[
X\sim Bin(100,0.03),\quad \lambda=np=3.
\]
\[
X\approx Pois(3).
\]
\[
P(X\le4)=\sum_{k=0}^{4}e^{-3}\frac{3^k}{k!}\approx0.8153.
\]

---

### EX-APPROX-104 — Normal approximation to Poisson

**题目**

\(X\sim Pois(80)\)。用正态近似求 \(P(X\ge90)\)。

**解法 / 可抄步骤**

\[
X\approx N(80,80).
\]
\[
P(X\ge90)\approx P(Y>89.5).
\]
\[
z=\frac{89.5-80}{\sqrt{80}}\approx1.062.
\]
\[
P(Z>1.062)\approx0.1441.
\]

---

### EX-APPROX-105 — 判断该用哪个近似

**题目**

\(Bin(1000,0.002)\)、\(Bin(200,0.5)\)、\(Bin(30,0.4)\) 分别适合什么近似？

**解法 / 可抄步骤**

1. \(n\) 大 \(p\) 小：\(Pois(\lambda=2)\)。
2. \(np=100,nq=100\)：\(N(100,50)\)。
3. \(np=12,nq=18\)：可用 normal approximation + CC；精确 binomial 也可。

---

### EX-APPROX-106 — Continuity correction 边界表

**题目**

把 \(P(X<10),P(X\le10),P(X>10),P(X\ge10),P(3<X\le8)\) 改成连续近似。

**解法 / 可抄步骤**

\[
P(X<10)\to P(Y<9.5)
\]
\[
P(X\le10)\to P(Y<10.5)
\]
\[
P(X>10)\to P(Y>10.5)
\]
\[
P(X\ge10)\to P(Y>9.5)
\]
\[
P(3<X\le8)\to P(3.5<Y<8.5)
\]

---

## 参考资料

- OpenStax normal approximation: https://openstax.org/books/statistics/pages/7-3-using-the-central-limit-theorem
- Penn State STAT 414 approximations: https://online.stat.psu.edu/stat414/Lesson28
- OpenStax Poisson examples: https://openstax.org/books/introductory-statistics-2e/pages/4-6-poisson-distribution
