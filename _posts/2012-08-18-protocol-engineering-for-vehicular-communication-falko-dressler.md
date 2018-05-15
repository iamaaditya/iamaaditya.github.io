---
title: Protocol Engineering for Vehicular Communication &#8211; Falko Dressler
author: aaditya prakash
layout: post
permalink: "/2012/08/protocol-engineering-for-vehicular-communication-falko-dressler/"
categories:
- computer science
- research
tags:
- AI
- traffic information system
date: 2012-08-18 00:00:00 +0000
---
This is the notes from the lecture I attended by <a title="Falko Dressler" href="http://www.ccs-labs.org/~dressler/" target="_blank">Dr Falko Dressler</a>, Professor of Computer Science at University of Innsbruck.

It may perhaps be little incoherent and is meant more to be notes to future self rather than an interesting read. Nonetheless if AI and Intelligent Traffic Systems interests you do read.

## Introduction

  * People Should follow Traffic Lights before making intelligent Traffic Lights
  * Focus &#8211; Intervehicular Communication
  * DSRC/WAVE
  * Traffic Information System (TIS)
  * Centralized vs Distributed
  * P2P vs Beaconing

## Infrastructure Assisted Data Exchange

  * Adhoc &#8211; Multihop Broadcasting
  * Short Range radio broadcast
  * Traffic Message Channel
  * Stationary Sensor
  * Traffic Channel
  * Floating Car Data (FCD) (&#8220;aktiv CoCar&#8221;)

  * Geocast Manager
  * CoCar aggressor
  * Centralized TIS + Adhoc Routing

## Communication

  * ### WAVE

  * Core System &#8211; IEEE 1609.1
  * Security &#8211; IEEE 1609.2
  * Network Services

  * MAC layer with extension IEEE 802.11a
  * Reduced inter symbol interference
  * Access Control and QoS in WAVE
  * Use of EDCA equivalent to IEE 802.11e EDCA (DCF -> EDCA)
  * Dedicated Frequency (reserved/assigned)
  * US -> FCC reserved 7 channels 10 MHz
  * EU -> ETSI reserved 5 channels 10 MHz
  * Japan -> Whitespace but not viable

  * Exclusive V2V and V2I communication
  * Channel Management
  * Slot Management
  * CAM Message (Co-operative Awareness Messages)
  * Periodic Beacons Containing&#8211;
  * Time, Speed, Position, Heading

  * For multiple devices we would need syncrhonisation

## SOTIS Approach

  * SOTIS &#8211; Self Organized Traffic Information System
  * Fully Distributed Approach
  * No communication approach
  * No data loss in fragmented
  * No unique node

  * Shortcoming and Open Issues
  * Infra &#8211; needs high marked penetration
  * Required/tolerable beacon interal highly dependent scenario
  * Design needs dedicated channel capacity

  * Dynamically &#8212;&#8211;
  * incorporate optional infra
  * adapt beacon interval
  * free all channels

### Hybrid using 3G/4G &#8211; Peer TIS

  * DHT &#8211; maintained in all cars
  * Communication using 3G/4G network

### Optimization

  * Data Caching &#8212; not possible to keep data fresh
  * DHT lookup entries &#8212; Yes, long indrections in the DHT can be prevented

### Fully Distributed &#8211; Adaptive Traffic Beacon (ATB)

  * Beacon interval &#8211; Measure of channel quality and message priorities
  * Infrastructure elements : RSU of different capacities
  * Light-weight SSU
  * Interconnected SSU

## Formulas Involved

### Interval parameter &#8211; <img src='http://s0.wp.com/latex.php?latex=I+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='I ' title='I ' class='latex' />

<img src='http://s0.wp.com/latex.php?latex=I%3D%281-w_%7BI%7D%29%2AP%5E%7B2%7D%2B%28w_%7BI%7D%2Ac%5E%7B2%7D%29+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='I=(1-w_{I})*P^{2}+(w_{I}*c^{2}) ' title='I=(1-w_{I})*P^{2}+(w_{I}*c^{2}) ' class='latex' /> 

  * c=channel quality
  * P = message prior
  * <img src='http://s0.wp.com/latex.php?latex=w_%7BI%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='w_{I} ' title='w_{I} ' class='latex' />= interval weighting

### Beacon Interval &#8211; <img src='http://s0.wp.com/latex.php?latex=%5Ctriangle+I+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\triangle I ' title='\triangle I ' class='latex' />

<img src='http://s0.wp.com/latex.php?latex=%5Ctriangle+I%3DI_%7Bmin%7D%2B%28I_%7Bmax%7D-I_%7Bmin%7D%29%2AI+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\triangle I=I_{min}+(I_{max}-I_{min})*I ' title='\triangle I=I_{min}+(I_{max}-I_{min})*I ' class='latex' /> 

  * I= interval

### Channel Quality &#8211; <img src='http://s0.wp.com/latex.php?latex=C+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='C ' title='C ' class='latex' />

<img src='http://s0.wp.com/latex.php?latex=C%3D%5Cfrac%7BN%2Bw_%7Bc%7D%2A%5Cfrac%7BS%2BK%7D%7B2%7D%7D%7B1%2Bw_%7Bc%7D%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='C=\frac{N+w_{c}*\frac{S+K}{2}}{1+w_{c}} ' title='C=\frac{N+w_{c}*\frac{S+K}{2}}{1+w_{c}} ' class='latex' /> 

  * N= Neighbour
  * K= Observed Collision
  * S= Signal to Noise Ratio

### Message Priority Estimation <img src='http://s0.wp.com/latex.php?latex=P+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='P ' title='P ' class='latex' />

<img src='http://s0.wp.com/latex.php?latex=P%3DB%2A%5Cfrac%7BA%2BD_%7Be%7D%2BD_%7Br%7D%7D%7B3%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='P=B*\frac{A+D_{e}+D_{r}}{3} ' title='P=B*\frac{A+D_{e}+D_{r}}{3} ' class='latex' /> 

  * A= Message age
  * <img src='http://s0.wp.com/latex.php?latex=D_%7Be%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='D_{e} ' title='D_{e} ' class='latex' /> = Distance to event
  * <img src='http://s0.wp.com/latex.php?latex=D_%7Br%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='D_{r} ' title='D_{r} ' class='latex' /> = Distance to next RSU
  * B= Knowledge of local RSU

### Criteria

  * Age of entry <img src='http://s0.wp.com/latex.php?latex=%5CDownarrow+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\Downarrow ' title='\Downarrow ' class='latex' />
  * Distance to event <img src='http://s0.wp.com/latex.php?latex=%5CUparrow+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\Uparrow ' title='\Uparrow ' class='latex' />
  * Distance to RSU <img src='http://s0.wp.com/latex.php?latex=%5CDownarrow+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\Downarrow ' title='\Downarrow ' class='latex' />
  * Beacon interval <img src='http://s0.wp.com/latex.php?latex=%5Cmathcal%7BL%7D+%5Cfrac%7B1%7D%7Blatency%7D+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\mathcal{L} \frac{1}{latency} ' title='\mathcal{L} \frac{1}{latency} ' class='latex' />

Let us see how soon we can see such intelligent designed traffic management systems, perhaps <a title="Google's Self Driven Car gets license to operate in Nevada" href="http://www.rediff.com/business/slide-show/slide-show-1-tech-google-self-driven-cars-on-us-roads/20120509.htm" target="_blank">Google&#8217;s Self Driven Car</a> and Dr. Sebastian Thrun&#8217;s dream project all will merge for better safety and efficiency in the road.