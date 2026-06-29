# 概率统计常用积分公式

> 位置：`docs/supplements/`  
> 用途：作为 `cheating_sheet.md` 之外的积分公式补充，专门服务于 VE401 / 401 概率统计题。  
> 重点：PDF 归一化、CDF、期望方差、连续变量变换、卷积、可靠性、正态近似、Gamma / Exponential / Weibull / Maxwell-Boltzmann 等题型。

---

## 0. 使用方法

做概率统计题时，积分通常出现在这些地方：

| 场景 | 你在算什么 | 常见积分 |
|---|---|---|
| PDF normalization | 求常数 \(c\) | \(\int f(x)dx=1\) |
| Probability / CDF | 求区间概率 | \(P(a<X<b)=\int_a^b f(x)dx\) |
| Expectation | 求均值 | \(E[X]=\int x f(x)dx\) |
| Variance | 求方差 | \(E[X^2]-E[X]^2\) |
| LOTUS | 求 \(E[g(X)]\) | \(\int g(x)f(x)dx\) |
| Transformation | 求新密度 | CDF method / Jacobian |
| Reliability | 求寿命、可靠度 | \(R(t)=P(T>t)\), \(E[T]=\int_0^\infty R(t)dt\) |
| Normal Approximation | 查正态表 | 标准化后查表，通常不手算原函数 |

---

## 1. 最基础的不定积分

### 1.1 幂函数积分

若 \(n\neq -1\)：

\[
\int x^n dx=\frac{x^{n+1}}{n+1}+C
\]

特殊情况：

\[
\int \frac{1}{x}dx=\ln|x|+C
\]

### 常见用法

Uniform、Pareto-like density、method of moments 经常出现：

\[
\int_1^\infty x^{-\alpha}dx
\]

若 \(\alpha>1\)：

\[
\int_1^\infty x^{-\alpha}dx=\frac{1}{\alpha-1}
\]

---

### 1.2 指数函数积分

若 \(a>0\)：

\[
\int e^{-ax}dx=-\frac{1}{a}e^{-ax}+C
\]

因此：

\[
\int_0^\infty e^{-ax}dx=\frac{1}{a}
\]

区间版本：

\[
\int_s^t ae^{-ax}dx=e^{-as}-e^{-at}
\]

### 常见用法

Exponential CDF：

\[
F(t)=\int_0^t \lambda e^{-\lambda x}dx=1-e^{-\lambda t}
\]

Reliability：

\[
R(t)=P(T>t)=e^{-\lambda t}
\]

---

## 2. Exponential / Gamma 型积分

这类积分在 exponential waiting time、reliability、Gamma distribution、MGF 里非常常见。

---

### 2.1 \(x e^{-ax}\) 积分

若 \(a>0\)：

\[
\int_0^\infty x e^{-ax}dx=\frac{1}{a^2}
\]

更一般地：

\[
\int_0^T x e^{-ax}dx=rac{1}{a^2}\left(1-e^{-aT}(1+aT)\right)
\]

### 推导提示

用 integration by parts：

\[
\int x e^{-ax}dx
= -\frac{x}{a}e^{-ax}-\frac{1}{a^2}e^{-ax}+C
\]

---

### 2.2 \(x^n e^{-ax}\) 积分

若 \(a>0\)，\(n=0,1,2,\ldots\)：

\[
\int_0^\infty x^n e^{-ax}dx=\frac{n!}{a^{n+1}}
\]

常用值：

| Integral | Value |
|---|---|
| \(\int_0^\infty e^{-ax}dx\) | \(1/a\) |
| \(\int_0^\infty x e^{-ax}dx\) | \(1/a^2\) |
| \(\int_0^\infty x^2 e^{-ax}dx\) | \(2/a^3\) |
| \(\int_0^\infty x^3 e^{-ax}dx\) | \(6/a^4\) |

### 常见用法

如果：

\[
X\sim \operatorname{Exp}(\lambda)
\]

则：

\[
E[X]=\int_0^\infty x\lambda e^{-\lambda x}dx=\lambda\cdot \frac{1}{\lambda^2}=\frac{1}{\lambda}
\]

\[
E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}dx=\lambda\cdot \frac{2}{\lambda^3}=\frac{2}{\lambda^2}
\]

所以：

\[
\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac{1}{\lambda^2}=\frac{1}{\lambda^2}
\]

---

### 2.3 Gamma function 版本

更一般地，若 \(a>0\)，\(p>0\)：

\[
\int_0^\infty x^{p-1}e^{-ax}dx=\frac{\Gamma(p)}{a^p}
\]

其中：

\[
\Gamma(n)=(n-1)!\quad \text{for integer } n
\]

常用半整数：

\[
\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}
\]

\[
\Gamma\left(\frac{3}{2}\right)=\frac{1}{2}\sqrt{\pi}
\]

\[
\Gamma\left(\frac{5}{2}\right)=\frac{3}{4}\sqrt{\pi}
\]

---

## 3. Weibull / Rayleigh 型积分

可靠性和 Maxwell-Boltzmann 题里常见：

\[
x e^{-a x^2}
\]

---

### 3.1 \(x e^{-a x^2}\) 积分

若 \(a>0\)：

\[
\int x e^{-a x^2}dx=-\frac{1}{2a}e^{-a x^2}+C
\]

因此：

\[
\int_0^T x e^{-a x^2}dx=\frac{1}{2a}\left(1-e^{-aT^2}\right)
\]

\[
\int_0^\infty x e^{-a x^2}dx=\frac{1}{2a}
\]

### 常见用法

若密度形如：

\[
f(t)=\frac{t}{50}e^{-t^2/100},\quad t\ge 0
\]

令 \(a=1/100\)，则：

\[
\int_0^T \frac{t}{50}e^{-t^2/100}dt=1-e^{-T^2/100}
\]

所以：

\[
R(T)=1-F(T)=e^{-T^2/100}
\]

---

### 3.2 \(x^2 e^{-a x^2}\) 与 Gaussian half integral

若 \(a>0\)：

\[
\int_0^\infty e^{-a x^2}dx=\frac{1}{2}\sqrt{\frac{\pi}{a}}
\]

\[
\int_0^\infty x^2 e^{-a x^2}dx=\frac{\sqrt{\pi}}{4a^{3/2}}
\]

更一般地：

\[
\int_0^\infty x^{2n}e^{-a x^2}dx
=\frac{(2n-1)!!}{2^{n+1}a^{n+1/2}}\sqrt{\pi}
\]

---

### 3.3 \(x^{2n+1} e^{-a x^2}\) 积分

若 \(a>0\)：

\[
\int_0^\infty x^{2n+1}e^{-a x^2}dx=\frac{n!}{2a^{n+1}}
\]

常用值：

| Integral | Value |
|---|---|
| \(\int_0^\infty x e^{-a x^2}dx\) | \(1/(2a)\) |
| \(\int_0^\infty x^3 e^{-a x^2}dx\) | \(1/(2a^2)\) |
| \(\int_0^\infty x^5 e^{-a x^2}dx\) | \(1/a^3\) |

---

## 4. Normal / Gaussian 积分

正态分布的积分一般没有初等闭式，所以考试里通常标准化后查表。

---

### 4.1 标准正态密度

\[
\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}
\]

归一化：

\[
\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz=1
\]

等价地：

\[
\int_{-\infty}^{\infty}e^{-z^2/2}dz=\sqrt{2\pi}
\]

半边积分：

\[
\int_0^\infty e^{-z^2/2}dz=\frac{\sqrt{2\pi}}{2}
\]

---

### 4.2 一般 Gaussian 积分

若 \(a>0\)：

\[
\int_{-\infty}^{\infty}e^{-a(x-b)^2}dx=\sqrt{\frac{\pi}{a}}
\]

半边特殊情况：

\[
\int_0^\infty e^{-a x^2}dx=\frac{1}{2}\sqrt{\frac{\pi}{a}}
\]

---

### 4.3 正态题核心不是硬积分，而是标准化

若：

\[
X\sim N(\mu,\sigma^2)
\]

则：

\[
Z=\frac{X-\mu}{\sigma}\sim N(0,1)
\]

所以：

\[
P(a<X<b)=P\left(\frac{a-\mu}{\sigma}<Z<\frac{b-\mu}{\sigma}\right)
\]

然后查标准正态表。

---

### 4.4 Completing the square 配方

遇到：

\[
e^{-ax^2-bx-c}
\]

先把二次项配方：

\[
ax^2+bx+c=a\left(x+\frac{b}{2a}\right)^2+c-\frac{b^2}{4a}
\]

所以：

\[
e^{-(ax^2+bx+c)}
=e^{-a\left(x+\frac{b}{2a}\right)^2}\cdot e^{-c+\frac{b^2}{4a}}
\]

### 常见用法

可靠性系统寿命期望中可能出现：

\[
\int_0^\infty e^{-(2t^2+13t)/200}dt
\]

先配方，再转化成标准正态尾概率。

---

## 5. Arctan / Logistic-like 积分

有些 PDF 归一化会出现：

\[
\frac{1}{1+x^2}
\]

---

### 5.1 Arctan 基本公式

\[
\int \frac{1}{1+x^2}dx=\arctan x+C
\]

\[
\int_0^\infty \frac{1}{1+x^2}dx=\frac{\pi}{2}
\]

\[
\int_{-\infty}^{\infty}\frac{1}{1+x^2}dx=\pi
\]

---

### 5.2 典型代换：\(e^x\)

遇到：

\[
\int \frac{1}{e^{-x}+e^x}dx
\]

先乘 \(e^x\)：

\[
\frac{1}{e^{-x}+e^x}=\frac{e^x}{1+e^{2x}}
\]

令：

\[
y=e^x,\quad dy=e^x dx
\]

则：

\[
\int \frac{e^x}{1+e^{2x}}dx=\int \frac{1}{1+y^2}dy=\arctan y+C
\]

所以：

\[
\int_{-\infty}^{\infty}\frac{1}{e^{-x}+e^x}dx
=\int_0^\infty \frac{1}{1+y^2}dy
=\frac{\pi}{2}
\]

---

## 6. Log identity 积分

有些 mixture distribution 或随机参数指数分布题会出现：

\[
\int_0^\infty \frac{e^{-ax}-e^{-bx}}{x}dx
\]

若 \(b>a>0\)：

\[
\boxed{
\int_0^\infty \frac{e^{-ax}-e^{-bx}}{x}dx=\ln\left(\frac{b}{a}\right)
}
\]

### 常见用法

若 \(X\sim Unif(1,2)\)，且 \(Z\mid X=x\sim Exp(x)\)，则：

\[
E[Z]=E\left[\frac{1}{X}\right]
=\int_1^2 \frac{1}{x}dx
=\ln 2
\]

如果从密度 \(f_Z(z)\) 再积分，也会出现上面的 log identity。

---

## 7. 分部积分 Integration by Parts

公式：

\[
\int u\,dv=uv-\int v\,du
\]

### 7.1 常见模板：\(\int x e^{-ax}dx\)

令：

\[
u=x,\quad dv=e^{-ax}dx
\]

则：

\[
du=dx,\quad v=-\frac{1}{a}e^{-ax}
\]

所以：

\[
\int x e^{-ax}dx
=-\frac{x}{a}e^{-ax}-\frac{1}{a^2}e^{-ax}+C
\]

---

### 7.2 常见模板：求 \(E[T]\)

若 \(T\ge 0\)，密度为 \(f(t)\)，可靠度 \(R(t)=P(T>t)\)，则：

\[
E[T]=\int_0^\infty t f(t)dt
\]

因为：

\[
f(t)=-R'(t)
\]

所以：

\[
E[T]=\int_0^\infty R(t)dt
\]

这是 reliability 题非常常用的公式。

---

## 8. 非负随机变量的 Survival 积分

如果 \(T\ge 0\)，那么：

\[
\boxed{E[T]=\int_0^\infty P(T>t)dt=\int_0^\infty R(t)dt}
\]

更一般地：

\[
E[T^n]=n\int_0^\infty t^{n-1}P(T>t)dt
\]

### 常见用法

Reliability system 的寿命分布有时密度很难写，但可靠度 \(R(t)\) 比较容易组合。

这时直接用：

\[
E[T]=\int_0^\infty R(t)dt
\]

---

## 9. 极坐标积分

二维 joint PDF 在圆盘、圆环、\(x^2+y^2\) 中出现时，优先用 polar coordinates。

---

### 9.1 极坐标代换

\[
x=r\cos\theta,\quad y=r\sin\theta
\]

\[
x^2+y^2=r^2
\]

面积元素：

\[
dxdy=r\,dr\,d\theta
\]

### 重要提醒

```text
极坐标积分一定不要漏掉 Jacobian r。
```

---

### 9.2 单位圆盘积分

单位圆盘：

\[
x^2+y^2\le 1
\]

对应：

\[
0\le r\le 1,\quad 0\le \theta\le 2\pi
\]

若密度中有 \(x^2+y^2\)，则：

\[
x^2+y^2=r^2
\]

所以：

\[
\iint_{x^2+y^2\le 1} c(x^2+y^2)dxdy
=\int_0^{2\pi}\int_0^1 c r^2\cdot r\,dr\,d\theta
\]

\[
=c\cdot 2\pi\cdot \frac{1}{4}
\]

---

### 9.3 常用角度积分

\[
\int_0^{2\pi}\cos\theta\,d\theta=0
\]

\[
\int_0^{2\pi}\sin\theta\,d\theta=0
\]

\[
\int_0^{2\pi}\cos^2\theta\,d\theta=\pi
\]

\[
\int_0^{2\pi}\sin^2\theta\,d\theta=\pi
\]

\[
\int_0^{2\pi}\sin\theta\cos\theta\,d\theta=0
\]

### 常见用法

二维圆盘对称分布中：

\[
E[X]=E[Y]=0
\]

\[
E[XY]=0
\]

通常可以直接用 symmetry / orthogonality 判断。

---

## 10. 卷积 Convolution 积分

如果 \(X,Y\) 独立连续，令：

\[
Z=X+Y
\]

则：

\[
\boxed{f_Z(z)=\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)dx}
\]

### 做题步骤

```text
Step 1: 写 z = x + y，所以 y = z - x
Step 2: 写 fZ(z)=∫ fX(x)fY(z-x) dx
Step 3: 根据 support 找 x 的积分范围
Step 4: 计算积分
```

### 典型例子：两个 U(0,1) 相加

若：

\[
X,Y\sim Unif(0,1)
\]

独立，则：

\[
f_Z(z)=
\begin{cases}
z, & 0<z<1\\
2-z, & 1<z<2\\
0, & \text{otherwise}
\end{cases}
\]

关键不是积分难，而是 support 分段。

---

## 11. Jacobian 变换积分

二维变量变换中，如果：

\[
U=g_1(X,Y),\quad V=g_2(X,Y)
\]

先求反函数：

\[
x=x(u,v),\quad y=y(u,v)
\]

再算：

\[
J=\left|\frac{\partial(x,y)}{\partial(u,v)}\right|
\]

密度：

\[
f_{U,V}(u,v)=f_{X,Y}(x(u,v),y(u,v))J
\]

最后若只要 \(U\) 的 density：

\[
f_U(u)=\int f_{U,V}(u,v)dv
\]

---

### 11.1 比值变换模板

求：

\[
U=\frac{X}{Y}
\]

常设：

\[
V=Y
\]

则：

\[
X=UV,\quad Y=V
\]

Jacobian：

\[
J=|V|
\]

所以：

\[
f_U(u)=\int_{-\infty}^{\infty} f_{X,Y}(uv,v)|v|dv
\]

积分范围由原 support 决定。

---

## 12. CDF Method 中常见积分

变量变换最稳的方法：

\[
F_Y(y)=P(Y\le y)
\]

然后把事件 \(Y\le y\) 改写成关于 \(X\) 的事件。

---

### 12.1 单调变换

若 \(Y=g(X)\)，且 \(g\) 单调可逆：

\[
f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|
\]

---

### 12.2 非单调变换：\(Y=X^2\)

若：

\[
Y=X^2
\]

则 \(y>0\) 时有两个来源：

\[
x=\sqrt y,\quad x=-\sqrt y
\]

所以：

\[
f_Y(y)=f_X(\sqrt y)\frac{1}{2\sqrt y}+f_X(-\sqrt y)\frac{1}{2\sqrt y},\quad y>0
\]

即：

\[
f_Y(y)=\frac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y},\quad y>0
\]

### 易错点

```text
Y = X^2 不能只取正根。
```

---

## 13. 常见概率题积分模板

### 13.1 PDF 归一化

若：

\[
f_X(x)=c g(x),\quad x\in S
\]

则：

\[
1=\int_S c g(x)dx
\]

所以：

\[
c=\frac{1}{\int_S g(x)dx}
\]

---

### 13.2 区间概率

连续型：

\[
P(a<X<b)=\int_a^b f_X(x)dx
\]

注意：

```text
连续型 P(X=a)=0，所以 < 和 <= 通常没有区别。
```

---

### 13.3 CDF

\[
F_X(x)=P(X\le x)=\int_{-\infty}^x f_X(t)dt
\]

如果 support 从 0 开始：

\[
F_X(x)=\int_0^x f_X(t)dt
\]

---

### 13.4 Expectation / LOTUS

\[
E[X]=\int x f_X(x)dx
\]

\[
E[X^2]=\int x^2 f_X(x)dx
\]

\[
\operatorname{Var}(X)=E[X^2]-E[X]^2
\]

LOTUS：

\[
E[g(X)]=\int g(x)f_X(x)dx
\]

---

## 14. 按分布整理的常用积分结果

### 14.1 Uniform \((a,b)\)

\[
f(x)=\frac{1}{b-a},\quad a<x<b
\]

\[
E[X]=\frac{a+b}{2}
\]

\[
\operatorname{Var}(X)=\frac{(b-a)^2}{12}
\]

需要的积分：

\[
\int_a^b x dx=\frac{b^2-a^2}{2}
\]

\[
\int_a^b x^2 dx=\frac{b^3-a^3}{3}
\]

---

### 14.2 Exponential rate \(\lambda\)

\[
f(t)=\lambda e^{-\lambda t},\quad t>0
\]

\[
F(t)=1-e^{-\lambda t}
\]

\[
R(t)=e^{-\lambda t}
\]

\[
E[T]=\frac{1}{\lambda}
\]

\[
\operatorname{Var}(T)=\frac{1}{\lambda^2}
\]

---

### 14.3 Gamma rate \(\lambda\), shape \(\alpha\)

\[
f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},\quad x>0
\]

\[
E[X]=\frac{\alpha}{\lambda}
\]

\[
\operatorname{Var}(X)=\frac{\alpha}{\lambda^2}
\]

关键积分：

\[
\int_0^\infty x^{\alpha-1}e^{-\lambda x}dx=\frac{\Gamma(\alpha)}{\lambda^\alpha}
\]

---

### 14.4 Normal \(N(\mu,\sigma^2)\)

\[
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
\]

\[
Z=\frac{X-\mu}{\sigma}\sim N(0,1)
\]

概率通过查表：

\[
P(a<X<b)=P\left(\frac{a-\mu}{\sigma}<Z<\frac{b-\mu}{\sigma}\right)
\]

---

### 14.5 Weibull / Rayleigh-like

如果：

\[
R(t)=e^{-\alpha t^\beta}
\]

则：

\[
f(t)=-R'(t)=\alpha\beta t^{\beta-1}e^{-\alpha t^\beta}
\]

常见 \(\beta=2\)：

\[
f(t)=2\alpha t e^{-\alpha t^2}
\]

积分核心：

\[
\int t e^{-\alpha t^2}dt=-\frac{1}{2\alpha}e^{-\alpha t^2}+C
\]

---

## 15. 最短考试速查版

```text
1. ∫ x^n dx = x^(n+1)/(n+1), n≠-1
2. ∫ 1/x dx = ln|x|
3. ∫_0^∞ e^(-ax) dx = 1/a
4. ∫_0^∞ x e^(-ax) dx = 1/a^2
5. ∫_0^∞ x^n e^(-ax) dx = n!/a^(n+1)
6. ∫ x e^(-a x^2) dx = -e^(-a x^2)/(2a)
7. ∫_0^∞ e^(-a x^2) dx = 1/2 sqrt(pi/a)
8. ∫ 1/(1+x^2) dx = arctan x
9. ∫_0^∞ 1/(1+x^2) dx = pi/2
10. ∫_{-∞}^{∞} e^(-z^2/2) dz = sqrt(2pi)
11. E[T] = ∫_0^∞ R(t) dt for T≥0
12. Polar: dxdy = r dr dθ
13. Convolution: fZ(z)=∫ fX(x)fY(z-x)dx
14. Jacobian: fUV = fXY(x(u,v),y(u,v)) |∂(x,y)/∂(u,v)|
```

---

## 16. 一句话总结

\[
\boxed{
\text{概率统计里的积分不是为了炫技，而是为了求面积、归一化、期望、变换后的密度和寿命期望。}
}
\]

如果考试时间紧，优先记住：

```text
exponential / gamma 积分
x e^(-a x^2) 积分
normal 标准化
arctan 积分
polar Jacobian r
survival expectation E[T]=∫R(t)dt
```
