# 01 — PMF / PDF / CDF / Expectation / Variance / LOTUS

> 覆盖范围：C-RV-001, C-RV-002

## 考试识别模板

```text
Discrete: P = sum PMF.
Continuous: P = integral PDF.
CDF: F(x)=P(X<=x).
Expectation: E[X]=sum/integral x*f.
Variance: Var(X)=E[X^2]-E[X]^2.
LOTUS: E[g(X)] = sum/integral g(x)*f(x), no need to find distribution of g(X).
```

## 典型例题

### EX-RV-101 — 离散 PMF 归一化 + CDF + E/Var

**题目**

随机变量 \(X\) 的 PMF 为 \(p_X(x)=c(x+1)\), \(x=0,1,2,3\)。求 \(c\)、\(F_X(2)\)、\(E[X]\)、\(Var(X)\)。

**解法 / 可抄步骤**

归一化：
\[
\sum_{x=0}^{3}c(x+1)=c(1+2+3+4)=10c=1
\Rightarrow c=\frac1{10}.
\]
因此 \(p(0)=0.1,p(1)=0.2,p(2)=0.3,p(3)=0.4\)。

\[
F_X(2)=P(X\le2)=0.1+0.2+0.3=0.6.
\]

\[
E[X]=0(0.1)+1(0.2)+2(0.3)+3(0.4)=2.
\]

\[
E[X^2]=0+1(0.2)+4(0.3)+9(0.4)=5.
\]

\[
Var(X)=E[X^2]-E[X]^2=5-4=1.
\]

---

### EX-RV-102 — 连续 PDF 归一化 + CDF

**题目**

\(f_X(x)=cx^2,\ 0<x<2\)。求 \(c\)、\(F_X(x)\)、\(P(1<X<2)\)。

**解法 / 可抄步骤**

\[
\int_0^2 cx^2dx=\frac{8c}{3}=1\Rightarrow c=\frac38.
\]

\[
F_X(x)=
\begin{cases}
0,&x\le0\\
\int_0^x \frac38t^2dt=\frac{x^3}{8},&0<x<2\\
1,&x\ge2
\end{cases}
\]

\[
P(1<X<2)=F(2)-F(1)=1-\frac18=\frac78.
\]

**常见坑**

连续型随机变量 \(P(X=1)=0\)，但 \(f_X(1)\) 可以不是 0；PDF 点值不是概率。

---

### EX-RV-103 — 从 CDF 求 PDF 与 median

**题目**

\[
F_X(x)=
\begin{cases}
0,&x<0\\
x^2,&0\le x\le1\\
1,&x>1
\end{cases}
\]
求 \(f_X(x)\)、\(P(0.2<X<0.8)\)、median。

**解法 / 可抄步骤**

\[
f_X(x)=F'_X(x)=2x,\quad 0<x<1.
\]

\[
P(0.2<X<0.8)=F(0.8)-F(0.2)=0.64-0.04=0.60.
\]

Median \(m\) 满足 \(F(m)=0.5\)：
\[
m^2=0.5\Rightarrow m=\sqrt{0.5}\approx0.707.
\]

---

### EX-RV-104 — LOTUS 离散：不求新分布

**题目**

\(X\) 的 PMF 为 \(P(X=1)=0.2,\ P(X=2)=0.5,\ P(X=4)=0.3\)。求 \(E[X^2+3X]\)。

**解法 / 可抄步骤**

用 LOTUS：
\[
E[g(X)]=\sum_x g(x)p(x).
\]
这里 \(g(x)=x^2+3x\)。

\[
E[X^2+3X]=4(0.2)+10(0.5)+28(0.3)=14.2.
\]

**常见坑**

一般 \(E[g(X)]
e g(E[X])\)。

---

### EX-RV-105 — LOTUS 连续：求 \(E[e^{-X}]\)

**题目**

\(X\sim Exp(\lambda=2)\)。求 \(E[e^{-X}]\)。

**解法 / 可抄步骤**

\[
f_X(x)=2e^{-2x},\quad x\ge0.
\]

\[
E[e^{-X}]=\int_0^\infty e^{-x}2e^{-2x}dx
=2\int_0^\infty e^{-3x}dx=\frac23.
\]

---

### EX-RV-106 — CDF=0.5 是 median，不一定是 mean

**题目**

\(X\sim Exp(2)\)。求 mean 和 median。

**解法 / 可抄步骤**

Mean:
\[
E[X]=\frac1\lambda=\frac12.
\]

Median \(m\):
\[
F(m)=1-e^{-2m}=0.5
\Rightarrow m=\frac{\ln2}{2}\approx0.3466.
\]

所以 mean \(0.5\) 不等于 median \(0.3466\)。

---

## 参考资料

- Penn State STAT 414 continuous RV: https://online.stat.psu.edu/stat414/Lesson14
