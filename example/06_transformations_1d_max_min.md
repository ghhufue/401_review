# 06 — 1D Transformations + Max / Min

> 覆盖范围：C-TRANS-001, C-TRANS-002

## 考试识别模板

```text
One-to-one: inverse -> support -> f_Y(y)=f_X(x(y))|dx/dy|.
Many-to-one: sum over all inverse roots.
Max: F_max(x)=F(x)^n.
Min: P(min>x)=P(all>x)=[1-F(x)]^n.
```

## 典型例题

### EX-TRANS-101 — Linear transformation

**题目**

\(X\sim Unif(0,1)\)，\(Y=3X+2\)。求 \(f_Y(y)\)。

**解法 / 可抄步骤**

\[
x=\frac{y-2}{3},\quad \left|\frac{dx}{dy}\right|=\frac13.
\]
Support:
\[
0<x<1\Rightarrow 2<y<5.
\]
\[
f_Y(y)=1\cdot\frac13,\quad 2<y<5.
\]

---

### EX-TRANS-102 — 单调非线性变换

**题目**

\(X\sim Unif(0,1)\)，\(Y=X^2\)。求 \(f_Y(y)\)。

**解法 / 可抄步骤**

\[
x=\sqrt y,\quad \left|\frac{dx}{dy}\right|=\frac{1}{2\sqrt y}.
\]
\[
f_Y(y)=\frac{1}{2\sqrt y},\quad 0<y<1.
\]

---

### EX-TRANS-103 — 非一对一变换

**题目**

\(X\sim Unif(-1,1)\)，\(Y=X^2\)。求 \(f_Y(y)\)。

**解法 / 可抄步骤**

两个根：\(x=\sqrt y\) 和 \(x=-\sqrt y\)。
\[
f_Y(y)=\frac12\frac{1}{2\sqrt y}+\frac12\frac{1}{2\sqrt y}
=\frac{1}{2\sqrt y},\quad 0<y<1.
\]

---

### EX-TRANS-104 — CDF method 递减变换

**题目**

\(X\sim Unif(0,1)\)，\(Y=1-X\)。求 \(F_Y(y)\)。

**解法 / 可抄步骤**

\[
F_Y(y)=P(1-X\le y)=P(X\ge1-y).
\]
\[
F_Y(y)=
\begin{cases}
0,&y<0\\
y,&0\le y\le1\\
1,&y>1
\end{cases}
\]
所以 \(Y\sim Unif(0,1)\)。

---

### EX-TRANS-105 — Max of iid Uniform

**题目**

\(X_1,\dots,X_n iid\sim Unif(0,1)\)，\(M=\max X_i\)。求 \(F_M\)、\(f_M\)。

**解法 / 可抄步骤**

\[
F_M(m)=P(X_1\le m,\dots,X_n\le m)=m^n,\quad 0<m<1.
\]
\[
f_M(m)=nm^{n-1}.
\]

---

### EX-TRANS-106 — Min of iid Exponential

**题目**

\(T_1,\dots,T_n iid\sim Exp(\lambda)\)，\(U=\min T_i\)。求分布。

**解法 / 可抄步骤**

\[
P(U>t)=P(T_1>t,\dots,T_n>t)=(e^{-\lambda t})^n=e^{-n\lambda t}.
\]
\[
U\sim Exp(n\lambda).
\]

---

### EX-TRANS-107 — Series/Parallel as min/max

**题目**

两个独立部件 CDF 都是 \(F(t)\)。串联系统和并联系统 reliability？

**解法 / 可抄步骤**

串联系统寿命是 \(\min(T_1,T_2)\)：
\[
R_s(t)=P(T_1>t,T_2>t)=[1-F(t)]^2.
\]

并联系统寿命是 \(\max(T_1,T_2)\)：
\[
F_p(t)=P(T_1\le t,T_2\le t)=F(t)^2.
\]
\[
R_p(t)=1-F(t)^2.
\]

---

### EX-TRANS-108 — Lognormal 变换

**题目**

\(X\sim N(\mu,\sigma^2)\)，\(Y=e^X\)。求 \(Y\) 的 PDF。

**解法 / 可抄步骤**

\[
x=\ln y,\quad \left|\frac{dx}{dy}\right|=\frac1y,\quad y>0.
\]
\[
f_Y(y)=\frac{1}{y\sigma\sqrt{2\pi}}\exp\left[-\frac{(\ln y-\mu)^2}{2\sigma^2}\right],\quad y>0.
\]

---

## 参考资料

- LibreTexts transformations: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_%28Siegrist%29/03%3A_Distributions/3.07%3A_Transformations_of_Random_Variables
