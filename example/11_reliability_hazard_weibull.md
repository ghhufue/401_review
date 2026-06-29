# 11 — Reliability / Hazard / Weibull / Systems

> 覆盖范围：C-REL-001

## 考试识别模板

```text
R(t)=P(T>t)=1-F(t).
h(t)=f(t)/R(t).
Series system: product of reliabilities.
Parallel system: 1 - product of failure probabilities.
Weibull β controls hazard trend.
```

## 典型例题

### EX-REL-101 — CDF 到 reliability

**题目**

\(F(t)=1-e^{-0.01t}\)，\(t\ge0\)。求 \(R(100)\)。

**解法 / 可抄步骤**

\[
R(t)=1-F(t)=e^{-0.01t}.
\]
\[
R(100)=e^{-1}\approx0.3679.
\]

---

### EX-REL-102 — Hazard rate

**题目**

\(T\sim Exp(0.02)\)。求 \(f(t),R(t),h(t)\)。

**解法 / 可抄步骤**

\[
f(t)=0.02e^{-0.02t},\quad R(t)=e^{-0.02t}.
\]
\[
h(t)=\frac{f(t)}{R(t)}=0.02.
\]

---

### EX-REL-103 — Series system

**题目**

两个独立串联部件，寿命分别 \(Exp(0.01)\)、\(Exp(0.02)\)。求 \(R_s(100)\)。

**解法 / 可抄步骤**

串联系统所有部件都活着：
\[
R_s(t)=e^{-0.01t}e^{-0.02t}=e^{-0.03t}.
\]
\[
R_s(100)=e^{-3}\approx0.0498.
\]

---

### EX-REL-104 — Parallel system

**题目**

两个独立并联部件，寿命分别 \(Exp(0.01)\)、\(Exp(0.02)\)。求 \(R_p(100)\)。

**解法 / 可抄步骤**

并联系统至少一个活着：
\[
R_p(t)=1-(1-R_1(t))(1-R_2(t)).
\]
\[
R_p(100)=1-(1-e^{-1})(1-e^{-2})\approx0.4534.
\]

---

### EX-REL-105 — Weibull hazard 趋势

**题目**

Weibull \(h(t)=rac{eta}{lpha}(t/lpha)^{eta-1}\)。判断 \(eta=0.5,1,2\) 的趋势。

**解法 / 可抄步骤**

看 \(\beta-1\)：
- \(\beta<1\)：decreasing hazard；
- \(\beta=1\)：constant hazard，即 exponential；
- \(\beta>1\)：increasing hazard。

---

### EX-REL-106 — 年故障概率换日故障概率

**题目**

一年坏掉概率 10%。假设每天独立且同概率，求每天故障概率。

**解法 / 可抄步骤**

一年不坏概率 \(0.90\)：
\[
(1-p_d)^{365}=0.90.
\]
\[
p_d=1-0.90^{1/365}\approx0.0002886.
\]
约 \(0.0289\%\) per day。

---

### EX-REL-107 — Competing risks

**题目**

\(T_A\sim Exp(0.01)\)，\(T_B\sim Exp(0.02)\)，独立。\(T=\min(T_A,T_B)\) 分布？A 先失效概率？

**解法 / 可抄步骤**

\[
P(T>t)=e^{-0.01t}e^{-0.02t}=e^{-0.03t}.
\]
\[
T\sim Exp(0.03).
\]
\[
P(A\text{ first})=\frac{0.01}{0.01+0.02}=\frac13.
\]

---

### EX-REL-108 — 用 survival 求 mean lifetime

**题目**

\(R(t)=e^{-0.5t}\)。求 \(E[T]\)。

**解法 / 可抄步骤**

非负寿命变量：
\[
E[T]=\int_0^\infty R(t)dt.
\]
\[
E[T]=\int_0^\infty e^{-0.5t}dt=2.
\]

---

## 参考资料

- reliability docs equations: https://reliability.readthedocs.io/en/stable/Equations%20of%20supported%20distributions.html
- LibreTexts transformations: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_%28Siegrist%29/03%3A_Distributions/3.07%3A_Transformations_of_Random_Variables
