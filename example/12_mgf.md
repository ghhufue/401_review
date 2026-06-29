# 12 — Moment Generating Function

> 覆盖范围：C-MGF-001

## 考试识别模板

```text
M_X(t)=E[e^{tX}].
E[X]=M'(0).
Var(X)=M''(0)-[M'(0)]².
Independent sum: multiply MGFs.
MGF can identify distribution if it exists.
```

## 典型例题

### EX-MGF-101 — 从 PMF 求 MGF

**题目**

\(P(X=0)=0.2,P(X=1)=0.5,P(X=2)=0.3\)。求 \(M_X(t)\)。

**解法 / 可抄步骤**

\[
M_X(t)=E[e^{tX}]=0.2+0.5e^t+0.3e^{2t}.
\]

---

### EX-MGF-102 — 用 MGF 求 mean/variance

**题目**

\(M_X(t)=0.2+0.5e^t+0.3e^{2t}\)。求 \(E[X]\)、\(Var(X)\)。

**解法 / 可抄步骤**

\[
M'(t)=0.5e^t+0.6e^{2t}\Rightarrow E[X]=M'(0)=1.1.
\]
\[
M''(t)=0.5e^t+1.2e^{2t}\Rightarrow E[X^2]=M''(0)=1.7.
\]
\[
Var(X)=1.7-1.1^2=0.49.
\]

---

### EX-MGF-103 — 识别 Binomial

**题目**

\(M_X(t)=(rac34+rac14e^t)^{20}\)。识别分布并写 PMF。

**解法 / 可抄步骤**

Binomial MGF：
\[
(1-p+pe^t)^n.
\]
所以：
\[
X\sim Bin(20,1/4).
\]
\[
P(X=x)=\binom{20}{x}(1/4)^x(3/4)^{20-x},\quad x=0,\dots,20.
\]

---

### EX-MGF-104 — 独立 Poisson 相加

**题目**

\(X\sim Pois(3),Y\sim Pois(5)\)，独立。用 MGF 证明 \(X+Y\sim Pois(8)\)。

**解法 / 可抄步骤**

Poisson MGF:
\[
M(t)=e^{\lambda(e^t-1)}.
\]
\[
M_{X+Y}=e^{3(e^t-1)}e^{5(e^t-1)}=e^{8(e^t-1)}.
\]
所以 \(X+Y\sim Pois(8)\)。

---

### EX-MGF-105 — Normal 线性组合

**题目**

\(X\sim N(1,4),Y\sim N(2,9)\)，独立。\(Z=2X-3Y\)。求分布。

**解法 / 可抄步骤**

独立正态线性组合仍正态。
\[
E[Z]=2(1)-3(2)=-4.
\]
\[
Var(Z)=2^2(4)+(-3)^2(9)=16+81=97.
\]
\[
Z\sim N(-4,97).
\]

---

### EX-MGF-106 — Exponential/Gamma MGF

**题目**

\(X\sim Exp(\lambda)\)。求 MGF，并说明 \(X_1+\cdots+X_k\) 的分布。

**解法 / 可抄步骤**

\[
M_X(t)=\int_0^\infty e^{tx}\lambda e^{-\lambda x}dx=\frac{\lambda}{\lambda-t},\quad t<\lambda.
\]
iid 和：
\[
M_{\sum X_i}(t)=\left(\frac{\lambda}{\lambda-t}\right)^k.
\]
所以：
\[
\sum_{i=1}^kX_i\sim Gamma(k,\lambda).
\]

---

### EX-MGF-107 — MGF 系数识别 PMF

**题目**

\(M_X(t)=0.1e^t+0.2e^{2t}+0.3e^{3t}+0.4e^{4t}\)。求 PMF。

**解法 / 可抄步骤**

\(e^{kt}\) 前面的系数就是 \(P(X=k)\)：
\[
P(X=1)=0.1,\ P(X=2)=0.2,\ P(X=3)=0.3,\ P(X=4)=0.4.
\]

---

### EX-MGF-108 — MGF 不存在怎么办

**题目**

如果某分布没有 MGF，是否就不能求期望和方差？

**解法 / 可抄步骤**

不是。MGF 只是工具。仍可用定义：
\[
E[X]=\int xf(x)dx,\quad Var(X)=E[X^2]-E[X]^2.
\]
题目给 MGF 就用 MGF；没给时不要强行用。

---

## 参考资料

- Penn State STAT 414 MGF: https://online.stat.psu.edu/stat414/Lesson09
- Penn State STAT 414 continuous RV: https://online.stat.psu.edu/stat414/Lesson14
