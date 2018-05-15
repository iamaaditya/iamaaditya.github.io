---
title: Bootstrap sampling in R
author: aaditya prakash
layout: post
permalink: "/2012/11/bootstrap-sampling-in-r/"
categories:
- computer science
- math
tags:
- R
- statistics
date: 2012-11-19 00:00:00 +0000
---
<a href="http://en.wikipedia.org/wiki/Bootstrapping_%28statistics%29" title="Bootstrap Sampling" target="_blank">Bootstrapping </a>is a very useful sampling method. While it&#8217;s robustness is not that simlar to MCMC or Metropolis-Hastings or Landau. Bootstrapping draws from provided distribution with replacement. 

While there are lot of fancy and featured enabled simulation and sampling softwares, nothing is better than writing codes from groudup. While the sampling code given below is not much featured enabled but anyone with some background can easily add the features as they require. The bootstrapping could be used in several scenarios specially when dealing with very large simulation scenario where it becomes infeasible to use deterministic rules to obtain the observables. More importantly while coding for AI where the sample state grows exponentially, simple sampling techniques like Bootstrapping comes into handy.

This blogpost presents the simple code to achieve Bootstrapping in R, readers not familiar with concepts of Bootstrapping will benefit from this <a href="http://people.revoledu.com/kardi/tutorial/Bootstrap/examples.htm" title="Tutorial on Bootstrapping" target="_blank">tutorial with examples via MS Excel</a>.

Following is the output obtained from the code given below:

### Output

<img class="size-medium wp-image-192 " title="Bootstrap in R" src="http://aaditya.info/blog/wp-content/uploads/2012/11/BootStrap_Sampling_in_R.png" alt="bootstrap in R" width="NaN" height="NaN" />

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
44
45
46
47
</pre>
      </td>
      
      <td class="code">
        <pre class="rsplus" style="font-family:monospace;"><span style="color: #228B22;">#Bootstrap </span>
<span style="color: #228B22;">#aaditya - 26/10/2012</span>
&nbsp;
<span style="color: #228B22;">######################################</span>
<span style="color: #0000FF; font-weight: bold;">dt</span> <span style="color: #080;">&lt;-</span> <span style="color: #0000FF; font-weight: bold;">read.<span style="">csv</span></span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">"successRatio.csv"</span>, stringsAsFactors<span style="color: #080;">=</span><span style="color: #0000FF; font-weight: bold;">F</span><span style="color: #080;">&#41;</span>
<span style="color: #228B22;">## successRatio.csv is file which contains samples eg. </span>
<span style="color: #228B22;">## SampleValue (Probabilty)</span>
<span style="color: #228B22;">## -0.0455</span>
<span style="color: #228B22;">## -0.0042</span>
<span style="color: #228B22;">## -0.0456</span>
<span style="color: #228B22;">## -0.0035</span>
<span style="color: #228B22;">## 0.0394</span>
<span style="color: #228B22;">## 0.0094</span>
&nbsp;
StartEq <span style="color: #080;">=</span> <span style="color: #ff0000;">100</span>
Iterations <span style="color: #080;">=</span> <span style="color: #ff0000;">1000</span>
NoOfEvents <span style="color: #080;">=</span> <span style="color: #ff0000;">100</span>
Rf <span style="color: #080;">=</span> <span style="color: #ff0000;">1</span>
<span style="color: #228B22;">####################################</span>
&nbsp;
eq<span style="color: #080;">&lt;-</span><span style="color: #0000FF; font-weight: bold;">rep</span><span style="color: #080;">&#40;</span>NA, NoOfEvents<span style="color: #080;">&#41;</span>
&nbsp;
doBSRun <span style="color: #080;">&lt;-</span> <span style="color: #0000FF; font-weight: bold;">function</span><span style="color: #080;">&#40;</span><span style="color: #080;">&#41;</span> <span style="color: #080;">&#123;</span>
  eq<span style="color: #080;">&#91;</span><span style="color: #ff0000;">1</span><span style="color: #080;">&#93;</span> <span style="color: #080;">&lt;-</span> StartEq
  <span style="color: #0000FF; font-weight: bold;">for</span><span style="color: #080;">&#40;</span>i <span style="color: #0000FF; font-weight: bold;">in</span> <span style="color: #ff0000;">2</span><span style="color: #080;">:</span>NoOfEvents<span style="color: #080;">&#41;</span> <span style="color: #080;">&#123;</span>
    eq<span style="color: #080;">&#91;</span>i<span style="color: #080;">&#93;</span> <span style="color: #080;">=</span> eq<span style="color: #080;">&#91;</span>i<span style="color: #080;">-</span><span style="color: #ff0000;">1</span><span style="color: #080;">&#93;</span>  <span style="color: #080;">*</span> <span style="color: #080;">&#40;</span><span style="color: #ff0000;">1</span> <span style="color: #080;">+</span> <span style="color: #0000FF; font-weight: bold;">sample</span><span style="color: #080;">&#40;</span><span style="color: #0000FF; font-weight: bold;">dt</span>$SampleValue,<span style="color: #ff0000;">1</span><span style="color: #080;">&#41;</span><span style="color: #080;">&#41;</span> <span style="color: #080;">*</span> Rf
  <span style="color: #080;">&#125;</span>
  <span style="color: #0000FF; font-weight: bold;">return</span><span style="color: #080;">&#40;</span>eq<span style="color: #080;">&#41;</span>
<span style="color: #080;">&#125;</span>
&nbsp;
values <span style="color: #080;">&lt;-</span> <span style="color: #0000FF; font-weight: bold;">replicate</span><span style="color: #080;">&#40;</span>Iterations, doBSRun<span style="color: #080;">&#40;</span><span style="color: #080;">&#41;</span><span style="color: #080;">&#41;</span>
&nbsp;
<span style="color: #0000FF; font-weight: bold;">par</span><span style="color: #080;">&#40;</span>xaxs<span style="color: #080;">=</span><span style="color: #ff0000;">"i"</span><span style="color: #080;">&#41;</span>
<span style="color: #0000FF; font-weight: bold;">plot</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">1</span><span style="color: #080;">:</span>NoOfEvents, <span style="color: #0000FF; font-weight: bold;">rep</span><span style="color: #080;">&#40;</span>NA, NoOfEvents <span style="color: #080;">&#41;</span>, 
     xlab<span style="color: #080;">=</span><span style="color: #ff0000;">"Iterations"</span>, ylab<span style="color: #080;">=</span><span style="color: #ff0000;">"Growth"</span>,
     ylim<span style="color: #080;">=</span><span style="color: #0000FF; font-weight: bold;">c</span><span style="color: #080;">&#40;</span><span style="color: #0000FF; font-weight: bold;">min</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#41;</span>,<span style="color: #0000FF; font-weight: bold;">max</span><span style="color: #080;">&#40;</span>values<span style="color: #080;">&#41;</span><span style="color: #080;">&#41;</span>,
     xlim<span style="color: #080;">=</span><span style="color: #0000FF; font-weight: bold;">c</span><span style="color: #080;">&#40;</span><span style="color: #ff0000;">1</span>,NoOfEvents<span style="color: #080;">&#41;</span>, main<span style="color: #080;">=</span><span style="color: #ff0000;">"Bootstrap Sampling"</span><span style="color: #080;">&#41;</span>
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

Extensive list of Bootstrap functions *(SPlus/Unix shell scripts)* can be found at <a href="http://lib.stat.cmu.edu/S/bootstrap.funs" title="Functions for BootStrap" target="_blank">http://lib.stat.cmu.edu/S/bootstrap.funs</a>