# 计算物理 -- $\mathcal{By\ A.I.B.}$
## Lecture 1 计算物理导论
## Lecture 2 Python（Numpy+Matplotlib）
## Lecture 3 经典数值方法

### 3.1 多项式插值

可以证明满足下面形式的多项式插值存在且唯一
$$
P_n = a_0+a_1x+a_2x^2+...+a_nx^n, a_1...a_n\in \mathcal{R}\\
P_n(x_i)=y_i
$$
多项式插值条件可以写为范德蒙行列式：
$$
\left.\left[\begin{array}{c} {y_0}\\ {y_1}\\\cdots\\ {y_n}\end{array}\right.\right]=\left[\begin{array}{cccc}1& {x_0}&\cdots& {x_0^n}\\1& {x_1}&\cdots& {x_1^n}\\1& {x_2}&\cdots& {x_2^n}\\1& {x_n}&\cdots& {x_n^n}\end{array}\right]\left[\begin{array}{c} {a_0}\\ {a_1}\\\cdots\\{a_n}\end{array}\right]
$$
**对于 $n + 1$ 个互不相同的插值节点，满足插值条件的 $n$ 次多项式的插值函数存在且唯一**

#### 3.1.1 Lagrange形式

构造一系列线性插值函数$l_k(x)$，在$x_k$这个点上为1，在其余节点上为0，通过线性组合得到Lagrange插值函数$P_n(x)$
$$
l_k(x)=\frac{(x-x_0)(x-x_1)...(x-x_{k-1})(x-x_{k+1})...(x-x_n)}{(x_k-x_0)(x_k-x_1)...(x_k-x_{k-1})(x_k-x_{k+1})...(x_k-x_n)} = \prod_{i\neq	k} \frac{x-x_i}{x_k-x_i}
$$
线性组合得到Lagrange插值函数：
$$
P_n(x)=\sum_{k=0}^{n}l_k(x)y_k
$$

#### 3.1.2 Newton形式

将一个$n$次多项式表示为下面的形式：
$$
N_n(x)=a_0+a_1(x-x_0)+a_2(x-x_0)(x-x_1)+...+a_n(x-x_0)(x-x_1)...(x-x_{n-1})
$$
 $n + 1$ 个点的插值成$n$次多项式，线性方程组如下：
$$
\left.\left\{\begin{array}{l}  {y_0=a_0}\\  {y_1=a_0+a_1(x_1-x_0)}\\  {y_2=a_0+a_1(x_2-x_0)+a_2(x_2-x_0)(x_2-x_1)}\\\cdots\\  {y_n=a_0+a_1(x_n-x_0)+\cdots +a_n(x_n-x_0)(x_n-x_1)(x_n-x_2)\cdots(x_n-x_{n-1})}\end{array}\right.\right.
$$
为了求解牛顿插值的各个系数，定义牛顿差商：
$$
F(x_0,x_1)=\frac{f(x_1)-f(x_0)}{x_1-x_0}\\
F(x_0,x_1,...,x_m)=\frac{F(x_1,x_2,...,x_m)-F(x_0,x_1,...,x_{m-1})}{x_m-x_0}
$$
用牛顿差商的形式改写牛顿多项式：
$$
N_n(x)=a_0+F(x_0,x_1)(x-x_0)+...+F(x_0,x_1,...,x_n)(x-x_0)...(x-x_n)
$$
如图所示，各阶差商的排布：

![image-20240329225451163](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240329225451163.png)

**计算顺序是先计算第一列，在根据第一列计算第二列，一直计算到最后一列**

#### 3.1.3 分段线性插值

为了减少Runge现象，可以对数据点集进行分段，每一段都进行低次插值，比如对每一段都进行线性（一次）的插值

#### 3.1.4 样条插值

为了保持分段线性插值收敛稳定、计算简单的优点，同时为了保持在整个插值区间上的光滑性，引入了样条插值，e.g. 三次样条插值：

**三次样条插值：**

+ $S(x) $满足插值条件$ S(x_k) = y_k, k\in (0, n)$；

+ $S(x) $在每个区间$ (x_k,x_{k+1})$ 上是不超过三次的多项式；

+ $S(x)，S' (x)，S''(x) $在整个区间上保持连续。

$$
S_k(x)=a_{k0}+a_{k1}x+a_{k2}x^2+a_{k3}x^3
$$

对于$n+1$个插值点，总共有$n$个区间，总参数数目为$4n$个

对于确定这样一组方程组，中间的$n+1-2=n-1$个点和$n+1$个插值条件分别可以带来如下的$3(n-1)$个和$n+1$约束方程：
$$
\begin{cases}
{S(x_k-0)=S(x_k+0),k=1,2,\cdots,n-1}\\
{S'(x_k-0)=S'(x_k+0),k=1,2,\cdots,n-1}\\
{S''(x_k-0)=S''(x_k+0),k=1,2,\cdots,n-1}\\{S(x_k)=y_k,k=0,2,\cdots,n}\\\end{cases}
$$
剩下两个约束方程可以由两端端点处的一阶导数或者二阶导数给定

### 3.2 数值微分

对于更多点的情况，假设点间隔$h$均匀,在$x_{i-1},x_i,x_{i+1}$三点的泰勒展开：
$$
f_{i+1}=f_i+hf_i'+\frac{h^2}{2!}f_i''+...\\
f_{i-1}=f_i-hf_i'+\frac{h^2}{2!}f_i''-...
$$
对于一阶导数的数值微分形式，分别对于（11）中的单个表达式和两式之差：
$$
f_i'=\frac{f_{i+1}-f_i}{h}+o(h)\\
f_i'=\frac{f_{i+1}-f_{i-1}}{h}+o(h^2)\\
$$
对于更高的精度，采用五点法$x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2}$的微分格式：
$$
\begin{gathered}
{f_{i+2}}    {=f_i+2h\cdot f_i^{\prime}+\frac{4h^2}{2!}\cdot f_i^{\prime\prime}+\frac{8h^3}{3!}\cdot f_i^{\prime\prime\prime}+\cdots} \\
   {f_{i-2}}    {=f_{i}-2h\cdot f_{i}^{\prime}+{\frac{4h^{2}}{2!}}\cdot f_{i}^{\prime\prime}-{\frac{8h^{3}}{3!}}\cdot f_{i}^{\prime\prime\prime}+\cdots } 
\end{gathered}
$$
通过三点法将三阶导数消去，可以得到一阶导数更加精确的形式：
$$
f'_i=\frac{f_{i-2}-8f_{i-1}+8f_{i+1}-f_{i+2}}{12h}+o(h^4)
$$
对二阶导数也可以用类似的方法

对于端点$x_0,x_n$：
$$
\begin{aligned}
&{f_0} =    {f}_{0}  \\
&{f}_{1}     {=f_{0}+h\cdot f_{0}^{\prime}+\frac{h^{2}}{2!}\cdot f_{0}^{\prime\prime}+O(h^{3})}  \\
&f_2     {=f_{0}+2h\cdot f_{0}^{\prime}+\frac{4h^{2}}{2!}\cdot f_{0}^{\prime\prime}+O(h^{3})} 
\end{aligned}
$$
通过线性组合的方式消去$f_0''$：
$$
f_0'=\frac{4f_1-3f_0-f_2}{2h}+o(h^2)
$$


同样对于$x_n$:
$$
f_n'=\frac{f_{n-2}+3f_{n}-4f_{n+1}}{2h}+o(h^3)
$$

## Lecture 5. 线性代数的数值求解

### 5.1 Gauss消元法

将系数矩阵和常数矩阵合并成一个增广矩阵后，利用消元法得到下列形式：
$$
\mathrm{(A,b)^{(3)}=\begin{pmatrix}a_{11}&a_{12}&a_{13}&a_{14}&b_{1}\\0&a_{22}^{(1)}&a_{23}^{(1)}&a_{24}^{(1)}&b_{2}^{(1)}\\0&0&a_{33}^{(2)}&a_{34}^{(2)}&b_{3}^{(2)}\\0&0&0&a_{44}^{(3)}&b_{4}^{(3)}\end{pmatrix}}
$$
在这个形式上可以较为容易的得到解向量$(x_1, x_2, ..., x_n)$​

> 列主元消元法
>
> 在高斯消元过程中，调换方程组顺序，使得在消元运算中，分母量的绝对值尽量更大，以**减少舍入误差的影响**。
>
> **如果在一列中选取模最大的元素调到主干方程位置再消元，我们称之为列主元消元法。**

### 5.2 LU分解

可以将原来具有$n^2$个独立变量的系数矩阵分解成上三角和下三角两个矩阵，为了保证两个矩阵一共也有$n^2$个独立变量，需要满足下面的形式：
$$
{L}=\begin{pmatrix}{l}_{11}&0&0&0\\{l}_{21}&{l}_{22}&0&0\\  {l}_{31}&  {l}_{32}&  {l}_{33}&0\\  {l}_{41}&  {l}_{42}&  {l}_{43}&  {l}_{44}\end{pmatrix},  {U}=\begin{pmatrix}1&  {u}_{12}&  {u}_{13}&  {u}_{14}\\0&1&  {u}_{23}&  {u}_{24}\\0&0&1&  {u}_{34}\\0&0&0&1\end{pmatrix}
$$

进行LU分解的过程中，需要先进行依次轮流求解L矩阵的行和U矩阵的列
$$
{l_{ik}=a_{ik}-\sum_{r=1}^{k-1}l_{ir}u_{rk},\quad i=k,k+1,\cdots,n}\\
{u_{kj}=\left(a_{kj}-\sum_{r=1}^{k-1}l_{kr}u_{rj}\right)/l_{kk},\quad j=k+1,k+2,\cdots,n}
$$

无论是$L$矩阵还是$U$矩阵，求解矩阵元$A_{ij}$时候用$L$矩阵的第$i$行与$U$矩阵的第$j$​列相乘进行运算

### 5.3 迭代法

将方程组转化为下列形式：
$$
\left.\left\{\begin{array}{lllllll}x_{1}=&&-\frac{a_{12}}{a_{11}}x_{2}&-\cdots&-\frac{a_{1n}}{a_{11}}x_{n}&+\frac{b_{1}}{a_{11}}\\x_{2}=&-\frac{a_{21}}{a_{22}}x_{1}&-&\cdots&-\frac{a_{2n}}{a_{22}}x_{n}&+\frac{b_{2}}{a_{22}}\\\cdots&\cdots&\cdots&\cdots&\cdots&\cdots\\x_{n}=&-\frac{a_{n1}}{a_{nn}}x_{1}&-\frac{a_{n2}}{a_{nn}}x_{2}&\cdots&-&+\frac{b_{n}}{a_{nn}}\end{array}\right.\right.
$$

#### 5.3.1 Jacobi迭代

可以将方程组写为迭代形式$\mathrm{X}^{k+1}=\mathrm{BX}^k+\mathcal{g}$其中$\mathrm{X}，{g}$分别是系数变换矩阵和常数向量
$$
\mathrm{B=\begin{pmatrix}0&-\frac{a_{12}}{a_{11}}&\cdots&-\frac{a_{1n}}{a_{11}}\\-\frac{a_{21}}{a_{22}}&0&\cdots&-\frac{a_{2n}}{a_{22}}\\\cdots&\cdots&\cdots&\cdots\\-\frac{a_{n1}}{a_{nn}}&-\frac{a_{n2}}{a_{nn}}&\cdots&0\end{pmatrix}~\mathcal{g}=\begin{pmatrix}\frac{b_{1}}{a_{11}}\\\frac{b_{2}}{a_{22}}\\\cdots\\\frac{b_{n}}{a_{nn}}\end{pmatrix}}
$$
迭代收敛条件：形如$X^{k+1}=BX^k+g$的迭代形式，迭代矩阵谱半径$\rho(B)=\max_{1\leq i\leq n}\abs{\lambda_i}<1$是迭代收敛的充分必要条件

利用谱分解的方式将特征值写为Dirac括号的形式：
$$
\sum_{{i=1}}^{{n}}\lambda_{{i}}\left|{b_{i}}\right\rangle\left\langle{b_{i}}\right|
$$
假设$X^*$是方程组的标准解，得到迭代形式：
$$
\mathrm{X^{*}-X^{(k+1)}}=\sum_{i=1}^{n}\lambda_{i}^{k} |b_{i}\rangle \langle b_{i}| \mathrm{(X^{*}-X^{(0)})}
$$
因此收敛的充分必要条件是$\rho(B)<1$​，数学上举证的L1范数总是大于谱半径，因此假如矩阵的L1范数小于1，可以判断矩阵一定收敛

#### 5.3.2 Gauss-Seidel 迭代

为了解决Jacobi迭代收敛较慢的问题，Gauss-Seidel迭代充分利用了已经更新的数据：
$$
x_i^{(k+1)} = \sum_{j=1}^{i-1} b_{ij} x_j^{(k+1)} + \sum_{j=i}^n b_{ij} x_j^{(k)} + g_i
$$

### 5.4 特征值和特征向量

#### 5.4.1 幂法求最大特征向量

假设矩阵$A$的特征值为$\lambda_i, i=1,...,n$并且从大到小排列，对应的特征向量为$\nu_i$,，任选一个初始向量$X^{(0)}$可以表示为特征向量的线性组合：
$$
\mathrm{X^{(0)}}=\alpha_{1}\nu_{1}+\alpha_{2}\nu_{2}+\cdots+\alpha_{n}\nu_{n}
$$
迭代计算$X^{(k+1)}=AX^{(k)}$得到：
$$
\begin{aligned}
\mathrm{X^{(k)}}&=\alpha_{1}\lambda_{1}^{k}\nu_{1}+\alpha_{2}\lambda_{2}^{k}\nu_{2}+\cdots+\alpha_{n}\lambda_{n}^{k}\nu_{n}\\
&=\lambda_1^k[\alpha_1\nu_1+\alpha_2(\frac{\lambda_2}{\lambda_1})^k\nu_2+...+\alpha_2(\frac{\lambda_n}{\lambda_1})^k\nu_n]\\
&\thickapprox \alpha_{1}\lambda_{1}^{k}\nu_{1}
\end{aligned}
$$
因此在迭代步数$k$足够大时：
$$
\lambda_1^{(k+1)}=\frac{X^{(k+1)}}{X^{(k)}}
$$
如果出现两个互为相反数最大特征值，迭代中会出现震荡，此时需要在迭代次数足够大时每走两步来计算最大特征值：
$$
\lambda_1^{(k+2)}=\sqrt{\frac{X^{(k+2)}}{X^{(k)}}}
$$
幂法求最小特征值的方法是求$A$矩阵的逆矩阵$A^{-1}$此时特征值变为原来的倒数，按照上面类似的方法求解

#### 5.4.2 实对称矩阵特征值的Jacobi方法

对于$n$阶的对称矩阵，存在正交矩阵$Q$使得：
$$
\mathrm{A'}=\mathrm{Q^{T}AQ}=\begin{pmatrix}\lambda_{1}&&&&\\&\lambda_{2}&&&\\&&&\cdots&\\&&&&\lambda_{\mathrm{n}}\end{pmatrix}
$$
此时$A'$和$A$具有相同的特征值，可以通过多次旋转变换，将非对角元消除，旋转矩阵为：
$$
R_n = \left( 
\begin{array}{cccccc}
1 & 0 & \cdots & 0 & 0 & 0 \\
0 & \cos(\theta) & \cdots & 0 & \sin(\theta) & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & 0 & 0 \\
0 & -\sin(\theta) & \cdots & 0 & \cos(\theta) & 0 \\
0 & 0 & \cdots & 0 & 0 & 1 \\
\end{array}
\right)
$$
一般每次选取最大的非对角元素作为旋转对象

旋转后：
$$
{b_{pq}=b_{qp}=a_{pq}\cos2\theta+{\frac{a_{pp}-a_{qq}}{2}}\sin2\theta}
$$
记${s=\frac{a_{pp}-a_{qq}}{2a_{pq}}},t=tan\theta$：
$$
t^2+2ts-1=0(s\neq 0)\\
t=1(s=0)
$$

## Lecture 6. 差分法求解微分方程

### 6.1 常微分方程

#### 6.1.1 Euler公式

形如下式的常微分方程：
$$
\frac{d\phi}{dx}=f(x, \phi)
$$
一阶**向前差分**公式：
$$
\frac{\phi_{n+1}-\phi_n}{h}=f(x_n,\phi_n)\\
\phi_{n+1}=\phi_n+h\cdot f(x_n,\phi_n)
$$
向后Eular公式具有更好的精度和稳定性，Picard迭代格式：
$$
\begin{cases}
\phi^{(0)}_{n+1}=\phi_n+h\cdot f(x_n,\phi_n)\\
\phi^{(k+1)}_{n+1}=\phi_n+h\cdot f(x_{n+1}, \phi_{n+1}^{(k)})
\end{cases} \ \ \ k=0,1,2,...
$$
迭代的收敛条件：$\abs{\phi^{(k+1)}_{(n+1)}-\phi_{(n+1)}^{(k)}}<\varepsilon$

#### 6.1.2 Runge-Kutta算法

对函数进行高阶泰勒展开：
$$
\phi_{n+1}=\phi_n+h\cdot \phi'(x_n)+\frac{h^2}{2!}\cdot \phi''(x_n)+o(h^3)
$$

舍去高阶小量：
$$
\begin{aligned}
\phi_{n+1}&=\phi_n+h\cdot [f(x_n,\phi_n)+\frac h2\cdot (\frac{\partial f}{\partial x}|_{(x_n,\phi_n)}+\frac{\partial f}{\partial \phi}\cdot \frac{\partial \phi}{\partial x}|_{(x_n,\phi_n)})] \\
&=\phi_n+h\cdot [f(x_n,\phi_n)+\frac h2\cdot (\frac{\partial f}{\partial x}|_{(x_n,\phi_n)}+\frac{\partial f}{\partial \phi}\cdot f(x_n,\phi_n)|_{(x_n,\phi_n)})]
\end{aligned}
$$
Runge-Kutta算法利用函数在$(x_n.\phi_n),(x_n+ah,\phi_n+bh\cdot f (x_n,\phi_n))$两点的函数值，通过数值微分的方法来拟合上面的偏微分：
$$
{c_1\cdot f(x_n,\phi_n)+c_2\cdot f\biggl(x_n+ah,\phi_n+bh\cdot f(x_n,\phi_n)\biggr)}=\\
{(c_1+c_2)\cdot f(x_n,\phi_n)+\frac{h}{2}\Big[2ac_2\frac{\partial f}{\partial x}|_{(x_n,\phi_n)}+2bc_2\frac{\partial f}{\partial\phi}|_{(x_n,\phi_n)}f(x_n,\phi_n)\Big]}
$$
对比$(22)$式，求选取待定系数$c_1=\frac12,c_2=\frac12$​：
$$
\begin{cases}
c_1+c_2=1\\
2ac_2=1\\
2bc_1=1\\
\end{cases}
$$
最终得到二阶Runge-Kutta的形式：
$$
\left.\left\{\begin{array}{l}\phi_{{n+1}}=\phi_{{n}}+\frac{{h}}{2}({k_1+k_2})\\{k_1=f(x_n,\phi_n)}\\{k_2=f(x_n+h,\phi_n+hk_1)}\end{array}\right.\right.
$$

利用类似的方法，我们可以得到更加高阶的Runge-Kutta公式，例如四阶的Runge-Kutta公式：
$$
\left.\left\{\begin{array}{l}\phi_{  {n+1}}=\phi_{  {n}}+\frac{  {h}}{6}(  {k}_1+2  {k}_2+2  {k}_3+  {k}_4)\\  {k}_1=  {f}(  {x}_{  {n}},\phi_{  {n}})\\  {k}_2=  {f}(  {x}_{  {n}}+\frac{1}{2}  {h},\phi_{  {n}}+\frac{1}{2}  {h}  {k}_1)\\  {k}_3=  {f}(  {x}_{  {n}}+\frac{1}{2}  {h},\phi_{  {n}}+\frac{1}{2}  {h}  {k}_2)\\  {k}_4=  {f}(  {x}_{  {n}}+  {h},\phi_{  {n}}+  {h}  {k}_3)\end{array}\right.\right.
$$

#### 6.1.3 常微分方程组

对于更加高阶的微分方程，可以通过还原变换成一阶常微分方程组，然后可以利用向前Eular公式或Runge-Kutta算法将变量进行离散化

例如谐振子问题：$\frac{d^2\phi}{dt^2}+\omega^2\phi=0$，利用变量代换$A(t)=\phi(t),B(t)=\frac{d\phi}{dt}$:
$$
\begin{cases}
\frac{dA(t)}{dt}=B(t)\\
\frac{dB(t)}{dt}=-\omega^2A(t)
\end{cases}
$$
四阶Runge-Kutta公式：
$$
\begin{cases}
y_{n+1}=y_n+\frac h6(ky_1+2ky_2+2ky_3+ky_4)\\
z_{n+1}=z_n+\frac h6(kz_1+2kz_2+2kz_3+kz_4)
\end{cases}
$$
其中：
$$
\left.\left\{\begin{array}{l}   {ky_1=f(x_n,y_n,z_n)}\\   {kz_1=g(x_n,y_n,z_n)}\\   {ky_2=f(x_n+\frac h2,y_n+\frac h2\cdot ky_1,z_n+\frac h2\cdot kz_1)}\\   {kz_2=g(x_n+\frac h2,y_n+\frac h2\cdot ky_1,z_n+\frac h2\cdot kz_1)}\\   {ky_3=f(x_n+\frac h2,y_n+\frac h2\cdot ky_2,z_n+\frac h2\cdot kz_2)}\\   {kz_3=g(x_n+\frac h2,y_n+\frac h2\cdot ky_2,z_n+\frac h2\cdot kz_2,}\\   {ky_4=f(x_n+h,y_n+h\cdot ky_3,z_n+h\cdot kz_3)}\\   {kz_4=g(x_n+h,y_n+h\cdot ky_3,z_n+h\cdot kz_3)}\end{array}\right.\right.
$$

### 6.2 偏微分方程数值解

#### 6.2.1 常见偏微分算子的差分格式

常见的偏微分方程有Poisson方程、Laplace方程、波动方程、扩散方程等，不同种类的偏微分方程可以通过变量的数目进行相应的格点划分,例如对于一阶偏导数和拉普拉斯算子分别可以得到：
$$
\frac{\partial \phi}{\partial x}|_{m,n}=\begin{cases}
\frac{\phi_{m+1,n}-\phi_{m,n}}{h}\ \ (向前Eular)\\
\frac{\phi_{m,n}-\phi_{m-1,n}}{h}\ \ (向后隐式)\\
\end{cases}
$$

$$
\begin{aligned}
\nabla^2\phi|_{m,n}&=\frac{\partial^2 \phi}{\partial x^2}+\frac{\partial^2 \phi}{\partial y^2}\\
&=\frac{\phi_{m+1,n}+\phi_{m-1,n}+\phi_{m,n+1}+\phi_{m,n-1}-4\phi_{m,n}}{h^2}
\end{aligned}
$$

对于偏微分算子$\frac{\partial^2}{\partial x\partial y}$，可以利用四个角上的格点来构造：
$$
\frac{\partial^2 \phi}{\partial x\partial y}=\frac{\phi_{m+1,n+1}+\phi_{m-1,n-1}-\phi_{m-1,n+1}-\phi_{m+1,n-1}}{4h^2}
$$
分母中的4是对四个格点上的值分别进行泰勒展开得到的结果，在上面的推导中都是默认对于$x,y$​的差分步长都是相同的

#### 6.2.2. 一维热传导方程

一维的热传导方程：
$$
\partial_t u=\alpha \partial_x^2u
$$
时间和空间的步长取$h_t,h_x$​，分别用一阶差分和二阶差分的公式带入：
$$
\frac{u_{m+1,n}-u_{m,n}}{h_t}=\alpha\frac{u_{m,n+1}+u_{m,n-1}-2u_{m,n}}{h_x^2}
$$
整理得到热传导方程的向前差分的格式：
$$
u_{m+1,n}=u_{m,n}+\frac{\alpha h_t}{h_x^2}\cdot \frac{u_{m,n+1}+u_{m,n-1}-2u_{m,n}}{h_x^2}
$$

#### 6.2.3. 波动方程

对于波动方程，拉普拉斯算子依然可以采用上述的离散化形式，关于时间$t$的离散化，可以利用变量代换的方式完成：
$$
\begin{cases}
\frac{\partial u}{\partial t}=v(x,t)\\
\frac{\partial v}{\partial t}=c^2\frac{\partial^2 u}{\partial x^2}
\end{cases}
$$

$$
\begin{cases}&{u_{m+1,n}=u_{m,n}+h_t\cdot v_{m,n}}\\&{v_{m+1,n}=v_{m,n}+h_t\cdot c^2\frac{u_{m,n+1}+u_{m,n-1}-2u_{m,n}}{h_{x}^2}}\\\end{cases}
$$

#### 6.2.4 Von Neumann稳定性分析

对于函数$u(x,t)$可以展开为傅里叶级数：
$$
u(x,t)=\sum_k c_k(t)e^{ikx}
$$
将傅里叶展开后的级数带入到偏微分方程的差分格式中，得到时间演化分别关于差分步长$h_x,h_t$​的关系

>$e.g.1$ 将傅里叶级数带入到热传导方程的差分格式中得到：
>$$
>\begin{aligned}
> {c_{k}(t+h_{t})}  &=c_{k}(t)+\frac{\alpha h_{t}}{h_{x}^{2}}\big(e^{ikh_{x}}+e^{-ikh_{x}}-2\big)c_{k}(t) \\
>&=c_{k}(t)\big[1+\frac{\alpha h_{t}}{h_{x}^{2}}(2\cos kh_{x}-2)\big] \\
>&= c_{k}(t)\big[1-\frac{4\alpha {h_{t}}}{ {h_{x}^{2}}}\sin^{2}\frac{ {kh_{x}}}{2}\big] 
>\end{aligned}
>$$
>为了保证$c_k(t)$不发散，需要满足：
>$$
>\abs{1-\frac{4\alpha h_t}{h_x^2}\sin^2\frac{kh_x}{2}}<1.0
>$$

>$e.g. 2$波动方程的稳定性分析：
>$$
>\begin{pmatrix}   u(   x,   t)\\   v(   x,   t)\end{pmatrix}=\sum_k\begin{pmatrix}   c_{   uk}(   t)\\   c_{   vk}(   t)\end{pmatrix}   e^{   ikx}
>$$
>
>
>类似的得到系数向量的传递矩阵：
>$$
>A=\begin{pmatrix}1&   {h_t}\\-\frac{4h_t c^2}{   {h_x^2}}\sin^2\frac{   {kh_x}}{2}&1\end{pmatrix}=\begin{pmatrix}1&   {h_t}\\-h_t   {r^2}&1\end{pmatrix},\quad   {r=\frac{2c}{h_x}\sin\frac{   {kh_x}}{2}}
>$$
>对于这个传递矩阵，差分格式的稳定性由特征值的模长决定：
>$$
>\lambda_{1,2}=1\pm ih_tr,\abs{\lambda_{1,2}}=\sqrt{1+h_t^2r^2}
>$$
>因此对于；任何初始态在迭代的次数足够多之后都会变的不稳定和发散，发散的程度取决于特征值大小以及相应的差分步长大小

#### 6.2.5 波动方程的向后隐式差分方法

将波动方程里面的时间步长$h_t$变为$-h_t$，可以得到隐式差分格式，此时需要对向后传递矩阵求逆
$$
c(t+h_t)=B^{-1}c(t)
$$
这时候得到的结果：
$$
\abs{\lambda_{1,2}}=\frac{1}{\sqrt{1+h_t^2r^2}}<1.0
$$
向后合适中严格保证了算法的稳定性，但是在Von Neumann稳定性分析中可以看出，经过足够多的迭代步数之后，除了$k=0$之外其他所有波的成分都会衰减成0，但实际上各种频谱成分应该都会存在

#### 6.2.6 Crank-Nicolson方法

 为了解决向后隐式差分格式带来的$k=0$之外成分衰减的问题，可以将向前和向后传递两种方式进行结合：
$$
\begin{cases}
u_{m+1,n}&=u_{m,n}+\frac{1}{2}h_t\cdot\left[v_{m,n}+v_{m+1,n}\right]\\v_{m+1,n}&=v_{m,n}+\frac{h_tc^2}{2h_x^2}\cdot[(u_{m+1,n+1}+u_{m+1,n-1}-2u_{m+1,n})\\
&+(u_{m,n+1}+u_{m,n-1}-2u_{m,n})]\\
\end{cases}
$$
此时传矩阵的特征值严格为0

## Lecture 7. 蒙特卡洛方法

### 7.1 随机数产生器

#### 7.1.1 真随机过程与准随机过程

+ 真随机过程：微观物理过程，比如量子尺度不可能预测每一次事件的结果，只能给出发生的概率
+ 准随机过程：可以用经典的物理定律描述，但是对于初始值微小差异和外界的放大干扰作用，无法精确预测

#### 7.1.2 线性同余法（LCG）生成伪随机数

通过LCG可以产生一系列在$[0,1]$上的随机分布，LCG的序列：
$$
X_{n+1}=(aX_n+c)\ \ \mathrm{mod}\ \ m \\
\xi_n=\frac{X_n}{m}
$$
其中$a$是乘子，$c$为增量，$m$是模数，$X_0$是种子，序列中的$X_n$只能是$0,1,...,m-1$中的一个值，因此$\xi_n$严格小于1

为了达到更好的随机数效果，需要$m$选值足够大；$c,m$互质；$m$的所有质因数都能整除$a-1$，在python中可以通过下列语法产生$(0,1)$中的随机浮点数：

```python
import random
a = random.random()
```

#### 7.1.4 均匀分布的统计检验

在区间$[0,1)$上的伪随机序列$\xi_1,...,\xi_n$，如果序列是随机分布的，将$[0,1)$划分为$k$个相同的子区间，对于每一个子区间内随机数的均值和方差都为$N/k$,同时由于具有约束条件$\sum_{i=1}^kN_i=N$，总共的自由度是$k-1$

**对于频率检验，定义统计量：**
$$
\chi^2=\sum_{i=1}^k\frac{(N_i-N/k)^2}{N/k}
$$
服从分布$\chi^2(k-1)$，与一定置信度下的$\chi^2_0$比较进行比较

**对于独立性检验：**

在$[0,1)$上产生$2N$个随机数$\xi_1,\xi_2,...,\xi_{2N}$，并且将这些随机数两两组成点对$(\xi_1,\xi_2),...,(\xi_{2N-1},\xi_{2N})$，类似的将$[0,1)\bigotimes[0,1)$的平面分成$k^2$个点格，如果是均匀分布，每个点格的均值和方差都是$\frac{N}{k^2}$，因此定义统计量：
$$
\chi^2 = \sum_{i=1}^N\sum_{j=1}^{N}\frac{(n_{ij}-\frac{N}{k^2})^2}{\frac{N}{k^2}}
$$
同样的，$\chi^2$服从$\chi^2(k^2-1)$的卡方分布，与一定置信度下的$\chi^2_0$比较进行比较

### 7.2 任意分布的抽样

#### 7.2.1 离散型随机变量

对于随机变量序列$X_1,X_2,...,X_n$，对应的概率分别为$p_1,p_2,...,p_n$，定义累积概率：
$$
\xi_0=0, \ \xi_i=\sum_{j=1}^{i}p_j
$$

在$[0,1)$中随机抽样得到$x^*$,如果满足：
$$
\xi_{k-1}<x^*<\xi_k
$$
那么此时抽样得到的随机变量为$X_k$

#### 7.2.2 连续随机变量：

##### 7.2.2.1 直接抽样法（反函数法）

对于$[a,b]$区间上概率密度函数为$f(x)$的随机变量$X$,分布函数为$\xi = F(\eta)=\int_a^\eta f(x)dx$，如果反函数$F^{-1}(\xi)$存在，$\xi$是$[0,1]$上均匀分布的随机变量，$\eta=F^{-1}(\xi)$是满足概率密度的采样方式

##### 7.2.2.2 变换抽样法

> 假设随机变量$X$的概率密度函数为$f(x)$，随机变量$y=y(x)$的概率密度函数为$g(y)$，根据概率密度函数的定义：
> $$
> f(x)dx=g(y)dy\\
> g(y)=f(x)\frac{\partial x}{\partial y}
> $$

因此，对于两个分布和抽样已知的随机变量$u,v$，可以将$x,y$的联合密度函数通过雅可比行列式变换到他们上面去：
$$
f(x,y)=g(u,v)\frac{\partial(u,v)}{\partial (x,y)}=g(u,v)\left|\begin{array}{cc}\frac{\partial u}{\partial x}&\frac{\partial u}{\partial y}\\\frac{\partial v}{\partial x}&\frac{\partial v}{\partial y}\end{array}\right|
$$
对$u,v$进行采样，得到独立$X,Y$​

> e.g. 高斯函数的抽样
>
> 对于满足高斯函数的分布，由于无法得到解析形式的积分结果，对于两个相互独立的均匀分布变量$u,v$，分布函数满足$g(u,v)=1$，利用积分变换法：
> $$
> \begin{cases}
> x=\sqrt{-2\ln u}\cos(2\pi v)\\
> y=\sqrt{-2\ln u}\sin(2\pi v)
> \end{cases}
> $$
> 反解得到：
> $$
> \begin{cases}
> u=e^{-\frac{x^2+y^2}{2}}\\
> v=\arctan(\frac yx)
> \end{cases}
> $$
> 因此：
> $$
> f(x,y)=g(u,v)\frac{\partial(u,v)}{\partial (x,y)}=\frac{1}{2\pi}e^{\frac{x^2+y^2}{2}}=f(x)\cdot f(y)
> $$
> 得到两个独立的高斯函数相乘，因此对于每一个高斯函数的采样只需要均匀采样$u,v$，计算得到$x,y$，就是满足高斯分布的采样  

##### 7.2.2.3 舍选抽样法

**第一类舍选采样法：**

对于$[a,b]$区间上概率密度函数为$f(x)$的随机变量$X$，$f(x)$存在最大值：
$$
L=\max_{x\in [a,b]}f(x)
$$
可以通过下面步骤进行采样：

+ 在$[0,1)$上均匀采样得到$\xi_1$，进行线性转化：
  $$
  \delta = a+\xi_1(b-a)
  $$

+ 再次在$[0,1)$上均匀采样得到$\xi_2$

+ 如果$\xi_2<f(\delta)/L$则保留采样值$\delta$不然舍弃

**第二类舍选法**

假如抽样的函数$f(x)$具有较为尖锐的峰不利于采样，可以用第二类舍选法进行采样：
$$
f(x)=L\cdot \frac{f(x)}{L\cdot h(x)}=L\cdot g(x)\cdot h(x)
$$
其中$L=\max_{x\in[a,b]}\frac{f(x)}{h(x)}$，将对$f(x)$的抽样转化到一个更加容易抽样的函数$h(x)$上面，此时将$h(x)$可以看成是概率密度函数：

+ 对$h(x)$采样得到$\eta_h$
+ 判断$random.random()<g(\eta_h)$是否成立
+ 如果成立，$\eta_h$可以作为$f(x)$的一个采样；如果不成立则重新从第一步开始采样

第一类舍选法采样是第二类舍选法$L=1$时候的特例

**第三类舍选法**

对第二类舍选法进一步推广，假如随机变量$X,Y$的联合密度函数是$g(x,y)$，所需要的采样假如可以表示为：
$$
f(x)=L\cdot \int_{-\infty}^{h(x)}g(x,y)dy\\
L=\frac{1}{\int_{-\infty}^{+\infty}\int_{-\infty}^{h(x)}g(x,y)dxdy}
$$

+ 根据联合密度函数采样得到$\eta_x,\eta_y$
+ 判断$\eta_y<h(\eta_x)$​是否成立
+ 如成立则选取$\eta_x$作为$f(x)$的一个采样值，如不成立返回第一步进行采                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             样

第三类舍选法成立只需要证明：
$$
P(\eta\leq x)=P(\eta_x\leq x| \eta_y\leq h(\eta_x))
$$


$$
\begin{aligned}
RHS &= \frac{\int_{-\infty}^{x}\int_{-\infty}^{h(t_1)}g(t_1,t_2)dt_2dt_1}{\int_{-\infty}^{+\infty}\int_{-\infty}^{h(t_1)}g(t_1,t_2)dt_2dt_1}\\
&=L\cdot \int_{-\infty}^{x}\int_{-\infty}^{h(t_1)}g(t_1,t_2)dt_2dt_1=LHS
\end{aligned}
$$




### 7.3 蒙特卡洛方法的应用

#### 7.3.1 蒙特卡洛方法计算积分

对于一些均匀分割无法充分采样的函数，如下图所示函数$f(x)=\sin^2(\frac{1}{x(2-x)})$：

![image-20240412202132020](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240412202132020.png)

对于被积函数，在积分区间$[a,b]$和区间上的最大值$L$构成覆盖区间的长方形面积为$A$，充分均匀投点$N$次，对于函数区间内投点采样：
$$
I=\frac{k}{N}\cdot A
$$
可以将这个采样看成是一个二项分布，落入或者不落入在函数范围内的概率是$\frac{I}{A},1-\frac{I}{A}$，因此得到$k$的涨落为：
$$
\sigma^2=Np(1-p)=N\frac{I}{A}(1-\frac{I}{A})
$$
得到积分的涨落为：
$$
\sigma(I)=\frac AN\sigma(k)=\sqrt{\frac{I(A-I)}{N}}
$$
从平衡均值角度解释蒙特卡洛算法积分，函数$f(x)$在区间$[a,b]$上的平均值为：
$$
<f>=\frac1{a-b}\int_a^bf(x)dx=\frac I{a-b}
$$
在积分区间上随机选取$N$个点$\xi_i$：
$$
<f>=\frac1N\sum_{i=1}^{N}f(\xi_i)\\
I=\frac{a-b}{N}\sum_{i=1}^{N}f(\xi_i)
$$
两边同时求方差：
$$
\sigma^2(I)=\frac{(b-a)^2}{N^2}\cdot N \cdot\sigma^2(f)
$$
因此类似与投点法，标准差反比于$\sqrt{N}$，比例系数系数跟函数的平坦程度有关；对于多维情况，看成$m$维超立方体的体积：
$$
I=\prod_{j=1}^{m}(b_j-a_j)[\sum_{i=1}^Nf(\xi_{1i},...,\xi_{mi})]
$$
此时标准差依然反比于$\sqrt{N}$

**重要抽样法：**

对于不平坦的函数$f(x)$，通过重要抽样法对函数进行转化：
$$
I=\int_a^bf(x)dx=\int_a^b\frac{f(x)}{g(x)}\cdot g(x)dx=\int_a^bf^*(x)\cdot g(x)dx
$$
通过已知且容易抽样的概率密度函数$g(x)$进行抽样得到$\xi_i$，$g(x),f(x)$的函数形式相接近，函数形式变的平坦
$$
I=\frac{a-b}{N}\sum_{i=1}^{N}f^*(\xi_i)\\
Var(I)=\frac{(b-a)^2}{N^2}\cdot N \cdot\sigma^2(f^*)<\frac{(b-a)^2}{N^2}\cdot N \cdot\sigma^2(f)
$$

#### 7.3.2 蒙特卡洛方法在统计物理上的应用

假如系统的哈密顿量为$H(\mathrm{X})$，密度分布函数的形式为$f(\mathrm{X})$，配分函数为$Z$，多维积分空间为$\Omega$​则有：
$$
Z=\int_\Omega f(H(\mathrm{X}))d\mathrm{X}
$$
物理量$A(\mathrm{X})$的平均值为：
$$
<A>=\frac1Z\int_\Omega A(\mathrm{X})f(H(\mathrm{X}))d\mathrm{X}
$$
也就是需要对满足概率密度函数为$\frac1Z
f(H(\mathrm{X}))$的函数进行采样，从而获得物理量的值

##### 7.3.2.1 **马尔科夫链：**

马尔科夫链具有无记忆的性质，下一状态的概率分布仅有当前的状态决定，同时状态转移在热平衡状态下具有细致平衡条件：
$$
w(x,x')P(x)=w(x',x)P(x')
$$

#### 7.3.2.2 Metropolis-Hastings 算法

状态$x,x'$分别具有能量$E,E'$，状态转移的概率为：
$$
P_{E\rightarrow E'}=\begin{cases}
1, \ E'< E\\
e^{-\beta(E'-E)}, \ E'\geq E
\end{cases}
$$
通过产生$[0,1]$上的随机数和$P_{E\rightarrow E'}$比较决定是否需要保留新的状态

#### 7.3.3 蒙特卡洛方法在量子力学中的应用

通过路径积分将传播子写成Boltzmann形式：
$$
{G(x,-i\tau,x,0)=A\int dx_1dx_2\cdots dx_nexp\Big[-\sum_{k=0}^nE(x_{k+1},\tau_{k+1},x_k,\tau_k)\Delta\tau/h\Big]}
$$
将基态波函数用传播子表示：
$$
|\psi_0(  {x})|^2=\frac{1}{  {Z}}\lim_{\tau\to\infty}\int  {dx}_1  {dx}_2\cdots  {dx}_n\exp\Big[-\sum_{  {k=0}}^  {n}  {E}(  {x}_{  {k+1}},\tau_{  {k+1}},  {x}_{  {k}},\tau_{  {k}})\Delta\tau/  {h}\Big]
$$

#### 7.3.4 模拟退火算法

将函数看成是一个统计系综的配分函数，假设基态能级为$E_0=0$当温度$T$向绝对零度冷却时，所有粒子向着最低能级凝聚：
$$
P_{E_i}=\begin{cases}
1,E_0=0\\
0,E_i>0\\
\end{cases}
$$
模拟退火的基本步骤：

+ 初始时选择一个较高的温度作为预热， e.g.  $\delta E=0.1$量级，选择初始温度$T_0=10.0$，状态转移的接受概率$P\thickapprox0.99$

+ 选择较为缓慢的温度冷却趋势，比如选择指数变化：
  $$
  T(t)=T_0e^{-t/\tau}
  $$

+ 选择合适的$\tau$，e.g. $\tau=10000$，每次状态更新之后降低温度直达最低温度

#### 7.3.5 随机行走的生长（DLA）算法

**DLA 算法的的模拟规则：**

+ 1 首先构造 2 维的方形点阵，在点阵中央原点处放置一个粒子作为生长的种子；
+ 2 从距原点足够远处释放一个试探粒子，让它作二维随机行走；
+ 3 如果该粒子走到种子或者已经跟种子聚集的的相邻位置，那么让粒子链接到种子团簇上；
+ 4 如果粒子走到大于起始圆的更远处 (如 2-3 倍的半径处)，这时认为粒子走了一条无用的轨迹，取消该粒子；
+ 5 不断重复以上过程以生成足够大尺寸形状。

## Lecture 8. 非线性问题与非传统方法

### 8.1 线性到非线性

线性系统具有以下两个性质：

+ 叠加性：$f(x+y)=f(x)+f(y)$
+  齐次性：$f(\alpha x)=\alpha f(x)$​

两条性质可以合并为：$f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$

常见的非线性系统可以进行简单分类：

+ 迭代映射：$x_{n+1}=f(x_n)$

+ 微分方程组：
  $$
  \begin{cases}
  \dot{x_1}=f_1(x_1,x_2,...,x_n)\\
  \dot{x_2}=f_2(x_1,x_2,...,x_n)\\
  ...\\
  \dot{x_n}=f_n(x_1,x_2,...,x_n)\\
  \end{cases}
  $$

### 8.2 离散的迭代映射

#### 8.2.1 离散迭代不动点的稳定性

不动点$x^*$满足：
$$
x^*=f(x^*)
$$
可以用微扰来分析不动点的稳定性，在不动点附近做扰动$x_n=x^*+\eta_n$，迭代之后：
$$
\begin{aligned}
x_{n+1}&=f(x_n)=f(x^*+\eta_n)=f(x^*)+f'(x^*)\eta_n+o(\eta_n^2)\\
&=x^*+\eta_{n+1},\ \eta_{n+1}=f'(x^*)
\end{aligned}\eta_n
$$
根据$\lambda=f'(x^*)$与1的大小关系判断不动点的稳定性，若$\abs{\lambda}<1$则不动点稳定；若$\abs{\lambda}>1$则不动点不稳定；若$\abs{\lambda}=1.0$则需要通过分析更加高阶的导数来判断

#### 8.2.2 逻辑斯蒂方程

逻辑斯蒂方程的离散形式可以写成：
$$
x_{n+1}=r\cdot x_n (1-x_n)
$$
不同$r$值下，在蛛网图中会出现不同的迭代情况，如下图所示：

![demo](C:\Users\Administrator\Desktop\demo.png)

可以看到会先出现灭绝，然后出现收敛到不动点，如出现分支，随后出现混沌现象，之后迎来短暂的周期，最后回到混沌

对于出现分叉现象，可以通过解方程$f(f(x))=x$来求解两个点，利用多项式除法除去两个不动点后得到二次方程，求解得到：
$$
x_{1,2}=\frac{r+1\pm \sqrt{(r-3)(r+1)}}{2r}
$$
对于四分叉现象，需要考察二分叉点的稳定性：
$$
\lambda=\frac{d}{dx}f(f(x))=f'(f(x))f'(x),\ f(x_i)=x_j(i,j=1,2,i\neq j)
$$
所以：
$$
\begin{aligned}
\lambda=f'(x_1)f'(x_2)&=r(1-2x_1)\cdot r(1-2x_2)\\
&=-r^2+2r+4\\
\end{aligned}
$$
$\abs{\lambda}<1.0$时二分叉稳定，不然会开始出现四分叉现象，带入$\lambda$的值解出$3.0<r<1+\sqrt 6$时二分叉稳定 

对于更多的周期性和无穷多周期的混沌现象时，引入**李雅普诺夫指数**来描述混沌，给定初值$x_0$和初始扰动$\delta_0$，多次迭代后存在偏离$\delta_n$，则Lyapunov指数$\lambda$的定义式为：
$$
\abs{\delta_n}=\abs{\delta_0}e^{n\lambda}
$$
当$\lambda$为正数时，迭代对于初值的敏感性很高，会发生混沌

从$\lambda$的定义出发计算：
$$
\begin{aligned}
\lambda&=\frac1n\ln\abs{\frac{\delta_n}{\delta_0}}\\
&=\frac1n\ln\abs{\frac{f^n(x_0+\delta_0)-f^n(x_0)}{\delta_0}}\\
&=\frac 1n\ln \abs{(f^n)'(x_0)}
\end{aligned}
$$
对复合函数$(f^n)'$导数的计算：
$$
(f^n)'(x_0)=f'(f^{n-1}(x_0))(f^{n-1})'(x_0)=...=\prod_{i=0}^{n-1}f'(f^{i}(x)),\ (f^0(x)=x)
$$
其中迭代$i$次后的$f^i(x)=x_i$，因此Lyapunov指数可以通过每一步迭代的导数来计算：
$$
\begin{aligned}
\lambda &=\frac 1n\ln \abs{(f^n)'(x_0)}\\
&=\frac 1n \ln\prod_{i=0}^{n-1}\abs{f'(x_i)}\\
&=\frac 1n \sum_{i=1}^{n-1}\ln\abs{f'(x_i)}
\end{aligned}
$$
Lyapunov指数小于0时处在稳定周期中；Lyapunov指数大于0时，系统出于混沌状态

### 8.3 非线性微分方程

#### 8.3.1 二维非线性系统

考虑二维的非线性系统：
$$
\begin{cases}
\dot{x}=f(x,y)\\
\dot{y}=g(x,y)\\
\end{cases}
$$
非线性方程组的不动点满足：
$$
f(x^*,y^*)=0,\ g(x^*,y^*)=0
$$
对于不动点的稳定性，需要关注不动点对应的Jacobi矩阵：
$$
\mathrm{A}=\frac{\partial (f,g)}{\partial (x,y)}
$$
求解$\mathrm{A}$的特征值，当 $\mathrm{A}$ 的两个特征值为$\lambda_1,\lambda_2$，那么：

+ 排斥子：当$\lambda_1,\lambda_2$均有正的实部时，意味着都要逃离这个不动点；

+ 吸引子：当$\lambda_1,\lambda_2$均有负的实部时，意味着都要靠近这个不动点；

+ 鞍点：当 $\lambda_1,\lambda_2$分别有正的和负的实部，意味着有进有出；

+ 中心：当$\lambda_1,\lambda_2$​分别是纯的虚数，意味着轨道围绕该点运动；

> e.g. 洛伦兹方程
>
> 洛伦兹方程用于描述天气体系：
> $$
> \begin{cases}
> \begin{aligned}&\dot{{x}}=\sigma({y-x})\\&\dot{{y}}={rx-y-xz}\\&\dot{{z}}={xy-bz}\end{aligned}
> \end{cases} \ \ \ (\sigma , r, b >0)
> $$
> 通过计算可以说明洛伦兹系统的收缩性：
> $$
> \begin{aligned}
> \text{V}& =\int_{ {V}}(\nabla\cdot{\vec{ {f}}}) {dV} \\
> &=\int_{ {V}}\Big(\frac{\partial}{\partial {x}}\Big[\sigma( {y-x})\Big]+\frac{\partial}{\partial {y}}\Big[ {rx-y-xz}\Big]+\frac{\partial}{\partial {z}}\Big[ {xy-bz}\Big]\Big) {dV} \\
> &=- \sigma-1- {b}<0
> \end{aligned}
> $$
> 发现洛伦兹方程存在三个不动点：
>
> $(0,0,0),(\sqrt{b(r-1)},\sqrt{b(r-1)},r-1),(-\sqrt{b(r-1)},-\sqrt{b(r-1)},r-1)$
>
> 分析对应的洛伦兹矩阵：
> $$
> \mathrm A=\begin{pmatrix}-\sigma&\sigma&0\\[2ex] r- z&-1&- x\\[2ex] y& x&- b\end{pmatrix}
> $$
> 对于$(0,0,0)$而言$r>1$是鞍点，$r<1$​是稳定的吸引子
>
> 对于剩下两个不动点也可以做类似的讨论









