# 平衡态统计力学

## 1. 最可几分布法与Maxwell-Boltzmann分布

###  1.1 粒子按照能级分布的约束条件

$$
\begin{aligned}
\sum_{\lambda}a_\lambda=N\\
\sum_{\lambda}\epsilon_\lambda a_\lambda=E
\end{aligned}
$$



 其中 $\lambda$表示能级， $\{a_\lambda\}$表示粒子数按能级分布的一种可能
 
$$
P(\{a_\lambda\})\propto W(\{a_\lambda\})
$$

其中 $P$是微观分布 $\{a_\lambda\}$出现的可能性， $W(\{a_\lambda\})$表示围观分布 $\{a_\lambda\}$可能的状态数（等概率原理）

 ### 1.2 Maxwell-Bolztmann分布

$$
W(\{a_\lambda\})=\frac{N!}{\prod_{\lambda}a_\lambda}\prod_{\lambda}g_\lambda^{a_\lambda}
$$

其中 $\frac{N!}{\prod_{\lambda}a_\lambda}$一项表示粒子可以在能级间相互交换， $\prod_{\lambda}g_\lambda^{a_\lambda}$一项表示粒子可以在能级内相互交换

求 $W\{a_\lambda\}$的最大值等价于求 $lnW\{a_\lambda\}$的最大值，利用拉格朗日乘子法考虑约束条件求最大值：

$$
-\sum_{\lambda}(ln\frac{a_\lambda}{g_\lambda}+\alpha+\beta\epsilon_\lambda)\delta a_\lambda=0
$$

其中已经利用的 $Stirling$公式： $  lnN! = N(lnN-1)\ (N\rightarrow \infty)$

得到 $Maxwell-Bolztmann$分布的表达式：

$$
\widetilde{a_\lambda}=g_\lambda e^{-\alpha-\beta\epsilon_\lambda}
$$

### 1.3 宏观热力学量表达式

定义配分函数 $Z$：

$$
Z=\sum_{\lambda}g_\lambda e^{-\beta \varepsilon_\lambda}\\
$$

相关的宏观物理学量由统计关系得出：

$$
\begin{aligned}
& E = -N\frac{\partial}{\partial \beta}lnZ\\
& \overline{Y_l}= -\frac{N}{\beta}\frac{\partial}{\partial y_l}lnZ\\
& S = Nk(lnZ-\beta\frac{\partial}{\partial \beta}lnZ)
\end{aligned}
$$

特别的，对于 $p-V$关系，在第三个式子中 $y_l=-V:p=-\frac{N}{\beta}\frac{\partial}{\partial V}lnZ$

### 1.4 经典极限

$$
Z=\sum_{n=0}^{\infty}e^{-\beta \varepsilon_n} \xrightarrow{\frac{\varDelta \varepsilon_n}{kT}\ll 1}Z=\int \cdots \int \frac{dq_1 \cdots dq_r dp_1 \cdots dp_r}{h^r}e^{-\beta \varepsilon}=\int \frac{d\omega}{h^r}e^{-\beta \varepsilon}
$$

其中 $\frac{d\omega}{h^r}$可以看成是某种形式上的态密度，而 $e^{-\beta \varepsilon}$可以看成是这个态密度的占据概率

## 2.  德拜固体理论

### 2.1 简正模密度

波矢 $\mathbf{k}=(n_1,n_2,n_3)$，$k=\abs{\mathbf{k}}$，存在关系：

$$
\omega=2\pi\nu=ck
$$

简正模密度计算：

$$
G(\nu)=\int_0^\nu g(\nu')d\nu'
$$

由$(9)$式可以得到：

$$
n_1^2+n_2^2+n_3^2\leq (\frac{L}{c}\nu)^2
$$

偏振态密度的积分可以转化为求对应球的体积，考虑具有两个偏振方向：

$$
G(\nu)=2\times\frac{4\pi}{3}(\frac{L\nu}{c})^3=\frac{8\pi V}{3c^3}\nu^3\\
g(\nu)=G'(\nu)=\frac{8\pi V}{c^3}\nu^2
$$

### 2.2 德拜固体理论

德拜将固体看成弹性介质，可以传播弹性波，包括具有两个偏振方向的横波以及具有一个偏振的纵波，此时简正模密度：

$$
g(\nu)=2\times \frac{4\pi V}{3c_t^2}\nu^2d\nu+1\times \frac{4\pi V}{3c_1^2} \nu^2 d\nu
$$

其中 $c_t,c_1$分别是横波和纵波的传播速度，假设 $c_t=c_1=c$，$g(\nu)=\frac{4\pi V}{c^2}\nu^2 d\nu$，德拜截止频率 $\nu_D$由下式给出，这里对简正模的积分应该等于整体的自由度，在三维空间中具有 $3N$个运动自由度：

$$
\int_0^{\nu_D}g(\nu)d\nu=3N\\
\nu_D^3=N\frac{9c^2}{4\pi V}
$$

频率为 $\nu$的的谐振子的平均能量由下面的计算给出（ $Z$是单粒子配分函数）：

$$
Z=\sum_{n=1}^{\infty}e^{-\beta(n+\frac{1}{2})h\nu} = \frac{e^{-\beta h\nu/2}}{1-e^{-\beta h \nu}}\\
\overline{\varepsilon(\nu)}=-\frac{\partial}{\partial \beta}lnZ=\frac{1}{2}h\nu+\frac{h\nu}{e^{h\nu /kT}-1}
$$

总能量 $\overline E$由$(13)$和$(15)$式给出：

$$
\overline{E}=\int_0^{\nu_D}\overline{\varepsilon(\nu)}g(\nu)d\nu=\frac{4\pi V}{c^2}\int_0^{\nu_D}\frac{h\nu^3}{e^{h\nu \beta}-1}d\nu
$$

讨论两种极端情况：

> **高温极限， $\beta \rightarrow 0$ ：**
> 
> $$
> e^{h\nu \beta}-1=h\nu \beta\\
> \overline{E}=\frac{4\pi V}{c^2}\int_0^{\nu_D}\frac{h\nu^3}{e^{h\nu \beta}-1}d\nu=\frac{4\pi V}{c^2 }\int_0^{\nu_D}kT\nu^2d\nu+E_0=\frac{4\pi VkT}{3c^2}\nu_D^3+E_0=3NKT+E_0
> $$
> 
> 此时的固体热容与经典理论一致：
> 
> $$
> C_V=\frac{\partial \overline E}{\partial T}=3NK
> $$
> 

>**低温极限， $\beta \rightarrow \infty,\nu_D \rightarrow \infty$：**
>
>$$
>\overline{E}=\frac{4\pi V}{c^2}\int_0^{\infty}\frac{h\nu^3}{e^{h\nu \beta}-1}d\nu\overset{x=h\nu \beta}{=}\frac{4\pi V}{c^2}(\frac{kT}{h\nu})^4\int_0^{\infty}\frac{x^3}{e^x-1}dx
>$$
>
> $\int_0^{\infty}\frac{x^3}{e^x-1}dx$是一个常数，此时热容满足：
>
>$$
>C_V=\frac{\partial \overline E}{\partial T}\propto T^3
>$$
>
>在低温情况下德拜固体理论解出的固体热容与利用声子气体的公式解出的关系一样，正比于 $T^3$，系数略有差别

德拜固体理论可以推广到 $n$维空间的情况，需要修改的地方是：（1）求解简正模密度的时候需要计算 $n$维球的体积（2）对简正模密度积分时，自由度变为 $nN$

## 3. 量子统计I：费米分布与玻色分布

 ### 3.1 费米统计与玻色统计

与 $Maxwell-Bolztmann$统计类似，费米统计与玻色统计按能级分布的 $\{a_\lambda\}$都满足约束条件：

$$
\begin{aligned}
\sum_{\lambda}a_\lambda=N\\
\sum_{\lambda}\epsilon_\lambda a_\lambda=E
\end{aligned}
$$


> **费米统计**的可能微观状态数：
> 
> $$
> W(\{a_\lambda\})=\mathbf{C}_{g_\lambda}^{a_\lambda}=\frac{g_\lambda !}{a_\lambda !(g_\lambda-a_\lambda)!}
> $$
> 
> 上式满足泡利不相容原理，不可能有两个粒子占据同一个量子态，对应的最可几分布：
> 
> $$
> a_\lambda=\frac{g_\lambda}{e^{\alpha+\beta \varepsilon_\lambda}+1}
> $$

> **玻色统计**的可能微观状态数：
> 
> $$
> W(\{a_\lambda\})=\frac{(g_\lambda+a_\lambda-1)!}{a_\lambda !(g_\lambda-1)!}
> $$
> 
> 玻色统计不需要满足$Pauli$不相容原理，利用隔板法划分，分母利用了隔板法，分子表示了同一隔板内粒子的全同性和隔板的全同，对应的对应的最可几分布：
> 
> $$
> a_\lambda=\frac{g_\lambda}{e^{\alpha+\beta \varepsilon_\lambda}-1}
> $$

### 3.2 量子统计配分函数

费米统计和玻色统计的配分函数：

$$
Z=\prod_{\lambda}(1\pm e^{-\alpha-\beta \varepsilon_\lambda})^{\pm g_\lambda}
$$

 $+,-$号分别对应费米统计和玻色统计，常用的是：
 
$$
lnZ=\pm \sum_{\lambda}g_\lambda\ ln(1\pm e^{-\alpha\pm\beta \varepsilon_\lambda})
$$

**粒子数、化学势的计算：**

$$
\bar N=-\frac{\partial }{\partial \alpha }lnZ
$$

由于体积 $V$是广延量，一般 $\bar N=-\frac{\partial }{\partial \alpha }lnZ\propto V$， $n=\frac{\bar N}{V}$，可以通过 $n=f(\alpha,\beta)$将 $\alpha=-\frac{\mu}{kT}=-\mu\beta$反解出来，从而进一步得到化学势；其余对应的热力学统计量与 $MB$分布的形式基本一致，熵的表达式变为：

$$
S = k(lnZ-\alpha\frac{\partial}{\partial \alpha}lnZ-\beta\frac{\partial}{\partial \beta}lnZ)
$$

### 3.3 量子巨正则系综

巨正则系综配分函数：

$$
\Xi=\sum_{N=0}^{\infty}\sum_se^{-\alpha N-\beta \varepsilon_{Ns}}
$$

用巨正则系综推导量子统计的核心是用 $\{a_\lambda\}$代替 $N,s$来表示求和：

$$
\Xi=\sum_{\{a_\lambda\}}W(\{a_\lambda\})e^{-\sum_\lambda(\alpha+\beta \varepsilon_\lambda)}
$$

上式表示对所有的 $\{a_\lambda\}$求和， $W(\{a_\lambda\})=\prod_\lambda W_\lambda$：

$$
W(\{a_\lambda\})=
\begin{cases}
\frac{g_\lambda !}{a_\lambda !(g_\lambda-a_\lambda)!}\ \ (Fermions)\\
\ \\
\frac{(g_\lambda+a_\lambda-1)!}{a_\lambda !(g_\lambda-1)!}\ \ (Bosons)
\end{cases}
$$

因此：

$$
\begin{aligned}
\Xi& =\sum_{\{a_\lambda\}}W(\{a_\lambda\})e^{-\sum_\lambda(\alpha+\beta \varepsilon_\lambda)}\\
   & =\sum_{\{a_\lambda\}}\prod_\lambda W_\lambda\ e^{-\sum_\lambda(\alpha+\beta \varepsilon_\lambda)}\\
   & =\prod_\lambda[\sum_{a_\lambda}W_\lambda e^{-(\alpha+\beta \varepsilon_\lambda)a_\lambda}]\\
   & =\prod_\lambda \Xi_\lambda
\end{aligned}
$$

利用二项式定理求和：

$$
\begin{aligned}
\Xi_\lambda&=\sum_{a_\lambda}W_\lambda e^{-(\alpha+\beta \varepsilon_\lambda)a_\lambda}\\
&=
\begin{cases}
(1+e^{-\alpha-\beta \varepsilon_\lambda})^{g_\lambda} \ \ (Fermions)\\
\ \\
(1-e^{-\alpha-\beta \varepsilon_\lambda})^{-g_\lambda} \ \ (Bosons)
\end{cases}
\end{aligned}
$$

推出量子配分函数同**3.2**中最可几分布法推导的表达式，可以求出每一个能级的粒子平均占据数：

$$
\overline {a_\lambda}=-\frac{\partial}{\partial \alpha}ln\Xi_\lambda=\frac{g_\lambda}{e^{\alpha+\beta \varepsilon_\lambda} \pm 1}
$$

利用最可几分布法推导 $Fermi-Dirac$分布和 $Bose-Einstein$分布时候用到了小量近似，但是利用巨正则系综推导量子统计的分布时，并没有利用小量近似，而是通过严格计算得到.
