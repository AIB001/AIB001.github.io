# Maxwell方程组的洛伦兹协变

## 电磁场张量

$$
{\boldsymbol{F}}^{\mu\nu}=\begin{pmatrix}0 & \frac{E_{x}}{c} & \frac{E_{y}}{c} & \frac{E_{z}}{c} \\ -\frac{E_{x}}{c} & 0 & B_{z} & -B_{y} \\ -\frac{E_{y}}{c} & -B_{z} & 0 & B_{x} \\ -\frac{E_{z}}{c} & B_{y} & -B_{x} & 0\end{pmatrix}
$$

同时存在与 $F^{\mu \gamma}$对偶的场张量 $G^{\mu \gamma}$

## 麦克斯韦方程的场张量形式

$$
\frac{\partial\boldsymbol{F}^{\mu \gamma}}{\partial{x^\gamma}}=\partial_\gamma \boldsymbol{F}^{\mu \gamma} = \mu_0J^\mu
$$

$$
\frac{\partial\boldsymbol{G}^{\mu \gamma}}{\partial{x^\gamma}} = 0 \Leftrightarrow \sum_{\lambda, \mu, \gamma}\partial_\lambda \boldsymbol{F}_{\mu \gamma}
$$

其中下标表示对$\lambda, \mu, \gamma$轮换求和；方程(2)和方程(3)分别对应两个 $Maxwell$方程

## Lorentz协变性证明

####  $\partial_\gamma \boldsymbol{F}^{\mu \gamma} = \mu_0J^\mu$ 协变证明

$$
\partial_\gamma \boldsymbol{F}^{\mu \gamma}=\partial_\gamma \Lambda_\lambda^\mu \Lambda_\sigma^\gamma\boldsymbol{F}^{\mu \gamma}
$$

同时，可以通过链式法则证明，对于四维矢量的梯度$\partial_\mu$也满足Lorentz变化关系式，也就是$\frac{\partial}{\partial x^\mu}$本身构成一个四维矢量，因此可以对(4)继续做Lorentz变换：

$$
\partial_\gamma \boldsymbol{F}^{\mu \gamma}=\partial_\gamma \Lambda_\lambda^\mu \Lambda_\sigma^\gamma\boldsymbol{\bar{F}}^{\lambda \sigma}=\Lambda_\lambda^\mu \Lambda_\sigma^\gamma \Lambda_{\gamma}^\sigma \bar{\partial}_\sigma \boldsymbol{\bar{F}}^{\lambda \sigma}=\Lambda_\lambda^\mu (\Lambda_\sigma^\gamma \Lambda_{\gamma}^\sigma) \bar{\partial}_\sigma \boldsymbol{\bar{F}}^{\lambda \sigma}
$$

括号中是一对正变换和逆变换：

$$
\Lambda_\sigma^\gamma \Lambda_{\gamma}^\sigma = 1
$$

因此：

$$
\partial_\gamma \boldsymbol{F}^{\mu \gamma}=\Lambda_\lambda^\mu \bar{\partial}_\sigma \boldsymbol{\bar{F}}^{\lambda \sigma}
$$

等式两边同时乘上Lorentz逆变换矩阵：

$$
\Lambda_\mu^\lambda \partial_\gamma \boldsymbol{F}^{\mu \gamma}=\bar{\partial}_\sigma \boldsymbol{\bar{F}}^{\lambda \sigma}
$$

利用(2)式：

$$
\Lambda_\mu^{\lambda}\mu_0J^\mu=\mu_0\bar{J}^\mu=\bar{\partial}_\sigma \boldsymbol{\bar{F}}^{\lambda \sigma}
$$

#### $\sum_{\lambda, \mu, \gamma}\partial_\lambda \boldsymbol{F}_{\mu \gamma}$协变证明

$$
\partial_\lambda \boldsymbol{F}_{\mu \gamma}=\Lambda^\mu_\sigma\Lambda^\gamma_\rho\Lambda_\lambda^\kappa\bar{\partial}_\kappa \boldsymbol{\bar{F}}_{\sigma \rho}
$$

对于剩下两个表达式，$\Lambda^\mu_\sigma\Lambda^\gamma_\rho\Lambda_\lambda^\kappa\bar{\partial}_\kappa$交换求和不变，因此：

$$
\sum_{\kappa, \sigma \rho}\bar{\partial}_\kappa \boldsymbol{\bar{F}}_{\sigma \rho}=0
$$
结合(9),(11)，证明了Maxwell方程组具有Lorentz协变.



