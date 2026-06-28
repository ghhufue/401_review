# EX-DIST-005 — Poisson Area Scaling

**Concept Tags:** `#poisson` `#area-scaling` `#at-least-one` `#complement-rule`  
**Related Concepts:** `C-DIST-001`  
**Source:** Assignment 3, Exercise 3.5  
**Problem Pattern:** Given an average count over a whole region, scale \(\lambda\) to a smaller sampled area, then use Poisson probability.

---

## Problem / 原题

Escherichia coli, a bacterium often found in the human digestive tract, can mutate from being streptomycin sensitive to being streptomycin resistant, which can cause the individual involved to become resistant to the antibiotic streptomycin. Assume that there is an average of two streptomycin-resistant bacteria on cultures drawn from a particular patient. Each culture has an area of 80 square centimeters.

1. What is the probability that a one-square-centimeter random sample from a single culture will contain at least one resistant bacterium?
2. What is the probability that at least one will be found in 5 randomly selected one-square-centimeter samples? Assume that the 5 samples are independent.

---

## 中文翻译

大肠杆菌常见于人体消化道中。它可能从对链霉素敏感变异为对链霉素有抗性，从而使相关个体对抗生素链霉素产生抗性。

假设从某个病人身上取出的培养皿中，平均有 2 个抗链霉素细菌。每个培养皿面积为 \(80\text{ cm}^2\)。

1. 随机从一个培养皿中取 \(1\text{ cm}^2\) 的样本，求这个样本中至少含有一个抗性细菌的概率。
2. 随机选取 5 个独立的 \(1\text{ cm}^2\) 样本，求至少发现一个抗性细菌的概率。

---

## Recognition / 分布识别

This is a **Poisson distribution** problem because it asks for the number of random occurrences in a fixed area.

这是泊松分布题，因为题目给的是某个面积区域内随机出现的细菌数量。

Let

\[
X=\text{number of resistant bacteria in a }1\text{ cm}^2\text{ sample}.
\]

The whole culture has area \(80\text{ cm}^2\) and average count 2, so the mean count per \(1\text{ cm}^2\) is

\[
\lambda_{1}=\frac{2}{80}=0.025.
\]

Therefore

\[
X\sim Pois(0.025).
\]

> Exam Tip: Poisson 的 \(\lambda\) 是“当前研究区域内的平均个数”。如果面积变小，\(\lambda\) 也要按比例缩小。

---

## Part (i)

We need

\[
P(X\ge 1).
\]

Use the complement rule:

\[
P(X\ge 1)=1-P(X=0).
\]

For \(X\sim Pois(\lambda)\),

\[
P(X=0)=e^{-\lambda}.
\]

Thus

\[
P(X\ge 1)=1-e^{-0.025}.
\]

Numerically,

\[
1-e^{-0.025}\approx 0.0247.
\]

**Final Answer:**

\[
\boxed{P(X\ge 1)=1-e^{-0.025}\approx 0.0247}
\]

---

## Part (ii)

Five independent \(1\text{ cm}^2\) samples have total mean count

\[
\lambda_5=5\lambda_1=5(0.025)=0.125.
\]

Let

\[
Y=\text{number of resistant bacteria found in the 5 samples}.
\]

Then

\[
Y\sim Pois(0.125).
\]

We need

\[
P(Y\ge 1)=1-P(Y=0)=1-e^{-0.125}.
\]

Numerically,

\[
1-e^{-0.125}\approx 0.1175.
\]

**Final Answer:**

\[
\boxed{P(Y\ge 1)=1-e^{-0.125}\approx 0.1175}
\]

---

## Alternative Method for Part (ii)

A single \(1\text{ cm}^2\) sample has no resistant bacteria with probability

\[
P(X=0)=e^{-0.025}.
\]

Five independent samples all have no resistant bacteria with probability

\[
(e^{-0.025})^5=e^{-0.125}.
\]

Therefore at least one sample contains a resistant bacterium:

\[
1-e^{-0.125}.
\]

---

## Common Mistakes / 常见错误

1. **Using \(\lambda=2\) directly for \(1\text{ cm}^2\).**  
   The value 2 is the average count in the full \(80\text{ cm}^2\) culture, not in a \(1\text{ cm}^2\) sample.

2. **Forgetting to scale \(\lambda\) by area.**  
   \[
   \lambda_{1}=\frac{2}{80},\qquad \lambda_5=5\cdot \frac{2}{80}.
   \]

3. **Computing \(P(X=1)\) instead of \(P(X\ge 1)\).**  
   “At least one” means use complement:
   \[
   P(X\ge 1)=1-P(X=0).
   \]

---

## Cheat-Sheet Template

For Poisson count in area/time/length:

\[
X\sim Pois(\lambda),\qquad P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
\]

For “at least one”:

\[
P(X\ge 1)=1-P(X=0)=1-e^{-\lambda}.
\]

If average count is given on a larger region:

\[
\lambda_{sample}=\lambda_{whole}\cdot \frac{\text{sample size}}{\text{whole size}}.
\]

For this problem:

\[
\lambda_{1cm^2}=2\cdot \frac{1}{80}=0.025,\qquad
\lambda_{5cm^2}=2\cdot \frac{5}{80}=0.125.
\]
