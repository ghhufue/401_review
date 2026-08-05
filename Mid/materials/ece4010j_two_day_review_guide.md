# ECE4010J 两天复习路线指南

> 这个文件是复习计划归档。实际考试速查请看根目录 `cheating_sheet.md`。

---

## 0. 总目标

两天速成不追求完整理解概率论，而是追求：

1. 看题识别题型。
2. 知道该查 cheating sheet 哪一节。
3. 知道该用哪个模板。
4. 能把文字条件翻译成概率事件。
5. 能确定积分区域 / support。
6. 能完成常见大题流程。

---

## Day 1：分布 + 一维随机变量 + 变换

| 时间 | 内容 | 目标 |
|---|---|---|
| 09:00-10:00 | PMF / PDF / CDF / E / Var / LOTUS | 建立随机变量基础 |
| 10:00-12:00 | 常见分布识别 | 看到题知道用什么分布 |
| 12:00-13:00 | 午饭 + 整理分布表 | 完成分布速查表 |
| 13:00-14:30 | Binomial / Poisson / Normal Approximation | 会做近似题 |
| 14:30-16:30 | Random Variable Transformation | 会做 max/min/g(X)/Jacobian |
| 17:00-19:00 | Poisson Process + Exponential | 会处理计数过程和等待时间 |
| 20:00-22:30 | Day 1 题型训练 + 整理模板 | 每类题整理一个模板 |

### Day 1 必须掌握

- PMF / PDF / CDF 区分。
- 离散求和、连续积分。
- Distribution recognition。
- Binomial exact / Poisson approximation / Normal approximation。
- Continuity correction。
- CDF method。
- Max / Min transformation。
- Jacobian transformation。
- Poisson process 与 Exponential waiting time。

---

## Day 2：联合分布 + 条件期望 + Reliability

| 时间 | 内容 | 目标 |
|---|---|---|
| 09:00-10:30 | Joint Distribution 基础 | 会 marginal / conditional / independence |
| 10:30-12:30 | Joint Density 大题模板 | 练完整流程题 |
| 12:30-13:30 | 午饭 + 整理 joint 模板 | 完成联合分布页 |
| 13:30-15:00 | Covariance / Correlation / Independence | 会判断独立、相关、不相关 |
| 15:00-17:00 | Conditional Expectation | 会算 E[X|Y] 和 total expectation |
| 17:30-19:30 | Reliability / Hazard / Weibull | 会做寿命和系统可靠性题 |
| 20:30-21:30 | MGF 快速掌握 | 会查 MGF、乘 MGF、识别分布 |
| 21:30-23:00 | 最终整理 + 模板复盘 | 完成最终 cheating sheet |

### Day 2 必须掌握

- Joint pdf / pmf。
- Marginal distribution。
- Conditional density。
- Conditional expectation。
- Total expectation / total variance。
- Independence 判断。
- Covariance / correlation。
- Reliability \(R(t)=P(T>t)\)。
- Hazard rate \(h(t)=f(t)/R(t)\)。
- Series / parallel system。
- Weibull hazard shape。
- MGF moment extraction and independent sums。

---

## 最低完成标准

时间不够时，至少完成根目录 `cheating_sheet.md` 中这些内容：

```text
1. Distribution Recognition Table
2. Common Distributions Formula Table
3. Normal approximation + continuity correction
4. CDF method / max / min / Jacobian
5. Joint density complete workflow
6. Conditional expectation template
7. Reliability / hazard / series / parallel
8. MGF independent sum
9. Common traps
```

---

## 自测清单

### 分布识别

- [ ] 我能区分 Binomial / Geometric / Negative Binomial。
- [ ] 我能区分 Binomial / Hypergeometric。
- [ ] 我知道 Poisson 什么时候用。
- [ ] 我知道 Exponential 是等待时间。
- [ ] 我知道 Gamma 是多个 Exponential 等待时间之和。
- [ ] 我知道 Weibull 用于 reliability。

### 变换

- [ ] 我会用 CDF method。
- [ ] 我会做 \(Y=\max(X_1,X_2)\)。
- [ ] 我会做 \(Y=\min(X_1,X_2)\)。
- [ ] 我知道非单调函数不能随便用反函数公式。
- [ ] 我知道二维变换要用 Jacobian。
- [ ] 我会先找 support。

### 联合分布

- [ ] 我会从 joint pdf 求 marginal。
- [ ] 我会从 joint pdf 求 conditional pdf。
- [ ] 我会求 \(E[X|Y=y]\)。
- [ ] 我知道 \(E[X|Y]\) 是随机变量。
- [ ] 我会用 total expectation。
- [ ] 我会判断 independence。

### 可靠性

- [ ] 我知道 \(R(t)=P(T>t)\)。
- [ ] 我知道 hazard rate 是 \(f(t)/R(t)\)。
- [ ] 我会做 series system。
- [ ] 我会做 parallel system。
- [ ] 我会把 still working / failed by 翻译成条件概率。
- [ ] 我知道 Weibull 的 hazard 由 \(eta\) 决定。

### MGF / 近似

- [ ] 我知道 MGF 定义。
- [ ] 我知道独立和的 MGF 相乘。
- [ ] 我会用 normal approximation。
- [ ] 我会 continuity correction。
- [ ] 我知道 CLT 的基本用途。