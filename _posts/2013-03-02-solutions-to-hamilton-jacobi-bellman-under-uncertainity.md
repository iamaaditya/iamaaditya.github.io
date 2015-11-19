---
title: Solutions to Hamilton-Jacobi-Bellman under uncertainity
author: aaditya prakash
layout: post
permalink: /2013/03/solutions-to-hamilton-jacobi-bellman-under-uncertainity/
categories:
  - math
  - research
tags:
  - research
---
After doing some reading on decision under un-certainity, I get the feeling that this I will be looking more into this. More so because I have the feeling like there is more to this field, lot of unknowns yet(which is still partly due to my lack of profound knowledge in the field). I feel this field is yet to mature.

Solution to Hamilton-Jacobi-Bellman (great story on how the -Bellman part was added to the equation) has been worked by several researchers, but I am looking into the prospect of applying the same under &#8216;uncertainity&#8217;.

The problem:  
\\[   V(x(0), 0) = \min\_u  \int\_0^T C[x(t),u(t)]\,dt + D[x(T)] \\]
  
The Solution:  
\\[  \dot{V}(x,t) + \min_u ( \nabla V(x,t) \cdot F(x, u) + C(x,u) ) = 0 \\]
  
usual constraints and conditions apply, full description at <a title="Hamilton-Jacobi-Equation" href="http://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi%E2%80%93Bellman_equation" target="_blank">this wiki page</a>

Last one month, I did some work; tried my hand with varies forms of solution. I looked into Stochastic Approaches in CFD simulations (Stochastic collocation), Chebyshev Polynomials, Galerkin Approximation, Pontryagin Maximum Principle). But I have failed and right now in life other priorities (grad-school applications) is keeping me from giving another serious look. (This work was part of the reason why no blog posts for a whole month).

I want to come back to this topic and work more, in the meantime, I am making note of some of the papers and materials I referred and will be doing so again in the near future.

### Light introduction and derivation of Hamilton-Jacobi-Bellman

Ian Mitchell

http://www.cs.ubc.ca/~mitchell/Class/CS532M.2007W2/Talks/hjbSham.pdf

*general read*

### Stochastic Perron&#8217;s method for Hamilton-Jacobi-Bellman equations

Bayraktar et al

http://arxiv.org/abs/1212.2170

* new approach *

### Hamilton-Jacobi-Bellman Equations &#8211; Analysis and Numerical Analysis

Iain Smears

http://www.maths.dur.ac.uk/Ug/projects/highlights/PR4/Smears\_HJB\_report.pdf

* Complete Thesis *

### Stochastic Approaches To Uncertainity Quantification In CFD Simulations

Mathelin et al

http://perso.limsi.fr/Individu/mathelin/research/NumUNC_MHZ.pdf

* Inspiration from CFD *

### Solution of Hamilton Jacobi Bellman Equations

Navasca et al

http://people.clarkson.edu/~cnavasca/KN1.pdf

* using Pontryagin maximum principle *

### Potential use of Ito lemma

See <a title="Ito's Lemma" href="http://en.wikipedia.org/wiki/It%C5%8D_calculus#It.C5.8D.27s_lemma" target="_blank">this equation</a>
