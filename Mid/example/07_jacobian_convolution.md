# 07 — Jacobian Transformation + Convolution

> 覆盖范围：C-TRANS-003, C-TRANS-004

## 考试识别模板

```text
2D transform:
solve inverse -> translate support -> compute J=|∂(x,y)/∂(u,v)| -> multiply.

Convolution:
Z=X+Y, f_Z(z)=∫ f_X(x)f_Y(z-x)dx.
Range must satisfy both supports.
```

## 典型例题

### EX-JAC-101 — \(U=X+Y,V=X-Y\)

**题目**

\(X,Y\) independent \(Unif(0,1)\)。令 \(U=X+Y,V=X-Y\)。求 joint PDF 形式和 support。

**解法 / 可抄步骤**

反解：
\[
x=\frac{u+v}{2},\quad y=\frac{u-v}{2}.
\]
Jacobian:
\[
J=\left|\begin{matrix}1/2&1/2\\1/2&-1/2\end{matrix}\right|=\frac12.
\]
Support:
\[
0<\frac{u+v}{2}<1,\quad 0<\frac{u-v}{2}<1
\]
即
\[
0<u+v<2,\quad 0<u-v<2.
\]
原 joint density 为 1，所以
\[
f_{U,V}(u,v)=\frac12
\]
在上述 support 上。

---

### EX-JAC-102 — \(S=X+Y,R=X/(X+Y)\)

**题目**

\(X,Y iid\sim Exp(\lambda)\)。令 \(S=X+Y,R=X/(X+Y)\)。求 \(f_{S,R}\)。

**解法 / 可抄步骤**

反解：
\[
x=rs,\quad y=(1-r)s.
\]
Support:
\[
s>0,\quad 0<r<1.
\]
Jacobian:
\[
J=s.
\]
\[
f_{S,R}(s,r)=\lambda^2e^{-\lambda s}s,\quad s>0,0<r<1.
\]

---

### EX-JAC-103 — 极坐标：二维标准正态到 Rayleigh

**题目**

\(X,Y\) independent standard normal。令 \(R=\sqrt{X^2+Y^2}\)。求 \(f_R(r)\)。

**解法 / 可抄步骤**

\[
f_{X,Y}(x,y)=\frac1{2\pi}e^{-(x^2+y^2)/2}.
\]
极坐标 \(x=r\cos\theta,y=r\sin\theta\)，Jacobian \(J=r\)。
\[
f_{R,\Theta}(r,\theta)=\frac1{2\pi}re^{-r^2/2}.
\]
积分掉 \(\theta\)：
\[
f_R(r)=re^{-r^2/2},\quad r>0.
\]

---

### EX-CONV-101 — 两个 Uniform 的和

**题目**

\(X,Y iid\sim Unif(0,1)\)，\(Z=X+Y\)。求 \(f_Z(z)\)。

**解法 / 可抄步骤**

\[
f_Z(z)=\int f_X(x)f_Y(z-x)dx.
\]
条件：
\[
0<x<1,\quad 0<z-x<1.
\]
所以
\[
\max(0,z-1)<x<\min(1,z).
\]
最终：
\[
f_Z(z)=
\begin{cases}
z,&0<z<1\\
2-z,&1<z<2\\
0,&otherwise
\end{cases}
\]

---

### EX-CONV-102 — 两个 Exponential 的和

**题目**

\(X,Y iid\sim Exp(\lambda)\)，\(Z=X+Y\)。求 \(f_Z(z)\)。

**解法 / 可抄步骤**

\[
f_Z(z)=\int_0^z \lambda e^{-\lambda x}\lambda e^{-\lambda(z-x)}dx
=\lambda^2ze^{-\lambda z},\quad z>0.
\]
所以 \(Z\sim Gamma(2,\lambda)\)。

---

### EX-CONV-103 — 离散卷积：两颗骰子

**题目**

两颗公平骰子点数 \(X,Y\)，\(Z=X+Y\)。求 \(P(Z=7)\)。

**解法 / 可抄步骤**

可行组合：
\[
(1,6),(2,5),(3,4),(4,3),(5,2),(6,1).
\]
\[
P(Z=7)=6/36=1/6.
\]

---

### EX-CONV-104 — 卷积上下限训练

**题目**

\(X\sim Unif(0,2)\)，\(Y\sim Unif(0,3)\)，独立。写出 \(Z=X+Y\) 的卷积积分上下限。

**解法 / 可抄步骤**

条件：
\[
0<x<2,\quad 0<z-x<3\Rightarrow z-3<x<z.
\]
所以
\[
f_Z(z)=\int_{\max(0,z-3)}^{\min(2,z)}\frac12\frac13dx.
\]
上下限比积分本身更重要。

---

## 参考资料

- LibreTexts transformations: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_%28Siegrist%29/03%3A_Distributions/3.07%3A_Transformations_of_Random_Variables
