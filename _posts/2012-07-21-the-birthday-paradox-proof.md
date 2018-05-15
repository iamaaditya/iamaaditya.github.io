---
title: The Birthday Paradox &#8211; Proof
author: aaditya prakash
layout: post
permalink: "/2012/07/the-birthday-paradox-proof/"
categories:
- math
tags:
- math
- probability
date: 2012-07-21 00:00:00 +0000
---
### <span style="color: #0000ff;">“In a room of just 23 people there’s a 50% chance of two people having the same birthday.”</span>

Above statement is briefly The Birthday Paradox. If you need more information kindly see  
<a title="Birthday Paradox Explained" href="http://www.damninteresting.com/the-birthday-paradox/" target="_blank"> Short Version</a> or the <a title="Birthday Paradox Explained" href="http://betterexplained.com/articles/understanding-the-birthday-paradox/" target="_blank">Long Version</a> and if you prefer video then <a title="Youtube video birthday paradox explained" href=" http://www.youtube.com/watch?v=98OTsYfTt-c&feature=player_embedded" target="_blank">Birthday Paradox &#8211; Youtube</a>

This article is about the Proof of the same and not the explanation.The proof of this seemingly counter intuitive result has always baffled me.

Following below I present the simplest possible proof of the same with least amount of clutter and redundancy.

*Credit of this proof goes to [Prof. Dan Boneh][1]. I love how simple it is. My LaTeX skills are still nascent so please bear with me. Do notify in case of inaccuracies.*

## **Theorem:**

<address>
  Notations used:
</address>

<address style="padding-left: 30px;">
  n = number of people
</address>

<address style="padding-left: 30px;">
  r = birthday of a given individual
</address>

<address style="padding-left: 30px;">
  Pr= Probability
</address>

<address style="padding-left: 30px;">
  B= number of days in a year (not incl. feb 29th)
</address>

<address>
  given,
</address>

<address style="padding-left: 30px;">
  n = 23, which can be rewritten as &#8212;
</address>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=n%3D1.2%2AB%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='n=1.2*B^{\frac{1}{2}}' title='n=1.2*B^{\frac{1}{2}}' class='latex' />  <em>(Since <img src='http://s0.wp.com/latex.php?latex=B%3D365%5CRightarrow+n%3D1.2%2AB%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D%5Capprox23&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='B=365\Rightarrow n=1.2*B^{\frac{1}{2}}\approx23' title='B=365\Rightarrow n=1.2*B^{\frac{1}{2}}\approx23' class='latex' />)</em>
</p>

*let * <img src='http://s0.wp.com/latex.php?latex=r_%7B1%7D%5Ccdots+r_%7Bn%7D%5Cepsilon&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='r_{1}\cdots r_{n}\epsilon' title='r_{1}\cdots r_{n}\epsilon' class='latex' /> *{1&#8230;B}* be IID integers

<h5 style="text-align: center;">
  <img src='http://s0.wp.com/latex.php?latex=Pr%5B%5Cexists+i%5Cneq+j%3Ar_%7Bi%7D%3Dr_%7Bj%7D%5D%5Cgeq%5Cfrac%7B1%7D%7B2%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='Pr[\exists i\neq j:r_{i}=r_{j}]\geq\frac{1}{2}' title='Pr[\exists i\neq j:r_{i}=r_{j}]\geq\frac{1}{2}' class='latex' />
</h5>

## Proof:

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%5CPr%5B%5Cexists+i%5Cneq+j%3Ar_%7Bi%7D%3Dr_%7Bj%7D%5D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\Pr[\exists i\neq j:r_{i}=r_{j}]' title='\Pr[\exists i\neq j:r_{i}=r_{j}]' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%3D1-Pr%5B%5Cforall+i%5Cneq+j%3Ar_%7Bi%7D%5Cneq+r_%7Bj%7D%5D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='=1-Pr[\forall i\neq j:r_{i}\neq r_{j}]' title='=1-Pr[\forall i\neq j:r_{i}\neq r_{j}]' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%3D1-%5Cfrac%7B%28B-1%29%7D%7BB%7D%5Cfrac%7B%28B-2%29%7D%7BB%7D%5Ccdots%5Cfrac%7B%28B-n%2B1%29%7D%7BB%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='=1-\frac{(B-1)}{B}\frac{(B-2)}{B}\cdots\frac{(B-n+1)}{B}' title='=1-\frac{(B-1)}{B}\frac{(B-2)}{B}\cdots\frac{(B-n+1)}{B}' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%3D1-%5Cprod_+%7Bi%3D1%7D%5E%7Bn-1%7D%281-%5Cfrac%7Bi%7D%7BB%7D%29&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='=1-\prod_ {i=1}^{n-1}(1-\frac{i}{B})' title='=1-\prod_ {i=1}^{n-1}(1-\frac{i}{B})' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=wkt%2C%5Cforall+x%5Cgeq0%2C1-x%5Cleq+e%5E%7B-x%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='wkt,\forall x\geq0,1-x\leq e^{-x}' title='wkt,\forall x\geq0,1-x\leq e^{-x}' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%3D1-%5Cprod_+%7Bi%3D1%7D%5E%7Bn-1%7De%5E%7B%5Cfrac%7B-i%7D%7BB%7D%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='=1-\prod_ {i=1}^{n-1}e^{\frac{-i}{B}}' title='=1-\prod_ {i=1}^{n-1}e^{\frac{-i}{B}}' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%3D1-e%5E%7B-%5Cfrac%7B1%7D%7BB%7D%5Csum%5Climits+_%7Bi%3D1%7D%5E%7Bn-1%7Di%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='=1-e^{-\frac{1}{B}\sum\limits _{i=1}^{n-1}i}' title='=1-e^{-\frac{1}{B}\sum\limits _{i=1}^{n-1}i}' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%3D1-e%5E%7B-%5Cfrac%7B1%7D%7BB%7D%5Cfrac%7Bn%28n-1%29%7D%7B2%7D%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='=1-e^{-\frac{1}{B}\frac{n(n-1)}{2}}' title='=1-e^{-\frac{1}{B}\frac{n(n-1)}{2}}' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%5Cgeq1-e%5E%7B-%5Cfrac%7Bn%5E%7B2%7D%7D%7B2B%7D%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\geq1-e^{-\frac{n^{2}}{2B}}' title='\geq1-e^{-\frac{n^{2}}{2B}}' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%5Cgeq1-e%5E%7B-0.72%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\geq1-e^{-0.72}' title='\geq1-e^{-0.72}' class='latex' /> (since <img src='http://s0.wp.com/latex.php?latex=n%3D1.2B%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D%5CRightarrow%5Cfrac%7Bn%5E%7B2%7D%7D%7B2%7D%3D0.72B%5CRightarrow%5Cfrac%7Bn%5E%7B2%7D%7D%7B2B%7D%3D0.72%29&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='n=1.2B^{\frac{1}{2}}\Rightarrow\frac{n^{2}}{2}=0.72B\Rightarrow\frac{n^{2}}{2B}=0.72)' title='n=1.2B^{\frac{1}{2}}\Rightarrow\frac{n^{2}}{2}=0.72B\Rightarrow\frac{n^{2}}{2B}=0.72)' class='latex' />
</p>

<p style="padding-left: 30px;">
  <img src='http://s0.wp.com/latex.php?latex=%5Cgeq0.513&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\geq0.513' title='\geq0.513' class='latex' />
</p>

<p style="padding-left: 420px;">
  QED
</p>

 You may download the <a title="Birthday Paradox Proof" href="http://aaditya.info/research/birthdayparadoxproof.tex" target="_blank">tex file here</a>.

 [1]: http://crypto.stanford.edu/~dabo/