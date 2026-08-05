# Bayes Theorem / 贝叶斯公式专题

> 位置：`docs/supplements/`  
> 用途：作为 `cheating_sheet.md` 之外的详细知识补充，专门整理条件概率、贝叶斯公式、全概率公式和常见考试题型。

---

## 0. 这一章解决什么问题？

贝叶斯题最常见的困难不是公式本身，而是 **条件概率方向反了**。

题目经常给你：

\[
P(B\mid A)
\]

但真正要求：

\[
P(A\mid B)
\]

这时就要用 Bayes theorem。

---

## 1. 条件概率基础

### 1.1 条件概率定义

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0
\]

含义：

```text
在 B 已经发生的前提下，A 发生的概率。
```

也可以理解成：

```text
样本空间从全集缩小到 B，问 B 里面有多少同时属于 A。
```

---

### 1.2 乘法公式

由条件概率定义可得：

\[
P(A\cap B)=P(A\mid B)P(B)
\]

也可以写成：

\[
P(A\cap B)=P(B\mid A)P(A)
\]

因此：

\[
P(A\mid B)P(B)=P(B\mid A)P(A)
\]

这就是 Bayes 公式的来源。

---

## 2. Bayes Theorem 标准形式

\[
\boxed{P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}}
\]

其中：

| 符号 | 中文含义 | 常见英文 |
|---|---|---|
| \(P(A)\) | A 原本发生的概率 | prior probability |
| \(P(B\mid A)\) | A 发生时看到证据 B 的概率 | likelihood |
| \(P(B)\) | 证据 B 出现的总概率 | evidence / normalizing constant |
| \(P(A\mid B)\) | 看到 B 之后 A 的概率 | posterior probability |

一句话：

```text
贝叶斯 = 用观测到的证据 B，反推原因 A 的概率。
```

---

## 3. 分母 P(B) 怎么算？全概率公式

很多题最容易卡在分母。

如果 \(A_1,A_2,\ldots,A_n\) 构成一个 partition，也就是：

1. 它们互斥；
2. 它们加起来覆盖所有可能情况；
3. 每个 \(P(A_i)>0\)。

那么：

\[
P(B)=\sum_i P(B\mid A_i)P(A_i)
\]

所以 Bayes 公式常写成：

\[
\boxed{
P(A_k\mid B)=
\frac{P(B\mid A_k)P(A_k)}
{\sum_i P(B\mid A_i)P(A_i)}
}
\]

---

## 4. 二分类 Bayes 模板

如果只有两种情况：

\[
A,\quad A^c
\]

题目给了证据 \(B\)，要求：

\[
P(A\mid B)
\]

那么直接套：

\[
\boxed{
P(A\mid B)=
\frac{P(B\mid A)P(A)}
{P(B\mid A)P(A)+P(B\mid A^c)P(A^c)}
}
\]

### 做题步骤

```text
Step 1: 定义原因 A 和证据 B
Step 2: 写 prior: P(A), P(A^c)
Step 3: 写 likelihood: P(B|A), P(B|A^c)
Step 4: 分子 = P(B|A)P(A)
Step 5: 分母 = 所有可能原因产生证据 B 的总概率
Step 6: 分子 / 分母
```

---

## 5. 多分类 Bayes 模板

如果可能原因有多个，例如：

\[
A_1,A_2,A_3
\]

证据是 \(B\)，要求：

\[
P(A_2\mid B)
\]

那么：

\[
P(A_2\mid B)=
\frac{P(B\mid A_2)P(A_2)}
{P(B\mid A_1)P(A_1)+P(B\mid A_2)P(A_2)+P(B\mid A_3)P(A_3)}
\]

### 常见场景

```text
Factory A/B/C produces widgets.
A disease may come from different populations.
A signal may come from different sources.
A selected item may come from different boxes.
```

---

## 6. 题型识别关键词

看到下面表达，优先想到 Bayes：

```text
Given that ...
Suppose we know that ...
Of those that fail, ...
Among defective items, ...
Given a positive test result, what is the probability ...
A test failed to yield 0, what is the probability the RNG is defective?
What percentage of widgets from factory A fail tolerance?
```

中文翻译：

```text
已知某件事发生了
在失败产品中...
在检测阳性的人中...
看到某个测试结果后，反推原因概率
题目给的是 P(结果 | 原因)，问 P(原因 | 结果)
```

---

## 7. 经典例题 1：工厂缺陷率反推

### 题型

三个工厂 A, B, C 生产产品。题目给：

\[
P(A),P(B),P(C)
\]

以及：

\[
P(A\mid fail),P(B\mid fail),P(C\mid fail)
\]

要求：

\[
P(fail\mid A),P(fail\mid B),P(fail\mid C)
\]

这就是反向条件概率。

---

### 已知量

\[
P(A)=0.20,\quad P(B)=0.45,\quad P(C)=0.35
\]

\[
P(fail)=0.05
\]

\[
P(A\mid fail)=0.25,\quad P(B\mid fail)=0.35,\quad P(C\mid fail)=0.40
\]

---

### 要求

\[
P(fail\mid A)
\]

用 Bayes 变形：

\[
P(fail\mid A)=\frac{P(A\mid fail)P(fail)}{P(A)}
\]

代入：

\[
P(fail\mid A)=\frac{0.25\cdot 0.05}{0.20}=0.0625
\]

所以 A 工厂产品失败率是：

\[
6.25\%
\]

同理：

\[
P(fail\mid B)=\frac{0.35\cdot 0.05}{0.45}\approx 0.039
\]

\[
P(fail\mid C)=\frac{0.40\cdot 0.05}{0.35}\approx 0.057
\]

---

### 易错点

```text
P(A | fail) 不是 A 工厂的失败率。
```

- \(P(A\mid fail)\)：失败产品中有多少来自 A；
- \(P(fail\mid A)\)：A 工厂生产的产品中有多少失败。

二者方向不同。

---

## 8. 经典例题 2：RNG 没有出现 0，反推是否 defective

### 题型

某个随机数生成器可能是 defective。

- defective 的概率：\(P(D)=0.2\)
- not defective 的概率：\(P(D^c)=0.8\)

defective 时不会生成 0。

一次测试生成 20 个数字，结果没有出现 0。问它 defective 的概率。

---

### 定义事件

令：

\[
D=\text{RNG is defective}
\]

\[
R=\text{20 tests produced no 0}
\]

要求：

\[
P(D\mid R)
\]

---

### 写出已知概率

如果 defective，它永远不会生成 0：

\[
P(R\mid D)=1
\]

如果 not defective，每次没有 0 的概率是 \(0.9\)，20 次都没有 0：

\[
P(R\mid D^c)=0.9^{20}=0.1216
\]

---

### 套二分类 Bayes

\[
P(D\mid R)=
\frac{P(R\mid D)P(D)}
{P(R\mid D)P(D)+P(R\mid D^c)P(D^c)}
\]

代入：

\[
P(D\mid R)=
\frac{1\cdot 0.2}{1\cdot 0.2+0.1216\cdot 0.8}
\]

\[
P(D\mid R)=0.6728
\]

---

### 直觉解释

20 次都没出现 0，会增强“它坏了”的可能性。

但是概率不是 1，因为正常 RNG 也有可能偶然 20 次都没出现 0。

---

## 9. 经典例题 3：疾病检测 / False Positive

这是最经典的 Bayes 题。

### 场景

- 疾病发生率：\(P(D)=0.01\)
- 没病概率：\(P(D^c)=0.99\)
- 有病时检测阳性：\(P(+\mid D)=0.99\)
- 没病时误报阳性：\(P(+\mid D^c)=0.05\)

问：

\[
P(D\mid +)
\]

---

### 套公式

\[
P(D\mid +)=
\frac{P(+\mid D)P(D)}
{P(+\mid D)P(D)+P(+\mid D^c)P(D^c)}
\]

代入：

\[
P(D\mid +)=
\frac{0.99\cdot 0.01}
{0.99\cdot 0.01+0.05\cdot 0.99}
\]

\[
P(D\mid +)=\frac{0.0099}{0.0099+0.0495}=\frac{0.0099}{0.0594}=0.1667
\]

所以即使检测阳性，真的有病的概率也只有约：

\[
16.67\%
\]

---

### 为什么这么低？

因为 base rate 很低：

\[
P(D)=0.01
\]

没病的人太多，哪怕误报率只有 \(5\%\)，误报的人数也可能很多。

---

## 10. Bayes 和 Independent 的关系

如果 \(A\) 和 \(B\) 独立，那么：

\[
P(A\mid B)=P(A)
\]

也就是知道 \(B\) 发生不会改变 \(A\) 的概率。

此时 Bayes 公式仍然成立：

\[
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
\]

因为独立时：

\[
P(B\mid A)=P(B)
\]

所以：

\[
P(A\mid B)=\frac{P(B)P(A)}{P(B)}=P(A)
\]

---

## 11. Bayes 和全概率的考试流程图

```text
题目问 P(原因 | 结果) 吗？
        |
        v
题目给 P(结果 | 原因) 吗？
        |
        v
用 Bayes
        |
        v
分子 = 当前原因产生该结果的概率
        |
        v
分母 = 所有可能原因产生该结果的概率总和
```

更具体：

```text
1. 先定义原因：A1, A2, ..., An
2. 定义证据：B
3. 写出每个 prior: P(Ai)
4. 写出每个 likelihood: P(B | Ai)
5. 目标如果是 P(Ak | B)：

   P(Ak | B) = P(B | Ak)P(Ak) / Σ P(B | Ai)P(Ai)
```

---

## 12. 常见英文表达对照

| English | 中文含义 | 概率形式 |
|---|---|---|
| given that B occurred | 已知 B 发生 | conditional probability |
| among those that failed | 在失败的里面 | \(P(\cdot\mid fail)\) |
| of those that test positive | 在检测阳性的里面 | \(P(\cdot\mid +)\) |
| false positive | 假阳性 | \(P(+\mid D^c)\) |
| false negative | 假阴性 | \(P(-\mid D)\) |
| sensitivity | 灵敏度 | \(P(+\mid D)\) |
| specificity | 特异度 | \(P(-\mid D^c)\) |
| prior | 先验概率 | \(P(A)\) |
| posterior | 后验概率 | \(P(A\mid B)\) |
| likelihood | 似然 | \(P(B\mid A)\) |
| evidence | 证据总概率 | \(P(B)\) |

---

## 13. 常见陷阱

### 陷阱 1：把 \(P(A\mid B)\) 和 \(P(B\mid A)\) 混淆

\[
P(A\mid B)\neq P(B\mid A)
\]

通常完全不是一个意思。

例子：

```text
P(来自 A 工厂 | 产品失败)
```

和：

```text
P(产品失败 | 来自 A 工厂)
```

不是同一个概率。

---

### 陷阱 2：分母只写一个情况

Bayes 的分母必须是：

\[
P(B)
\]

也就是证据 B 出现的总概率。

二分类时：

\[
P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)
\]

不要只写：

\[
P(B\mid A)P(A)
\]

那只是分子。

---

### 陷阱 3：忽略 base rate

即使检测很准，如果事件本身非常稀有，看到阳性之后的后验概率也可能不高。

这类题常考：

```text
rare disease + false positive
```

---

### 陷阱 4：把 percent of failed items 和 failure rate 混淆

```text
25% of failed widgets were from A
```

表示：

\[
P(A\mid fail)=0.25
\]

不是：

\[
P(fail\mid A)=0.25
\]

---

### 陷阱 5：没有检查 partition

用全概率公式时，\(A_i\) 必须覆盖所有可能原因，并且彼此互斥。

例如工厂 A/B/C 题中：

\[
A,B,C
\]

必须满足：

\[
P(A)+P(B)+P(C)=1
\]

---

## 14. 最短背诵版

```text
Bayes 用法：
题目给 P(结果 | 原因)，问 P(原因 | 结果)

公式：
P(A | B) = P(B | A)P(A) / P(B)

分母：
P(B) = 所有原因产生 B 的概率总和

二分类：
P(A | B)
= P(B | A)P(A)
  / [P(B | A)P(A) + P(B | A^c)P(A^c)]

核心直觉：
posterior = likelihood × prior / evidence
```

---

## 15. 一句话总结

\[
\boxed{
\text{Bayes theorem 是用“结果出现了”去反推“哪个原因更可能”。}
}
\]
