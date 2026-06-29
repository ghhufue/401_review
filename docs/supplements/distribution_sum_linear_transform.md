# 分布相加与线性变换总结

> 位置：`docs/supplements/`  
> 用途：作为 `cheating_sheet.md` 之外的知识补充，帮助判断常见随机变量经过相加、线性组合或简单变换后会变成什么分布。

---

## 0. 总原则

讨论随机变量相加时，通常默认：

\[
X,Y \text{ independent}
\]

也就是 **独立**。

如果不独立，只知道 \(X\) 和 \(Y\) 各自的边缘分布，通常不能唯一确定 \(X+Y\) 的分布。

---

## 1. 永远先会用的两个公式

### 1.1 期望的线性性

只要期望存在：

\[
E[aX+bY+c]=aE[X]+bE[Y]+c
\]

这个公式 **不要求独立**。

---

### 1.2 方差公式

如果 \(X,Y\) 独立：

\[
\operatorname{Var}(aX+bY+c)
=
a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)
\]

如果 \(X,Y\) 不独立：

\[
\operatorname{Var}(aX+bY)
=
a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)+2ab\operatorname{Cov}(X,Y)
\]

**考试提醒**：

\[
\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
\]

只有在 \(X,Y\) 独立时成立。

---

## 2. Bernoulli 相加

如果：

\[
X_i\sim \operatorname{Bernoulli}(p)
\]

独立同分布，那么：

\[
X_1+X_2+\cdots+X_n\sim \operatorname{Binomial}(n,p)
\]

### 直觉

每个 Bernoulli 只表示一次试验是否成功：

\[
X_i=
\begin{cases}
1, & \text{success}\\
0, & \text{failure}
\end{cases}
\]

所以 n 个 Bernoulli 相加就是：

\[
\text{n 次试验中的成功次数}
\]

这就是 Binomial。

---

## 3. Binomial 相加

如果：

\[
X\sim \operatorname{Binomial}(n_1,p)
\]

\[
Y\sim \operatorname{Binomial}(n_2,p)
\]

且 \(X,Y\) 独立，并且 **成功概率 p 相同**，那么：

\[
X+Y\sim \operatorname{Binomial}(n_1+n_2,p)
\]

### 直觉

前 \(n_1\) 次试验的成功次数，加上后 \(n_2\) 次试验的成功次数，就是总共 \(n_1+n_2\) 次试验的成功次数。

### 易错点

如果两个 binomial 的 \(p\) 不一样，例如：

\[
X\sim \operatorname{Binomial}(n_1,p_1),\quad
Y\sim \operatorname{Binomial}(n_2,p_2)
\]

且 \(p_1\neq p_2\)，那么 \(X+Y\) 一般 **不是普通 Binomial**。

---

## 4. Poisson 相加

如果：

\[
X\sim \operatorname{Poisson}(\lambda_1)
\]

\[
Y\sim \operatorname{Poisson}(\lambda_2)
\]

且独立，那么：

\[
X+Y\sim \operatorname{Poisson}(\lambda_1+\lambda_2)
\]

### 直觉

两个独立计数过程合并后，平均发生次数相加。

例如：

- A 类电话每小时数量 \(\sim \operatorname{Pois}(3)\)
- B 类电话每小时数量 \(\sim \operatorname{Pois}(5)\)

那么总电话数：

\[
X+Y\sim \operatorname{Pois}(8)
\]

### 考试关键词

看到：

```text
independent Poisson counts
combine counts
total number of events
```

优先想到：

\[
\lambda \text{ 相加}
\]

---

## 5. Geometric 相加

这里要先明确 geometric 的定义。

如果：

\[
X_i\sim \operatorname{Geometric}(p)
\]

表示 **等到第 1 次成功所需的试验次数**，取值为：

\[
1,2,3,\ldots
\]

那么：

\[
X_1+X_2+\cdots+X_r\sim \operatorname{NegativeBinomial}(r,p)
\]

也常叫：

\[
\operatorname{Pascal}(r,p)
\]

### 直觉

- \(X_1\)：等到第 1 次成功用了多少次；
- \(X_2\)：从第 1 次成功后，再等到第 2 次成功用了多少次；
- ...
- \(X_r\)：再等到第 r 次成功用了多少次。

所以：

\[
X_1+\cdots+X_r
\]

表示：

\[
\boxed{\text{等到第 r 次成功总共用了多少次试验}}
\]

### Pascal PMF

若 \(S\) 表示第 \(r\) 次成功发生在第 \(x\) 次试验，则：

\[
P(S=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r},\quad x=r,r+1,\ldots
\]

### 易错点

不要把 geometric 的和误认为 binomial。

- Binomial：固定试验次数，问成功了几次；
- Pascal / Negative Binomial：固定成功次数，问总共用了几次试验。

---

## 6. Exponential 相加

如果：

\[
X_i\sim \operatorname{Exp}(\lambda)
\]

独立同 rate 参数，那么：

\[
X_1+X_2+\cdots+X_n\sim \operatorname{Gamma}(n,\lambda)
\]

当 \(n\) 是正整数时，也叫：

\[
\operatorname{Erlang}(n,\lambda)
\]

特别地：

\[
X+Y\sim \operatorname{Gamma}(2,\lambda)
\]

**不是 exponential**。

### 直觉

在 Poisson process 中：

- 一个 exponential：等第 1 次事件发生的时间；
- 两个 exponential 相加：等第 2 次事件发生的时间；
- n 个 exponential 相加：等第 n 次事件发生的时间。

### 重要对比：min 仍然是 exponential

如果：

\[
X\sim \operatorname{Exp}(\lambda_1),\quad
Y\sim \operatorname{Exp}(\lambda_2)
\]

且独立，那么：

\[
\min(X,Y)\sim \operatorname{Exp}(\lambda_1+\lambda_2)
\]

所以要区分：

```text
sum of exponential -> Gamma / Erlang
min of exponential -> Exponential
```

---

## 7. Gamma 相加

如果：

\[
X\sim \operatorname{Gamma}(\alpha_1,\lambda)
\]

\[
Y\sim \operatorname{Gamma}(\alpha_2,\lambda)
\]

且独立，并且 **rate 参数 \(\lambda\) 相同**，那么：

\[
X+Y\sim \operatorname{Gamma}(\alpha_1+\alpha_2,\lambda)
\]

### 记法

```text
Gamma + Gamma -> Gamma
前提：rate 相同
结果：shape 相加
```

### 易错点

如果两个 Gamma 的 rate 不同，一般不能直接写成一个普通 Gamma。

---

## 8. Normal 相加与线性组合

如果：

\[
X\sim N(\mu_X,\sigma_X^2)
\]

\[
Y\sim N(\mu_Y,\sigma_Y^2)
\]

且独立，那么：

\[
X+Y\sim N(\mu_X+\mu_Y,\sigma_X^2+\sigma_Y^2)
\]

更一般地：

\[
aX+bY+c\sim N(a\mu_X+b\mu_Y+c,
\ a^2\sigma_X^2+b^2\sigma_Y^2)
\]

前提是 \(X,Y\) 独立正态。

### 例子

若：

\[
X\sim N(10,4),\quad Y\sim N(3,9)
\]

独立，求：

\[
2X-3Y+5
\]

均值：

\[
2\cdot 10-3\cdot 3+5=16
\]

方差：

\[
2^2\cdot 4+(-3)^2\cdot 9=16+81=97
\]

所以：

\[
2X-3Y+5\sim N(16,97)
\]

### 易错点

标准差不能直接加，应该加的是方差。

---

## 9. Chi-square 相加

如果：

\[
X\sim \chi^2_{k_1}
\]

\[
Y\sim \chi^2_{k_2}
\]

且独立，那么：

\[
X+Y\sim \chi^2_{k_1+k_2}
\]

也就是：

```text
chi-square 相加 -> 自由度相加
```

### 应用场景

这个结论常用于：

- sample variance；
- confidence interval for variance；
- 正态样本平方和。

---

## 10. Uniform 相加

Uniform 对加法一般 **不封闭**。

例如：

\[
X,Y\sim \operatorname{Uniform}(0,1)
\]

独立，则：

\[
X+Y
\]

不是 Uniform，而是三角形分布：

\[
f_{X+Y}(z)=
\begin{cases}
z, & 0<z<1\\
2-z, & 1<z<2\\
0, & \text{otherwise}
\end{cases}
\]

### 直觉

- 和接近 0 的组合很少；
- 和接近 2 的组合也很少；
- 和接近 1 的组合最多。

所以密度中间高，两边低。

---

## 11. t 分布和 F 分布相加

### t 分布

如果：

\[
X,Y\sim t
\]

那么：

\[
X+Y
\]

一般不再是 t 分布，也通常没有考试中需要背的简单闭式形式。

### F 分布

两个 F 分布相加，一般也不是 F 分布。

### 考试策略

遇到 t 或 F：

- 通常不是让你直接求“两个 t 相加”的分布；
- 更常见的是用 t 做均值置信区间，用 F 做方差比检验。

---

## 12. 单个随机变量的线性变换 \(Y=aX+b\)

### 12.1 任何分布都能先算期望方差

如果：

\[
Y=aX+b
\]

那么：

\[
E[Y]=aE[X]+b
\]

\[
\operatorname{Var}(Y)=a^2\operatorname{Var}(X)
\]

---

### 12.2 Normal 的线性变换

如果：

\[
X\sim N(\mu,\sigma^2)
\]

那么：

\[
aX+b\sim N(a\mu+b,a^2\sigma^2)
\]

Normal 对线性变换封闭。

---

### 12.3 Uniform 的线性变换

如果：

\[
X\sim \operatorname{Uniform}(a,b)
\]

那么线性变换后仍然是 Uniform。

例如：

\[
X\sim \operatorname{Uniform}(0,1)
\]

\[
Y=2X+3
\]

则：

\[
Y\sim \operatorname{Uniform}(3,5)
\]

如果系数为负，比如：

\[
Y=-2X+3
\]

区间端点会反过来，但结果仍然是 Uniform：

\[
Y\sim \operatorname{Uniform}(1,3)
\]

---

### 12.4 Exponential 的缩放和平移

如果：

\[
X\sim \operatorname{Exp}(\lambda)
\]

且：

\[
Y=cX,\quad c>0
\]

那么：

\[
Y\sim \operatorname{Exp}\left(\frac{\lambda}{c}\right)
\]

这是使用 rate 参数时的写法。

如果使用 scale 参数 \(\beta=1/\lambda\)，那么 scale 会变成：

\[
c\beta
\]

如果：

\[
Y=X+b
\]

则它不是标准 exponential，而是 shifted exponential，因为 support 从：

\[
x>0
\]

变成：

\[
y>b
\]

---

## 13. 两个通用方法

### 13.1 MGF 方法

如果 \(X,Y\) 独立，那么：

\[
M_{X+Y}(t)=M_X(t)M_Y(t)
\]

如果乘出来的结果刚好是某个已知分布的 MGF，就能识别 \(X+Y\) 的分布。

### Poisson 例子

\[
M_X(t)=e^{\lambda_1(e^t-1)}
\]

\[
M_Y(t)=e^{\lambda_2(e^t-1)}
\]

所以：

\[
M_{X+Y}(t)=e^{(\lambda_1+\lambda_2)(e^t-1)}
\]

这正是：

\[
\operatorname{Poisson}(\lambda_1+\lambda_2)
\]

---

### 13.2 Convolution 方法

如果 \(X,Y\) 独立连续，那么：

\[
f_{X+Y}(z)=\int_{-\infty}^{\infty} f_X(x)f_Y(z-x)\,dx
\]

这个叫：

```text
convolution 卷积
```

考试里一般不会每次都要求硬卷积，更常见的是识别常见封闭性结论。

---

## 14. 最重要考试记忆表

| 输入分布 | 相加后的结果 | 条件 |
|---|---|---|
| Bernoulli | Binomial | 独立、同一个 \(p\) |
| Binomial | Binomial | 独立、同一个 \(p\)，\(n\) 相加 |
| Poisson | Poisson | 独立，\(\lambda\) 相加 |
| Geometric | Negative Binomial / Pascal | 独立、同一个 \(p\) |
| Exponential | Gamma / Erlang | 独立、同一个 rate |
| Gamma | Gamma | 独立、同一个 rate，shape 相加 |
| Normal | Normal | 独立 normal，均值线性组合，方差按平方系数相加 |
| Chi-square | Chi-square | 独立，自由度相加 |
| Uniform | 一般不是 Uniform | 两个 \(U(0,1)\) 相加是三角形 |
| t | 一般不是 t | 不封闭 |
| F | 一般不是 F | 不封闭 |

---

## 15. 最短背诵版

```text
Bernoulli 加起来 -> Binomial

Binomial + Binomial -> Binomial
前提：p 相同

Poisson + Poisson -> Poisson
lambda 相加

Geometric 加起来 -> Pascal / Negative Binomial
表示等到第 r 次成功总共用了多少次

Exponential 加起来 -> Gamma / Erlang
不是 exponential

Gamma + Gamma -> Gamma
前提：rate 相同，shape 相加

Normal 的线性组合 -> Normal
均值线性组合，方差按系数平方相加

Chi-square + Chi-square -> Chi-square
自由度相加

Uniform + Uniform -> 通常不是 uniform
两个 U(0,1) 相加是三角形
```

---

## 16. 一句话总结

\[
\boxed{\text{相加后是否还是原分布，关键看这个分布族是否对加法封闭。}}
\]

考试里最常用的封闭分布族是：

\[
\boxed{\text{Poisson, Normal, Gamma, Chi-square, 同 p 的 Binomial}}
\]
