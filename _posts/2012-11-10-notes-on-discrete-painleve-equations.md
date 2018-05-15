---
title: Notes on Discrete Painlevé Equations
author: aaditya prakash
layout: post
permalink: "/2012/11/notes-on-discrete-painleve-equations/"
categories:
- math
- research
tags:
- Nonlinear Systems
- Notes
date: 2012-11-10 00:00:00 +0000
---
Painlevé equations are used to solve non-linear second order differential equation. For more on Painleve&#8217;s work <a title="Painlevé's Works" href="http://www.math.h.kyoto-u.ac.jp/~takasaki/soliton-lab/chron/painleve.html" target="_blank">see this</a> and for short refresher on Painlevé equations, <a title="Painlevé's Equations" href="http://www.encyclopediaofmath.org/index.php/Painlev%C3%A9_equation" target="_blank">Encylopedia of Mathmematics</a>.

This note concerns more on the Discrete derivatives of Painlevé&#8217;s Equations.

Integratibility is not a well defined term. Poincaré&#8217;s definition of Integrabiliy is &#8211; to integrate a DE is to find for the general solution, a finite expression, in a finite number of funtions. i.e Solution should be a single value.

Soliton Systems for e.g are single valued :  
<img src='http://s0.wp.com/latex.php?latex=%5Cforall+x+%28+x+%5Cepsilon+Domain%29+%5CRightarrow+1+%5Crightarrow+1+%2C+1+%5Crightarrow+M+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\forall x ( x \epsilon Domain) \Rightarrow 1 \rightarrow 1 , 1 \rightarrow M ' title='\forall x ( x \epsilon Domain) \Rightarrow 1 \rightarrow 1 , 1 \rightarrow M ' class='latex' />

Multi valued functions of a complex variable have branch points, i.e critical points. While implies critical singularities of a linear ODE are fixed

We can derive new functions from Non-linear equations :  
<img src='http://s0.wp.com/latex.php?latex=%7Bw%7D%27%3D%5Cfrac%7Bw-w%5E%7B3%7D%7D%7Bz%28z%2B1%29%7D+%2C+w%280%29+%3D+c+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='{w}&#039;=\frac{w-w^{3}}{z(z+1)} , w(0) = c ' title='{w}&#039;=\frac{w-w^{3}}{z(z+1)} , w(0) = c ' class='latex' />  
**solution**: <img src='http://s0.wp.com/latex.php?latex=w%28z%29+%3D+c+%5Csqrt%7B%5Cfrac%7B1%2Bz%7D%7B1%2Bc%5E%7B2%7Dz%7D%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='w(z) = c \sqrt{\frac{1+z}{1+c^{2}z}} ' title='w(z) = c \sqrt{\frac{1+z}{1+c^{2}z}} ' class='latex' />  
Singular at <img src='http://s0.wp.com/latex.php?latex=z+%3D+-1+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='z = -1 ' title='z = -1 ' class='latex' /> is said to be fixed.

e.g  
1. <img src='http://s0.wp.com/latex.php?latex=%7Bw%7D%27+%2B+w%5E%7B2%7D+%3D+0+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='{w}&#039; + w^{2} = 0 ' title='{w}&#039; + w^{2} = 0 ' class='latex' />  
**solution**: <img src='http://s0.wp.com/latex.php?latex=w+%3D+%28z-z_%7B0%7D%29%5E%7B-1%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='w = (z-z_{0})^{-1} ' title='w = (z-z_{0})^{-1} ' class='latex' />  
2. <img src='http://s0.wp.com/latex.php?latex=2%7Bw%7D%27%2Bw%5E%7B3%7D+%3D+0+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='2{w}&#039;+w^{3} = 0 ' title='2{w}&#039;+w^{3} = 0 ' class='latex' />  
**solution**: <img src='http://s0.wp.com/latex.php?latex=w+%3D+%28z-z_%7B0%7D%29%5E%7B%5Cfrac%7B-1%7D%7B2%7D%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='w = (z-z_{0})^{\frac{-1}{2}} ' title='w = (z-z_{0})^{\frac{-1}{2}} ' class='latex' />

Singularities of a nonlinear systems generally do not show Painlevé Property*

***Painlevé Property**  
An ODE is said to possess the Painlevé property if all its solution are single valued. Beauty of having this property is it allows the transformation of Painlevé Equations into Riccati Equations, which could be solved using known techniques.  
Riccati Equations are fo the form :

<img src='http://s0.wp.com/latex.php?latex=%7Bw%7D%27+%3D+aw%5E%7B2%7D+%2B+bw+%2B+c+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='{w}&#039; = aw^{2} + bw + c ' title='{w}&#039; = aw^{2} + bw + c ' class='latex' /> &#8212; (I)

Painlevé Classified Equatios into 6 types (Transcedants). They were mostly forgotten but their revival was necessitated after soliton systems.

[<img class="size-medium wp-image-192 " title="painlevé equations" src="http://aaditya.info/blog/wp-content/uploads/2012/11/painleve-equations-300x147.png" alt="painlevé equations" width="NaN" height="NaN" />][1]

&nbsp;

Dicrete Painlevé was discovered mostly due to efforts on Quantum Gravity. See <a title="Discrete Painleve in Quantum Gravity" href="http://projecteuclid.org/DPubS/Repository/1.0/Disseminate?view=body&id=pdf_1&handle=euclid.cmp/1104248588" target="_blank">Discrete Painlevé equations and their appearance in quantum gravity by AS Fokas et al.</a>

On discretisation, Riccati Equation given above at  (I) becomes

<img src='http://s0.wp.com/latex.php?latex=%7Bx%7D%27+%3D+%28x_%7Bn%2B1%7D+-+x_%7Bn%7D%29+%5CDelta+t+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='{x}&#039; = (x_{n+1} - x_{n}) \Delta t ' title='{x}&#039; = (x_{n+1} - x_{n}) \Delta t ' class='latex' /> 

A caveat though, Non-linear discretisation is not unique and may result in incorrect functions. Discretisation should be fo rational form and have homographic mapping. There are more than 20 discrete Painlevé Equations.

Solutions to Discrete Painlevé Equations can be found <a title="Solutions to Discrete Painleve Equations" href="http://www.sciencedirect.com/science/article/pii/S0898122101001808" target="_blank">on this paper by A.Ramani et al</a>

 [1]: http://aaditya.info/blog/wp-content/uploads/2012/11/painleve-equations.png