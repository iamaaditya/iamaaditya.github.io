---
title: 'Pascal&#8217;s Triangle in Standard ML'
author: aaditya prakash
layout: post
permalink: /2013/01/pascal-triangle-in-sml/
categories:
  - computer science
tags:
  - programming
  - SML
---
It has been a while that I posted something (grad school applications !). For past few weeks I have been learning Standard ML (SML), my first foray into functional programming language. I must say, I was skeptical at first due to &#8216;no-state&#8217; concept but it is turning out to be great experience. Recursion can only be appreciated when you have to write programs without loop. This makes me rethink about learning Scala and Haskell.

For a nice 73 slide introduction on SML <a href="http://courses.cs.vt.edu/~cs3304/Spring02/lectures/lect04.pdf" title="Introduction to SML" target="_blank">see this</a>. One of power of SML lies in doing proofs. For those who are already intiated with SML, you might want to look <a href="https://github.com/agentcoops/SML-Proof-Manipulation" title="SML Proof Manipulation" target="_blank">SML Proof Manipulation</a>. If you want to learn how to start writing proofs in SML then here is a nice tutorial on the same [Implementing Constructive Proof Rules for SML in MetaSML][1]

I like to write Pascal&#8217;s triangle as my generic hello world program. Given below is my attempt at pascal&#8217;s triangle, a beautiful binomial expansion tree. Though I will confess that this is not the most elegant solution to Pascal&#8217;s triangle but I have considered readibility over conciseness.

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
</pre>
      </td>
      
      <td class="code">
        <pre class="pascal" style="font-family:monospace;">fun choose<span style="color: #009900;">&#40;</span>r <span style="color: #000066;">:</span> int<span style="color: #000066;">,</span> k <span style="color: #000066;">:</span> int<span style="color: #009900;">&#41;</span> <span style="color: #000066;">=</span> 
    <span style="color: #000000; font-weight: bold;">if</span> k <span style="color: #000066;">=</span> <span style="color: #cc66cc;">1</span> <span style="color: #000000; font-weight: bold;">then</span> r
    <span style="color: #000000; font-weight: bold;">else</span> <span style="color: #000000; font-weight: bold;">if</span> k <span style="color: #000066;">=</span> <span style="color: #cc66cc;"></span> orelse k <span style="color: #000066;">=</span> r <span style="color: #000000; font-weight: bold;">then</span> <span style="color: #cc66cc;">1</span>
    <span style="color: #000000; font-weight: bold;">else</span> choose<span style="color: #009900;">&#40;</span>r<span style="color: #000066;">-</span><span style="color: #cc66cc;">1</span><span style="color: #000066;">,</span>k<span style="color: #009900;">&#41;</span> <span style="color: #000066;">+</span> choose<span style="color: #009900;">&#40;</span>r<span style="color: #000066;">-</span><span style="color: #cc66cc;">1</span><span style="color: #000066;">,</span>k<span style="color: #000066;">-</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#41;</span>
&nbsp;
fun pascal_triangle<span style="color: #009900;">&#40;</span>x <span style="color: #000066;">:</span> int<span style="color: #009900;">&#41;</span> <span style="color: #000066;">=</span>
    <span style="color: #000000; font-weight: bold;">if</span> <span style="color: #009900;">&#40;</span>x &lt;<span style="color: #000066;">=</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#41;</span> <span style="color: #000000; font-weight: bold;">then</span> <span style="color: #009900;">&#91;</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#93;</span>
    <span style="color: #000000; font-weight: bold;">else</span>
        let fun count <span style="color: #009900;">&#40;</span>from<span style="color: #000066;">:</span>int<span style="color: #009900;">&#41;</span> <span style="color: #000066;">=</span>
            <span style="color: #000000; font-weight: bold;">if</span> from<span style="color: #000066;">=</span>x <span style="color: #000000; font-weight: bold;">then</span> <span style="color: #cc66cc;">1</span><span style="color: #000066;">::</span><span style="color: #009900;">&#91;</span><span style="color: #009900;">&#93;</span> <span style="color: #000000; font-weight: bold;">else</span> choose<span style="color: #009900;">&#40;</span>x<span style="color: #000066;">,</span>from<span style="color: #009900;">&#41;</span> <span style="color: #000066;">::</span> count<span style="color: #009900;">&#40;</span>from<span style="color: #000066;">+</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#41;</span>            
        <span style="color: #000000; font-weight: bold;">in</span> count<span style="color: #009900;">&#40;</span><span style="color: #cc66cc;"></span><span style="color: #009900;">&#41;</span><span style="color: #000066;">::</span>pascal_triangle<span style="color: #009900;">&#40;</span>x<span style="color: #000066;">-</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#41;</span>
    <span style="color: #000000; font-weight: bold;">end</span></pre>
      </td>
    </tr>
  </table>
</div>

*Note while the &#8220;choose&#8221; function could have been written as nested function inside &#8220;pascal_triangle&#8221; (like the &#8220;count&#8221; function), for the reasons of simplicity and comprehension I have put is as separate code. Same goes for the parenthesis around attributes, which are not required by the compiler.

 [1]: http://www.cs.bham.ac.uk/research/projects/poplog/paradigms_lectures/Theorem.html "Proofs in SML"