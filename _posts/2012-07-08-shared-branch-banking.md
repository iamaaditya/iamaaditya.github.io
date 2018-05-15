---
title: Paradigm towards shared Branch Banking
author: aaditya prakash
layout: post
permalink: "/2012/07/shared-branch-banking/"
categories:
- research
tags:
- Networking
date: 2012-07-08 00:00:00 +0000
---
Long time ago when I was in my native town I had to do some banking operations on my account. To my surprise I found that the place didn&#8217;t have a branch of the bank where I had my account.

This was not a cash transfer issue from one account to another, this could have been easily solved by various Interbank settlements like SWIFT, ECS etc. This was a hardcore banking operation which could be completed only if bank&#8217;s own server were accessible.

Soon I realized that branches of other banks couldn&#8217;t serve my purpose. I wished there were ways in which banks could link together to serve larger area. While is it not financially sound for a bank to have branches at all the possible locations, at least banks coming together and connecting their network could solve most of the problem. This lead me into discussing the problems prohibiting the same with some of the senior managers at various bank. It seems all the banks work on their own legacy system thus are highly incompatible for any form of integration.

I thought there should be some solution because this problem of networking was rather trivial compared to modern day networking problems faced by computer scientists. Thus started a long journey into researching ways to combined banks server so that one outlet could serve multiple banks. When I found none existed I decided to attempt and provide the solution to this problem. Since this involved banking domain knowledge my friend Rajan Jha, who has several years of experience in handling technology of banking softwares, gladly accepted my request for joint research work.

I am glad to say that after months and months of pouring over available solutions, technology, breakthroughs, possible problems (which seemed infinite) we completed our model. Experts of this domain have given their stamp of approval for our model. Currently the paper describing the model is in review at an international journal. However you may read the preprint of the same here:  
<a href="http://aaditya.info/blog/wp-content/uploads/2012/07/Paper_Protocol_for_Common_Branch_Platform.pdf" target="_blank">Interface Protocol for common branch platform</a>

For a quick overview, you may want to see a <a href="https://sites.google.com/site/researchbyprakash/sharedbanking/Paper_Protocol_for_Common_Branch_Platform_Slides.pdf?attredirects=0&" target="_blank">17 slide presentation here</a>

For those who only want the gist of it, the Abstract of the paper is given below.

&nbsp;

**ABSTRACT**

Majority of banking transactions are done from branches. Internet Banking and mobile Banking have grown very slowly due to lack of technological sophistication among masses. ATMs have spread well but haven’t been able to provide low cost solution.

All the above alternate banking means are also very limited in scope of banking transactions. Thus branches will remain major source of transactions. Any solution that wants to reduce overhead of transaction cost must reduce cost of running a branch.

We propose an innovative interface protocol that will allow an access to multiple banks from a single outlet. This will enable a single branch to serve customers of several banks. This will in essence deleverage infrastructure of branch from banking business, allow banks to focus on service and product and not infrastructure, which is not its core competency. Having common branch will drastically reduce the number of branches required for given population and area; this will reduce operational cost of banking by manifolds.

&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-

I would like to thank my friend/co-author Rajan K Jha for the support and all the help.