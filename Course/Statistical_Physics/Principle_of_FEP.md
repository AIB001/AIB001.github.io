# 自由能微扰（FEP）原理

## 1. 系综与系综平均

### 1.1 系综

在林宗涵的《热力学与统计物理学》中对系综做出描述：

> **系综**是假想的、和所研究的系统性质完全相同的、彼此独立、**各自处于某一微观状态**的大量系统的集合.

> 这些微观状态会形成一个分布，哈密顿量 $H(\mathbf p,\mathbf q)$常用于描述这些微观状态

常见的系综有：

+ 微正则系综- $(N,V,E)$系综：保持粒子数、体积、能量不变，下同
+ 正则系综-  $(N,V,T)$系综
+ 巨正则系综-  $(\mu,V,T)$​系综：用于描述开放体系，比如表面吸附过程等
+  $(N,P,T)$系综：常用于生物大分子体系等

### 1.2 系综平均

刘维尔定理：

>将系综在相空间中的运动看成代表点组成流体的运动，这个流体是**不可压缩的**，数学形式：
>
> $$
> \frac{\partial \rho}{\partial t}=\{\rho,H\}\ \ \ \  \ \frac{d\rho}{dt}=0
> $$

上式中大括号表示泊松括号。因此， $\rho(\mathbf p,\mathbf q)$的表达式中不显含时间，对于平衡态，分布函数 $\rho(\mathbf p,\mathbf q)$是相空间中的位形函数。因此，对于系综平均可以用经典概率论中的 $pdf$函数计算，物理量 $u(\mathbf p,\mathbf q,t)$在 $t$时刻的系综平均： 

$$
<u(\mathbf p,\mathbf q,t)> = \iint u(\mathbf p,\mathbf q,t)\rho(\mathbf p,\mathbf q)d\mathbf pd\mathbf q
$$

对于经典正则系综满足麦克斯韦分布：

$$
\rho(\mathbf p,\mathbf q)d\mathbf p d\mathbf q=\frac{e^{-\beta H(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q}{\iint e^{-\beta H(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q }
$$
期中分母正比于配分函数 $Z$：

$$
Z=\frac{1}{h^{r}}\iint e^{-\beta H(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q
$$
因此：


$$
<u(\mathbf p,\mathbf q,t)> = \iint u(\mathbf p,\mathbf q,t) \frac{e^{-\beta H(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q}{\iint e^{-\beta H(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q } d\mathbf p d\mathbf q \overset{h=1}{=} \frac{1}{Z} \iint u(\mathbf p,\mathbf q,t) e^{-\beta H(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q
$$


## 2. 微扰法求解自由能变化

### 2.1 自由能

在正则系综之中，自由能 $F$：

$$
F=-kTlnZ
$$
因此求解自由能变化也就变成了求解各个平衡态下的配分函数：

$$
\Delta F=F_1-F_0=-kTln\frac{\iint e^{-\beta H_1(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q}{\iint e^{-\beta H_0(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q}
$$

其中 $H_0(\mathbf p,\mathbf q),H_1(\mathbf p,\mathbf q)$ 表示的是不同形式的哈密顿量，例如一些项的消失、一些物理常数的变化（比如实际计算过程中使用湮灭的手段让 $\varepsilon_0$等物理常数降低到接近 $0$）

但是在实际问题中，求解配分函数涉及到复杂的各态历经过程，也就是，为了求出配分函数的形式，需要遍历所有可能的微观状态（统计物理的基本假设是所有可能的量子态出现的概率相等）。引用一段看到的话：

>好在很多时候相较于自由能绝对值，我们**只需要了解体系反应过程中自由能的改变数值**，求计算近似的主要目的就是加速解的数值收敛，设法**绕过复杂的遍态历经**

对于在一个短时间内改变的哈密顿量 $(H_0,F_0)\overset{t\ll 1}{\longrightarrow}(H_1,F_1)$，可以构造对系综的微扰来求解自由能变化

### 2.2 微扰法求解

当研究的前后体系变化不大的时候，我们可以用微扰法来得到 $\Delta F$有利于做数值计算的形式，前后系统的变化不大，可以假设：

$$
H_1=H_0+\Delta H
$$

$$
\Delta F_{0\rightarrow 1}=F_1-F_0=-kTln\frac{\iint e^{-\beta (H_0(\mathbf p,\mathbf q)+\Delta H)}d\mathbf p d\mathbf q}{\iint e^{-\beta H_0(\mathbf p,\mathbf q)}d\mathbf p d\mathbf q}=-kTln(\frac{1}{Z}\iint e^{-\beta \Delta H} e^{-\beta H_0(\mathbf p,\mathbf q)} d\mathbf p d\mathbf q)
$$

上式中 $\frac{1}{Z}\iint e^{-\beta \Delta H} e^{-\beta H_0(\mathbf p,\mathbf q)} d\mathbf p d\mathbf q$的形式就是 $e^{-\beta \Delta H}$在哈密顿量 $H_0$下的系综平均，因此：

$$
\Delta F_{0\rightarrow 1} =-kT\ln(<e^{-\beta \Delta H_{0\rightarrow 1}}>_0)
$$
其中下标 $0$表示在哈密顿量 $H_0$的形式下的系综平均。对于这个哈密顿体系，由于具有时间反演性质：

$$
\Delta F_{1\rightarrow 0}=-kT\ln(<e^{-\beta \Delta H_{1\rightarrow 0}}>_1)
$$
由于 $\Delta F_{0\rightarrow 1} = - \Delta F_{1\rightarrow 0},\Delta H_{0\rightarrow 1}=-\Delta H_{0\rightarrow 1}$，因此：

$$
\Delta F_{0\rightarrow 1} =-kT\ln(<e^{-\beta \Delta H_{0\rightarrow 1}}>_0)=kT\ln(<e^{-\beta \Delta H_{1\rightarrow 0}}>_1)=-kT\ln(<e^{-\beta \Delta H_{0\rightarrow 1}}>_1)
$$

### 2.3 数值近似

利用下列两个泰勒关系式，得到在 $H_0$下的系综得到的自由能变化 $\Delta F$的微扰展开表达式：

$$
e^x=\sum_{n=1}^{+\infty}\frac{1}{n!}x^n\\
ln(1+x)=\sum_{n=1}^{+\infty}(-)^n\frac{1}{n}x^n
$$

$$
\begin{aligned}
\Delta F=& -kTln(<e^{-\beta \Delta H}>_0) \\
=&-kTln(1-\beta<\Delta H>_0+\frac{1}{2}\beta^2<\Delta H^2>_0)\\
=&-kT(-\beta <\Delta H>_0+\frac{1}{2}\beta^2<\Delta H^2>_0)+\frac{kT}{2}(-\beta <\Delta H>_0+\frac{1}{2}\beta^2<\Delta H^2>_0)^2\\
=& <\Delta H>_0-\frac{\beta}{2}<\Delta H^2>_0+\frac{\beta}{2}<\Delta H>_0^2+\omicron(<\Delta H>_0^2)=<\Delta H>_0-\frac{\beta}{2}<Var(\Delta H)>_0
\end{aligned}
$$

同样的，在 $H_1$下的系综也可以得到类似的自由能变化，为了不混淆符号不进一步展开。也就是无论从状态 $0$变化到 状态$1$还是从状态 $1$变化到状态 $0$都可以在理论上得到绝对值一样的自由能变化微扰结果。对 $\Delta F=<\Delta H>_0-\frac{\beta}{2}<Var(\Delta H)>_0$讨论，第一项是在 $\Delta H$下的系综平均。第二项反应了系综涨落带来的影响。

对于一个同样大小量级的 $\Delta H$，第一项反映了哈密顿量自身改变带来的影响；第二项则代表了系综涨落对自由能微扰大小的影响。涨落的大小与整个体系的大小相关，在正则系综中，能量涨落 $D(E)\propto\frac{1}{\sqrt{N}}$， $N$为整个体系的粒子数。

利用分子动力学、蒙特卡洛等方法，将较大的微扰转化为较小的微扰的叠加，逐步算出体系自由能的改变。
