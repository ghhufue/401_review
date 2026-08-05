# 06 - Simple Linear Regression and Correlation

> 这一章用一组小数据贯穿 OLS、残差、SSE、系数推断、mean-response interval、prediction interval 和 Pearson correlation。

---

## Shared data

For Examples 1-5, use

| \(x_i\) | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| \(y_i\) | 2 | 3 | 5 | 4 | 6 |

Assume the simple linear regression model

\[
Y_i=\beta_0+\beta_1x_i+\varepsilon_i.
\]

---

## Example 1 - Fit the least-squares line

### Problem

Compute \(ar x,ar y,S_{xx},S_{xy},S_{yy}\), and find the least-squares line.

### 中文分析

先计算三个中心化平方和，再直接使用 \(\hat\beta_1=S_{xy}/S_{xx}\) 和 \(\hat\beta_0=ar y-\hat\beta_1ar x\)。

### Solution

The sample means are

\[
\bar x=3,
\qquad
\bar y=4.
\]

Compute

\[
S_{xx}=\sum(x_i-\bar x)^2=10,
\]

\[
S_{xy}=\sum(x_i-\bar x)(y_i-\bar y)=9,
\]

and

\[
S_{yy}=\sum(y_i-\bar y)^2=10.
\]

The slope estimate is

\[
\hat\beta_1=\frac{S_{xy}}{S_{xx}}
=\frac9{10}=0.9.
\]

The intercept estimate is

\[
\hat\beta_0
=\bar y-\hat\beta_1\bar x
=4-0.9(3)
=1.3.
\]

Therefore, the fitted line is

\[
\boxed{\hat y=1.3+0.9x}.
\]

The fitted line passes through \((\bar x,\bar y)=(3,4)\).

---

## Example 2 - Residuals, SSE, and error variance

### Problem

Using the fitted line, compute the fitted values, residuals, SSE, and \(s^2\).

### 中文分析

回归误差方差的自由度是 \(n-2\)，因为估计了截距和斜率两个参数。

### Solution

The fitted values are

\[
\hat y=(2.2,3.1,4.0,4.9,5.8).
\]

The residuals are

\[
e_i=y_i-\hat y_i,
\]

so

\[
e=(-0.2,-0.1,1.0,-0.9,0.2).
\]

The residual sum of squares is

\[
SSE=\sum e_i^2
=0.04+0.01+1+0.81+0.04
=1.90.
\]

The error variance estimate is

\[
s^2=\frac{SSE}{n-2}
=\frac{1.90}{3}
=0.6333.
\]

Thus,

\[
s=\sqrt{0.6333}=0.7958.
\]

### 快速检查

含截距的最小二乘回归中，残差和应接近 0：

\[
-0.2-0.1+1-0.9+0.2=0.
\]

---

## Example 3 - Test and confidence interval for the slope

### Problem

Test

\[
H_0:\beta_1=0
\qquad	ext{versus}\qquad
H_a:\beta_1\ne0
\]

at \(\alpha=0.05\), and construct a 95% confidence interval for \(eta_1\).

Use \(t_{0.975,3}=3.182\).

### 中文分析

斜率推断使用 \(t_{n-2}\)。斜率显著表示存在显著线性关系，不代表因果。

### Solution

The standard error of the slope is

\[
SE(\hat\beta_1)
=\frac{s}{\sqrt{S_{xx}}}
=\frac{0.7958}{\sqrt{10}}
=0.2517.
\]

The test statistic is

\[
t=\frac{0.9-0}{0.2517}=3.576.
\]

The degrees of freedom are

\[
df=n-2=3.
\]

Since

\[
|3.576|>3.182,
\]

reject \(H_0\). The two-sided p-value is approximately \(0.0374\).

The 95% confidence interval is

\[
0.9\pm3.182(0.2517),
\]

which gives

\[
\boxed{(0.099,1.701)}.
\]

**Conclusion:** There is evidence of a positive linear association between \(x\) and the mean response.

---

## Example 4 - Confidence interval for the intercept

### Problem

Construct a 95% confidence interval for \(eta_0\).

### Solution

The standard error is

\[
SE(\hat\beta_0)
=s\sqrt{\frac1n+\frac{\bar x^2}{S_{xx}}}.
\]

Thus,

\[
SE(\hat\beta_0)
=0.7958\sqrt{\frac15+\frac{3^2}{10}}
=0.8347.
\]

The confidence interval is

\[
1.3\pm3.182(0.8347).
\]

Therefore,

\[
\boxed{(-1.356,3.956)}.
\]

### 中文分析

截距代表 \(x=0\) 时的平均响应。如果 \(x=0\) 不在数据范围内，截距的实际语境解释可能没有意义，即使它在代数上必须存在。

---

## Example 5 - Mean-response interval and prediction interval

### Problem

At \(x_0=6\), construct

1. a 95% confidence interval for the mean response \(E[Y\mid x_0]\);
2. a 95% prediction interval for one new observation.

### 中文分析

两者中心相同，但 prediction interval 根号内多一个 \(1\)，因此更宽。这里 \(x_0=6\) 已稍超出观测范围 1-5，应同时提醒外推风险。

### Solution

The fitted value is

\[
\hat y(6)=1.3+0.9(6)=6.7.
\]

For the mean response,

\[
SE_{\text{mean}}
=s\sqrt{\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}.
\]

Thus,

\[
SE_{\text{mean}}
=0.7958\sqrt{\frac15+\frac{(6-3)^2}{10}}
=0.8347.
\]

The mean-response interval is

\[
6.7\pm3.182(0.8347),
\]

so

\[
\boxed{(4.044,9.356)}.
\]

For one new observation,

\[
SE_{\text{pred}}
=s\sqrt{1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}
=1.1533.
\]

The prediction interval is

\[
6.7\pm3.182(1.1533),
\]

so

\[
\boxed{(3.030,10.370)}.
\]

The prediction interval is wider because it includes both parameter-estimation uncertainty and the random variation of a new individual response.

---

## Example 6 - Pearson correlation and its test

### Problem

Compute Pearson's sample correlation coefficient and test

\[
H_0:\rho=0
\qquad	ext{versus}\qquad
H_a:\rho\ne0.
\]

### 中文分析

简单线性回归含截距时，\(R^2=r^2\)，并且检验 \(eta_1=0\) 与检验 \(ho=0\) 给出相同的 t 统计量。

### Solution

The sample correlation is

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
=\frac9{\sqrt{10(10)}}
=0.9.
\]

The test statistic is

\[
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}.
\]

Therefore,

\[
t
=\frac{0.9\sqrt3}{\sqrt{1-0.9^2}}
=3.576.
\]

With \(df=3\), the two-sided p-value is approximately \(0.0374\). Reject \(H_0\).

**Conclusion:** There is significant positive linear correlation between \(x\) and \(y\).

Also,

\[
R^2=r^2=0.81.
\]

About 81% of the observed sample variation in \(y\) is explained by the fitted linear relationship with \(x\).

### 易错点

- \(r=0\) 只表示没有线性相关，不表示完全没有关系。
- 相关显著不等于因果。
- 异常值可能显著改变 \(r\) 和回归斜率。

---

## Example 7 - Diagnose regression problems

### Problem

For each residual-plot pattern, identify the likely problem.

1. Residuals form a clear U-shape.
2. Residual spread increases as fitted values increase.
3. Residuals alternate in long runs above and below zero over time.
4. One point has an extreme \(x\)-value and strongly changes the fitted line.

### Solution

1. The linearity assumption is violated; a curved mean structure may be needed.
2. The constant-variance assumption is violated; the errors are heteroscedastic.
3. The independence assumption may be violated; serial correlation may be present.
4. The point has high leverage and may be influential.

### 中文补充

诊断题通常不要求立刻给出复杂修正，但要会说明 ordinary t/F inference 可能不再可靠，并指出变换、加权、加入曲线项或使用时间序列结构等方向。

---

## Example 8 - Matrix and projection interpretation

### Problem

In the model

\[
y=X\beta+\varepsilon,
\]

state the least-squares estimator and explain the geometric meaning of the fitted vector.

### Solution

If \(X^TX\) is invertible, the least-squares estimator is

\[
\hat\beta=(X^TX)^{-1}X^Ty.
\]

The fitted vector is

\[
\hat y=X\hat\beta
=X(X^TX)^{-1}X^Ty
=Hy,
\]

where

\[
H=X(X^TX)^{-1}X^T
\]

is the hat matrix.

Geometrically, \(\hat y\) is the orthogonal projection of \(y\) onto the column space of \(X\). Therefore the residual vector

\[
e=y-\hat y
\]

is orthogonal to every column of \(X\).

### 中文分析

这是讲义中的理解性内容，优先级低于手算回归，但常用于解释为什么残差和为 0、拟合直线经过 \((\bar x,\bar y)\)。

---

## 章末速记

```text
b1 = Sxy/Sxx, b0 = y-bar - b1 x-bar.
SSE = sum residual^2, s^2 = SSE/(n-2).
Slope/intercept/correlation inference uses t_{n-2}.
Prediction interval = mean-response interval formula with an extra 1.
Check linearity, constant variance, independence, normality, and influential points.
```
