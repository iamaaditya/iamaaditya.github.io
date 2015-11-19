---
title: 'Hello &#8216;Lucene&#8217; World &#8211; Web Implementation'
author: aaditya prakash
layout: post
permalink: /2012/10/hello-lucene-world-web-implementation/
categories:
  - computer science
tags:
  - Java
  - Lucene
---
Lucene is a Java Library by Apache used extensively for making custom search engines and indexing. Here are few of the features of Lucene, straight from the <a title="Lucene from Apache" href="http://lucene.apache.org/core/" target="_blank">Lucene&#8217;s homepage</a> :

> <p id="scalable-high-performance-indexing">
>   <strong>Scalable, High-Performance Indexing</strong>
> </p>
> 
>   * over 95GB/hour on modern hardware
>   * small RAM requirements &#8212; only 1MB heap
>   * incremental indexing as fast as batch indexing
>   * index size roughly 20-30% the size of text indexed
> 
> <p id="powerful-accurate-and-efficient-search-algorithms">
>   <strong>Powerful, Accurate and Efficient Search Algorithms</strong>
> </p>
> 
>   * ranked searching &#8212; best results returned first
>   * many powerful query types: phrase queries, wildcard queries, proximity queries, range queries and more
>   * fielded searching (e.g., title, author, contents)
>   * date-range searching
>   * sorting by any field
>   * multiple-index searching with merged results
>   * allows simultaneous update and searching

<div>
  If you want a quick 5 min tutorial on Lucene, <a title="Lucene in 5 min" href="http://www.lucenetutorial.com/lucene-in-5-minutes.html" target="_blank">here you go</a>. Once you seen the structure of Lucene it would be nice to have hello world implementation of it so that you could see it&#8217;s working in the barebone structure. Recently I had the similar problem; while there were numerous examples of Lucene implementation I couldn&#8217;t find the minimal &#8216;hello world&#8217; implementation of web search using Lucene. I am a old-school, to understand working of a new language or library, I like to see the minimal implementation upon which I love to tinker.
</div>

<div>
  Thus, inability to find anything like that made me write one. Therefore I present you &#8220;Hello World&#8221; with Lucene Web interface.
</div>

<div>
  Note:
</div>

<div>
  -You need to have Lucene Library installed and index built (see the 5 min tutorial link above)
</div>

<div>
  -For real application it is not a good and safe practice to write Java inside JSP, instead you use servlets
</div>

<div>
  -This is not intended to be Lucene tutorial or Lucene best practice. This code is minimal required code to have a crude sample web search engine running on Lucene.
</div>

## Code

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
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
</pre>
      </td>
      
      <td class="code">
        <pre class="html4strict" style="font-family:monospace;"><span style="color: #00bbdd;">&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"</span>
<span style="color: #00bbdd;">   "http://www.w3.org/TR/html4/loose.dtd"&gt;</span>
<span style="color: #009900;">&lt;!</span>
<span style="color: #009900;">	Project	:		Lucened Enabled Simple <span style="color: #000066;">Text</span> Search</span>
<span style="color: #009900;">	Author	:		Aaditya Prakash</span>
<span style="color: #009900;">	Date	:		<span style="color: #cc66cc;">25</span>- Sep-<span style="color: #cc66cc;">2012</span> <span style="color: #cc66cc;">16</span>:<span style="color: #cc66cc;">21</span></span>
<span style="color: #009900;">--&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;%@ page import<span style="color: #66cc66;">=</span><span style="color: #ff0000;">"SearchWebCall"</span> %&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">html</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">head</span>&gt;</span>
	<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">title</span>&gt;</span> Lucene Enabled Simple Text Search <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">title</span>&gt;</span>
&nbsp;
	<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">script</span> <span style="color: #000066;">type</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"text/javascript"</span>&gt;</span>
&nbsp;
	<span style="color: #808080; font-style: italic;">&lt;!-- Validation to prevent some characters, </span>
<span style="color: #808080; font-style: italic;">	currently Lucene Doesn't parse these characters --&gt;</span>
			function isSpclChar(){
				var iChars = "!@#^<span style="color: #ddbb00;">&amp;</span>*()+=-[]\\\';,./{}|~`\":<span style="color: #009900;">&lt;&gt;</span>?";
				for (var i = 0; i <span style="color: #009900;">&lt; document.lucene.input.<span style="color: #000066;">value</span>.length; i++<span style="color: #66cc66;">&#41;</span> <span style="color: #66cc66;">&#123;</span></span>
<span style="color: #009900;">					if <span style="color: #66cc66;">&#40;</span>iChars.indexOf<span style="color: #66cc66;">&#40;</span>document.lucene.input.<span style="color: #000066;">value</span>.charAt<span style="color: #66cc66;">&#40;</span>i<span style="color: #66cc66;">&#41;</span><span style="color: #66cc66;">&#41;</span> !<span style="color: #66cc66;">=</span> -<span style="color: #cc66cc;">1</span><span style="color: #66cc66;">&#41;</span> <span style="color: #66cc66;">&#123;</span></span>
<span style="color: #009900;">						<span style="color: #66cc66;">//</span>throwback the unallowed character</span>
<span style="color: #009900;">						document.lucene.input.<span style="color: #000066;">value</span> <span style="color: #66cc66;">=</span> document.lucene.input.<span style="color: #000066;">value</span>.slice<span style="color: #66cc66;">&#40;</span><span style="color: #cc66cc;"></span>,-<span style="color: #cc66cc;">1</span><span style="color: #66cc66;">&#41;</span>;</span>
<span style="color: #009900;">						return false;</span>
<span style="color: #009900;">					<span style="color: #66cc66;">&#125;</span></span>
<span style="color: #009900;">				<span style="color: #66cc66;">&#125;</span></span>
<span style="color: #009900;">			<span style="color: #66cc66;">&#125;</span></span>
&nbsp;
<span style="color: #009900;">	&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">script</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">head</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">body</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">h1</span>&gt;</span>Lucene Enabled Simple Text Search <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">h1</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">form</span> <span style="color: #000066;">name</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"lucene"</span> <span style="color: #000066;">action</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"index.jsp"</span> <span style="color: #000066;">method</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"get"</span>&gt;</span>
		<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">input</span> <span style="color: #000066;">name</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"input"</span> <span style="color: #000066;">size</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"30"</span> <span style="color: #000066;">id</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"input"</span> <span style="color: #000066;">onkeyup</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"isSpclChar()"</span><span style="color: #66cc66;">/</span>&gt;</span>
		<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">br</span> <span style="color: #66cc66;">/</span>&gt;</span>
		<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">input</span> <span style="color: #000066;">type</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"submit"</span> <span style="color: #000066;">value</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"Search"</span> <span style="color: #66cc66;">/</span>&gt;</span>
<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">form</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">br</span> <span style="color: #66cc66;">/</span>&gt;</span>
&nbsp;
<span style="color: #009900;">&lt;%</span>
<span style="color: #009900;">	String searchString<span style="color: #66cc66;">&#91;</span><span style="color: #66cc66;">&#93;</span> <span style="color: #66cc66;">=</span> new String<span style="color: #66cc66;">&#91;</span><span style="color: #cc66cc;">2</span><span style="color: #66cc66;">&#93;</span>;</span>
<span style="color: #009900;">	String result<span style="color: #66cc66;">&#91;</span><span style="color: #66cc66;">&#93;</span> <span style="color: #66cc66;">=</span> new String<span style="color: #66cc66;">&#91;</span><span style="color: #cc66cc;">100</span><span style="color: #66cc66;">&#93;</span>;</span>
<span style="color: #009900;">	searchString<span style="color: #66cc66;">&#91;</span><span style="color: #cc66cc;"></span><span style="color: #66cc66;">&#93;</span> <span style="color: #66cc66;">=</span> <span style="color: #ff0000;">"-query"</span>;</span>
<span style="color: #009900;">	searchString<span style="color: #66cc66;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #66cc66;">&#93;</span> <span style="color: #66cc66;">=</span> request.getParameter<span style="color: #66cc66;">&#40;</span><span style="color: #ff0000;">"input"</span><span style="color: #66cc66;">&#41;</span>;</span>
&nbsp;
<span style="color: #009900;">	if<span style="color: #66cc66;">&#40;</span>searchString<span style="color: #66cc66;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #66cc66;">&#93;</span> !<span style="color: #66cc66;">=</span> null<span style="color: #66cc66;">&#41;</span> <span style="color: #66cc66;">&#123;</span></span>
<span style="color: #009900;">		<span style="color: #66cc66;">//</span> send the Search term to obtain the result, </span>
<span style="color: #009900;">		<span style="color: #66cc66;">//</span>all processing happens in the <span style="color: #000066;">class</span> </span>
<span style="color: #009900;">		<span style="color: #66cc66;">//</span><span style="color: #66cc66;">&#40;</span>keeping jsp <span style="color: #000066;">code</span> to minimum<span style="color: #66cc66;">&#41;</span></span>
<span style="color: #009900;">		result <span style="color: #66cc66;">=</span> SearchWebCall.filter<span style="color: #66cc66;">&#40;</span>searchString<span style="color: #66cc66;">&#41;</span>;</span>
<span style="color: #009900;">		int noOfMatch<span style="color: #66cc66;">=</span><span style="color: #cc66cc;"></span>;</span>
&nbsp;
<span style="color: #009900;">		out.print<span style="color: #66cc66;">&#40;</span><span style="color: #ff0000;">"Search Result of : &lt;b&gt;</span></span>" + searchString[1] + "<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">b</span>&gt;&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">br</span>&gt;&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">br</span>&gt;</span>");
		for(int i=0; i<span style="color: #009900;">&lt; result.length; i++<span style="color: #66cc66;">&#41;</span><span style="color: #66cc66;">&#123;</span></span>
&nbsp;
<span style="color: #009900;">			<span style="color: #66cc66;">//</span>format the results</span>
<span style="color: #009900;">			if <span style="color: #66cc66;">&#40;</span>result<span style="color: #66cc66;">&#91;</span>i<span style="color: #66cc66;">&#93;</span> !<span style="color: #66cc66;">=</span> null<span style="color: #66cc66;">&#41;</span> <span style="color: #66cc66;">&#123;</span></span>
<span style="color: #009900;">				out.print<span style="color: #66cc66;">&#40;</span>i+<span style="color: #cc66cc;">1</span> + <span style="color: #ff0000;">". "</span><span style="color: #66cc66;">&#41;</span>;</span>
<span style="color: #009900;">				<span style="color: #66cc66;">//</span>results are displayed as hyperlinks to faciliate information retrieval</span>
<span style="color: #009900;">				out.print<span style="color: #66cc66;">&#40;</span><span style="color: #ff0000;">"&lt;a href=\"</span><span style="color: #ff0000;">"+result[i]+"</span>\<span style="color: #ff0000;">"&gt;</span></span>"+result[i]+"<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">a</span>&gt;</span>");
				out.print("<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">br</span> <span style="color: #66cc66;">/</span>&gt;</span>");
				noOfMatch++;
			}
		}
		out.print("<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;">h2</span>&gt;&lt;<span style="color: #000000; font-weight: bold;">p</span>&gt;</span> No. of Matches: " + noOfMatch+ " <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">h2</span>&gt;</span>");
	}
//end of JSP
%&gt;
<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">body</span>&gt;</span>
<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><span style="color: #000000; font-weight: bold;">html</span>&gt;</span></pre>
      </td>
    </tr>
  </table>
</div>