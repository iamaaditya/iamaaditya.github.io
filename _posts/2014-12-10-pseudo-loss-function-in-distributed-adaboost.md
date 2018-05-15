---
title: 'Pseudo loss function in distributed Adaboost'
author: aaditya prakash
layout: post
permalink: /2014/12/pseudo-loss-function-in-distributed-adaboost/
categories:
  - computer science
  - math
tags:
  - algorithms
  - machine learning
---
This is the sketch of proof of correctness of <img src='http://s0.wp.com/latex.php?latex=L_%7BHedge%28%5Cbeta%29%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='L_{Hedge(\beta)} ' title='L_{Hedge(\beta)} ' class='latex' />, pseudo loss function, in the case of distributed boosting algorithm. It has been known that boosting of functions with each applicator with more than 0.5 accuracy is sufficient to guarantee lowest minimum accuracy in iterative pooling. A similar sketch is presented for the distributed case where the score from each stage is not shared across all the computing nodes. While this guarantees the correctness, it does not guarantee the convergence, which is still a highly sought after problem in distributed algorithm.

For people uninitiated in the problem, it is highly advised to [read this paper][1] or for much simpler and faster read, [these slides][2].

## Notations

<img src='http://s0.wp.com/latex.php?latex=w+%3D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='w = ' title='w = ' class='latex' /> weights Vector

<img src='http://s0.wp.com/latex.php?latex=T+%3D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='T = ' title='T = ' class='latex' /> Number of iterations

<img src='http://s0.wp.com/latex.php?latex=%5Cbeta&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\beta' title='\beta' class='latex' /> = Parameter <img src='http://s0.wp.com/latex.php?latex=%5Cepsilon%5B0%2C1%5D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\epsilon[0,1] ' title='\epsilon[0,1] ' class='latex' />  
  
<img src='http://s0.wp.com/latex.php?latex=%5Cell%5E%7Bt%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\ell^{t} ' title='\ell^{t} ' class='latex' />= Loss Vector for the <img src='http://s0.wp.com/latex.php?latex=t+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='t ' title='t ' class='latex' /> iteration (trials)

N = Total Number of weak learners

<img src='http://s0.wp.com/latex.php?latex=%7BL_i%3D+%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='{L_i= } ' title='{L_i= } ' class='latex' />Strategy i&#8217;s cumulative loss = <img src='http://s0.wp.com/latex.php?latex=%5Csum_%7Bt%3D1%7D%5E%7BT%7D%5Cell_%7Bi%7D%5E%7Bt%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\sum_{t=1}^{T}\ell_{i}^{t} ' title='\sum_{t=1}^{T}\ell_{i}^{t} ' class='latex' />  
  
<img src='http://s0.wp.com/latex.php?latex=L_%7BA%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='L_{A} ' title='L_{A} ' class='latex' />= Algorithm A&#8217;s total cumulative loss = <img src='http://s0.wp.com/latex.php?latex=%5Csum_%7Bt%3D1%7D%5E%7BT%7D%5Cmathbf%7Bp%7D%5E%7Bt%7D.%5Cell%5E%7Bt%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\sum_{t=1}^{T}\mathbf{p}^{t}.\ell^{t} ' title='\sum_{t=1}^{T}\mathbf{p}^{t}.\ell^{t} ' class='latex' />

&nbsp;

## Algorithm

Consider the following Algorithm

Hedge(<img src='http://s0.wp.com/latex.php?latex=%5Cbeta+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\beta ' title='\beta ' class='latex' />) :

Do for t = 1, 2, &#8230;, *T*

1. Choose Allocation

\\[  
\mathbf{p}^{t}=\frac{\mathbf{w}^{t}}{\sum\_{i-1}^{N}w\_{i}^{t}}  
\\]

2. Receive loss vector <img src='http://s0.wp.com/latex.php?latex=%5Cell%5E%7Bt%7D%5Cepsilon%5B0%2C1%5D%5E%7BN%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\ell^{t}\epsilon[0,1]^{N} ' title='\ell^{t}\epsilon[0,1]^{N} ' class='latex' /> from environment

3. Suffer loss <img src='http://s0.wp.com/latex.php?latex=%5Cmathbf%7Bp%7D%5E%7Bt%7D.%5Cell%5E%7Bt%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\mathbf{p}^{t}.\ell^{t} ' title='\mathbf{p}^{t}.\ell^{t} ' class='latex' />

4. Set the new weights

\\[  
w\_{i}^{t+1}=w\_{i}^{t}\beta^{\ell_{i}^{t}}  
\\]

## To Prove

\\[  
ln(\sum\_{i=1}^{N}w\_{i}^{T+1})\leq-(1-\beta)L_{Hedge(\beta)}  
\\]

## Proof

From the Hedge(<img src='http://s0.wp.com/latex.php?latex=%5Cbeta+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\beta ' title='\beta ' class='latex' />) function, we know that

\\[  
\sum\_{i=1}^{N}w\_{i}^{t+1}=\sum\_{i=1}^{N}w\_{i}^{t}\beta^{\ell_{i}^{t}}  
\\]

For <img src='http://s0.wp.com/latex.php?latex=%5Calpha%5Cgeq0+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\alpha\geq0 ' title='\alpha\geq0 ' class='latex' /> and <img src='http://s0.wp.com/latex.php?latex=r%5Cepsilon%5B0%2C1%5D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='r\epsilon[0,1] ' title='r\epsilon[0,1] ' class='latex' />, by convexity we know that  
<img src='http://s0.wp.com/latex.php?latex=%5Calpha%5E%7Br%7D%5Cleq1-%281-%5Calpha%29r&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\alpha^{r}\leq1-(1-\alpha)r' title='\alpha^{r}\leq1-(1-\alpha)r' class='latex' />, therefore above eqn can be rewritten  
as,

\\[  
\sum\_{i=1}^{N}w\_{i}^{t+1}\leq\sum\_{i=1}^{N}w\_{i}^{t}(1-(1-\beta)\ell_{i}^{t})  
\\]

\\[  
\sum\_{i=1}^{N}w\_{i}^{t+1}\leq\left(\sum\_{i=1}^{N}w\_{i}^{t}\right)(1-(1-\beta)\mathbf{p}^{t}.\ell_{i}^{t})  
\\]

For all the trials <img src='http://s0.wp.com/latex.php?latex=t%3D1%2C%5Cldots%2CT+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='t=1,\ldots,T ' title='t=1,\ldots,T ' class='latex' />

\\[  
\sum\_{i=1}^{N}w\_{i}^{t+1}\leq\prod_{t=1}^{T}(1-(1-\beta)\mathbf{p}^{t}.\ell^{t}  
\\]

(since <img src='http://s0.wp.com/latex.php?latex=1%2Bx%5Cleq+e%5E%7Bx%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='1+x\leq e^{x} ' title='1+x\leq e^{x} ' class='latex' /> )

\\[  
\sum\_{i=1}^{N}w\_{i}^{t+1}\leq exp\left(-(1-\beta)\sum_{t=1}^{T}\mathbf{p}^{t}.\ell^{t}\right)  
\\]

Taking log on both sides

\\[  
ln\left(\sum\_{i=1}^{N}w\_{i}^{t+1}\right)\leq-(1-\beta)\sum_{t=1}^{T}\mathbf{p}^{t}.\ell^{t}  
\\]

Taking negative sign and switching the equality

\\[  
(1-\beta)\sum\_{t=1}^{T}\mathbf{p}^{t}.\ell^{t}\leq ln\left(\sum\_{i=1}^{N}w_{i}^{t+1}\right)  
\\]

\\[  
\sum\_{t=1}^{T}\mathbf{p}^{t}.\ell^{t}\leq\frac{ln\left(\sum\_{i=1}^{N}w_{i}^{t+1}\right)}{(1-\beta)}  
\\]

Now from the definition of <img src='http://s0.wp.com/latex.php?latex=L_%7BA%7D+%3D+%5Csum_%7Bt%3D1%7D%5E%7BT%7D%5Cmathbf%7Bp%7D%5E%7Bt%7D.%5Cell%5E%7Bt%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='L_{A} = \sum_{t=1}^{T}\mathbf{p}^{t}.\ell^{t} ' title='L_{A} = \sum_{t=1}^{T}\mathbf{p}^{t}.\ell^{t} ' class='latex' />,  
since the algorithm here is Hedge(<img src='http://s0.wp.com/latex.php?latex=%5Cbeta+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\beta ' title='\beta ' class='latex' />), where <img src='http://s0.wp.com/latex.php?latex=%5Cbeta+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\beta ' title='\beta ' class='latex' />is the  
parameter, <img src='http://s0.wp.com/latex.php?latex=L_%7BA%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='L_{A} ' title='L_{A} ' class='latex' />, is called as <img src='http://s0.wp.com/latex.php?latex=L_%7BHedge%28%5Cbeta%29%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='L_{Hedge(\beta)} ' title='L_{Hedge(\beta)} ' class='latex' />

therefore,

\\[  
L\_{Hedge(\beta)}\leq\frac{ln\left(\sum\_{i=1}^{N}w_{i}^{t+1}\right)}{(1-\beta)}  
\\]

<p style="text-align: right;">
  <span style="text-decoration: underline;">QED</span>
</p>

 [1]: http://www-users.cs.umn.edu/~aleks/papers/kdd_01.pdf
 [2]: http://www-users.cs.umn.edu/~banerjee/Teaching/Spring06/talks/Paper02Tim1.ppt
