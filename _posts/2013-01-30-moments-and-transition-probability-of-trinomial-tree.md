---
title: Moments and transition probability of Trinomial Tree
author: aaditya prakash
layout: post
permalink: "/2013/01/moments-and-transition-probability-of-trinomial-tree/"
categories:
- math
tags:
- probability
date: 2013-01-30 00:00:00 +0000
---
I just switched from using WP-Latex to MathJax since Chrome is soon going to have built-in support for MathJax and it is easier to recover the tex codes for the reader.

To test out the functionality, I wanted to write down some equations befitting to the occasion. I scraped through my notes to see if there was anything interesting and worth posting. I stumbled upon <a href="http://en.wikipedia.org/wiki/Trinomial_tree" title="Trinomial Tree Wiki" target="_blank">Trinomial Tree</a> \( \ddagger \). Now it is not that common and haven&#8217;t seen much usage of Trinomial Tree outside finance (One of the ways for Options Pricing), nonetheless I thought it would be interesting to refresh these formulas, you never know when you might need them again.

Trinomial Tree, a special case of binomial tree where instead of two we have three branches, lets call them Up \( u \) , Middle \( m \) and Down \(d \) . Transition of each step could then be defined as &#8212;  

&nbsp;&nbsp;\\( S(t + \Delta t) = S(t) \times u \\) with probability  \\( p_u \\) 

&nbsp;&nbsp;\\( S(t + \Delta t) = S(t) \times 1 \\) with probability  \\( 1 - p\_u - p\_d \\)

&nbsp;&nbsp;\\( S(t + \Delta t) = S(t) \times d \\) with probability  \\( p_d \\)


For simplicity sake let&#8217;s consider that transition magnitude is same on each side, i.e  
$$ u = e^{\sigma \sqrt{2 \Delta t} } \, , \,\, d = e^{-\sigma \sqrt{2 \Delta t }} \, , \,\, m=1 $$

then the **transition probability** is given by  
$$ p_u = \left ( \frac{e^\frac{r \Delta t}{2} &#8211; e^{-\sigma\sqrt{\frac{r \Delta t}{2}}}}{e^{\sigma\sqrt{\frac{r \Delta t}{2}}} &#8211; e^{-\sigma\sqrt{\frac{r \Delta t}{2}}}} \right ) ^2 $$

$$ p_u = \left ( \frac{ e^{\sigma\sqrt{\frac{r \Delta t}{2}}} + e^\frac{r \Delta t}{2} }{e^{\sigma\sqrt{\frac{r \Delta t}{2}}} &#8211; e^{-\sigma\sqrt{\frac{r \Delta t}{2}}}} \right ) ^2 $$

$$ p\_m = 1 &#8211; p\_u &#8211; p_d $$

from above equations we can derive the **moments **as given below,  
$$ \mathbb{E}[S(t\_{i+1})|S(t\_i)] = e^{r \Delta t}S(t_i) $$

$$ \mathbb{V}ar[S(t\_{i+1})|S(t\_i)] = \Delta t S(t_i)^2 \sigma ^2 + \mathcal{O}(\Delta t^\frac{3}{2}) $$

\\( \ddagger \\) <a href="http://en.wikipedia.org/wiki/Phelim_Boyle" title="Phelim Boyle" target="_blank">Phelim Boyle</a> in 1986.

An excellent<a href="http://www41.homepage.villanova.edu/klaus.volpert/teaching/financial_math/Fall10/Presentations/Trinomial.pptx" title="Background on Trinomial Tree" target="_blank"> 23 slide </a>background on Trinomial including other forms besides Boyle&#8217;s.
