# 401 Final 详细 Cheating Sheet

> **用途**：期末考试携带/快速查阅。  
> **内容原则**：只整理公式、定义、适用条件、理解和易混点；不包含例题。  
> **语言原则**：重要概念同时保留中文与英文，普通解释使用中文。  
> **资料范围**：`Final/docs/README.md`、`final_rc_estimate.pdf`、`final_rc_tests.pdf`、`Final_RC_MZM.pptx`、`Regression.pdf`，并参考样卷反映的题型组织方式。

---

## 0. 符号、分位数与总原则 Notation & General Rules

### 0.1 常用符号

| 符号 | 含义 |
|---|---|
| \(X_1,\ldots,X_n\) | 观测前的随机样本 **random sample** |
| \(x_1,\ldots,x_n\) | 观测后的具体样本值 **observed values** |
| \(\mu,\sigma^2,p,\theta\) | 总体参数 **population parameters** |
| \(\bar X,S^2,\hat\theta\) | 统计量/估计量 **statistic / estimator** |
| \(\bar x,s^2,\hat\theta_{\mathrm{obs}}\) | 统计量在当前样本上的数值 **estimate** |
| \(n\) | 样本量 **sample size** |
| \(\alpha\) | 显著性水平 **significance level**，也是第一类错误概率 |
| \(\beta\) | 第二类错误概率 **Type II error probability** |
| \(1-\beta\) | 功效 **power** |
| \(\nu\) 或 \(df\) | 自由度 **degrees of freedom** |
| \(SE(\hat\theta)\) | 标准误 **standard error** |
| \(O\), \(E\) | 观测频数 **observed count**、期望频数 **expected count** |

### 0.2 分位数记号 Quantile Convention

统一规定：

\[
P(Z\le z_q)=q,\qquad
P(T_\nu\le t_{q,\nu})=q
\]

\[
P(\chi^2_\nu\le \chi^2_{q,\nu})=q,\qquad
P(F_{\nu_1,\nu_2}\le F_{q,\nu_1,\nu_2})=q
\]

因此：

- 双侧 \(100(1-\alpha)\%\) 区间通常用 \(1-\alpha/2\) 分位数；
- 右尾显著性水平 \(\alpha\) 使用 \(1-\alpha\) 分位数；
- 左尾临界点直接使用 \(\alpha\) 分位数，或利用对称性写成负的右侧临界值（仅适用于对称分布）。

### 0.3 所有统计推断题的六个核心问题

1. 数据结构是什么：一个样本、两个独立样本、配对样本、分类频数还是回归数据？
2. 目标参数是什么：均值、方差、均值差、方差比、比例结构、斜率还是相关系数？
3. 方法需要什么假设：独立性、正态性、等方差、对称性、线性、同方差等？
4. 检验统计量是什么，它在 \(H_0\) 下服从什么参考分布？
5. 自由度从哪里来？
6. 最终结论能说明什么，不能说明什么？

---

# Part I. 随机样本、统计量与抽样分布

## 1. 随机样本 Random Sample

### 1.1 独立同分布 Independent and Identically Distributed, i.i.d.

\[
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim} f(x;\theta)
\]

表示：

- **同分布 identically distributed**：每个 \(X_i\) 来自同一个总体分布；
- **独立 independent**：一个观测值不提供另一个观测值的随机信息。

有限总体中，严格独立抽样通常对应有放回抽样；总体很大且抽样比例很小时，无放回抽样也常近似视为独立。

### 1.2 参数、统计量、估计量、估计值

- **参数 Parameter**：描述总体的固定未知量，如 \(\mu,\sigma^2,\theta\)。
- **统计量 Statistic**：只由样本构成、表达式不含未知参数的随机变量。
- **估计量 Estimator**：专门用来估计参数的统计量，如 \(\hat\theta\)。
- **估计值 Estimate**：把实际数据代入估计量后得到的具体数值。

观测前 \(\bar X\) 是随机变量；观测后 \(\bar x\) 是数字。

---

## 2. 样本均值与样本方差 Sample Mean & Sample Variance

### 2.1 样本均值 Sample Mean

\[
\bar X=\frac1n\sum_{i=1}^n X_i
\]

若 \(E[X_i]=\mu\)、\(\operatorname{Var}(X_i)=\sigma^2\)，且样本独立：

\[
E[\bar X]=\mu
\]

\[
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}
\]

\[
SE(\bar X)=\frac{\sigma}{\sqrt n}
\]

若 \(\sigma\) 未知，通常用：

\[
\widehat{SE}(\bar X)=\frac{S}{\sqrt n}
\]

**理解**：样本量扩大 \(k\) 倍，标准误只缩小到原来的 \(1/\sqrt{k}\)，不是 \(1/k\)。

### 2.2 样本方差 Sample Variance

无偏样本方差：

\[
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\]

等价计算式：

\[
S^2=
\frac{1}{n-1}
\left(
\sum_{i=1}^n X_i^2-n\bar X^2
\right)
\]

总体方差定义：

\[
\sigma^2=E[(X-\mu)^2]
\]

样本方差用 \(n-1\) 的原因：

- \(n\) 个偏差 \(X_i-\bar X\) 满足约束
  \[
  \sum_{i=1}^n(X_i-\bar X)=0;
  \]
- 只有 \(n-1\) 个偏差可以自由变化；
- 用 \(n-1\) 可使
  \[
  E[S^2]=\sigma^2.
  \]

### 2.3 自由度 Degrees of Freedom

**自由度**可以理解为：在已有约束或已经估计若干参数后，仍能独立变化的信息数量。

常见来源：

- 样本方差：估计了一个均值，\(df=n-1\)；
- 简单线性回归：估计截距和斜率两个参数，残差 \(df=n-2\)；
- 两样本 pooled t：两组共估计两个均值，\(df=n_1+n_2-2\)；
- \(r\times c\) 列联表：固定边际总数后，\(df=(r-1)(c-1)\)。

自由度决定参考分布的形状和临界值。

---

## 3. 抽样分布 Sampling Distribution

**抽样分布 Sampling distribution**：在重复抽样中，某个统计量所服从的概率分布。

### 3.1 中心极限定理 Central Limit Theorem, CLT

若 \(X_i\) i.i.d.，\(E[X_i]=\mu\)，\(\operatorname{Var}(X_i)=\sigma^2<\infty\)，则当 \(n\) 足够大：

\[
\frac{\bar X-\mu}{\sigma/\sqrt n}
\overset{\text{approx}}{\sim}N(0,1)
\]

等价地：

\[
\bar X\overset{\text{approx}}{\sim}
N\left(\mu,\frac{\sigma^2}{n}\right)
\]

CLT 说明的是**样本均值的分布**趋近正态，不是原始数据本身变成正态。

### 3.2 正态样本的三个核心结论

若：

\[
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2)
\]

则：

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right)
\]

\[
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}
\]

并且：

\[
\bar X\ \text{与}\ S^2\ \text{相互独立}
\]

最后一个独立性是构造精确 t 分布的关键。

---

# Part II. 点估计与最大似然

## 4. 点估计 Point Estimation

### 4.1 偏差 Bias

\[
\operatorname{Bias}(\hat\theta)
=
E[\hat\theta]-\theta
\]

- 若 \(\operatorname{Bias}(\hat\theta)=0\)，称为**无偏估计量 unbiased estimator**；
- 偏差为正：长期平均高估；
- 偏差为负：长期平均低估。

无偏不等于每次估计都准确，只表示重复抽样的平均值正确。

### 4.2 方差 Variance

\[
\operatorname{Var}(\hat\theta)
=
E\left[(\hat\theta-E[\hat\theta])^2\right]
\]

表示估计量在重复抽样中的波动程度。

### 4.3 标准误 Standard Error

\[
SE(\hat\theta)=\sqrt{\operatorname{Var}(\hat\theta)}
\]

标准差描述原始数据波动；标准误描述估计量波动。

### 4.4 均方误差 Mean Squared Error, MSE

\[
\operatorname{MSE}(\hat\theta)
=
E[(\hat\theta-\theta)^2]
\]

分解：

\[
\boxed{
\operatorname{MSE}(\hat\theta)
=
\operatorname{Var}(\hat\theta)
+
\operatorname{Bias}(\hat\theta)^2
}
\]

比较估计量时：

- 两者都无偏：比较方差；
- 存在偏差：比较 MSE 更全面；
- 略有偏但方差明显更小的估计量，MSE 可能更小。

### 4.5 一致性 Consistency

\[
\hat\theta_n\xrightarrow{P}\theta
\]

表示样本量增大时，估计量以概率意义逼近真实参数。

常用充分判断思路：

\[
\operatorname{Bias}(\hat\theta_n)\to0,
\qquad
\operatorname{Var}(\hat\theta_n)\to0
\]

则通常可利用切比雪夫不等式说明一致性。

---

## 5. 矩估计 Method of Moments, MOM

### 5.1 总体原点矩与样本原点矩

第 \(k\) 阶总体原点矩：

\[
\mu_k'=E[X^k]
\]

第 \(k\) 阶样本原点矩：

\[
m_k'=\frac1n\sum_{i=1}^nX_i^k
\]

若有 \(p\) 个未知参数，通常取前 \(p\) 个矩方程：

\[
m_k'=\mu_k'(\theta_1,\ldots,\theta_p),
\qquad k=1,\ldots,p
\]

解得：

\[
\hat\theta_{1,\mathrm{MOM}},\ldots,
\hat\theta_{p,\mathrm{MOM}}
\]

单参数最常见形式：

\[
\bar X=E_\theta[X]
\]

### 5.2 MOM 的理解

- 用样本中的经验平均替代总体理论平均；
- 一般计算直接，但不保证无偏；
- 也不保证方差最小；
- 得到估计量后，仍可继续计算 Bias、Variance、MSE 和一致性。

---

## 6. 最大似然估计 Maximum Likelihood Estimation, MLE

### 6.1 似然函数 Likelihood Function

对于已观测数据 \(x_1,\ldots,x_n\)，若样本独立：

离散型：

\[
L(\theta;x_1,\ldots,x_n)
=
\prod_{i=1}^n p(x_i;\theta)
\]

连续型：

\[
L(\theta;x_1,\ldots,x_n)
=
\prod_{i=1}^n f(x_i;\theta)
\]

**最重要的理解**：

- pdf/pmf 中，把参数固定，变量是数据 \(x\)；
- likelihood 中，把数据固定，变量是参数 \(\theta\)；
- likelihood 不是“参数的概率分布”，只是衡量不同参数对当前数据的相对支持程度。

MLE：

\[
\hat\theta_{\mathrm{ML}}
=
\arg\max_{\theta\in\Theta}L(\theta)
\]

题目未给具体数值时，仍可得到以 \(X_1,\ldots,X_n\) 或 \(\bar X\) 表示的**估计量公式**；只有要求数值估计时才需要具体样本值。

### 6.2 对数似然 Log-Likelihood

\[
\ell(\theta)=\log L(\theta)
\]

由于对数严格递增：

\[
\arg\max_\theta L(\theta)
=
\arg\max_\theta \ell(\theta)
\]

独立样本乘积转为求和：

\[
\ell(\theta)
=
\sum_{i=1}^n\log f(x_i;\theta)
\]

### 6.3 得分函数 Score Function

\[
U(\theta)
=
\frac{\partial\ell(\theta)}{\partial\theta}
\]

内部驻点通常满足：

\[
U(\theta)=0
\]

但“导数为 0”只说明候选点，不自动说明是最大值。

### 6.4 MLE 固定流程

1. 写参数空间 \(\Theta\)；
2. 写联合 likelihood，不能漏掉支持集条件；
3. 取 log-likelihood；
4. 求一阶导并解 score equation；
5. 检查候选解是否在参数空间中；
6. 检查二阶导、导数变号或直接比较函数值；
7. 检查边界；
8. 写最终 MLE。

### 6.5 支持集依赖参数 Support Depending on Parameter

若密度的取值范围本身含 \(\theta\)，必须保留指示函数：

\[
L(\theta)
=
\left[\prod_{i=1}^nf(x_i;\theta)\right]
I\{x_1,\ldots,x_n\in\mathcal X_\theta\}
\]

此时最大值常出现在：

- 样本最大值 \(X_{(n)}\)；
- 样本最小值 \(X_{(1)}\)；
- 参数空间边界；

不能只机械求导。

### 6.6 MLE 的不变性 Invariance Property

若 \(\hat\theta_{\mathrm{ML}}\) 是 \(\theta\) 的 MLE，且目标参数为：

\[
\eta=g(\theta)
\]

则通常：

\[
\hat\eta_{\mathrm{ML}}
=
g(\hat\theta_{\mathrm{ML}})
\]

若 \(g\) 非一一对应，应理解为在所有满足 \(g(\theta)=\eta\) 的参数中最大化 profile likelihood，但考试中通常直接使用不变性。

### 6.7 MLE 与无偏估计的区别

正态总体中：

\[
\hat\mu_{\mathrm{ML}}=\bar X
\]

\[
\hat\sigma^2_{\mathrm{ML}}
=
\frac1n\sum_{i=1}^n(X_i-\bar X)^2
\]

而无偏样本方差为：

\[
S^2
=
\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\]

因此：

- MLE 不保证无偏；
- “使观测数据最可能”与“重复抽样平均正确”是不同标准。

---

# Part III. 四个核心参考分布

## 7. 标准正态分布 Standard Normal Distribution

\[
Z\sim N(0,1)
\]

标准化：

\[
Z=\frac{X-\mu}{\sigma}
\]

样本均值在 \(\sigma\) 已知时：

\[
Z=
\frac{\bar X-\mu}{\sigma/\sqrt n}
\]

特点：

- 关于 0 对称；
- 无自由度参数；
- 用于总体标准差已知的均值推断，或大样本近似。

---

## 8. 卡方分布 Chi-Square Distribution

若 \(Z_1,\ldots,Z_\nu\overset{\mathrm{iid}}{\sim}N(0,1)\)，则：

\[
\chi^2=Z_1^2+\cdots+Z_\nu^2
\sim\chi^2_\nu
\]

特点：

- 只取非负值；
- 右偏；
- 自由度越大越接近对称；
- 不关于 0 对称，双侧区间必须分别查两个分位数。

正态样本方差枢轴量：

\[
\frac{(n-1)S^2}{\sigma^2}
\sim\chi^2_{n-1}
\]

主要用途：

- 单总体方差/标准差置信区间；
- 单总体方差检验；
- 分类频数的拟合优度、独立性和同质性检验。

注意：方差推断中的卡方精确结论依赖正态总体；分类数据的卡方检验则来自大样本频数近似，不要求原始数值服从正态。

---

## 9. Student t 分布

若：

\[
Z\sim N(0,1),\quad
V\sim\chi^2_\nu,\quad
Z\perp V
\]

则：

\[
T=
\frac{Z}{\sqrt{V/\nu}}
\sim t_\nu
\]

正态样本且 \(\sigma\) 未知：

\[
T=
\frac{\bar X-\mu}{S/\sqrt n}
\sim t_{n-1}
\]

特点：

- 关于 0 对称；
- 尾部比标准正态更厚；
- 自由度越大越接近 \(N(0,1)\)；
- 额外尾部反映用 \(S\) 估计 \(\sigma\) 带来的不确定性。

主要用途：

- 单样本均值；
- 两独立样本均值差；
- 配对样本均值差；
- 回归系数；
- Pearson 相关系数。

---

## 10. F 分布

若：

\[
U\sim\chi^2_{\nu_1},
\quad
V\sim\chi^2_{\nu_2},
\quad
U\perp V
\]

则：

\[
F=
\frac{U/\nu_1}{V/\nu_2}
\sim F_{\nu_1,\nu_2}
\]

两个独立正态样本：

\[
\frac{S_1^2/\sigma_1^2}
     {S_2^2/\sigma_2^2}
\sim F_{n_1-1,n_2-1}
\]

在 \(H_0:\sigma_1^2=\sigma_2^2\) 下：

\[
F=\frac{S_1^2}{S_2^2}
\sim F_{n_1-1,n_2-1}
\]

特点：

- 只取正值；
- 通常右偏；
- 分子、分母自由度顺序不能交换；
- 倒数性质：
  \[
  F\sim F_{\nu_1,\nu_2}
  \Longrightarrow
  \frac1F\sim F_{\nu_2,\nu_1}.
  \]

---

# Part IV. 置信区间 Confidence Intervals

## 11. 置信区间的正确理解

随机区间：

\[
[L(X_1,\ldots,X_n),U(X_1,\ldots,X_n)]
\]

满足：

\[
P_\theta(L\le\theta\le U)=1-\alpha
\]

频率学派解释：

> 若重复抽样并使用同一方法构造区间，长期约有 \(100(1-\alpha)\%\) 的区间覆盖真实参数。

数据已经观测后，区间端点已经固定；不能写“固定参数有 95% 概率在当前区间中”。

### 11.1 枢轴量 Pivot / Pivotal Quantity

枢轴量 \(Q(X;\theta)\)：

- 含未知参数；
- 但其分布不依赖未知参数，或已完全确定。

通用步骤：

\[
P(a\le Q(X;\theta)\le b)=1-\alpha
\]

再通过代数变形把 \(\theta\) 放到中间。

### 11.2 一般结构

大量对称分布区间具有：

\[
\boxed{
\text{点估计}
\pm
\text{临界值}
\times
\text{标准误}
}
\]

其中：

\[
\text{误差界 Margin of Error}
=
\text{临界值}\times SE
\]

区间变窄的主要方式：

- 增大 \(n\)；
- 降低置信水平；
- 降低数据波动；
- 改善设计、使用配对等以减少无关变异。

---

## 12. 单总体均值区间 One-Sample Mean CI

### 12.1 \(\sigma\) 已知

条件：正态总体，或课程允许的大样本近似。

\[
\boxed{
\mu\in
\bar X
\pm
z_{1-\alpha/2}\frac{\sigma}{\sqrt n}
}
\]

### 12.2 \(\sigma\) 未知

正态总体下精确：

\[
\boxed{
\mu\in
\bar X
\pm
t_{1-\alpha/2,n-1}\frac{S}{\sqrt n}
}
\]

自由度：

\[
df=n-1
\]

---

## 13. 单总体方差与标准差区间

条件：总体近似正态。

由于：

\[
\frac{(n-1)S^2}{\sigma^2}
\sim\chi^2_{n-1}
\]

方差区间：

\[
\boxed{
\frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}}
}
\]

标准差区间：

\[
\boxed{
\sqrt{
\frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}}
}
<
\sigma
<
\sqrt{
\frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}}
}
}
\]

记忆：

- 大卡方分位数放下界分母；
- 小卡方分位数放上界分母；
- 标准差区间必须最后开平方。

---

## 14. 两独立总体均值差区间

目标参数：

\[
\mu_1-\mu_2
\]

### 14.1 两总体方差已知

\[
\boxed{
(\mu_1-\mu_2)\in
(\bar X_1-\bar X_2)
\pm
z_{1-\alpha/2}
\sqrt{
\frac{\sigma_1^2}{n_1}
+
\frac{\sigma_2^2}{n_2}
}
}
\]

### 14.2 方差未知但假设相等 Pooled t Interval

合并方差 **pooled variance**：

\[
S_p^2
=
\frac{
(n_1-1)S_1^2+(n_2-1)S_2^2
}{
n_1+n_2-2
}
\]

\[
S_p=\sqrt{S_p^2}
\]

区间：

\[
\boxed{
(\mu_1-\mu_2)\in
(\bar X_1-\bar X_2)
\pm
t_{1-\alpha/2,n_1+n_2-2}
S_p\sqrt{\frac1{n_1}+\frac1{n_2}}
}
\]

自由度：

\[
df=n_1+n_2-2
\]

理解：\(S_p^2\) 是两组组内方差按各自自由度加权的平均。

### 14.3 方差未知且不相等 Welch Interval

\[
\boxed{
(\mu_1-\mu_2)\in
(\bar X_1-\bar X_2)
\pm
t_{1-\alpha/2,\nu}
\sqrt{
\frac{S_1^2}{n_1}
+
\frac{S_2^2}{n_2}
}
}
\]

Welch-Satterthwaite 自由度：

\[
\boxed{
\nu
\approx
\frac{
\left(S_1^2/n_1+S_2^2/n_2\right)^2
}{
\frac{(S_1^2/n_1)^2}{n_1-1}
+
\frac{(S_2^2/n_2)^2}{n_2-1}
}
}
\]

若表格只提供整数自由度，按课程要求取整；保守做法常向下取整。

---

## 15. 配对均值差区间 Paired Mean Difference CI

定义每一对的差值：

\[
D_i=X_i-Y_i
\]

然后：

\[
\bar D=\frac1n\sum_{i=1}^nD_i
\]

\[
S_D^2
=
\frac1{n-1}
\sum_{i=1}^n(D_i-\bar D)^2
\]

区间：

\[
\boxed{
\mu_D\in
\bar D
\pm
t_{1-\alpha/2,n-1}
\frac{S_D}{\sqrt n}
}
\]

关键：

- \(n\) 是配对数量；
- 使用差值的标准差 \(S_D\)，不能使用两列各自标准差直接拼接；
- 差值方向必须和目标参数定义一致。

---

## 16. 两总体方差比区间

目标：

\[
\frac{\sigma_1^2}{\sigma_2^2}
\]

由：

\[
\frac{S_1^2/S_2^2}{\sigma_1^2/\sigma_2^2}
\sim F_{n_1-1,n_2-1}
\]

得到：

\[
\boxed{
\frac{S_1^2/S_2^2}
     {F_{1-\alpha/2,n_1-1,n_2-1}}
<
\frac{\sigma_1^2}{\sigma_2^2}
<
\frac{S_1^2/S_2^2}
     {F_{\alpha/2,n_1-1,n_2-1}}
}
\]

条件：两个样本独立，两个总体近似正态。

---

# Part V. 假设检验总框架

## 17. 原假设与备择假设 Null & Alternative Hypotheses

- **原假设 Null hypothesis, \(H_0\)**：作为计算参考分布的基准陈述，通常包含等号；
- **备择假设 Alternative hypothesis, \(H_1\) / \(H_a\)**：研究者希望寻找证据支持的方向。

常见方向：

\[
H_1:\theta\ne\theta_0
\quad\text{双侧 two-sided}
\]

\[
H_1:\theta>\theta_0
\quad\text{右尾 right-tailed}
\]

\[
H_1:\theta<\theta_0
\quad\text{左尾 left-tailed}
\]

方向必须由研究问题预先决定，不能看完数据再选尾部。

---

## 18. 检验统计量 Test Statistic

一般结构：

\[
\boxed{
\text{Test statistic}
=
\frac{
\text{估计值}-\text{\(H_0\) 假设值}
}{
\text{\(H_0\) 下的标准误}
}
}
\]

它衡量样本结果离 \(H_0\) 预测值有多少个标准误。

---

## 19. p-value

**p-value**：

> 假设 \(H_0\) 为真时，得到当前统计量或比当前结果更不利于 \(H_0\) 的结果的概率。

决策：

\[
p\le\alpha
\Longrightarrow
\text{reject }H_0
\]

\[
p>\alpha
\Longrightarrow
\text{fail to reject }H_0
\]

不能写：

- “p-value 是 \(H_0\) 为真的概率”；
- “p-value 大证明 \(H_0\) 正确”；
- “不拒绝 \(H_0\) 就接受 \(H_0\)”。

### 19.1 对称参考分布的 p-value

设观测统计量为 \(t_{\mathrm{obs}}\)，CDF 为 \(F\)。

右尾：

\[
p=P(T\ge t_{\mathrm{obs}}\mid H_0)
=
1-F(t_{\mathrm{obs}})
\]

左尾：

\[
p=P(T\le t_{\mathrm{obs}}\mid H_0)
=
F(t_{\mathrm{obs}})
\]

双侧（对称分布）：

\[
p=
2P(T\ge |t_{\mathrm{obs}}|\mid H_0)
\]

或：

\[
p=2\min\{F(t_{\mathrm{obs}}),1-F(t_{\mathrm{obs}})\}
\]

卡方和 F 分布不对称，双侧 p-value 必须根据两个尾部分别处理，不能机械套 \(2P(X\ge|x|)\)。

---

## 20. 临界值法 Critical-Value Approach

右尾：

\[
T>c_\alpha
\Longrightarrow
\text{reject }H_0
\]

其中：

\[
P_{H_0}(T>c_\alpha)=\alpha
\]

左尾：

\[
T<c_\alpha
\Longrightarrow
\text{reject }H_0
\]

双侧对称分布：

\[
|T|>c_{\alpha/2}
\Longrightarrow
\text{reject }H_0
\]

p-value 法和临界值法必须给出相同决策。

---

## 21. 两类错误与功效 Errors & Power

| 真实情况 / 决策 | 不拒绝 \(H_0\) | 拒绝 \(H_0\) |
|---|---:|---:|
| \(H_0\) 真实 | 正确 | 第一类错误 Type I |
| \(H_0\) 错误 | 第二类错误 Type II | 正确 |

第一类错误：

\[
P(\text{reject }H_0\mid H_0\text{ true})=\alpha
\]

第二类错误：

\[
P(\text{fail to reject }H_0\mid H_1\text{ true})=\beta
\]

功效：

\[
\boxed{
\operatorname{Power}=1-\beta
}
\]

功效表示：当某个具体备择参数值真实时，检验正确拒绝 \(H_0\) 的概率。

### 21.1 影响功效的因素

- \(n\) 增大：power 增大；
- \(\alpha\) 增大：power 增大，但第一类错误也增大；
- 真实效应 \(|\theta-\theta_0|\) 增大：power 增大；
- 数据波动 \(\sigma\) 增大：power 降低；
- 单侧检验在方向正确时通常比同显著性水平双侧检验功效高。

---

## 22. 单样本 Z 检验的功效

设：

\[
X_i\sim N(\mu,\sigma^2),\qquad \sigma\text{ 已知}
\]

定义标准化效应：

\[
\delta
=
\frac{(\mu_1-\mu_0)\sqrt n}{\sigma}
\]

### 22.1 右尾检验

\[
H_0:\mu=\mu_0,
\qquad
H_1:\mu>\mu_0
\]

拒绝条件：

\[
\bar X>
\mu_0+z_{1-\alpha}\frac{\sigma}{\sqrt n}
\]

在真实均值 \(\mu_1\) 下：

\[
\boxed{
\operatorname{Power}(\mu_1)
=
1-\Phi\left(
z_{1-\alpha}
-
\frac{(\mu_1-\mu_0)\sqrt n}{\sigma}
\right)
}
\]

### 22.2 左尾检验

\[
\boxed{
\operatorname{Power}(\mu_1)
=
\Phi\left(
z_{\alpha}
-
\frac{(\mu_1-\mu_0)\sqrt n}{\sigma}
\right)
}
\]

### 22.3 双侧检验

\[
H_1:\mu\ne\mu_0
\]

\[
\boxed{
\operatorname{Power}(\mu_1)
=
\Phi(-z_{1-\alpha/2}-\delta)
+
1-\Phi(z_{1-\alpha/2}-\delta)
}
\]

### 22.4 目标功效对应的样本量近似

设希望检测的差异大小：

\[
\Delta=|\mu_1-\mu_0|
\]

单侧：

\[
\boxed{
n
\approx
\left[
\frac{(z_{1-\alpha}+z_{1-\beta})\sigma}{\Delta}
\right]^2
}
\]

双侧：

\[
\boxed{
n
\approx
\left[
\frac{(z_{1-\alpha/2}+z_{1-\beta})\sigma}{\Delta}
\right]^2
}
\]

最终样本量向上取整。

---

## 23. 置信区间与双侧检验的对偶性

对于显著性水平 \(\alpha\) 的双侧检验：

\[
H_0:\theta=\theta_0
\]

- 若 \(\theta_0\) 不在 \(100(1-\alpha)\%\) CI 中，则拒绝 \(H_0\)；
- 若 \(\theta_0\) 在 CI 中，则不拒绝 \(H_0\)。

这要求区间和检验：

- 使用相同模型；
- 使用相同标准误；
- 使用相同自由度；
- 都是双侧。

---

# Part VI. 参数检验 Parametric Tests

## 24. 单总体均值检验

### 24.1 \(\sigma\) 已知：One-Sample Z Test

\[
Z
=
\frac{\bar X-\mu_0}{\sigma/\sqrt n}
\sim N(0,1)\quad(H_0)
\]

拒绝域：

双侧：

\[
|Z|>z_{1-\alpha/2}
\]

右尾：

\[
Z>z_{1-\alpha}
\]

左尾：

\[
Z<z_{\alpha}=-z_{1-\alpha}
\]

条件：

- 随机、独立样本；
- 总体正态，或样本量足够大；
- \(\sigma\) 已知。

### 24.2 \(\sigma\) 未知：One-Sample t Test

\[
T
=
\frac{\bar X-\mu_0}{S/\sqrt n}
\sim t_{n-1}\quad(H_0)
\]

自由度：

\[
df=n-1
\]

条件：

- 随机、独立样本；
- 小样本时总体应近似正态；
- 无严重异常值；
- 大样本下 t 方法通常对轻度非正态较稳健。

---

## 25. 单总体方差检验 One-Variance Chi-Square Test

条件：总体正态。

\[
H_0:\sigma^2=\sigma_0^2
\]

\[
\boxed{
\chi^2_{\mathrm{obs}}
=
\frac{(n-1)S^2}{\sigma_0^2}
\sim\chi^2_{n-1}
}
\]

自由度：

\[
df=n-1
\]

拒绝域：

右尾 \(H_1:\sigma^2>\sigma_0^2\)：

\[
\chi^2_{\mathrm{obs}}
>
\chi^2_{1-\alpha,n-1}
\]

左尾 \(H_1:\sigma^2<\sigma_0^2\)：

\[
\chi^2_{\mathrm{obs}}
<
\chi^2_{\alpha,n-1}
\]

双侧 \(H_1:\sigma^2\ne\sigma_0^2\)：

\[
\chi^2_{\mathrm{obs}}
<
\chi^2_{\alpha/2,n-1}
\quad\text{或}\quad
\chi^2_{\mathrm{obs}}
>
\chi^2_{1-\alpha/2,n-1}
\]

由于卡方分布不对称，左右临界值大小不相反。

---

## 26. 两独立总体均值检验

目标：

\[
H_0:\mu_1-\mu_2=\Delta_0
\]

通常 \(\Delta_0=0\)。

### 26.1 已知总体方差 Two-Sample Z Test

\[
Z
=
\frac{
(\bar X_1-\bar X_2)-\Delta_0
}{
\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}
}
\sim N(0,1)
\]

### 26.2 等方差 Pooled Two-Sample t Test

假设：

\[
\sigma_1^2=\sigma_2^2=\sigma^2
\]

合并方差：

\[
S_p^2
=
\frac{
(n_1-1)S_1^2+(n_2-1)S_2^2
}{
n_1+n_2-2
}
\]

统计量：

\[
\boxed{
T
=
\frac{
(\bar X_1-\bar X_2)-\Delta_0
}{
S_p\sqrt{1/n_1+1/n_2}
}
\sim t_{n_1+n_2-2}
}
\]

自由度：

\[
df=n_1+n_2-2
\]

条件：

- 两组相互独立；
- 每组内部独立；
- 两总体近似正态，或样本量足够；
- 两总体方差相等。

### 26.3 不等方差 Welch t Test

\[
\boxed{
T
=
\frac{
(\bar X_1-\bar X_2)-\Delta_0
}{
\sqrt{S_1^2/n_1+S_2^2/n_2}
}
}
\]

\[
\boxed{
\nu
\approx
\frac{
(S_1^2/n_1+S_2^2/n_2)^2
}{
(S_1^2/n_1)^2/(n_1-1)
+
(S_2^2/n_2)^2/(n_2-1)
}
}
\]

条件：

- 两组相互独立；
- 不要求总体方差相等；
- 正态性/大样本条件与两样本 t 类似。

**选择理解**：

- Pooled t 把两组方差信息合成一个共同估计，若等方差假设正确，效率较高；
- 方差不等时，pooled 标准误可能错误；
- Welch 对不等方差更稳健；
- 按课程材料的流程，可能先进行 F 检验再决定 pooled 或 Welch。

---

## 27. 两总体方差检验 Two-Variance F Test

\[
H_0:\sigma_1^2=\sigma_2^2
\]

\[
\boxed{
F_{\mathrm{obs}}=\frac{S_1^2}{S_2^2}
\sim F_{n_1-1,n_2-1}
}
\]

自由度：

\[
df_1=n_1-1,\qquad df_2=n_2-1
\]

右尾 \(H_1:\sigma_1^2>\sigma_2^2\)：

\[
F_{\mathrm{obs}}>
F_{1-\alpha,n_1-1,n_2-1}
\]

左尾 \(H_1:\sigma_1^2<\sigma_2^2\)：

\[
F_{\mathrm{obs}}<
F_{\alpha,n_1-1,n_2-1}
\]

双侧：

\[
F_{\mathrm{obs}}<
F_{\alpha/2,n_1-1,n_2-1}
\quad\text{或}\quad
F_{\mathrm{obs}}>
F_{1-\alpha/2,n_1-1,n_2-1}
\]

注意：

- 分子是谁，\(df_1\) 就对应谁；
- 若为了查表把较大样本方差放分子，必须同步交换自由度并正确处理双侧概率；
- F 检验对非正态和异常值较敏感。

---

## 28. 配对 t 检验 Paired t Test

先定义：

\[
D_i=X_i-Y_i
\]

检验：

\[
H_0:\mu_D=\mu_{D,0}
\]

统计量：

\[
\boxed{
T
=
\frac{\bar D-\mu_{D,0}}{S_D/\sqrt n}
\sim t_{n-1}
}
\]

配对 t 本质是对差值 \(D_i\) 做 one-sample t。

条件：

- 各对之间独立；
- 每一对内部可以相关，这正是配对设计的目的；
- 差值总体近似正态，或配对数量足够大；
- 检查的是差值分布，而不是两列各自是否正态。

**独立与配对判断**：

- 不同对象随机分到两组：独立；
- 同一对象前后测量：配对；
- 匹配年龄/性别等形成一一对应：配对；
- 配对时样本量是“对数”，不是两列观测总数。

---

# Part VII. 非参数检验 Nonparametric Tests

## 29. 非参数方法的含义

**非参数检验 Nonparametric test** 并非“无任何假设”，而是减少对具体分布族和参数形式的依赖。

常见优势：

- 适用于偏态、异常值明显的数据；
- 可用于有序等级数据；
- 小样本且正态假设不可信时更合适。

代价：

- 在正态模型完全成立时，可能比参数检验功效低；
- 某些方法检验的是中位数或分布位置，而不一定是均值；
- 仍要求独立性、连续性、对称性等条件中的一部分。

---

## 30. 符号检验 Sign Test

适用：

- 配对差值；
- 单样本中位数；
- 只利用高于/低于假设值的方向；
- 数据偏态或异常值严重。

定义差值：

\[
D_i=X_i-Y_i
\]

删除 \(D_i=0\)，剩余有效样本量记为 \(n'\)。

正号数量：

\[
Q_+=\#\{D_i>0\}
\]

在原假设“正负方向等可能”下：

\[
\boxed{
Q_+\sim\operatorname{Binomial}(n',1/2)
}
\]

等价统计量也可使用：

\[
Q_-=\#\{D_i<0\}
\]

或：

\[
Q=\min(Q_+,Q_-)
\]

双侧 p-value 需考虑两个方向，并且离散分布下实际显著性水平可能小于设定的 \(\alpha\)。

Sign test：

- 使用方向；
- 不使用差值绝对大小；
- 稳健但信息利用较少。

---

## 31. Wilcoxon 符号秩检验 Wilcoxon Signed-Rank Test

适用：

- 配对样本或单样本位置问题；
- 差值分布连续、近似对称；
- 不希望依赖正态分布；
- 能使用差值的方向和相对大小。

步骤：

1. 计算差值 \(D_i\)；
2. 删除 \(D_i=0\)；
3. 对 \(|D_i|\) 从小到大排序；
4. 并列值使用平均秩 **midrank**；
5. 恢复每个差值的正负号；
6. 计算：
   \[
   W_+=\sum_{\{i:D_i>0\}}R_i
   \]
   \[
   W_-=\sum_{\{i:D_i<0\}}R_i
   \]
7. 根据备择方向选择统计量或计算 p-value。

无并列、无零差值时：

\[
W_++W_-=\frac{n(n+1)}2
\]

在 \(H_0\) 下：

\[
E[W_+]=\frac{n(n+1)}4
\]

\[
\operatorname{Var}(W_+)
=
\frac{n(n+1)(2n+1)}{24}
\]

大样本正态近似：

\[
Z
\approx
\frac{W_+-E[W_+]\mp0.5}
{\sqrt{\operatorname{Var}(W_+)}}
\]

其中 \(\mp0.5\) 是连续性修正，方向取决于所计算尾部。存在并列秩和零差值时，方差需要修正。

与 Sign test 比较：

- Sign test：只看正负；
- Signed-rank：看正负和绝对差值秩；
- Signed-rank 信息更多，但通常需要差值分布近似对称。

---

## 32. Wilcoxon 秩和检验 / Mann–Whitney U

英文：

- **Wilcoxon rank-sum test**
- **Mann–Whitney U test**

适用：

- 两个相互独立样本；
- 数据是连续型或有序等级；
- 正态/等方差条件不可信；
- 希望比较两组分布位置。

设：

\[
N=n_1+n_2
\]

步骤：

1. 合并两组数据；
2. 从小到大排序；
3. 并列值取平均秩；
4. 计算第一组秩和：
   \[
   R_1=\sum_{\text{group 1}}R_i
   \]
5. 转换为：
   \[
   U_1
   =
   R_1-\frac{n_1(n_1+1)}2
   \]
6. 同理：
   \[
   U_2
   =
   R_2-\frac{n_2(n_2+1)}2
   \]
7. 恒有：
   \[
   U_1+U_2=n_1n_2
   \]

无并列值时，在 \(H_0\) 下：

\[
E[U_1]=\frac{n_1n_2}{2}
\]

\[
\operatorname{Var}(U_1)
=
\frac{n_1n_2(N+1)}{12}
\]

大样本正态近似：

\[
Z
\approx
\frac{
U_1-n_1n_2/2\mp0.5
}{
\sqrt{n_1n_2(N+1)/12}
}
\]

若存在并列组，大小分别为 \(t_j\)，常用方差修正：

\[
\operatorname{Var}(U)
=
\frac{n_1n_2}{12}
\left[
N+1
-
\frac{
\sum_j(t_j^3-t_j)
}{
N(N-1)
}
\right]
\]

解释边界：

- 一般检验两组分布是否相同；
- 若两组分布形状和离散程度相同，只相差位置，可解释为位置/中位数差异；
- 不是直接比较样本均值。

---

## 33. 参数与非参数方法对应关系

| 数据结构 | 参数方法 | 非参数方法 |
|---|---|---|
| 一个样本位置 | One-sample t | Sign / Signed-rank |
| 配对样本 | Paired t | Sign / Signed-rank |
| 两独立样本 | Pooled/Welch t | Rank-sum / Mann–Whitney U |

不能混淆：

- **rank-sum**：两个独立样本；
- **signed-rank**：配对差值/单样本；
- **sign test**：配对差值，只看方向。

---

# Part VIII. 分类数据与卡方检验

## 34. 频数数据 Categorical Count Data

分类数据检验使用的是**个数 count/frequency**，不是均值或方差。

基本统计量：

\[
\boxed{
\chi^2
=
\sum
\frac{(O-E)^2}{E}
}
\]

每个单元格贡献：

\[
\frac{(O-E)^2}{E}
\]

贡献越大，表示该格观测值与 \(H_0\) 期望偏离越明显。

---

## 35. 卡方拟合优度检验 Chi-Square Goodness-of-Fit Test

目的：判断一个分类变量的总体比例是否符合给定理论比例。

原假设：

\[
H_0:
p_1=p_{1,0},\ldots,p_k=p_{k,0}
\]

其中：

\[
\sum_{i=1}^kp_{i,0}=1
\]

期望频数：

\[
\boxed{
E_i=np_{i,0}
}
\]

统计量：

\[
\boxed{
\chi^2
=
\sum_{i=1}^k
\frac{(O_i-E_i)^2}{E_i}
}
\]

自由度：

\[
\boxed{
df=k-1-m
}
\]

其中：

- \(k\)：分类数量；
- \(1\)：总频数固定带来的一个约束；
- \(m\)：为计算理论比例而从当前数据中估计的参数个数。

若所有理论比例完全预先给定：

\[
df=k-1
\]

结论：拒绝 \(H_0\) 表示观测分类分布与给定比例不一致；不说明哪一个具体机制一定正确。

---

## 36. 卡方独立性检验 Chi-Square Test of Independence

目的：同一总体中的两个分类变量是否独立。

原假设：

\[
H_0:
\text{变量 A 与变量 B 独立}
\]

对于 \(r\times c\) 列联表：

\[
\boxed{
E_{ij}
=
\frac{
(\text{第 }i\text{ 行总数})
(\text{第 }j\text{ 列总数})
}{N}
}
\]

统计量：

\[
\boxed{
\chi^2
=
\sum_{i=1}^r
\sum_{j=1}^c
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
}
\]

自由度：

\[
\boxed{
df=(r-1)(c-1)
}
\]

拒绝 \(H_0\)：有证据表明两个分类变量存在关联。  
不能直接推出因果关系。

---

## 37. 卡方同质性检验 Chi-Square Test of Homogeneity

目的：比较多个总体/处理组是否具有相同的分类比例。

原假设：

\[
H_0:
\text{所有总体的分类分布相同}
\]

期望频数、统计量和自由度与独立性检验相同：

\[
E_{ij}
=
\frac{
(\text{行总数})(\text{列总数})
}{N}
\]

\[
\chi^2
=
\sum_{i,j}
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
\]

\[
df=(r-1)(c-1)
\]

区别在研究设计：

- **Independence**：从一个总体抽样，同时记录两个分类变量；
- **Homogeneity**：从多个总体/处理组分别抽样，比较分类比例。

---

## 38. 分类卡方检验的条件

1. 使用频数，不是百分比；
2. 每个个体只进入一个单元格；
3. 个体之间独立；
4. 分类互斥且穷尽；
5. 期望频数不能过小。

常见近似规则：

- 最理想：所有 \(E\ge5\)；
- 较宽松规则：没有 \(E<1\)，且低于 5 的格子不超过约 20%；
- 具体以课程规则为准。

若期望频数过小：

- 合理合并分类；
- 使用精确检验；
- 不应把观察频数人为改大。

### 38.1 标准化残差 Standardized Residual

基础形式：

\[
r_{ij}
=
\frac{O_{ij}-E_{ij}}{\sqrt{E_{ij}}}
\]

绝对值较大的格子对总体卡方统计量贡献更大。整体显著后，可用残差帮助定位差异来源，但需注意多重比较。

---

# Part IX. 简单线性回归 Simple Linear Regression

## 39. 回归模型 Regression Model

\[
\boxed{
Y_i=\beta_0+\beta_1x_i+\varepsilon_i
}
\]

其中：

- \(\beta_0\)：截距 **intercept**；
- \(\beta_1\)：斜率 **slope**；
- \(\varepsilon_i\)：随机误差 **random error**；
- \(x_i\)：解释变量/预测变量 **explanatory variable / predictor**；
- \(Y_i\)：响应变量 **response variable**。

条件均值：

\[
E[Y_i\mid x_i]
=
\beta_0+\beta_1x_i
\]

条件方差：

\[
\operatorname{Var}(Y_i\mid x_i)
=
\sigma^2
\]

回归直线描述的是 \(Y\) 在给定 \(x\) 下的**平均响应**，不是所有个体都落在直线上。

---

## 40. 回归假设 Regression Assumptions

常用记忆：LINE。

1. **Linearity 线性**
   \[
   E[Y\mid x]=\beta_0+\beta_1x
   \]
2. **Independence 独立**
   \[
   \varepsilon_i\perp\varepsilon_j,\quad i\ne j
   \]
3. **Normality 正态**
   \[
   \varepsilon_i\sim N(0,\sigma^2)
   \]
   主要用于小样本精确 t/F 推断。
4. **Equal variance / Homoscedasticity 同方差**
   \[
   \operatorname{Var}(\varepsilon_i\mid x_i)=\sigma^2
   \]

另需：

- \(x_i\) 有足够变化，即 \(S_{xx}>0\)；
- 模型设定正确；
- 没有单个异常/高杠杆点完全支配结果。

---

## 41. 三个中心化平方和

\[
\boxed{
S_{xx}
=
\sum_{i=1}^n(x_i-\bar x)^2
}
\]

\[
\boxed{
S_{yy}
=
\sum_{i=1}^n(y_i-\bar y)^2
}
\]

\[
\boxed{
S_{xy}
=
\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)
}
\]

计算式：

\[
S_{xx}
=
\sum x_i^2-\frac{(\sum x_i)^2}{n}
\]

\[
S_{yy}
=
\sum y_i^2-\frac{(\sum y_i)^2}{n}
\]

\[
S_{xy}
=
\sum x_iy_i-\frac{(\sum x_i)(\sum y_i)}{n}
\]

---

## 42. 最小二乘估计 Ordinary Least Squares, OLS

目标：

\[
\min_{\beta_0,\beta_1}
\sum_{i=1}^n
(y_i-\beta_0-\beta_1x_i)^2
\]

估计斜率：

\[
\boxed{
\hat\beta_1
=
b_1
=
\frac{S_{xy}}{S_{xx}}
}
\]

估计截距：

\[
\boxed{
\hat\beta_0
=
b_0
=
\bar y-b_1\bar x
}
\]

拟合值：

\[
\hat y_i=b_0+b_1x_i
\]

残差：

\[
\boxed{
e_i=y_i-\hat y_i
}
\]

### 42.1 OLS 的重要代数性质

含截距的简单线性回归中：

\[
\sum_{i=1}^ne_i=0
\]

\[
\sum_{i=1}^nx_ie_i=0
\]

\[
\sum_{i=1}^n\hat y_i=\sum_{i=1}^ny_i
\]

拟合直线经过：

\[
\boxed{
(\bar x,\bar y)
}
\]

残差与拟合值正交：

\[
\sum_{i=1}^ne_i\hat y_i=0
\]

---

## 43. 平方和分解 ANOVA Decomposition

总平方和：

\[
\boxed{
SST
=
\sum_{i=1}^n(y_i-\bar y)^2
=
S_{yy}
}
\]

回归平方和：

\[
\boxed{
SSR
=
\sum_{i=1}^n(\hat y_i-\bar y)^2
}
\]

残差平方和：

\[
\boxed{
SSE
=
\sum_{i=1}^n(y_i-\hat y_i)^2
=
\sum e_i^2
}
\]

含截距模型：

\[
\boxed{
SST=SSR+SSE
}
\]

简单线性回归中：

\[
SSR=b_1S_{xy}
=
\frac{S_{xy}^2}{S_{xx}}
\]

\[
SSE=S_{yy}-\frac{S_{xy}^2}{S_{xx}}
\]

---

## 44. 误差方差估计

模型中未知误差方差为 \(\sigma^2\)。

残差自由度：

\[
df_E=n-2
\]

均方误差：

\[
\boxed{
MSE
=
s^2
=
\frac{SSE}{n-2}
}
\]

残差标准差：

\[
\boxed{
s=\sqrt{MSE}
}
\]

这里的 \(s\) 估计的是回归误差标准差 \(\sigma\)，表示数据点围绕真实回归线的典型垂直波动。

---

## 45. 决定系数 Coefficient of Determination, \(R^2\)

\[
\boxed{
R^2
=
\frac{SSR}{SST}
=
1-\frac{SSE}{SST}
}
\]

含截距模型通常：

\[
0\le R^2\le1
\]

解释：

> \(R^2\) 是样本中响应变量总变异被当前回归模型解释的比例。

不能由高 \(R^2\) 自动推出：

- 因果关系；
- 模型假设成立；
- 外推可靠；
- 预测误差一定小；
- 没有异常值；
- 模型不会过拟合。

简单线性回归且含截距时：

\[
\boxed{
R^2=r^2
}
\]

---

## 46. 斜率与截距的抽样分布

在模型假设成立时：

\[
E[\hat\beta_1]=\beta_1
\]

\[
\operatorname{Var}(\hat\beta_1)
=
\frac{\sigma^2}{S_{xx}}
\]

估计标准误：

\[
\boxed{
SE(\hat\beta_1)
=
\frac{s}{\sqrt{S_{xx}}}
}
\]

截距：

\[
E[\hat\beta_0]=\beta_0
\]

\[
\operatorname{Var}(\hat\beta_0)
=
\sigma^2
\left(
\frac1n+\frac{\bar x^2}{S_{xx}}
\right)
\]

\[
\boxed{
SE(\hat\beta_0)
=
s
\sqrt{
\frac1n+\frac{\bar x^2}{S_{xx}}
}
}
\]

协方差：

\[
\operatorname{Cov}(\hat\beta_0,\hat\beta_1)
=
-\frac{\bar x\sigma^2}{S_{xx}}
\]

---

## 47. 回归系数的 t 检验与区间

### 47.1 斜率检验

\[
H_0:\beta_1=\beta_{1,0}
\]

\[
\boxed{
T
=
\frac{
\hat\beta_1-\beta_{1,0}
}{
SE(\hat\beta_1)
}
\sim t_{n-2}
}
\]

最常见：

\[
H_0:\beta_1=0
\]

含义：检验总体中 \(x\) 与 \(Y\) 是否存在线性关联。

斜率区间：

\[
\boxed{
\beta_1
\in
\hat\beta_1
\pm
t_{1-\alpha/2,n-2}
SE(\hat\beta_1)
}
\]

### 47.2 截距检验

\[
H_0:\beta_0=\beta_{0,0}
\]

\[
T
=
\frac{
\hat\beta_0-\beta_{0,0}
}{
SE(\hat\beta_0)
}
\sim t_{n-2}
\]

截距区间：

\[
\boxed{
\beta_0
\in
\hat\beta_0
\pm
t_{1-\alpha/2,n-2}
SE(\hat\beta_0)
}
\]

截距只有在 \(x=0\) 有实际意义且 \(0\) 位于合理数据范围内时，语境解释才可靠。

---

## 48. 回归的 F 检验 ANOVA F Test

简单线性回归：

\[
df_R=1,\qquad df_E=n-2
\]

回归均方：

\[
MSR=\frac{SSR}{1}=SSR
\]

误差均方：

\[
MSE=\frac{SSE}{n-2}
\]

统计量：

\[
\boxed{
F
=
\frac{MSR}{MSE}
\sim F_{1,n-2}
\quad(H_0:\beta_1=0)
}
\]

在只有一个预测变量且含截距时：

\[
\boxed{
F=T_{\text{slope}}^2
}
\]

因此斜率双侧 t 检验和整体回归 F 检验给出相同 p-value。

---

## 49. 平均响应置信区间 Mean Response CI

给定：

\[
x=x_0
\]

点估计：

\[
\hat y_0
=
\hat\beta_0+\hat\beta_1x_0
\]

平均响应：

\[
E[Y\mid x_0]
=
\beta_0+\beta_1x_0
\]

标准误：

\[
\boxed{
SE_{\mathrm{mean}}(x_0)
=
s
\sqrt{
\frac1n+
\frac{(x_0-\bar x)^2}{S_{xx}}
}
}
\]

区间：

\[
\boxed{
E[Y\mid x_0]
\in
\hat y_0
\pm
t_{1-\alpha/2,n-2}
s
\sqrt{
\frac1n+
\frac{(x_0-\bar x)^2}{S_{xx}}
}
}
\]

特点：

- 在 \(x_0=\bar x\) 附近最窄；
- 离 \(\bar x\) 越远越宽；
- 估计的是大量同类对象的平均值。

---

## 50. 单个新观测预测区间 Prediction Interval

新观测：

\[
Y_{\mathrm{new}}(x_0)
\]

预测标准误：

\[
\boxed{
SE_{\mathrm{pred}}(x_0)
=
s
\sqrt{
1+\frac1n+
\frac{(x_0-\bar x)^2}{S_{xx}}
}
}
\]

预测区间：

\[
\boxed{
Y_{\mathrm{new}}(x_0)
\in
\hat y_0
\pm
t_{1-\alpha/2,n-2}
s
\sqrt{
1+\frac1n+
\frac{(x_0-\bar x)^2}{S_{xx}}
}
}
\]

与平均响应区间相比，多出的：

\[
\boxed{1}
\]

代表新个体自身的随机误差，因此：

\[
\text{Prediction interval}
\quad\text{一定宽于}\quad
\text{Mean response CI}
\]

前提是两者在相同 \(x_0\)、置信水平和模型下比较。

---

## 51. Pearson 相关系数 Pearson Correlation Coefficient

样本相关系数：

\[
\boxed{
r
=
\frac{S_{xy}}
{\sqrt{S_{xx}S_{yy}}}
}
\]

性质：

\[
-1\le r\le1
\]

- \(r>0\)：正线性方向；
- \(r<0\)：负线性方向；
- \(|r|\) 越接近 1：线性关系越强；
- \(r=0\)：无线性相关，不代表完全无关系；
- 无量纲；
- 交换 \(x,y\) 不改变 \(r\)；
- 对异常值敏感；
- 线性变换中的平移和正比例缩放不改变 \(|r|\)。

总体相关系数：

\[
\rho
\]

检验：

\[
H_0:\rho=0
\]

\[
\boxed{
T
=
\frac{
r\sqrt{n-2}
}{
\sqrt{1-r^2}
}
\sim t_{n-2}
}
\]

条件通常要求成对观测独立，并且总体近似二元正态或回归模型条件适合。

简单线性回归中：

\[
\boxed{
\hat\beta_1
=
r\frac{s_y}{s_x}
}
\]

且：

\[
R^2=r^2
\]

检验 \(H_0:\rho=0\) 与检验 \(H_0:\beta_1=0\) 等价。

**Correlation does not imply causation：相关不等于因果。**

---

## 52. 残差诊断 Regression Diagnostics

残差图理想特征：

- 围绕 0 随机分布；
- 没有明显曲线；
- 垂直散布宽度大致恒定；
- 没有孤立极端点；
- 随观测顺序没有周期或趋势。

常见问题：

### 52.1 非线性 Nonlinearity

残差图出现曲线或系统形状。  
说明线性均值结构可能不合适。

### 52.2 异方差 Heteroscedasticity

残差散布呈漏斗形。  
说明：

\[
\operatorname{Var}(\varepsilon_i\mid x_i)
\]

不是常数，常规标准误和区间可能失真。

### 52.3 异常值 Outlier

响应方向上残差特别大。  
异常值不一定高杠杆。

### 52.4 高杠杆点 High-Leverage Point

\(x_i\) 远离 \(\bar x\)，可能强烈影响斜率。

简单线性回归杠杆值：

\[
\boxed{
h_{ii}
=
\frac1n+
\frac{(x_i-\bar x)^2}{S_{xx}}
}
\]

性质：

\[
0\le h_{ii}\le1
\]

\[
\sum_{i=1}^nh_{ii}=2
\]

因为简单线性回归估计两个参数。

### 52.5 高影响点 Influential Point

删除该点后拟合结果明显改变。  
影响同时取决于：

- 杠杆；
- 残差大小。

### 52.6 外推 Extrapolation

在观测 \(x\) 范围之外预测。即使样本内线性拟合良好，区间也可能无法反映模型结构改变的风险。

---

# Part X. 回归的矩阵与几何理解

## 53. 一般线性模型 Matrix Form

\[
\boxed{
\mathbf y
=
X\boldsymbol\beta
+
\boldsymbol\varepsilon
}
\]

其中：

- \(\mathbf y\in\mathbb R^n\)；
- \(X\in\mathbb R^{n\times p}\)；
- \(\boldsymbol\beta\in\mathbb R^p\)；
- \(\boldsymbol\varepsilon\sim N(\mathbf0,\sigma^2I)\) 用于精确正态推断。

若 \(X\) 满列秩：

\[
\boxed{
\hat{\boldsymbol\beta}
=
(X^TX)^{-1}X^T\mathbf y
}
\]

协方差矩阵：

\[
\boxed{
\operatorname{Cov}(\hat{\boldsymbol\beta})
=
\sigma^2(X^TX)^{-1}
}
\]

估计：

\[
\widehat{\operatorname{Cov}}(\hat{\boldsymbol\beta})
=
MSE\,(X^TX)^{-1}
\]

残差自由度：

\[
df_E=n-p
\]

\[
MSE=\frac{SSE}{n-p}
\]

---

## 54. Hat Matrix 与投影

拟合值：

\[
\hat{\mathbf y}
=
X\hat{\boldsymbol\beta}
\]

定义 hat matrix：

\[
\boxed{
H
=
X(X^TX)^{-1}X^T
}
\]

则：

\[
\boxed{
\hat{\mathbf y}=H\mathbf y
}
\]

残差：

\[
\boxed{
\mathbf e
=
\mathbf y-\hat{\mathbf y}
=
(I-H)\mathbf y
}
\]

重要性质：

\[
H^T=H
\quad\text{对称}
\]

\[
H^2=H
\quad\text{幂等}
\]

\[
\operatorname{tr}(H)=p
\]

\[
X^T\mathbf e=\mathbf0
\]

几何解释：

- \(\hat{\mathbf y}\) 是 \(\mathbf y\) 在 \(X\) 的列空间上的正交投影；
- \(\mathbf e\) 与该列空间正交；
- OLS 选择离 \(\mathbf y\) 最近的可拟合向量。

---

# Part XI. 泛化、过拟合与正则化

## 55. 训练误差与测试误差

- **Training error 训练误差**：在拟合数据上的误差；
- **Test error / Generalization error 测试误差/泛化误差**：在新数据上的误差。

增加模型复杂度通常不会增加训练误差，但可能增加测试误差。

---

## 56. 过拟合 Overfitting

模型过度追随样本噪声：

- 训练误差很低；
- 新数据误差较高；
- 参数对样本扰动敏感；
- 高阶多项式可能出现剧烈摆动。

过拟合不是“模型拟合得太好”，而是模型拟合了不可重复的随机噪声。

---

## 57. 偏差—方差权衡 Bias–Variance Tradeoff

预测误差可概念性分为：

\[
\text{Prediction Error}
=
\text{Bias}^2
+
\text{Variance}
+
\text{Irreducible Noise}
\]

- 模型太简单：偏差高、方差低，可能欠拟合；
- 模型太复杂：偏差低、方差高，可能过拟合；
- 目标是在泛化误差层面取得平衡。

---

## 58. Ridge Regression

目标函数：

\[
\boxed{
\min_{\beta_0,\boldsymbol\beta}
\left[
\sum_{i=1}^n
(y_i-\beta_0-\mathbf x_i^T\boldsymbol\beta)^2
+
\lambda\sum_{j=1}^{p-1}\beta_j^2
\right]
}
\]

通常不惩罚截距。

矩阵形式：

\[
\hat{\boldsymbol\beta}_{\mathrm{ridge}}
=
(X^TX+\lambda I^*)^{-1}X^T\mathbf y
\]

其中 \(I^*\) 对截距位置取 0。

作用：

- 收缩系数；
- 降低方差；
- 缓解多重共线性；
- 引入偏差以换取更好泛化；
- 通常不会把系数精确压到 0。

使用前通常应标准化不同量纲的预测变量。

---

## 59. Lasso Regression

目标函数：

\[
\boxed{
\min_{\beta_0,\boldsymbol\beta}
\left[
\sum_{i=1}^n
(y_i-\beta_0-\mathbf x_i^T\boldsymbol\beta)^2
+
\lambda\sum_{j=1}^{p-1}|\beta_j|
\right]
}
\]

作用：

- 收缩系数；
- 某些系数可精确变为 0；
- 同时完成变量选择；
- 预测变量高度相关时，选择结果可能不稳定。

\(\lambda\) 越大：

- 惩罚越强；
- 模型越简单；
- 偏差通常增大；
- 方差通常减小。

---

# Part XII. 方法选择速查

## 60. 检验方法总表

| 目标/数据结构 | 条件 | 方法 | 统计量分布 / df |
|---|---|---|---|
| 一个总体均值 | \(\sigma\) 已知 | One-sample Z | \(N(0,1)\) |
| 一个总体均值 | \(\sigma\) 未知，正态/适当大样本 | One-sample t | \(t_{n-1}\) |
| 一个总体方差 | 正态总体 | Chi-square variance test | \(\chi^2_{n-1}\) |
| 两独立均值 | 方差已知 | Two-sample Z | \(N(0,1)\) |
| 两独立均值 | 方差未知且相等 | Pooled t | \(t_{n_1+n_2-2}\) |
| 两独立均值 | 方差未知且不等 | Welch t | \(t_\nu\) |
| 两总体方差 | 两独立正态样本 | F test | \(F_{n_1-1,n_2-1}\) |
| 配对均值差 | 差值近似正态 | Paired t | \(t_{n-1}\) |
| 配对位置差 | 只看方向 | Sign test | \(\operatorname{Bin}(n',1/2)\) |
| 配对位置差 | 差值近似对称 | Signed-rank | 精确表/正态近似 |
| 两独立分布位置 | 非正态/等级数据 | Rank-sum / Mann–Whitney | 精确表/正态近似 |
| 一个分类变量是否符合比例 | 期望频数足够 | Chi-square GOF | \(\chi^2_{k-1-m}\) |
| 两分类变量是否关联 | 期望频数足够 | Chi-square independence | \(\chi^2_{(r-1)(c-1)}\) |
| 多总体分类比例是否相同 | 期望频数足够 | Chi-square homogeneity | \(\chi^2_{(r-1)(c-1)}\) |
| 回归斜率 | LINE 条件 | Slope t test | \(t_{n-2}\) |
| 简单回归整体显著性 | LINE 条件 | Regression F test | \(F_{1,n-2}\) |
| Pearson 相关 | 成对独立、适当分布条件 | Correlation t test | \(t_{n-2}\) |

---

## 61. 区间方法总表

| 参数 | 区间核心 |
|---|---|
| \(\mu,\sigma\) 已知 | \(\bar X\pm z^*\sigma/\sqrt n\) |
| \(\mu,\sigma\) 未知 | \(\bar X\pm t^*S/\sqrt n\) |
| \(\sigma^2\) | \((n-1)S^2/\chi^2\) 两侧反向分位数 |
| \(\mu_1-\mu_2\)，等方差 | 差值 \(\pm t^*S_p\sqrt{1/n_1+1/n_2}\) |
| \(\mu_1-\mu_2\)，不等方差 | 差值 \(\pm t_\nu^*\sqrt{S_1^2/n_1+S_2^2/n_2}\) |
| 配对 \(\mu_D\) | \(\bar D\pm t^*S_D/\sqrt n\) |
| \(\sigma_1^2/\sigma_2^2\) | 样本方差比除以两个 F 分位数 |
| 回归斜率 | \(b_1\pm t^*SE(b_1)\) |
| 回归截距 | \(b_0\pm t^*SE(b_0)\) |
| 平均响应 | \(\hat y_0\pm t^*s\sqrt{1/n+(x_0-\bar x)^2/S_{xx}}\) |
| 新观测预测 | 上式根号内多 \(1\) |

---

# Part XIII. 高频理解与易错点

## 62. 最大似然相关

- likelihood 把数据固定、参数当变量；
- 没有数值样本也能推导 MLE 的符号公式；
- 导数为 0 不保证最大；
- 支持集含参数时必须检查边界、最大值和最小值；
- MLE 不保证无偏；
- 参数变换可使用 MLE 不变性。

## 63. 自由度相关

- 自由度不是样本量的另一种写法；
- 每估计一个独立参数或施加一个独立约束，通常损失一个自由度；
- t、卡方、F、回归的临界值都依赖自由度；
- F 分布有两个自由度，顺序不能交换。

## 64. 区间相关

- 置信水平是方法的长期覆盖率；
- 预测区间比平均响应区间宽；
- 卡方和 F 区间不是简单的“估计值 \(\pm\) 临界值×SE”；
- 方差区间分母中的大小分位数顺序容易写反。

## 65. 检验相关

- \(H_0\) 通常含等号；
- 单尾/双尾由研究问题决定；
- p-value 不是 \(P(H_0\text{ true})\)；
- 不拒绝 \(H_0\) 不等于证明 \(H_0\)；
- 统计显著不等于实际效应大；
- 显著性水平 \(\alpha\) 是事先设定的规则，不是数据算出来的；
- 检验结论应写“有/没有足够证据”，而不是“证明”。

## 66. 两样本相关

- 独立样本和配对样本不能混用；
- 配对问题先算差值，再变成单样本问题；
- pooled t 需要等方差；
- Welch t 不合并方差；
- 方差检验对非正态敏感。

## 67. 非参数相关

- Sign test 只看方向；
- Signed-rank 用于配对；
- Rank-sum 用于独立两组；
- 秩检验比较的是分布位置/随机优势，不一定等同于均值差；
- 并列秩使用平均秩；
- 零差值的处理会改变有效样本量。

## 68. 卡方相关

- 使用观测频数，不直接使用百分比；
- GOF 的 \(df=k-1-m\)；
- 独立性/同质性的 \(df=(r-1)(c-1)\)；
- 总体检验显著只能说明至少某些格子偏离；
- 关联不等于因果；
- 小期望频数会破坏卡方近似。

## 69. 回归相关

- 斜率描述平均响应每增加一个 \(x\) 单位的变化；
- 截距可能没有实际解释；
- \(R^2\) 高不保证因果、预测或模型正确；
- \(r=0\) 只代表无线性关系；
- 回归斜率检验、相关检验和简单回归 F 检验彼此等价；
- 外推风险无法仅靠公式区间完全体现；
- 异常值、高杠杆点、高影响点是不同概念；
- 预测区间根号内多出的 \(1\) 来自新个体误差。

---

# Part XIV. 考场书写模板

## 70. 假设检验统一模板

1. **Parameter 参数**：明确 \(\mu,\mu_1-\mu_2,\sigma^2,\rho,\beta_1\) 等含义。
2. **Hypotheses 假设**：
   \[
   H_0:\cdots,\qquad H_1:\cdots
   \]
3. **Assumptions 条件**：独立、正态、等方差、配对、对称、期望频数等。
4. **Test statistic 统计量**：
   \[
   \text{公式}
   \]
5. **Reference distribution 参考分布与 df**：
   \[
   T\sim t_\nu,\quad
   \chi^2\sim\chi^2_\nu,\quad
   F\sim F_{\nu_1,\nu_2}
   \]
6. **Observed value 代入值**：
   \[
   T_{\mathrm{obs}}=\cdots
   \]
7. **p-value / rejection region**。
8. **Decision 决策**：reject 或 fail to reject。
9. **Context conclusion 语境结论**：有/没有足够统计证据支持备择陈述。

---

## 71. 置信区间统一模板

1. 定义目标参数；
2. 确认数据结构；
3. 写方法及条件；
4. 写点估计；
5. 写标准误；
6. 写临界值和自由度；
7. 写区间；
8. 用参数语境解释；
9. 不把固定参数描述成随机变量。

---

## 72. 回归题统一流程

\[
\bar x,\bar y
\]

\[
S_{xx},S_{xy},S_{yy}
\]

\[
b_1=\frac{S_{xy}}{S_{xx}}
\]

\[
b_0=\bar y-b_1\bar x
\]

\[
SSE=S_{yy}-\frac{S_{xy}^2}{S_{xx}}
\]

\[
s^2=\frac{SSE}{n-2}
\]

然后根据要求选择：

- 系数标准误和 t 检验/CI；
- \(R^2\)；
- mean response CI；
- prediction interval；
- Pearson \(r\) 和相关检验；
- 残差诊断。

---

# Part XV. 中英文术语速查 Glossary

| 中文 | English |
|---|---|
| 总体 | Population |
| 样本 | Sample |
| 随机样本 | Random sample |
| 独立同分布 | Independent and identically distributed, i.i.d. |
| 参数 | Parameter |
| 统计量 | Statistic |
| 估计量 | Estimator |
| 估计值 | Estimate |
| 抽样分布 | Sampling distribution |
| 点估计 | Point estimation |
| 偏差 | Bias |
| 无偏 | Unbiased |
| 方差 | Variance |
| 标准误 | Standard error |
| 均方误差 | Mean squared error, MSE |
| 一致性 | Consistency |
| 矩估计 | Method of moments, MOM |
| 最大似然估计 | Maximum likelihood estimation, MLE |
| 似然函数 | Likelihood function |
| 对数似然 | Log-likelihood |
| 得分函数 | Score function |
| 参数空间 | Parameter space |
| 支持集 | Support |
| 不变性 | Invariance property |
| 自由度 | Degrees of freedom |
| 分位数 | Quantile |
| 枢轴量 | Pivotal quantity / Pivot |
| 置信区间 | Confidence interval |
| 置信水平 | Confidence level |
| 误差界 | Margin of error |
| 原假设 | Null hypothesis |
| 备择假设 | Alternative hypothesis |
| 显著性水平 | Significance level |
| 检验统计量 | Test statistic |
| 拒绝域 | Rejection region |
| p 值 | p-value |
| 第一类错误 | Type I error |
| 第二类错误 | Type II error |
| 功效 | Power |
| 单侧检验 | One-sided test |
| 双侧检验 | Two-sided test |
| 合并方差 | Pooled variance |
| 等方差 | Equal variance / Homoscedastic |
| 不等方差 | Unequal variance / Heteroscedastic |
| 配对样本 | Paired samples |
| 独立样本 | Independent samples |
| 非参数检验 | Nonparametric test |
| 符号检验 | Sign test |
| 符号秩检验 | Wilcoxon signed-rank test |
| 秩和检验 | Wilcoxon rank-sum test |
| 拟合优度 | Goodness of fit |
| 独立性检验 | Test of independence |
| 同质性检验 | Test of homogeneity |
| 观测频数 | Observed frequency |
| 期望频数 | Expected frequency |
| 列联表 | Contingency table |
| 简单线性回归 | Simple linear regression |
| 最小二乘 | Ordinary least squares, OLS |
| 响应变量 | Response variable |
| 解释变量 | Explanatory variable |
| 预测变量 | Predictor |
| 截距 | Intercept |
| 斜率 | Slope |
| 拟合值 | Fitted value |
| 残差 | Residual |
| 总平方和 | Total sum of squares, SST |
| 回归平方和 | Regression sum of squares, SSR |
| 残差平方和 | Error/residual sum of squares, SSE |
| 均方误差 | Mean square error, MSE |
| 决定系数 | Coefficient of determination, \(R^2\) |
| 平均响应 | Mean response |
| 预测区间 | Prediction interval |
| 相关系数 | Correlation coefficient |
| 同方差性 | Homoscedasticity |
| 异方差性 | Heteroscedasticity |
| 异常值 | Outlier |
| 杠杆值 | Leverage |
| 影响点 | Influential point |
| 外推 | Extrapolation |
| 帽子矩阵 | Hat matrix |
| 投影 | Projection |
| 过拟合 | Overfitting |
| 欠拟合 | Underfitting |
| 泛化 | Generalization |
| 偏差—方差权衡 | Bias–variance tradeoff |
| 岭回归 | Ridge regression |
| 套索回归 | Lasso regression |

---

# Part XVI. 最后一分钟公式索引

\[
E[\bar X]=\mu,\qquad
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}
\]

\[
S^2=\frac1{n-1}\sum(X_i-\bar X)^2
\]

\[
\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta
\]

\[
\operatorname{MSE}
=
\operatorname{Var}+\operatorname{Bias}^2
\]

\[
L(\theta)=\prod f(x_i;\theta),
\qquad
\ell(\theta)=\sum\log f(x_i;\theta)
\]

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}
\]

\[
T=\frac{\bar X-\mu}{S/\sqrt n}
\sim t_{n-1}
\]

\[
\frac{(n-1)S^2}{\sigma^2}
\sim\chi^2_{n-1}
\]

\[
\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}
\sim F_{n_1-1,n_2-1}
\]

\[
S_p^2
=
\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}
{n_1+n_2-2}
\]

\[
T_{\mathrm{pooled}}
=
\frac{(\bar X_1-\bar X_2)-\Delta_0}
{S_p\sqrt{1/n_1+1/n_2}}
\]

\[
T_{\mathrm{Welch}}
=
\frac{(\bar X_1-\bar X_2)-\Delta_0}
{\sqrt{S_1^2/n_1+S_2^2/n_2}}
\]

\[
T_{\mathrm{paired}}
=
\frac{\bar D-\mu_{D,0}}{S_D/\sqrt n}
\]

\[
\chi^2_{\mathrm{categorical}}
=
\sum\frac{(O-E)^2}{E}
\]

\[
E_{ij}
=
\frac{(\text{row total})(\text{column total})}{N}
\]

\[
df_{\mathrm{GOF}}=k-1-m
\]

\[
df_{\mathrm{table}}=(r-1)(c-1)
\]

\[
b_1=\frac{S_{xy}}{S_{xx}},
\qquad
b_0=\bar y-b_1\bar x
\]

\[
SSE=S_{yy}-\frac{S_{xy}^2}{S_{xx}}
\]

\[
s^2=\frac{SSE}{n-2}
\]

\[
SE(b_1)=\frac{s}{\sqrt{S_{xx}}}
\]

\[
R^2=1-\frac{SSE}{SST}=r^2
\]

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
\]

\[
T_r=
\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}
\]

\[
SE_{\mathrm{mean}}
=
s\sqrt{
\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}
}
\]

\[
SE_{\mathrm{pred}}
=
s\sqrt{
1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}
}
\]

---

## 资料文件

- `Final/docs/README.md`
- `Final/docs/material/final_rc_estimate.pdf`
- `Final/docs/material/final_rc_tests.pdf`
- `Final/docs/material/Final_RC_MZM.pptx`
- `Final/docs/material/Regression.pdf`
- `Final/docs/material/401final_exercises_solutions.pdf`（仅用于确认题型组织，不作为唯一考试范围）
