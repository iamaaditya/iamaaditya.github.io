---
title: Why Simulated Annealing works
author: aaditya prakash
layout: post
permalink: "/2012/10/why-simulated-annealing-works/"
categories:
- computer science
- research
tags:
- research
- simulated annealing
date: 2012-10-07 00:00:00 +0000
---
Of all optimization methods, **Simulated Annealing** is one of the most fascinating one. If you need a quick refresher in Simulated Annealing then see <a title="Slides on Simulated Annealing" href="http://www.slideshare.net/KirillNetreba/simulated-annealing-5880806" target="_blank">this slide</a>. Is Simulated Annealing better than other techniques in finding the global optima ? Perhaps. I will discuss why I think it is one of the best optimization technique and why so.

Simulated Annealing is another example of use of <a title="Value of Interdisciplinary Research" href="http://aaditya.info/blog/2012/09/value-of-interdisciplinary-research/" target="_blank">Interdisciplinary research</a>, about which I wrote two weeks ago. Annealing is a metallurgical process, where heating a metal beyond a critical temperature and slow cooling gives it unique properties (related to lower energy states). Simulated  Annealing is, as the name suggests, simulation of annealing process. Algorithm for Simulated Annealing is very close to real annealing process. Infact the cost function used is same as the distribution underlying the movement of molecules in annealing process, which is Boltzmann distribution.

<p style="text-align: left; padding-left: 180px;">
  P(E) = e<span style="font-size:xx-small; vertical-align:super;">-E/kT</span>
</p>

<p style="text-align: left; padding-left: 180px;">
  where, P(E) = Energy Function associated with Boltzman distribution
</p>

<p style="text-align: left; padding-left: 230px;">
  T = Temperature of the molecule
</p>

<p style="text-align: left; padding-left: 230px;">
  k = Boltzman constant ( 1.380 x 10<span style="font-size:xx-small; vertical-align:super;">-23</span> J/K)
</p>

 Above function gives the probability of molecule at given Temperature, in Simulated Annealing it transcends to the search space. At higher Temperature(T) there is no restriction on the search space and algorithm is free to move anywhere. Certainly this means it will lead to some non-efficient movement across the solution space and perhaps in the wrong direction. As counter-intuitive it may sound,** it is this erratic behaviour that gives Simulated Annealing the power to find global optima** and not get stuck at local optimum.

As the local gradient function will lead the heuristics into the local optima, a non-negligible probability of search iteration moving outside the gradient descent will help push the search agent outside the realm of locality. This ensures that there will be search beyond local descent. Caveat though, this also means that sometimes even when the agent has successfully found the &#8216;best solution&#8217; it will move away from it. This is nature of all non-deterministic and stochastic algorithm and this cannot be dealt with.

Now if there were no way to finally stop this random walk then this method would never reach a solution and the heuristic would be equivalent to random search, but as shown by the energy function above, when the Temperature(T) gradually decreases the movement across solution space is constrained. Gradually it starts behaving like a &#8216;Gradient Descent&#8217;. After critical Temperature (T*<span style="font-size:xx-small; vertical-align:sub;">LOW</span>*), algorithm zeroes on the currently found gradient slope.

Consider a wild case of solution space where the base of Global Optima is very narrow (read lower probability for agent following uniform distribution) and local optimum with broad base. This means any search agent has higher probability of getting stuck at local optimum. For e.g as in the figure below :

<img class="aligncenter" title="Narrow base Global optima" src="http://aaditya.info/blog/wp-content/uploads/2012/10/local-optima.png" alt="Why simulated annealing works" width="250" height="190" />

It is for these kind of search space, Simulated Annealing works and performs much better than other optimization techniques. Certainly this is not the best method for several other solution space requiring more foresighted heuristics. Nevertheless due to this unique property Simulated Annealing is not going to become obsolete very soon.

More <a title="Detailed Overview of Simulated Annealing" href="https://docs.google.com/viewer?a=v&q=cache:Mpqd8-X4CgQJ:163.18.62.64/wisdom/Simulated%2520annealing%2520overview.pdf+&hl=en&gl=in&pid=bl&srcid=ADGEEShBlkIOttIy_eWNnTTFvjfi8lYLm-M0KvuT3YRlCsTal3OWGeX2AsDDaH7mHHe0hKOwMwd5TiYADsqBNP11neoRM2Y_xu9ywf-uP-ewRwACnn_TTXHxu9rIZw-cwF_ZIlljjpsn&sig=AHIEtbQG-nLhngFv7QrvXDa-Chu4T_MPKw" target="_blank">detailed presentation</a> of Simulated Annealing