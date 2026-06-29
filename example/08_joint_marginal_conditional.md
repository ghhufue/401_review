# 08 — Joint / Marginal / Conditional / Independence

> 覆盖范围：C-JOINT-001, C-COND-001

## 考试识别模板

```text
Joint problem:
1. Draw/write support.
2. Normalize if c unknown.
3. Marginal integrates out the other variable; bounds come from support.
4. Conditional = joint / marginal.
5. Independence requires factorization and product support.
```

## 典型例题

### EX-JOINT-101 — 三角区域 joint PDF

**题目**

\(f(x,y)=c,\ 0<y<x<1\)。求 \(c,f_X(x),f_Y(y),f_{Y|X}(y|x)\)。

**解法 / 可抄步骤**

\[
\int_0^1\int_0^x c\,dy\,dx=\frac c2=1\Rightarrow c=2.
\]
\[
f_X(x)=\int_0^x2dy=2x,\quad 0<x<1.
\]
\[
f_Y(y)=\int_y^1 2dx=2(1-y),\quad 0<y<1.
\]
\[
f_{Y|X}(y|x)=\frac{2}{2x}=\frac1x,\quad 0<y<x.
\]

---

### EX-JOINT-102 — unit square 上 \(c(x+y)\)

**题目**

\(f(x,y)=c(x+y),0<x<1,0<y<1\)。求 \(c\)，判断独立性。

**解法 / 可抄步骤**

\[
\int_0^1\int_0^1 c(x+y)dydx=c=1.
\]
\[
f_X(x)=\int_0^1(x+y)dy=x+\frac12.
\]
\[
f_Y(y)=y+\frac12.
\]
\[
f_X(x)f_Y(y)=(x+\frac12)(y+\frac12)\ne x+y.
\]
所以不独立。

---

### EX-JOINT-103 — support 导致不独立

**题目**

\(f(x,y)=2,\ 0<y<x<1\)。判断 \(X,Y\) 是否独立。

**解法 / 可抄步骤**

不独立。虽然 joint density 是常数，但 support 是三角形，不是 \(S_X	imes S_Y\) 的矩形区域。

---

### EX-JOINT-104 — 离散 joint PMF 表

**题目**

\[
\begin{array}{c|cc}
p(x,y)&y=0&y=1\\\hline
x=0&0.2&0.1\\
x=1&0.3&0.4
\end{array}
\]
求 \(P(X=1)\)、\(P(Y=1)\)、\(P(X=1|Y=1)\)，判断独立。

**解法 / 可抄步骤**

\[
P(X=1)=0.3+0.4=0.7,\quad P(Y=1)=0.1+0.4=0.5.
\]
\[
P(X=1|Y=1)=0.4/0.5=0.8.
\]
独立检查：
\[
P(X=1,Y=1)=0.4\ne0.7\cdot0.5=0.35.
\]
所以不独立。

---

### EX-JOINT-105 — 条件密度

**题目**

\(f(x,y)=6xy,\ 0<x<1,0<y<1\)。求 \(f_{X|Y}(x|y)\)，判断独立。

**解法 / 可抄步骤**

\[
f_Y(y)=\int_0^1 6xy dx=3y.
\]
\[
f_{X|Y}(x|y)=\frac{6xy}{3y}=2x,\quad 0<x<1.
\]
\[
f_X(x)=3x,\quad f_X(x)f_Y(y)=9xy\ne6xy.
\]
不独立。

---

### EX-JOINT-106 — 区域概率

**题目**

\((X,Y)\) 均匀分布在单位正方形。求 \(P(X+Y<1)\)。

**解法 / 可抄步骤**

\[
P=\int_0^1\int_0^{1-x}1\,dy\,dx=\int_0^1(1-x)dx=\frac12.
\]

---

### EX-JOINT-107 — Conditional expectation from joint

**题目**

\(f(x,y)=2,\ 0<y<x<1\)。求 \(E[Y|X=x]\)。

**解法 / 可抄步骤**

\[
f_{Y|X}(y|x)=\frac1x,\quad 0<y<x.
\]
所以 \(Y|X=x\sim Unif(0,x)\)：
\[
E[Y|X=x]=x/2.
\]

---

### EX-JOINT-108 — Joint LOTUS

**题目**

\((X,Y)\) 均匀分布在单位正方形。求 \(E[XY]\)。

**解法 / 可抄步骤**

\[
E[XY]=\int_0^1\int_0^1xy\,dy\,dx=\frac12\cdot\frac12=\frac14.
\]

---

## 参考资料

- LibreTexts joint continuous: https://stats.libretexts.org/Courses/Saint_Mary%27s_College_Notre_Dame/MATH_345__-_Probability_%28Kuter%29/5%3A_Probability_Distributions_for_Combinations_of_Random_Variables/5.2%3A_Joint_Distributions_of_Continuous_Random_Variables
- LibreTexts joint discrete: https://stats.libretexts.org/Courses/Saint_Mary%27s_College_Notre_Dame/MATH_345__-_Probability_%28Kuter%29/5%3A_Probability_Distributions_for_Combinations_of_Random_Variables/5.1%3A_Joint_Distributions_of_Discrete_Random_Variables
