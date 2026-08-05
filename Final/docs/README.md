# 401 Final 复习范围与学习路线

> 目标：根据 `Final/docs/material` 中的知识讲义与样卷，梳理期末考试需要掌握的内容、知识依赖、常见题型和复习优先级。

## 1. 材料定位

### 知识范围来源

以下四份材料决定“需要学习什么”：

1. [`final_rc_estimate.pdf`](material/final_rc_estimate.pdf)
   - 随机样本与统计量
   - 点估计、矩估计、最大似然估计
   - 参考分布
   - 置信区间
   - 假设检验基础
2. [`final_rc_tests.pdf`](material/final_rc_tests.pdf)
   - 单样本与双样本假设检验
   - 方差检验
   - pooled t、Welch t、配对检验
   - 非参数检验
   - 第一类/第二类错误与功效
3. [`Final_RC_MZM.pptx`](material/Final_RC_MZM.pptx)
   - 两总体方差比较
   - 非参数比较
   - 配对数据与相关性
   - 分类数据分析
   - 根据数据结构选择检验方法
4. [`Regression.pdf`](material/Regression.pdf)
   - 简单线性回归
   - 最小二乘估计
   - 回归推断与预测
   - 相关系数
   - 回归的几何/矩阵解释及泛化问题

### 样卷

[`401final_exercises_solutions.pdf`](material/401final_exercises_solutions.pdf) **只是样卷及解答，不是考试范围的唯一来源**。

它的用途是：

- 判断老师会怎样组合知识点；
- 熟悉计算量和书写格式；
- 检查自己能否从题目描述中选出正确方法；
- 练习完整地写出假设、统计量、自由度、结论和解释。

---

## 2. 总体知识地图

建议按照下面的依赖顺序学习：

```text
随机样本与统计量
        ↓
估计量：Bias / Variance / MSE
        ↓
矩估计与最大似然估计
        ↓
Z、χ²、t、F 参考分布
        ↓
置信区间
        ↓
假设检验基本流程
        ↓
单样本 / 双样本 / 配对 / 非参数 / 分类数据检验
        ↓
简单线性回归与相关性
```

不能只背公式。每一种方法都要同时掌握：

1. **适用的数据结构**；
2. **所需假设**；
3. **统计量及其参考分布**；
4. **自由度**；
5. **拒绝域或 p-value 的判断**；
6. **如何用题目语境写结论**。

---

# Part A：随机样本、统计量与估计

## 3. 随机样本和统计量

### 3.1 随机样本

应理解：

- \(X_1,\ldots,X_n\) 是来自同一总体的随机样本；
- 随机样本通常表示这些变量 **独立同分布（i.i.d.）**；
- 观测前 \(X_i\) 是随机变量，观测后得到具体数值 \(x_i\)。

### 3.2 统计量

统计量是样本的函数，并且表达式中不包含未知参数。

重点统计量：

\[
\bar X=\frac1n\sum_{i=1}^n X_i
\]

\[
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\]

需要会：

- 根据总体的 \(E[X]\)、\(\operatorname{Var}(X)\) 求 \(E[\bar X]\)、\(\operatorname{Var}(\bar X)\)；
- 区分总体参数、随机统计量和观测值；
- 理解为什么样本方差使用 \(n-1\)。

---

## 4. 估计量的评价

### 4.1 偏差 Bias

\[
\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta
\]

- Bias 为 0：无偏估计量；
- Bias 不为 0：估计量平均而言会偏离真实参数。

### 4.2 方差 Variance

\[
\operatorname{Var}(\hat\theta)
\]

表示估计量在重复抽样中的波动程度。

### 4.3 均方误差 MSE

\[
\operatorname{MSE}(\hat\theta)
=E[(\hat\theta-\theta)^2]
=\operatorname{Var}(\hat\theta)+\operatorname{Bias}(\hat\theta)^2
\]

应会比较两个估计量：

- 不能只看是否无偏；
- 一个略有偏但方差很小的估计量，MSE 可能更小；
- 题目可能要求直接推导估计量的方差或 MSE。

### 4.4 一致性

理解基本含义：样本量越来越大时，估计量越来越接近真实参数。

复习时至少要能判断：

- Bias 是否随 \(n\to\infty\) 消失；
- Variance 是否随 \(n\to\infty\) 趋近 0。

---

## 5. 矩估计 Method of Moments

核心步骤：

1. 写出总体矩，如 \(E[X]\)、\(E[X^2]\)；
2. 用样本矩替代总体矩；
3. 解出未知参数。

单参数最常见形式：

\[
\bar X=E_\theta[X]
\]

需要会：

- 从给定 pdf/pmf 计算 \(E[X]\)；
- 解出矩估计量；
- 进一步计算该估计量的 Bias、Variance 或 MSE；
- 多参数时使用多个矩方程。

样卷中出现过：由 \(\bar X=E[X]\) 得到参数的矩估计，并继续推导估计量方差。

---

## 6. 最大似然估计 MLE

### 6.1 基本定义

对于 i.i.d. 样本：

\[
L(\theta)=\prod_{i=1}^n f(x_i;\theta)
\]

对数似然：

\[
\ell(\theta)=\log L(\theta)
\]

最大化 \(L\) 与最大化 \(\ell\) 等价。

### 6.2 完整解题流程

必须形成固定模板：

1. 写明参数空间；
2. 写出 likelihood；
3. 取 log-likelihood；
4. 求导并解 score equation：
   \[
   \ell'(\theta)=0
   \]
5. 检查该解确实是全局最大值；
6. 检查边界、参数限制以及是否存在内部解。

证明最大值的方法：

- 二阶导数为负；
- 一阶导数在解的两侧由正变负；
- 比较驻点与边界；
- 直接比较似然函数大小。

### 6.3 必会典型例子

- Poisson：
  \[
  \hat\lambda_{ML}=\bar X
  \]
- Normal：
  \[
  \hat\mu_{ML}=\bar X
  \]
  \[
  \hat\sigma^2_{ML}=\frac1n\sum_{i=1}^n(X_i-\bar X)^2
  \]

注意：MLE 的正态方差估计分母是 \(n\)，而无偏样本方差分母是 \(n-1\)。

样卷中出现过：根据给定分布写 likelihood、求导，并得到形如

\[
\hat\theta_{ML}^2=\frac1{2n}\sum X_i^2
\]

的估计结果。

---

# Part B：参考分布与置信区间

## 7. 四个核心参考分布

## 7.1 标准正态分布 Z

当总体正态且总体标准差已知时：

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)
\]

也可能在大样本近似中使用，但做题时要先确认课程允许的条件。

## 7.2 卡方分布 \(\chi^2\)

若总体为正态：

\[
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}
\]

用途：

- 单总体方差的置信区间；
- 单总体方差的假设检验。

**正态总体假设非常重要。**

## 7.3 Student t 分布

若总体正态、\(\sigma\) 未知：

\[
T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}
\]

用途：

- 单总体均值区间与检验；
- 两总体均值比较；
- 配对 t 检验；
- 回归系数推断；
- Pearson 相关系数检验。

## 7.4 F 分布

对于两个独立正态样本，在原假设 \(\sigma_1^2=\sigma_2^2\) 下：

\[
F=\frac{S_1^2}{S_2^2}\sim F_{n_1-1,n_2-1}
\]

用途：

- 比较两个总体方差；
- 判断是否适合使用 pooled t-test。

---

## 8. 置信区间

### 8.1 正确理解置信水平

置信区间是随机区间。

“95% 置信”表示：重复抽样并重复构造区间时，长期来看约 95% 的区间会覆盖真实参数。

不要写成“参数有 95% 的概率落在已经算出的固定区间中”。

### 8.2 枢轴量法

通用推导方法：

1. 找到包含参数但分布已知的枢轴量 \(Q\)；
2. 选取 \(a,b\)，使
   \[
   P(a\le Q\le b)=1-\alpha
   \]
3. 代入 \(Q\)；
4. 代数变形，把目标参数放到不等式中间。

### 8.3 单总体均值区间

已知 \(\sigma\)：

\[
\bar X\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}
\]

未知 \(\sigma\)：

\[
\bar X\pm t_{1-\alpha/2,n-1}\frac{S}{\sqrt n}
\]

### 8.4 单总体方差区间

令 \(\chi^2_{q,\nu}\) 表示自由度为 \(\nu\) 的卡方分布的 \(q\) 分位数：

\[
\left(
\frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}},
\frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}}
\right)
\]

标准差区间对两个端点开平方。

要特别注意：较大的卡方临界值放在下界的分母中。

### 8.5 两总体均值差区间

需要分别掌握：

- 独立且方差相等：pooled t interval；
- 独立但方差不等：Welch interval；
- 配对数据：先转化为差值 \(D_i=X_i-Y_i\)，再做单样本 t interval。

---

# Part C：假设检验

## 9. 假设检验的统一流程

任何检验题都按以下步骤书写：

1. 定义参数；
2. 写 \(H_0\) 与 \(H_1\)；
3. 判断单侧还是双侧；
4. 检查方法所需假设；
5. 写统计量及 \(H_0\) 下的分布；
6. 代入样本计算统计量；
7. 用临界值或 p-value 作决定；
8. 用题目语境写结论。

### 9.1 单侧与双侧

- “different / changed” → 双侧；
- “greater / improved / exceeds” → 右尾；
- “less / below / decreased” → 左尾。

方向必须由研究问题决定，不能看完数据再选。

### 9.2 p-value

p-value 是：在 \(H_0\) 为真时，得到当前结果或更极端结果的概率。

决策：

\[
p\le\alpha \Rightarrow \text{reject }H_0
\]

\[
p>\alpha \Rightarrow \text{fail to reject }H_0
\]

不要把 “fail to reject” 写成“证明 \(H_0\) 正确”。

### 9.3 两类错误与功效

- Type I error：\(H_0\) 真实却拒绝，概率为 \(\alpha\)；
- Type II error：\(H_0\) 错误却未拒绝，概率为 \(\beta\)；
- Power：
  \[
  1-\beta
  \]

应理解功效受以下因素影响：

- 样本量；
- 显著性水平；
- 真实效应大小；
- 数据波动。

材料中存在“给定备择参数求 power”以及“达到目标 power 求样本量”的题型。

### 9.4 置信区间与双侧检验的对偶

对于显著性水平 \(\alpha\) 的双侧检验：

- 若 \(H_0\) 中的参数值不在 \(100(1-\alpha)\%\) 置信区间内，则拒绝 \(H_0\)；
- 若参数值在区间内，则不拒绝。

---

## 10. 单样本检验

### 10.1 均值，\(\sigma\) 已知

\[
Z=\frac{\bar X-\mu_0}{\sigma/\sqrt n}
\]

### 10.2 均值，\(\sigma\) 未知

\[
T=\frac{\bar X-\mu_0}{S/\sqrt n}\sim t_{n-1}
\]

拒绝域：

- 双侧：\(|T|>t_{1-\alpha/2,n-1}\)；
- 右尾：\(T>t_{1-\alpha,n-1}\)；
- 左尾：\(T<-t_{1-\alpha,n-1}\)。

### 10.3 单总体方差

在正态总体假设下：

\[
\chi^2=\frac{(n-1)S^2}{\sigma_0^2}\sim\chi^2_{n-1}
\]

必须会根据 \(H_1\) 选择左尾、右尾或双尾临界值。

---

## 11. 两独立样本均值比较

先确认两组数据是否真正独立。

### 11.1 方差相等：Pooled t-test

合并方差：

\[
S_p^2=
\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}
{n_1+n_2-2}
\]

统计量：

\[
T=
\frac{(\bar X_1-\bar X_2)-\Delta_0}
{S_p\sqrt{1/n_1+1/n_2}}
\sim t_{n_1+n_2-2}
\]

样卷中出现过 pooled t 检验及均值差置信区间。

### 11.2 方差不等：Welch t-test

\[
T=
\frac{(\bar X_1-\bar X_2)-\Delta_0}
{\sqrt{S_1^2/n_1+S_2^2/n_2}}
\]

Welch-Satterthwaite 自由度：

\[
\nu\approx
\frac{(S_1^2/n_1+S_2^2/n_2)^2}
{(S_1^2/n_1)^2/(n_1-1)+(S_2^2/n_2)^2/(n_2-1)}
\]

需要知道为什么不能在方差明显不等时仍使用 pooled variance。

### 11.3 两方差比较

\[
F=\frac{S_1^2}{S_2^2}
\]

需会：

- 写 \(H_0:\sigma_1^2=\sigma_2^2\)；
- 根据备择假设决定单尾/双尾；
- 正确填写分子和分母自由度；
- 用结果决定 pooled t 还是 Welch t。

---

## 12. 配对样本

典型场景：

- 同一对象治疗前后；
- 同一学生两次成绩；
- 成对匹配的实验对象。

先定义：

\[
D_i=X_i-Y_i
\]

然后对差值做单样本分析。

### 12.1 配对 t-test

若差值近似正态：

\[
T=\frac{\bar D-\mu_{D,0}}{S_D/\sqrt n}\sim t_{n-1}
\]

关键点：检验的是“差值总体的均值”，不是把两列当成独立样本。

### 12.2 非正态配对数据

- 只利用正负方向：Sign test；
- 能利用差值大小和方向：Wilcoxon signed-rank test。

---

## 13. 非参数检验

非参数方法不是“完全没有假设”，而是减少对具体总体分布形式的依赖。

### 13.1 Sign test

忽略差值为 0 的样本，只记录正负号。

在原假设下：

\[
Q_+\sim\operatorname{Binomial}(n,1/2)
\]

适合：

- 配对数据；
- 只希望检验中位数方向；
- 数据偏态或含明显异常值。

### 13.2 Wilcoxon signed-rank test

步骤：

1. 计算每对差值；
2. 删除 0 差值；
3. 对绝对差值排序并赋秩；
4. 恢复正负号；
5. 计算正秩和 \(W_+\) 与负秩和 \(W_-\)；
6. 根据检验方向使用相应统计量。

比 sign test 利用更多信息，但通常要求差值分布具有一定对称性。

### 13.3 Wilcoxon rank-sum / Mann-Whitney U

适合两个独立样本，特别是：

- 数据明显非正态；
- 样本量较小；
- 数据偏态；
- 数据是有序等级；
- t 检验假设不合适。

步骤：

1. 合并两组数据；
2. 从小到大排序；
3. 处理并列秩；
4. 求某组秩和；
5. 使用精确分布或正态近似作判断。

样卷中出现过 Wilcoxon rank-sum 题型。

---

## 14. 检验方法选择表

| 数据关系 | 分布/尺度情况 | 推荐方法 |
|---|---|---|
| 一个样本均值 | 正态，\(\sigma\) 已知 | One-sample Z |
| 一个样本均值 | 正态，\(\sigma\) 未知 | One-sample t |
| 一个总体方差 | 正态总体 | \(\chi^2\) test |
| 两个独立样本 | 正态、方差相等 | Pooled/Student two-sample t |
| 两个独立样本 | 正态、方差不等 | Welch t |
| 两个独立样本 | 非正态、偏态、小样本或等级数据 | Wilcoxon rank-sum / Mann-Whitney U |
| 配对样本 | 差值近似正态 | Paired t |
| 配对样本 | 差值非正态、偏态或小样本 | Wilcoxon signed-rank |
| 配对样本 | 只使用差值方向 | Sign test |
| 两总体方差 | 两个独立正态样本 | F test |
| 分类变量 | 频数表 | Chi-square independence/homogeneity |

考试中最容易丢分的不是算术，而是：

- 把配对样本当独立样本；
- 方差不等却使用 pooled t；
- 非正态小样本仍机械使用 t-test；
- 把连续变量方法用于分类频数；
- 自由度写错；
- 单尾、双尾方向写反。

---

# Part D：分类数据

## 15. 卡方独立性/同质性检验

材料和样卷涉及列联表的卡方方法。

### 15.1 期望频数

\[
E_{ij}=
\frac{(\text{第 }i\text{ 行总数})(\text{第 }j\text{ 列总数})}{N}
\]

### 15.2 检验统计量

\[
\chi^2=\sum_i\sum_j\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
\]

自由度：

\[
(r-1)(c-1)
\]

### 15.3 两种常见表述

- **Independence**：同一总体中的两个分类变量是否独立；
- **Homogeneity**：不同总体是否具有相同的分类比例。

计算形式相同，但研究设计和结论语句不同。

### 15.4 必须会检查

- 观测值是频数，不是百分比；
- 个体之间独立；
- 期望频数不能过小；
- 显著后只能说明存在关联或分布不同，不能直接说明因果。

样卷中出现过 chi-square homogeneity 题型。

---

# Part E：简单线性回归与相关性

## 16. 回归模型

简单线性回归模型：

\[
Y_i=\beta_0+\beta_1x_i+\varepsilon_i
\]

典型假设：

- \(E[\varepsilon_i]=0\)；
- \(\operatorname{Var}(\varepsilon_i)=\sigma^2\) 恒定；
- 误差独立；
- 做精确 t/F 推断时通常假设误差正态。

条件均值和方差：

\[
E[Y\mid x]=\beta_0+\beta_1x
\]

\[
\operatorname{Var}(Y\mid x)=\sigma^2
\]

应理解：回归描述的是 \(Y\) 的平均变化，而不是说所有点都落在直线上。

---

## 17. 最小二乘估计

定义：

\[
S_{xx}=\sum(x_i-\bar x)^2
\]

\[
S_{yy}=\sum(y_i-\bar y)^2
\]

\[
S_{xy}=\sum(x_i-\bar x)(y_i-\bar y)
\]

斜率和截距：

\[
\hat\beta_1=\frac{S_{xy}}{S_{xx}}
\]

\[
\hat\beta_0=\bar y-\hat\beta_1\bar x
\]

拟合直线一定经过：

\[
(\bar x,\bar y)
\]

残差：

\[
e_i=y_i-\hat y_i
\]

残差平方和：

\[
SSE=\sum e_i^2
\]

误差方差估计：

\[
s^2=\frac{SSE}{n-2}
\]

需要会从原始数据表计算全部中间量，而不是只会使用软件输出。

---

## 18. 回归系数的推断

### 18.1 斜率标准误

\[
SE(\hat\beta_1)=\frac{s}{\sqrt{S_{xx}}}
\]

检验：

\[
H_0:\beta_1=\beta_{1,0}
\]

\[
T=\frac{\hat\beta_1-\beta_{1,0}}{SE(\hat\beta_1)}
\sim t_{n-2}
\]

斜率置信区间：

\[
\hat\beta_1\pm t_{1-\alpha/2,n-2}SE(\hat\beta_1)
\]

### 18.2 截距标准误

\[
SE(\hat\beta_0)
=s\sqrt{\frac1n+\frac{\bar x^2}{S_{xx}}}
\]

截距区间同样使用 \(t_{n-2}\)。

样卷要求过斜率和截距的置信区间计算。

---

## 19. 均值响应区间与预测区间

在 \(x=x_0\) 处：

\[
\hat y(x_0)=\hat\beta_0+\hat\beta_1x_0
\]

### 19.1 平均响应的置信区间

\[
\hat y(x_0)\pm
 t^*s\sqrt{
 \frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}
 }
\]

### 19.2 单个新观测值的预测区间

\[
\hat y(x_0)\pm
 t^*s\sqrt{
 1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}
 }
\]

预测区间多出的 \(1\) 表示新个体本身的随机波动，所以它一定比平均响应区间更宽。

样卷中出现过 prediction interval。

---

## 20. Pearson 相关系数

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
\]

性质：

- \(-1\le r\le1\)；
- 正负表示线性方向；
- 绝对值表示线性关系强弱；
- 无量纲；
- 对异常值敏感；
- \(r\approx0\) 不代表完全没有关系，可能存在强非线性关系。

检验：

\[
H_0:\rho=0
\]

\[
T=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}
\sim t_{n-2}
\]

样卷中出现过 Pearson correlation test。

在含截距的简单线性回归中：

\[
R^2=r^2
\]

但相关不等于因果。

---

## 21. 回归诊断与使用边界

至少要能识别：

- 非线性趋势；
- 残差方差随 \(x\) 改变；
- 异常值和高影响点；
- 误差相关；
- 超出观测 \(x\) 范围的外推风险。

`Regression.pdf` 还涉及以下理解性内容，可作为第二优先级：

- 矩阵形式 \(y=X\beta+\varepsilon\)；
- \(\hat\beta=(X^TX)^{-1}X^Ty\)；
- hat matrix 与投影解释；
- 模型自由度和残差自由度；
- 多项式回归中的过拟合；
- bias-variance tradeoff；
- ridge/lasso 对泛化能力的作用。

这些内容应先理解概念，再根据老师课堂和作业深度决定是否做复杂推导。

---

# Part F：样卷反映出的实际题型

## 22. 样卷已经覆盖的题型

样卷表明至少需要具备以下综合能力：

1. **分类数据**
   - 计算列联表期望频数；
   - 完成 chi-square homogeneity test；
   - 写自由度和语境结论。
2. **参数估计**
   - MLE；
   - Method of Moments；
   - 推导估计量方差。
3. **非参数检验**
   - Wilcoxon rank-sum；
   - 合并排序、计算秩和、作出决定。
4. **两独立样本均值比较**
   - pooled variance；
   - pooled t-test；
   - 均值差置信区间。
5. **简单线性回归**
   - 计算 \(S_{xx},S_{xy},S_{yy}\)；
   - 求 \(\hat\beta_0,\hat\beta_1\)；
   - 计算 SSE 和 \(s^2\)；
   - 斜率/截距区间；
   - prediction interval。
6. **相关性**
   - Pearson \(r\)；
   - 检验 \(H_0:\rho=0\)。

## 23. 样卷没有充分覆盖但讲义要求学习的内容

不能因为样卷没出现就跳过：

- 单总体方差的卡方检验与区间；
- 两总体方差的 F 检验；
- Welch t-test；
- 配对 t-test；
- Sign test；
- Wilcoxon signed-rank；
- Type II error 和 power；
- 检验方法选择；
- 回归诊断与平均响应区间。

---

# Part G：推荐复习顺序

## 24. 第一阶段：建立基础

完成标准：看到符号就知道它是参数、统计量还是观测值。

- i.i.d. 随机样本；
- \(\bar X,S^2\)；
- Bias、Variance、MSE；
- 矩估计；
- MLE 固定步骤。

## 25. 第二阶段：掌握四个参考分布

完成标准：能够根据问题立即判断使用 Z、t、\(\chi^2\) 还是 F。

- 每个统计量的公式；
- 使用条件；
- 自由度；
- 单尾/双尾临界值。

## 26. 第三阶段：统一掌握假设检验

完成标准：任何检验都能独立写出 8 步完整答案。

先学：

1. one-sample Z/t；
2. one-variance \(\chi^2\)；
3. two-variance F；
4. pooled t 与 Welch t；
5. paired t；
6. rank-sum、signed-rank、sign；
7. chi-square categorical tests。

## 27. 第四阶段：回归

完成标准：从数据表开始，能够手算到最终推断和预测。

顺序：

1. \(S_{xx},S_{xy},S_{yy}\)；
2. \(\hat\beta_0,\hat\beta_1\)；
3. 残差、SSE、\(s^2\)；
4. 系数检验与区间；
5. mean-response interval 与 prediction interval；
6. Pearson correlation test；
7. 残差诊断与外推。

## 28. 第五阶段：用样卷做整合

做样卷时不要只核对数字。每题额外回答：

- 为什么选这个方法？
- 哪些条件允许使用它？
- 如果条件改变，应换成什么方法？
- 自由度从哪里来？
- 结论能说明什么，不能说明什么？

---

# Part H：考前自检清单

## 29. 估计

- [ ] 会判断一个表达式是否是统计量；
- [ ] 会计算 Bias、Variance、MSE；
- [ ] 会用矩方程求 MOM；
- [ ] 会完整写 MLE，不遗漏参数空间和最大值检查；
- [ ] 会区分 MLE 方差估计与无偏样本方差。

## 30. 区间与检验

- [ ] 能在 Z、t、\(\chi^2\)、F 中正确选择；
- [ ] 会写单尾和双尾假设；
- [ ] 会使用临界值和 p-value；
- [ ] 能解释 Type I、Type II 和 power；
- [ ] 会用 CI 判断双侧检验结论；
- [ ] 自由度不会写错。

## 31. 方法选择

- [ ] 独立与配对不会混淆；
- [ ] pooled 与 Welch 不会混淆；
- [ ] 正态参数方法与非参数方法会选择；
- [ ] rank-sum 与 signed-rank 不会混淆；
- [ ] 分类频数会使用 chi-square 方法。

## 32. 回归

- [ ] 会算 \(S_{xx},S_{xy},S_{yy}\)；
- [ ] 会算斜率、截距、残差、SSE 和 \(s^2\)；
- [ ] 会做斜率/截距的区间与检验；
- [ ] 会区分平均响应区间与预测区间；
- [ ] 会计算并检验 Pearson 相关系数；
- [ ] 知道相关不等于因果；
- [ ] 知道不能随意外推。

---

## 33. 最高优先级总结

时间有限时，优先保证下面六块：

1. **MOM + MLE + Bias/Variance/MSE**；
2. **Z/t/\(\chi^2\)/F 的使用条件和自由度**；
3. **pooled t、Welch t、paired t 的选择与完整计算**；
4. **Wilcoxon rank-sum、signed-rank、sign test 的区别**；
5. **chi-square 列联表检验**；
6. **简单线性回归全流程 + prediction interval + correlation test**。

最终目标不是“看懂答案”，而是看到题目后能完成：

```text
识别数据结构
→ 选择方法
→ 检查假设
→ 写统计量和分布
→ 计算与判断
→ 用语境解释结论
```
