# 09 — Conditional Expectation + Total Laws

> 覆盖范围：C-COND-001

## 考试识别模板

```text
E[X|Y=y] = average of X under conditional distribution.
E[X]=E(E[X|Y]).
Var(X)=E[Var(X|Y)] + Var(E[X|Y]).
Random sum: E[sum_{i=1}^N Xi]=E[N]E[X] if independent.
```

## 典型例题

### EX-COND-101 — 离散条件期望

**题目**

\[
\begin{array}{c|cc}
p(x,y)&y=0&y=1\\\hline
x=0&0.2&0.1\\
x=2&0.3&0.4
\end{array}
\]
求 \(E[X|Y=1]\)。

**解法 / 可抄步骤**

\[
P(Y=1)=0.5.
\]
\[
P(X=0|Y=1)=0.1/0.5=0.2,\quad P(X=2|Y=1)=0.4/0.5=0.8.
\]
\[
E[X|Y=1]=0(0.2)+2(0.8)=1.6.
\]

---

### EX-COND-102 — 连续条件期望

**题目**

\(f(x,y)=2,\ 0<y<x<1\)。求 \(E[X|Y=y]\)。

**解法 / 可抄步骤**

\[
f_Y(y)=\int_y^1 2dx=2(1-y).
\]
\[
f_{X|Y}(x|y)=\frac{1}{1-y},\quad y<x<1.
\]
所以 \(X|Y=y\sim Unif(y,1)\)：
\[
E[X|Y=y]=\frac{y+1}{2}.
\]

---

### EX-COND-103 — Law of Total Expectation

**题目**

产品来自 A 线概率 0.7，缺陷数均值 2；B 线概率 0.3，缺陷数均值 5。求总体缺陷数均值。

**解法 / 可抄步骤**

\[
E[X]=E(E[X|L])=2(0.7)+5(0.3)=2.9.
\]

---

### EX-COND-104 — Law of Total Variance

**题目**

沿用上一题，\(Var(X|A)=1, Var(X|B)=4\)。求 \(Var(X)\)。

**解法 / 可抄步骤**

\[
Var(X)=E[Var(X|L)]+Var(E[X|L]).
\]
\[
E[Var(X|L)]=1(0.7)+4(0.3)=1.9.
\]
条件均值随机变量取 2 和 5，总均值 2.9：
\[
Var(E[X|L])=0.7(2-2.9)^2+0.3(5-2.9)^2=1.89.
\]
\[
Var(X)=1.9+1.89=3.79.
\]

---

### EX-COND-105 — Random Sum

**题目**

订单数 \(N\sim Pois(10)\)，每单金额均值 20，独立。总金额 \(S=\sum_{i=1}^{N}X_i\)。求 \(E[S]\)。

**解法 / 可抄步骤**

\[
E[S|N=n]=20n.
\]
\[
E[S]=E(E[S|N])=E[20N]=20E[N]=200.
\]

---

### EX-COND-106 — Exponential 剩余寿命期望

**题目**

\(T\sim Exp(\lambda)\)。求 \(E[T-s|T>s]\) 和 \(E[T|T>s]\)。

**解法 / 可抄步骤**

Memoryless:
\[
T-s|T>s\sim Exp(\lambda).
\]
\[
E[T-s|T>s]=1/\lambda.
\]
\[
E[T|T>s]=s+1/\lambda.
\]

---

## 参考资料

- LibreTexts joint continuous: https://stats.libretexts.org/Courses/Saint_Mary%27s_College_Notre_Dame/MATH_345__-_Probability_%28Kuter%29/5%3A_Probability_Distributions_for_Combinations_of_Random_Variables/5.2%3A_Joint_Distributions_of_Continuous_Random_Variables
- Penn State STAT 414 exponential/gamma: https://online.stat.psu.edu/stat414/Lesson15
