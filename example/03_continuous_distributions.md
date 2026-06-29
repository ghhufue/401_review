# 03 — Continuous Distributions

> 覆盖范围：C-DIST-002, C-PP-001, C-REL-001

## 考试识别模板

```text
Uniform: equal length -> equal probability.
Exponential: waiting time to next Poisson event; memoryless.
Gamma/Erlang: waiting time to kth Poisson event.
Normal: standardize by Z=(X-μ)/σ.
Weibull: lifetime with flexible hazard.
```

## 典型例题

### EX-CONT-101 — Uniform 区间概率

**题目**

\(X\sim Unif(0,10)\)。求 \(P(3<X<8)\)、\(E[X]\)、\(Var(X)\)。

**解法 / 可抄步骤**

\[
P(3<X<8)=\frac{8-3}{10}=0.5.
\]
\[
E[X]=\frac{0+10}{2}=5,\quad Var(X)=\frac{(10-0)^2}{12}=\frac{100}{12}.
\]

---

### EX-CONT-102 — Uniform 条件概率

**题目**

\(X\sim Unif(0,10)\)。求 \(P(X>7\mid X>4)\)。

**解法 / 可抄步骤**

\[
P(X>7\mid X>4)=\frac{P(X>7)}{P(X>4)}
=\frac{3/10}{6/10}=\frac12.
\]

---

### EX-CONT-103 — Exponential 等下一次事件

**题目**

机器平均每小时 0.5 次故障。令 \(T\) 为下一次故障等待时间。求 \(P(T>3)\)。

**解法 / 可抄步骤**

\[
T\sim Exp(0.5).
\]
\[
P(T>3)=e^{-0.5\cdot3}=e^{-1.5}.
\]

---

### EX-CONT-104 — Exponential memoryless

**题目**

\(T\sim Exp(0.5)\)。已知已运行 4 小时，求还要再运行超过 3 小时的概率。

**解法 / 可抄步骤**

\[
P(T>7\mid T>4)=P(T>3)=e^{-1.5}.
\]

---

### EX-CONT-105 — Gamma/Erlang 等第 k 次事件

**题目**

Poisson process rate \(2\)/hour。令 \(W\) 为第 3 次事件发生时间。写出 PDF。

**解法 / 可抄步骤**

\[
W\sim Gamma(\alpha=3,\lambda=2).
\]
\[
f_W(w)=\frac{2^3}{\Gamma(3)}w^2e^{-2w}=4w^2e^{-2w},\quad w>0.
\]

---

### EX-CONT-106 — Normal 标准化

**题目**

\(X\sim N(75,10^2)\)。求 \(P(X>90)\)。

**解法 / 可抄步骤**

\[
P(X>90)=P\left(Z>\frac{90-75}{10}\right)=P(Z>1.5)\approx0.0668.
\]

---

### EX-CONT-107 — Rate vs Scale

**题目**

\(T\sim Exp(\lambda=4)\) 与 \(T\sim Exp(eta=4)\) 的均值分别是多少？

**解法 / 可抄步骤**

Rate form: \(E[T]=1/\lambda=1/4\)。  
Scale form: \(E[T]=\beta=4\)。

考试中一定先看参数是 rate 还是 scale。

---

### EX-CONT-108 — Weibull survival

**题目**

\(T\) 服从 Weibull，scale \(lpha=200\)，shape \(eta=2\)。求 \(R(100)\)。

**解法 / 可抄步骤**

\[
R(t)=e^{-(t/\alpha)^\beta}.
\]
\[
R(100)=e^{-(100/200)^2}=e^{-0.25}\approx0.7788.
\]

---

## 参考资料

- Penn State STAT 414 continuous RV: https://online.stat.psu.edu/stat414/Lesson14
- Penn State STAT 414 exponential/gamma: https://online.stat.psu.edu/stat414/Lesson15
- reliability docs equations: https://reliability.readthedocs.io/en/stable/Equations%20of%20supported%20distributions.html
