# VE401 Sample Midterm 2021 - 逐题知识补充

> 这个文件是 `cheating_sheet.md` 之外的详细题目讲解区，用来放每一题的解题步骤、题型识别和涉及知识点。  
> 来源：`ve401_sample_midterm_2021_sol.pdf`。  
> 维护方式：可以手动编辑，也可以用 `scripts/add_midterm_supplement.py` 继续逐题追加。

---

## 使用方式

每题都按下面结构整理：

- **题型定位**：先判断这是哪类题。
- **解题步骤**：考试时按步骤套。
- **涉及知识点**：对应需要复习的公式和概念。
- **易错点**：最容易丢分的地方。

<!-- AUTO-MIDTERM-SUPPLEMENT-ZONE-START -->

## SM21-001 — Multiple Choice 综合判断

**题型定位**：基础概念辨析题，考查方差、独立性、二项事件、指数分布、正态变换。

**解题步骤**：

1. 若 X, Y 独立，则 `Var(X - Y) = Var(X) + Var(Y)`，因为 `Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)`。
2. 独立性的最强判据是联合密度或联合 PMF 可分解：`fXY(x,y) = fX(x) fY(y)`。
3. 两次抛不公平硬币，得到“两次相同”的概率是 `p^2 + (1-p)^2 = 1 - 2p(1-p)`。当 `p != 1/2` 时比 `1/2` 大。
4. 指数分布的 PDF 从 0 开始单调下降，所以众数 mode 是 0。
5. 正态变量的线性变换仍正态；平方变换 `Y = X^2` 一般不再正态。

**涉及知识点**：

- 独立变量方差相加。
- Independence: joint = marginal product。
- Bernoulli / Binomial 基本概率。
- Exponential distribution 的形状和 memoryless 性质。
- Normal distribution 对线性变换封闭，但对非线性变换不封闭。

**易错点**：

- `rhoXY = 0` 或 `E[XY]=E[X]E[Y]` 只表示不相关，不一定独立。
- `Var(X-Y)` 不是 `Var(X)-Var(Y)`。

---

## SM21-002 — Bayes: 工厂缺陷率反推

**题型定位**：Bayes theorem。已知“失败产品来自哪个工厂”，反推“某工厂产品失败概率”。

**解题步骤**：

1. 先列已知量：`P(A)=0.20, P(B)=0.45, P(C)=0.35, P(fail)=0.05`。
2. 题目给的是反向条件概率：`P(A|fail)=0.25, P(B|fail)=0.35, P(C|fail)=0.40`。
3. 用 Bayes 公式：`P(fail|A)=P(A|fail) P(fail) / P(A)`。
4. 分别代入：
   - `P(fail|A)=0.25*0.05/0.20=0.0625`
   - `P(fail|B)=0.35*0.05/0.45≈0.039`
   - `P(fail|C)=0.40*0.05/0.35≈0.057`

**涉及知识点**：

- Conditional probability。
- Bayes theorem。
- `P(A|fail)` 和 `P(fail|A)` 方向不同。

**易错点**：

- 不能把“失败产品中 25% 来自 A”直接当成“A 工厂失败率 25%”。

---

## SM21-003 — Pascal / Negative Binomial: 第 r 次成功发生在第 x 次

**题型定位**：重复抛硬币，问第 r 个 head 出现的位置。第一问是 Pascal 分布；第二问是条件组合计数。

**解题步骤**：

**i) 第 5 个 head 在第 10 次：**

1. 第 10 次必须是 head。
2. 前 9 次中必须刚好有 4 个 head。
3. 概率：`C(9,4) (1/2)^10 = 0.123`。

**ii) 已知第 10 个 head 在第 25 次，求第 5 个 head 的位置 X：**

1. 第 25 次是第 10 个 head，所以前 24 次中有 9 个 head。
2. 若第 5 个 head 在第 x 次，则：
   - 前 `x-1` 次中有 4 个 head；
   - 第 x 次是 head；
   - 第 `x+1` 到 24 次中还要有 4 个 head。
3. 总样本数是从前 24 次中选 9 个 head：`C(24,9)`。
4. 所以 `P(X=x)=C(x-1,4) C(24-x,4) / C(24,9)`，其中 `5 <= x <= 20`。

**涉及知识点**：

- Pascal / Negative Binomial distribution。
- 条件概率中的“等可能组合”思想。
- 第 r 次成功位置题：最后一次必须是成功。

**易错点**：

- 第二问不要再乘 `(1/2)^24`，因为在条件空间里所有 9 个 head 的位置组合等可能，概率因子会约掉。

---

## SM21-004 — Bayes: 测试没有出现 0 后判断 RNG 是否坏

**题型定位**：二分类 Bayes。观测结果是“20 次都没有 0”。

**解题步骤**：

1. 设 `D` 表示 defective，`R` 表示 20 次测试没有出现 0。
2. 先写先验：`P(D)=0.2, P(not D)=0.8`。
3. 若 defective，则不会生成 0：`P(R|D)=1`。
4. 若 not defective，则每次没有 0 的概率是 0.9，所以 `P(R|not D)=0.9^20=0.1216`。
5. Bayes：`P(D|R)=P(R|D)P(D) / [P(R|D)P(D)+P(R|not D)P(not D)]`。
6. 代入得 `1*0.2 / (1*0.2 + 0.1216*0.8) = 0.6728`。

**涉及知识点**：

- Bayes theorem。
- Evidence / observation 的总概率分母。
- 独立重复试验概率相乘。

**易错点**：

- 看到“20 次没出 0”不能直接判定一定坏，因为正常 RNG 也可能偶然没出 0。

---

## SM21-005 — Exponential Failure Time: 已知夜里已坏，求 5 点还没坏的概率

**题型定位**：指数分布失效时间 + 条件概率。10 pm 到 6 am 共 8 小时；5 am 是第 7 小时。

**解题步骤**：

1. 平均 24 小时失败一次，失效率 `lambda = 1/24`。
2. Time to failure `T` 服从指数分布，密度 `f(t)=lambda e^(-lambda t)`。
3. 已知 6 am 已经坏了，即 `T <= 8`。
4. 要求 5 am 还在工作，但 6 am 已坏，即 `7 < T <= 8`。
5. 条件概率：`P(7<T<=8 | T<=8) = P(7<T<=8) / P(T<=8)`。
6. 用 CDF `F(t)=1-e^(-t/24)`：
   - 分子 `F(8)-F(7)=e^(-7/24)-e^(-8/24)`；
   - 分母 `F(8)=1-e^(-8/24)`。
7. 得到约 `0.108`。

**涉及知识点**：

- Poisson process 与 exponential waiting time。
- `R(t)=P(T>t)=e^(-lambda t)`。
- 条件概率。

**易错点**：

- 题目不是问“从 5 点到 6 点坏的无条件概率”，而是在已知 6 点已经坏的前提下求条件概率。

---

## SM21-006 — Binomial Normal Approximation: 连续性修正

**题型定位**：大 n 二项分布用正态近似。

**解题步骤**：

1. 令 `X ~ Bin(n=28800, p=0.5)`。
2. 均值 `mu=np=14400`。
3. 方差 `sigma^2=np(1-p)=7200`，所以 `sigma=sqrt(7200)=60sqrt(2)`。
4. 要求 `P(14380 <= X <= 14399)`。
5. 连续性修正：`P(14379.5 <= X <= 14399.5)`。
6. 标准化：`Z=(X-mu)/sigma`。
7. 得到大约 `P(-0.24 <= Z <= -0.0059)`。
8. 查表得约 `0.0948`。

**涉及知识点**：

- Binomial to Normal approximation。
- Continuity correction / half-unit correction。
- Standardization: `Z=(X-mu)/sigma`。

**易错点**：

- 区间端点要做 `±0.5` 修正，否则答案会偏。

---

## SM21-007 — Overbooking: 酒店超订的正态近似

**题型定位**：二项分布正态近似 + 反解最大 reservation 数。

**解题步骤**：

**i) 215 个预订，求够房概率：**

1. 每个旅客出现概率 0.9，所以 `T ~ Bin(215,0.9)`。
2. `mu=215*0.9=193.5`，`sigma=sqrt(215*0.9*0.1)=4.399`。
3. 要求 `P(T<=200)`。
4. 连续性修正为 `P(X<=200.5)`。
5. 标准化：`z=(200.5-193.5)/4.399=1.59`。
6. 查表得约 `0.94`。

**ii) 入住超过 190 间：**

1. “more than 190” 即 `T>=191`。
2. 连续性修正为 `P(X>=190.5)`。
3. `z=(190.5-193.5)/4.399=-0.68`。
4. 所以概率约 `P(Z>=-0.68)=0.752`。

**iii) 至少 99% 概率够房，最多接多少 reservation：**

1. 设接受 `R` 个预订，则 `T ~ Bin(R,0.9)`。
2. 正态近似：`mu=0.9R`，`sigma=sqrt(0.9*0.1R)=0.3sqrt(R)`。
3. 目标：`P(T<=200) >= 0.99`。
4. 连续性修正：`P(X<=200.5)>=0.99`。
5. 查表 `z_0.99≈2.33`，所以 `(200.5-0.9R)/(0.3sqrt(R)) >= 2.33`。
6. 解不等式，取较小根附近，得到 `R <= 211`。

**涉及知识点**：

- Binomial approximation。
- Normal quantile 反查。
- “at least 99% certain” 对应左尾概率 0.99。

**易错点**：

- 出现概率是 0.9，不是 no-show 的 0.1。
- 第三问是反解 n，不是直接把 215 代进去。

---

## SM21-008 — Poisson Approximation: 缺陷 drill bits

**题型定位**：小概率二项分布用 Poisson 近似。

**解题步骤**：

1. 每包 100 个，每个 defective 概率 0.02。
2. 缺陷数 `X ~ Bin(100,0.02)`，用 `Pois(lambda=np=2)` 近似。

**i) 没有 defective：**

- `P(X=0)=e^-2≈0.135`。

**ii) 不超过 3 个 defective：**

- `P(X<=3)=sum_{k=0}^3 e^-2 2^k/k!≈0.857`。

**iii) 至少 100 个 non-defective 的包装大小：**

1. 若包装大小为 `N`，defective 数 `X≈Pois(0.02N)`。
2. 至少 100 个好品等价于 `X <= N-100`。
3. 先试 `N=104`，则允许最多 4 个 defective，`lambda=2.08`。
4. `P(X<=4 | lambda=2.08)>0.9`，所以 104 个足够。

**涉及知识点**：

- Poisson approximation to Binomial: `lambda=np`。
- “至少 100 个好品”转换为“缺陷数不超过 N-100”。

**易错点**：

- 第三问的 `lambda` 要随包装大小 N 改变，不再固定为 2。

---

## SM21-009 — Bernoulli 样本均值转换为 Binomial

**题型定位**：样本均值概率，先把 `Xbar` 转成样本和。

**解题步骤**：

1. 每个 `Xi ~ Bernoulli(1/2)`。
2. 样本和 `S=X1+...+X10 ~ Bin(10,1/2)`。
3. `Xbar > 3/4` 等价于 `S/10 > 0.75`，即 `S > 7.5`。
4. 因为 S 是整数，所以 `S >= 8`。
5. 概率 `P(S>=8)=P(S=8)+P(S=9)+P(S=10)=0.0547`。

**涉及知识点**：

- Bernoulli sum is Binomial。
- Sample mean to sample sum。
- 离散变量严格不等号转整数边界。

**易错点**：

- `Xbar > 0.75` 不是 `S > 7`，而是 `S >= 8`。

---

## SM21-010 — Geometric 样本和是 Pascal

**题型定位**：多个 geometric random variables 相加。

**解题步骤**：

1. 若 `Xi ~ Geometric(p)` 表示等到第 1 次成功所需试验次数。
2. `X1+...+X10` 表示等到第 10 次成功总共用了多少次试验。
3. 所以样本和服从 Pascal / Negative Binomial，参数 `r=10, p=1/2`。
4. `Xbar <= 1.5` 等价于 `S <= 15`。
5. Pascal PMF：`P(S=x)=C(x-1, r-1) p^r (1-p)^(x-r)`。
6. 当 `p=1/2` 时，也可写成 `C(x-1,9) (1/2)^x`。
7. 求和 `x=10` 到 `15`，得到 `309/2048≈0.15`。

**涉及知识点**：

- Geometric 的定义：等待一次成功的试验次数。
- Pascal / Negative Binomial：等待第 r 次成功的总试验次数。
- 样本均值转样本和。

**易错点**：

- 不要把 10 个 geometric 的和误认为 binomial。

---

## SM21-011 — Normal Distribution: 规格范围、超过目标值、中心区间

**题型定位**：单个正态变量标准化。

**解题步骤**：

设厚度 `T ~ N(8.1, 0.1^2)`。

**i) 在规格 7.9 到 8.2 内：**

1. 标准化：`Z=(T-8.1)/0.1`。
2. `7.9` 对应 `z=-2`，`8.2` 对应 `z=1`。
3. `P(7.9<=T<=8.2)=P(-2<=Z<=1)=0.4772+0.3413=0.8185`。

**ii) 超过 target 8.0：**

1. `8.0` 对应 `z=-1`。
2. `P(T>=8)=P(Z>=-1)=0.8413`。

**iii) 找 L 使 90% 在 `8.1±L` 内：**

1. 中间 90% 意味着两边各 5%。
2. 查 `z_0.95=1.645`。
3. `L = 1.645 * 0.1 = 0.1645`。

**涉及知识点**：

- Normal standardization。
- 对称性查表。
- 中心置信/覆盖区间：middle 90% 对应 `z_0.95`。

**易错点**：

- target 是 8.0，但分布均值是 8.1；标准化要减均值 8.1。

---

## SM21-012 — Continuous PDF Normalization and Transformation: Y=X^2

**题型定位**：连续 PDF 归一化、积分求 CDF、非单调变换。

**解题步骤**：

**i) 求 c：**

1. PDF 必须满足积分为 1。
2. `fX(x)=c/(e^-x+e^x)`。
3. 用代换 `y=e^x`，积分变为 `c * integral_0^infty 1/(1+y^2) dy = c*pi/2`。
4. 所以 `c=2/pi`。

**ii) 求 `P(X<=1)`：**

1. 积分 `integral_{-infty}^1 fX(x) dx`。
2. 同样用 `y=e^x`，上限变成 `e`。
3. 得 `P(X<=1)=2/pi * arctan(e)`。

**iii) 求 `Y=X^2` 的密度：**

1. `x^2` 不是一一对应，不能只用单根。
2. 对 `y>0`，有 `X=sqrt(y)` 和 `X=-sqrt(y)` 两个来源。
3. 因为原 PDF 是偶函数，所以两边贡献相同。
4. `fY(y)= [fX(sqrt(y))+fX(-sqrt(y))] * 1/(2sqrt(y))`。
5. 化简：`fY(y)= 2/[pi sqrt(y)(e^-sqrt(y)+e^sqrt(y))]`，`y>0`；否则为 0。

**涉及知识点**：

- PDF normalization。
- CDF method for transformation。
- 非单调变换要考虑所有 preimages。

**易错点**：

- `Y=X^2` 的 support 是 `y>=0`。
- 不能漏掉负根 `-sqrt(y)`。

---

## SM21-013 — Maxwell-Boltzmann: LOTUS 和能量变换

**题型定位**：连续随机变量期望、方差、物理量变换。

**解题步骤**：

**i) 求 `E[V]` 和 `Var(V)`：**

1. 用 LOTUS：`E[V]=integral_0^infty v fV(v) dv`。
2. 题目密度中含 `v^2 e^{-a v^2/2}`，乘上 v 后变成 `v^3 e^{-a v^2/2}`。
3. 通过换元或已知 Gaussian 积分，得到 `E[V]=2 sqrt(2kT/(m pi))`。
4. 再算 `E[V^2]=integral v^2 fV(v) dv = 3kT/m`。
5. `Var(V)=E[V^2]-E[V]^2 = (kT/m)(3-8/pi)`。

**ii) 动能 `E = mV^2/2` 的均值：**

1. 直接用线性性：`E[kinetic]=m/2 * E[V^2]`。
2. 得 `3kT/2`。

**iii) 动能密度 `fE`：**

1. 变换 `epsilon = m v^2 / 2`，所以 `v=sqrt(2epsilon/m)`。
2. 因为速度 V 的 support 是 `v>0`，这里只取正根。
3. Jacobian：`dv/depsilon = 1/sqrt(2m epsilon)`。
4. `fE(epsilon)=fV(sqrt(2epsilon/m))*1/sqrt(2m epsilon)`。
5. 化简为 `2/sqrt(pi) * (kT)^(-3/2) * sqrt(epsilon) * e^(-epsilon/(kT))`，`epsilon>0`。

**涉及知识点**：

- LOTUS: `E[g(X)] = integral g(x)fX(x)dx`。
- Variance formula。
- 单调变换的 Jacobian。
- Support: 能量必须大于 0。

**易错点**：

- 第 iii 问不是对整个实数取正负两根，因为 V 本身只在 `v>0` 有密度。

---

## SM21-014 — Correlation Coefficient: 四面骰二阶段随机过程

**题型定位**：离散联合分布 + covariance + correlation。

**解题步骤**：

1. `X=1` 表示第一掷为偶数，`X=0` 表示奇数，所以 `X~Bernoulli(1/2)`。
2. 因此 `E[X]=1/2, Var(X)=1/4`。
3. 列出 Y 的分布：
   - 第一掷为 1 或 3 时直接保留；
   - 第一掷为 2 或 4 时再掷一次并相加。
4. 得到 `P(Y=1)=4/16, P(Y=3)=5/16, P(Y=4)=1/16, P(Y=5)=2/16, P(Y=6)=2/16, P(Y=7)=1/16, P(Y=8)=1/16`。
5. 计算 `E[Y]=15/4`，`E[Y^2]=300/16`，所以 `Var(Y)=75/16`。
6. `XY` 只有在 `X=1` 时等于 Y，因此只统计第一掷为偶数的情况：`E[XY]=44/16`。
7. `Cov(X,Y)=E[XY]-E[X]E[Y]=44/16-(1/2)(15/4)=14/16`。
8. `rho = Cov(X,Y)/sqrt(Var(X)Var(Y)) = 7/(5sqrt(3))`。

**涉及知识点**：

- Correlation coefficient。
- Covariance: `Cov(X,Y)=E[XY]-E[X]E[Y]`。
- 离散随机变量先列 PMF 再求矩。

**易错点**：

- `P(Y=3)` 包含两种来源：第一掷直接是 3，以及第一掷为 2 后第二掷为 1。

---

## SM21-015 — Correlation Coefficient: 两枚 weighted coins

**题型定位**：条件过程下的 Bernoulli 相关性。

**解题步骤**：

1. 第一 toss 用黑币，`P(X=1)=p`，所以 `E[X]=p, Var(X)=p(1-p)`。
2. 第二 toss 的硬币取决于第一 toss：
   - 若 `X=0`，继续用黑币，第二次 head 概率 p；
   - 若 `X=1`，用红币，第二次 head 概率 `1-p`。
3. 用全概率：`P(Y=1)=p(1-p)+(1-p)p=2p(1-p)`。
4. 因为 Y 仍是 Bernoulli，所以 `Var(Y)=q(1-q)`，其中 `q=2p(1-p)`。
5. `XY=1` 只在第一 toss head 且第二 toss head 时发生，概率 `p(1-p)`。
6. `Cov(X,Y)=p(1-p)-p*2p(1-p)=p(1-p)(1-2p)`。
7. 相关系数：`rho=(1-2p)/sqrt(2[(1-p)^2+p^2])`。

**涉及知识点**：

- Conditional probability。
- Law of total probability。
- Bernoulli variance。
- Covariance / correlation。

**易错点**：

- 第二次 head 概率不是固定 p，也不是固定 `1-p`，而要按第一次结果分情况。

---

## SM21-016 — Bivariate PDF: 极坐标、矩、U=X/Y 变换

**题型定位**：二维连续分布，圆盘 support，适合极坐标；最后一问是比值变换。

**解题步骤**：

**i) 求 c：**

1. 在单位圆盘内 `fXY=c(x^2+y^2)`。
2. 用极坐标：`x=r cosθ, y=r sinθ, dxdy=r dr dθ`。
3. 积分为 `integral_0^{2pi} integral_0^1 c r^2 * r dr dθ = c * 2pi * 1/4`。
4. 令其等于 1，得 `c=2/pi`。

**ii) 求 `E[X], E[Y]`：**

- 分布关于 x 轴、y 轴都对称，所以 `E[X]=E[Y]=0`。

**iii) 求方差：**

1. `Var(X)=E[X^2]`。
2. `E[X^2]=(2/pi) integral cos^2θ dθ integral_0^1 r^5 dr`。
3. 用 `integral_0^{2pi} cos^2θ dθ = pi`，得到 `Var(X)=1/3`。
4. 对称性给出 `Var(Y)=1/3`。

**iv) 相关系数：**

1. `E[XY]` 中角度部分含 `cosθ sinθ`，在 `0` 到 `2pi` 积分为 0。
2. 所以 `Cov(X,Y)=0`，`rho=0`。

**v) 求 `U=X/Y` 的密度：**

1. 设 `U=X/Y, V=Y`，则 `X=UV, Y=V`。
2. Jacobian `|d(x,y)/d(u,v)|=|v|`。
3. 原 support 要求 `(uv)^2+v^2 <= 1`，所以 `|v| <= 1/sqrt(1+u^2)`。
4. `fU(u)=integral fXY(uv,v)|v| dv`。
5. 计算后得到 `fU(u)=1/[pi(1+u^2)]`，`u` 属于全体实数。

**涉及知识点**：

- Polar coordinates。
- Symmetry arguments。
- Joint transformation + Jacobian。
- 比值分布通常令 `U=X/Y, V=Y`。

**易错点**：

- 极坐标积分不要漏 Jacobian `r`。
- `rho=0` 不代表 X,Y 独立；这里只说明不相关。

---

## SM21-017 — Random Parameter Exponential: 条件密度混合

**题型定位**：层级模型 / mixture distribution。先给 X，再给 `Z|X=x`。

**解题步骤**：

1. `X ~ Uniform(1,2)`，所以 `fX(x)=1` for `1<x<2`。
2. 条件密度：`fZ|X(z|x)=x e^{-xz}`，`z>0`。
3. 联合密度：`fXZ(x,z)=fZ|X(z|x)fX(x)=x e^{-xz}`，其中 `1<x<2, z>0`。
4. 对 x 积分得到边缘密度：`fZ(z)=integral_1^2 x e^{-xz} dx`。
5. 积分结果：`fZ(z)=(e^-z - 2e^-2z)/z + (e^-z - e^-2z)/z^2`，`z>0`。
6. 求期望可以用条件期望更快：`E[Z]=E[E(Z|X)]`。
7. 对指数分布 `E[Z|X=x]=1/x`。
8. 所以 `E[Z]=integral_1^2 1/x dx = ln 2`。

**涉及知识点**：

- Conditional density。
- Joint density = conditional density * marginal density。
- Marginalization。
- Law of total expectation。

**易错点**：

- 指数分布参数这里是 rate `x`，均值是 `1/x`，不是 x。

---

## SM21-018 — Reliability: A 串联两个 B 的并联系统

**题型定位**：可靠性系统。A 必须工作；两个 B 至少一个工作。

**解题步骤**：

1. 对指数寿命，若密度 `f(t)=1/beta e^{-t/beta}`，可靠度 `R(t)=P(T>t)=e^{-t/beta}`。
2. 所以 `RA(t)=e^{-t/100}`，`RB(t)=e^{-t/50}`。
3. 两个 B 是并联系统，至少一个工作：
   - 失败概率是两个都失败：`(1-RB)^2`；
   - 可靠度 `R_B_parallel=1-(1-RB)^2=2e^{-t/50}-e^{-t/25}`。
4. A 与 B 子系统串联，所以总可靠度相乘：`R(t)=RA(t)R_B_parallel(t)=2e^{-3t/100}-e^{-t/20}`。
5. 单个组件期望寿命：指数分布 scale 分别是 `100` 和 `50`。
6. 系统期望寿命可用 `E[T]=integral_0^infty R(t)dt`。
7. `E[T]=2*(100/3)-20=140/3≈46.67`。

**涉及知识点**：

- Reliability function `R(t)=P(T>t)`。
- Series system: reliabilities multiply。
- Parallel system: use complement of all fail。
- Nonnegative random variable: `E[T]=integral_0^infty R(t)dt`。

**易错点**：

- 两个 B 不是串联；系统说 “both B fail” 才会让 B 子系统失败，说明 B 是并联冗余。

---

## SM21-019 — Reliability: Weibull A 与 B-C 串联系统并联

**题型定位**：可靠性系统 + Weibull-like component + survival integral。

**解题步骤**：

**i) 单个组件可靠度：**

1. `RA(t)=1-integral_0^t (s/50)e^{-s^2/100} ds = e^{-t^2/100}`。
2. `RB(t)=e^{-t/40}`。
3. `RC(t)=e^{-t/25}`。

**ii) 系统可靠度：**

1. B 与 C 串联，所以 `RBC(t)=RB(t)RC(t)=e^{-13t/200}`。
2. 整体是 A 与 BC 子系统并联，所以系统失败等价于 A 失败且 BC 失败。
3. `R(t)=1-(1-RA)(1-RBC)`。
4. 展开得 `R(t)=e^{-13t/200}+e^{-t^2/100}-e^{-(2t^2+13t)/200}`。

**iii) 组件期望寿命：**

1. 对非负寿命，`E[T]=integral_0^infty R(t)dt`。
2. `E[A]=integral_0^infty e^{-t^2/100}dt=5sqrt(pi)`。
3. 指数分布 B、C 的期望分别为 `40`、`25`。

**iv) 系统期望寿命：**

1. 使用 `E[T_system]=integral_0^infty R(t)dt`。
2. 分三项积分：`integral e^{-13t/200}`, `integral e^{-t^2/100}`, `integral e^{-(2t^2+13t)/200}`。
3. 第三项需要配方并查标准正态表。
4. 最终约 `17.89`。

**涉及知识点**：

- Survival function。
- Series / parallel reliability composition。
- Weibull / Rayleigh 型密度。
- Completing the square。

**易错点**：

- 不要直接把密度相乘；系统组合一般先组合可靠度或失败概率。

---

## SM21-020 — Method of Moments: Pareto-like 分布估计 θ

**题型定位**：矩估计。先用理论均值表达参数，再用样本均值替换。

**解题步骤**：

1. 密度为 `fθ(x)=(θ+1)/x^{θ+2}`，`x>1`。
2. 计算理论均值：`E[X]=integral_1^infty x*(θ+1)x^{-θ-2} dx`。
3. 化简为 `(θ+1) integral_1^infty x^{-θ-1} dx = (θ+1)/θ = 1+1/θ`。
4. 解出 `θ=1/(E[X]-1)`。
5. 用样本均值 `Xbar` 替代 `E[X]`。
6. Method-of-moments estimator: `θhat=1/(Xbar-1)`。

**涉及知识点**：

- Method of moments。
- Heavy-tail / Pareto-like density。
- 用样本矩替代理论矩。

**易错点**：

- 估计量是随机变量，要写 `Xbar`，不是某个固定 x。

---

## SM21-021 — Uniform(0,θ): MOM 与 MLE

**题型定位**：经典参数估计题。均匀分布上界 θ 的 MOM 和 MLE 不同。

**解题步骤**：

**i) Method of Moments：**

1. 若 `X ~ Uniform(0,θ)`，则 `E[X]=θ/2`。
2. 解得 `θ=2E[X]`。
3. 用样本均值替代：`θhat_MOM=2Xbar`。

**ii) Maximum Likelihood：**

1. 样本联合似然：`L(θ)=1/θ^n`，前提是所有样本都落在 `[0,θ]`。
2. 这个前提等价于 `θ >= max Xi`。
3. 在可行范围内，`1/θ^n` 随 θ 增大而减小。
4. 所以最大值在最小可行 θ 处取得：`θhat_MLE=max Xi`。

**涉及知识点**：

- Method of moments。
- Maximum likelihood estimator。
- 参数影响 support 时，MLE 常在边界取得。

**易错点**：

- 对 Uniform(0,θ)，不能只对 log-likelihood 求导，因为 θ 同时决定 support。

---

## SM21-022 — Exponential MLE with Right Censoring

**题型定位**：寿命试验右删失 censored data 的 MLE。

**解题步骤**：

1. 寿命 `T ~ Exponential(scale β)`，密度 `f(t)=1/β e^{-t/β}`。
2. 有 m 个硬盘在停止时间 T 之前失效，失效时间为 `T1,...,Tm`。
3. 另外 `n-m` 个硬盘到停止时间 T 还没坏，只知道寿命大于 T。
4. 对已坏样本，用密度贡献 `f(Ti)`。
5. 对未坏样本，用 survival 贡献 `P(T>T_stop)=e^{-T_stop/β}`。
6. 所以似然：`L(β)=β^{-m} exp[-(T1+...+Tm+(n-m)T_stop)/β]`。
7. 取 log：`ell(β)=-m lnβ - A/β`，其中 `A=sum Ti+(n-m)T_stop`。
8. 求导并令 0：`-m/β + A/β^2=0`。
9. 得 `βhat=A/m`。

**涉及知识点**：

- Right censoring。
- Likelihood = failed density * censored survival。
- Exponential scale parameter MLE。

**易错点**：

- 未坏的硬盘不能丢掉，它们贡献的是 `P(T>T_stop)`。
- 如果 m=0，通常没有有限 MLE；题目默认有失效样本。

---

## SM21-023 — MLE: Rayleigh-like density 参数 θ

**题型定位**：连续分布 MLE，参数既在分母也在指数里。

**解题步骤**：

1. 密度：`fθ(x)=x/θ * exp(-x^2/(2θ))`，`x>0`。
2. 对样本 `x1,...,xn`，似然：`L(θ)=prod xi * θ^{-n} * exp[-sum xi^2/(2θ)]`。
3. 取 log：`ell(θ)=sum ln xi - n lnθ - (1/(2θ))sum xi^2`。
4. 对 θ 求导：`ell'(θ)=-n/θ + (sum xi^2)/(2θ^2)`。
5. 令导数为 0：`θhat = (1/(2n)) sum xi^2`。

**涉及知识点**：

- Maximum likelihood。
- Log-likelihood。
- Rayleigh-like distribution。

**易错点**：

- 求导时 `-sum xi^2/(2θ)` 对 θ 的导数是 `+sum xi^2/(2θ^2)`。

---

## SM21-024 — Quartiles, IQR, Freedman-Diaconis Histogram

**题型定位**：数据可视化和正态性直观判断。

**解题步骤**：

1. 先排序 36 个数据。
2. 四分位数：`q1=4.85, q2=6.4, q3=8.05`。
3. IQR：`q3-q1=3.2`。
4. Freedman-Diaconis bin width：`h=2*IQR/n^(1/3)`。
5. `n=36`，所以 `h≈1.94`，可取 1.9 或 2。
6. 若用宽度 2、从 2.5 开始的 bins，可得到大致 counts：
   - `[2.5,4.5)`: 6
   - `[4.5,6.5)`: 12
   - `[6.5,8.5)`: 11
   - `[8.5,10.5)`: 6
   - `[10.5,12.5)`: 1
7. 图形大致单峰、不强烈偏斜，因此没有明显证据反对正态分布。

**涉及知识点**：

- Quartiles。
- Interquartile range。
- Freedman-Diaconis rule。
- Histogram shape interpretation。

**易错点**：

- 画 histogram 时边界不要刚好卡在数据点上，否则归 bin 会不清楚。

---

## SM21-025 — Boxplot: 四分位数、fences、正态性判断

**题型定位**：箱线图和 outlier 判断。

**解题步骤**：

1. 四分位数同上一题：`q1=4.85, q2=6.4, q3=8.05`。
2. IQR：`3.2`。
3. 下 fence：`q1-1.5IQR=4.85-4.8=0.05`。
4. 上 fence：`q3+1.5IQR=8.05+4.8=12.85`。
5. 最小值 3.0，大于下 fence；最大值 12.2，小于上 fence，所以没有 outlier。
6. 箱线图五数概括：min=3.0, q1=4.85, median=6.4, q3=8.05, max=12.2。
7. whiskers 有一定不对称，但中位数不太偏，没有明显 outlier，因此没有强证据反对正态。

**涉及知识点**：

- Box-and-whisker plot。
- IQR fences: `q1-1.5IQR`, `q3+1.5IQR`。
- Outlier rule。

**易错点**：

- fence 不是 whisker 本身；whisker 画到 fence 内的最小/最大观测值。

---

## SM21-026 — Confidence Interval for Variance

**题型定位**：正态总体方差的双侧置信区间，用 chi-square 分布。

**解题步骤**：

1. 样本量 `n=34`，自由度 `df=n-1=33`。
2. 样本方差 `s^2=2.778`。
3. 对正态总体，有 `(n-1)S^2/sigma^2 ~ chi-square(df)`。
4. 双侧 90% CI，显著性 `alpha=0.10`，两端各 `0.05`。
5. 查表：`chi2_0.95,33≈47.4`，`chi2_0.05,33≈20.9`。
6. 方差区间：`[(n-1)s^2/chi2_0.95, (n-1)s^2/chi2_0.05]`。
7. 代入得 `[1.93, 4.39]`。

**涉及知识点**：

- Variance CI for normal population。
- Chi-square distribution。
- 自由度 `n-1`。

**易错点**：

- 分母上下分位点方向容易反：下界用大的 chi-square 分位点，上界用小的 chi-square 分位点。

---

## SM21-027 — Confidence Interval for Mean

**题型定位**：总体方差未知、样本来自正态分布，均值双侧 t 区间。

**解题步骤**：

1. 样本量 `n=34`，自由度 `df=33`。
2. 样本均值 `xbar=6.98`。
3. 样本方差 `s^2=2.778`，所以 `s≈1.67`。
4. 双侧 95% CI，查 `t_0.025,33≈2.0345`。
5. 区间：`xbar ± t * s/sqrt(n)`。
6. 误差项约 `2.0345*1.67/sqrt(34)≈0.58`。
7. 所以 `mu` 的区间为 `6.98 ± 0.58`，即约 `[6.40, 7.56]`。

**涉及知识点**：

- t confidence interval for mean。
- Unknown variance -> use sample standard deviation s。
- Degrees of freedom `n-1`。

**易错点**：

- 方差未知时用 t，不用 z。
- CI for mean 用 `s/sqrt(n)`，不是直接用 s。

<!-- AUTO-MIDTERM-SUPPLEMENT-INSERT-BEFORE -->

<!-- AUTO-MIDTERM-SUPPLEMENT-ZONE-END -->
