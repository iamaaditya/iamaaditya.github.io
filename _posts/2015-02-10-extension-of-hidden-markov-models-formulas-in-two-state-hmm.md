---
title: 'Extension of Hidden Markov Models &#8211; Formulas in two state HMM'
author: aaditya prakash
layout: post
permalink: /2015/02/extension-of-hidden-markov-models-formulas-in-two-state-hmm/
categories:
  - computer science
  - math
tags:
  - HMM
  - machine learning
---
Extending the hidden markov models, where the current state is affected by past two states. This can be useful in simulation of games or in less sophisticated pricing models (more accurate would be an exponential decay of all past terms).

## Notations

I have kept the notations close to as provided in Chapter 6 of &#8220;Speech and Language Processing&#8221;, Second Edition by Martin and Jurafsky.

\(\lambda\) Common term for all HMM parameters. All the probabilties  
will be conditioned to this term i.e \(P(&#8230;&#8230;|\lambda)\)

\(T\) denotes the total number of time steps

\(N\) denotes the total number of states

\(o_{t}\) denotes the observed variable (state) at time step t

\(q_{t}\) denotes the hidden variale (state) at time step t

## Formulas

### Distribution of \(\alpha_{t}(i,j)\)

\(\alpha_{t}(i,j)\) denotes the joint probability distribution of all observed variables until time \(t\) and current and the last states.

\[  
\alpha\_{t}(i,j)=P(o\_{1},o\_{2},\dots,o\_{t},q\_{t-1}=i,q\_{t}=j|\lambda)  
\]

Where \(\lambda\) is the given HMM parameters.

### Base case of \(\alpha_{t}(i,j)\)

Consider the following notation:

\[  
a\_{ij}=P(q\_{t}=j|q_{t-1}=i)  
\]

\[  
a\_{ijk}=P(q\_{t+1}=k|q\_{t}=j,q\_{t-1}=i)  
\]

then base cases are &#8211;

\[  
\alpha\_{1}(i=0,j)=a\_{i=0,j}b\_{j}(o\_{1})  
\]

\[  
\alpha\_{2}(i,j)=\alpha\_{1}(0,j)a\_{ij}b\_{j}(o_{2})  
\]

It should be noted that if the second state (\(q_{2}\() is also allowed to be entry point, then it needs an additional base case of &#8212;

\[  
\alpha\_{2}(i=0,j)=\sum\_{i=1}^{N}\alpha\_{1}(i=0,j)a\_{ij}b\_{j}(o\_{2})  
\]

### Inductive step

\[  
\alpha\_{t}(j,k)=\sum\_{i=1}^{N}\alpha\_{t-1}(i,j)\times a\_{ijk}\times b\_{k}(o\_{t})\text{ where, }3\leq t\leq T  
\]

### Termination step

\[  
P(O|\lambda)=\sum\_{i=1}^{N}\sum\_{j=1}^{N}\alpha\_{T}(i,j)\times a\_{iF}\times a\_{jF}\times a\_{ijF}  
\]

## Estimated Expected Transitions

### \(\xi_{t}\)

\(\xi_{t}\) = Probability of being in state k at t+1, j at t and i at t-1

\[  
\xi\_{t}=P(q\_{t+1}=k,q\_{t}=j,q\_{t-1}=i|o\_{1},\dots o\_{T})=\frac{\alpha\_{t}(i,j)\times\beta\_{t+1}(j,k)\times a\_{ijk}b\_{k}(o\_{t+1})}{\alpha(q\_{f})}  
\]

### \(\gamma_{t}\)

\(\gamma_{t}\) = Probability of being in state i at &#8216;t&#8217;, given all the obervations

\[  
\gamma\_{t}=P(q\_{t}=i|o\_{1},\dots,o\_{T})=\frac{\sum\_{j}^{N}\alpha(j,i),\beta(j,i)}{\alpha(q\_{f})}  
\]

where \(\alpha(q\_{f})=P(o\_{1},\dots,o_{T})\) (joint probability of all observed variables)

{*}Please note that for \(\gamma\_{t}\) values, the \(i\) and \(j\) are interchanged in \(\alpha\) and \(\beta\) values, because I wanted to keep the input as \(q\_{t}=i\), as provided in the problem, whereas convention in textbook is to denote \(i\) as antecedent to \(j\).

<a title="Proofs for the two state hidden markov model" href="http://aaditya.info/research/hmm_two_states.pdf" target="_blank">Detailed proofs has been provided here</a>