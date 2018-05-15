---
title: Monte Carlo Simulation in R
author: aaditya prakash
layout: post
permalink: "/2012/11/monte-carlo-simulation-in-r/"
categories:
- computer science
- math
tags:
- R
- statistics
date: 2012-11-19 00:00:00 +0000
---
While the last post dealt with Bootstrap Sampling, no sampling discussion can be complete without discussion &#8216;Monte Carlo&#8217; simulation. Readers please note, I will **not **discuss &#8220;MCMC (Markov Chain Monte Carlo)&#8221; *(perhaps in the future)*. MCMC primarily deals with distribution of equilibrium of the given Markov Chain.

Monte Carlo simulation is much used *(perhaps overused)* sampling for all physical simulation techniques. While the algorithm for generating Monte Carlo samples is very simple, its usage is widespread. Particularly in Computational Physics for modeling behavior of sub-atomic particles, in Robotics for generating possible states where the actual game state could be exponentially large and in bioinformatics for probabilistic graphical models and last but not least Monte Carlo Integration.

Readers not familiar with Monte Carlo may benefit from this <a href="http://www.cs.otago.ac.nz/cosc453/student_tutorials/monte_carlo.pdf" title="Tutorial on Monte Carlo" target="_blank">tutorial by Jonathan Pengelly</a>, as this blogpost restricts to presenting the simple code in R to do Monte Carlo simulation. Having a clean and grounds-up code is always beneficial as this helps tweak and reformulate the basics.

Following is the output obtained from the code given below:

### Output

<img class="size-medium wp-image-192 " title="Monte Carlo in R" src="http://aaditya.info/blog/wp-content/uploads/2012/11/Monte_Carlo_Simulation_in_R.png" alt="Monte Carlo in R" width="NaN" height="NaN" />

### Code

<div class="wp_syntax">
  <table>
    <tr>
      <td class="line_numbers">
        <pre>1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
</pre>
      </td>
      
      <td class="code">
        <pre class="rsplus" style="font-family:monospace;"><span style="color: #228B22;">#Monte Carlo simulation </span>
<span style="color: #228B22;">#aaditya - 26/10/2012</span>
&nbsp;
<span style="color: #228B22;">######################################</span>
StartEq <span style="color: #080;">=</span> <span style="color: #ff0000;">100</span>
SuccessPcnt <span style="color: #080;">=</span> <span style="color: #ff0000;">61.54</span>
SuccessAvg <span style="color: #080;">=</span> <span style="color: #ff0000;">2444.78</span>
FailureAvg <span style="color: #080;">=</span> <span style="color: #ff0000;">1667.37</span>
Iterations <span style="color: #080;">=</span> <span style="color: #ff0000;">1000</span>
NoOfEvents <span style="color: #080;">=</span> <span style="color: #ff0000;">100</span>
Rf <span style="color: #080;">=</span> <span style="color: #ff0000;">1</span>
<span style="color: #228B22;">#####################################</span>
eq<span style="color: #080;">&lt;-</span><span style="color: #0000FF; font-weight: bold;">rep</span><span style="color: #080;">&#40;</span>NA, NoOfEvents<span style="color: #080;">&#41;</span>
&nbsp;
doMCRun <span style="color: #080;">&lt;-</span> <span style="color: #0000FF; font-weight: bold;">function</span><span style="color: #080;">&#40;</span><span style="color: #080;">&#41;</span> <span style="color: #080;">&#123;</span>
  eq<span style="color: #080;">&#91;</span><span style="color: #ff0000;">1</span><span style="color: #080;">&#93;</span> <span style="color: #080;">&lt;-</span> StartEq
  <span style="color: #0000FF; font-weight: bold;">for</span><span style="color: #080;">&#40;</span>i <span style="color: #0000FF; font-weight: bold;">in</span> <span style="color: #ff0000;">2</span><span style="color: #080;">:</span>NoOfEvents<span style="color: #080;">&#41;</span> <span style="color: #080;">&#123;</span>
    <span style="color: #0000FF; font-weight: bold;">if</span><span style="color: #080;">&#40;</span><span style="color: #0000FF; font-weight: bold;">runif</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">1</span>,<span style="color: #ff0000;"></span>,<span style="color: #ff0000;">100</span><span style="color: #080;">&#41;</span><span style="color: #080;">&lt;</span> SuccessPcnt<span style="color: #080;">&#41;</span>
      pl<span style="color: #080;">=</span> SuccessAvg <span style="color: #080;">*</span> Rf
    <span style="color: #0000FF; font-weight: bold;">else</span>
      pl<span style="color: #080;">=</span> <span style="color: #080;">-</span><span style="color: #ff0000;">1</span><span style="color: #080;">*</span>FailureAvg <span style="color: #080;">*</span> Rf
      eq<span style="color: #080;">&#91;</span>i<span style="color: #080;">&#93;</span> <span style="color: #080;">=</span> eq<span style="color: #080;">&#91;</span>i<span style="color: #080;">-</span><span style="color: #ff0000;">1</span><span style="color: #080;">&#93;</span>  <span style="color: #080;">+</span> pl
  <span style="color: #080;">&#125;</span>
  <span style="color: #0000FF; font-weight: bold;">return</span><span style="color: #080;">&#40;</span>eq<span style="color: #080;">&#41;</span>
<span style="color: #080;">&#125;</span>
&nbsp;
values <span style="color: #080;">&lt;-</span> <span style="color: #0000FF; font-weight: bold;">replicate</span><span style="color: #080;">&#40;</span>Iterations, doMCRun<span style="color: #080;">&#40;</span><span style="color: #080;">&#41;</span><span style="color: #080;">&#41;</span>
&nbsp;
<span style="color: #0000FF; font-weight: bold;">par</span><span style="color: #080;">&#40;</span>xaxs<span style="color: #080;">=</span><span style="color: #ff0000;">"i"</span><span style="color: #080;">&#41;</span>
<span style="color: #0000FF; font-weight: bold;">plot</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">1</span><span style="color: #080;">:</span>NoOfEvents, <span style="color: #0000FF; font-weight: bold;">rep</span><span style="color: #080;">&#40;</span>NA, NoOfEvents <span style="color: #080;">&#41;</span>, 
     xlab<span style="color: #080;">=</span><span style="color: #ff0000;">"Iterations"</span>, ylab<span style="color: #080;">=</span><span style="color: #ff0000;">"Growth"</span>,
     ylim<span style="color: #080;">=</span><span style="color: #0000FF; font-weight: bold;">c</span><span style="color: #080;">&#40;</span><span style="color: #0000FF; font-weight: bold;">min</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#41;</span>,<span style="color: #0000FF; font-weight: bold;">max</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#41;</span><span style="color: #080;">&#41;</span>,
     xlim<span style="color: #080;">=</span><span style="color: #0000FF; font-weight: bold;">c</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">1</span>,NoOfEvents<span style="color: #080;">&#41;</span>, main<span style="color: #080;">=</span><span style="color: #ff0000;">"Monte Carlo Simulation"</span><span style="color: #080;">&#41;</span>
<span style="color: #0000FF; font-weight: bold;">matlines</span><span style="color: #080;">&#40;</span>values,type<span style="color: #080;">=</span><span style="color: #ff0000;">"l"</span>,lty<span style="color: #080;">=</span><span style="color: #ff0000;">1</span><span style="color: #080;">&#41;</span>
&nbsp;
sd1 <span style="color: #080;">=</span> <span style="color: #0000FF; font-weight: bold;">sd</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#91;</span>NoOfEvents,<span style="color: #080;">&#93;</span><span style="color: #080;">&#41;</span>
mean1 <span style="color: #080;">=</span> <span style="color: #0000FF; font-weight: bold;">mean</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#91;</span>NoOfEvents,<span style="color: #080;">&#93;</span><span style="color: #080;">&#41;</span>
<span style="color: #0000FF; font-weight: bold;">print</span><span style="color: #080;">&#40;</span><span style="color: #0000FF; font-weight: bold;">summary</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#91;</span>NoOfEvents,<span style="color: #080;">&#93;</span><span style="color: #080;">&#41;</span><span style="color: #080;">&#41;</span>
sdString <span style="color: #080;">=</span> <span style="color: #0000FF; font-weight: bold;">paste</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">"SD : "</span>, sd1<span style="color: #080;">&#41;</span>
<span style="color: #0000FF; font-weight: bold;">write</span><span style="color: #080;">&#40;</span>sdString, <span style="color: #0000FF; font-weight: bold;">file</span><span style="color: #080;">=</span><span style="color: #ff0000;">""</span><span style="color: #080;">&#41;</span>
outputString <span style="color: #080;">=</span> <span style="color: #0000FF; font-weight: bold;">paste</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">"With 99.73% confidence the final growth will be between"</span>, 
                     mean1 <span style="color: #080;">-</span> <span style="color: #ff0000;">3</span><span style="color: #080;">*</span>sd1, <span style="color: #ff0000;">" and "</span>, mean1 <span style="color: #080;">+</span> <span style="color: #ff0000;">3</span><span style="color: #080;">*</span>sd1<span style="color: #080;">&#41;</span> 
<span style="color: #0000FF; font-weight: bold;">write</span><span style="color: #080;">&#40;</span>outputString, <span style="color: #0000FF; font-weight: bold;">file</span><span style="color: #080;">=</span><span style="color: #ff0000;">""</span><span style="color: #080;">&#41;</span></pre>
      </td>
    </tr>
  </table>
</div>