# 10 — Covariance / Correlation / Independence

> 覆盖范围：C-COV-001

## 考试识别模板

```text
Cov(X,Y)=E[XY]-E[X]E[Y].
ρ=Cov/(σXσY).
Independent => Cov=0.
Cov=0 does not generally imply independent.
Exception: jointly normal.
```

## 典型例题

### EX-COV-101 — 从 joint PMF 求 covariance

**题目**

\[
\begin{array}{c|cc}
p(x,y)&y=0&y=1\\\hline
x=0&0.2&0.1\\
x=1&0.3&0.4
\end{array}
\]
求 \(Cov(X,Y)\)。

**解法 / 可抄步骤**

\[
E[X]=0.7,\quad E[Y]=0.5.
\]
\[
E[XY]=1\cdot1\cdot0.4=0.4.
\]
\[
Cov(X,Y)=0.4-0.7(0.5)=0.05.
\]

---

### EX-COV-102 — 独立推出 covariance 为 0

**题目**

\(X,Y\) 独立，\(E[X]=3,E[Y]=4\)。求 \(E[XY]\), \(Cov(X,Y)\)。

**解法 / 可抄步骤**

独立：
\[
E[XY]=E[X]E[Y]=12.
\]
\[
Cov(X,Y)=12-3\cdot4=0.
\]

---

### EX-COV-103 — 零 covariance 不代表独立

**题目**

\(X\sim Unif(-1,1)\)，\(Y=X^2\)。说明 \(Cov(X,Y)=0\) 但不独立。

**解法 / 可抄步骤**

\[
Cov(X,Y)=Cov(X,X^2)=E[X^3]-E[X]E[X^2].
\]
对称性给出：
\[
E[X]=0,\quad E[X^3]=0.
\]
所以 \(Cov=0\)。但 \(Y=X^2\) 完全由 \(X\) 决定，因此不独立。

---

### EX-COV-104 — 线性组合方差

**题目**

\(Var(X)=4,Var(Y)=9,Cov(X,Y)=2\)。求 \(Var(3X-2Y)\)。

**解法 / 可抄步骤**

\[
Var(aX+bY)=a^2Var(X)+b^2Var(Y)+2abCov(X,Y).
\]
\[
Var(3X-2Y)=9(4)+4(9)+2(3)(-2)(2)=48.
\]

---

### EX-COV-105 — Correlation coefficient

**题目**

\(Var(X)=4,Var(Y)=9,Cov(X,Y)=3\)。求 \(ho\)。

**解法 / 可抄步骤**

\[
\rho=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}=\frac{3}{2\cdot3}=\frac12.
\]

---

### EX-COV-106 — Joint normal 的特殊性

**题目**

\((X,Y)\) 是 bivariate normal，且 \(ho=0\)。是否独立？

**解法 / 可抄步骤**

是。对一般分布，\(ho=0\) 不推出独立；但对 jointly normal，zero correlation implies independence。

---

## 参考资料

- LibreTexts joint continuous: https://stats.libretexts.org/Courses/Saint_Mary%27s_College_Notre_Dame/MATH_345__-_Probability_%28Kuter%29/5%3A_Probability_Distributions_for_Combinations_of_Random_Variables/5.2%3A_Joint_Distributions_of_Continuous_Random_Variables
