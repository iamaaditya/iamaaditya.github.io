---
title: Qubit operations and Quantum Measurement in Mathematica
author: aaditya prakash
layout: post
permalink: "/2012/08/qubit-operations-and-quantum-measurement-in-mathematica/"
categories:
- computer science
- math
tags:
- mathematica
- quantum computing
date: 2012-08-11 00:00:00 +0000
---
This is a short note on how to get started with Quantum Computing with Mathematica.

This is not intended to be either comprehensive or pedagogical. There are several resources online like http://www.quantiki.org/ and http://qubit.org/

First Download the excellent Mathematica Package by José Luis Gómez-Muñoz and Francisco Delgado from here http://homepage.cem.itesm.mx/lgomez/quantum/index.htm . The instructions to install them are given here [http://homepage.cem.itesm.mx/lgomez/quantum/installation.pdf][1]

* * *

<p class="CellLabel">
  In[1]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_1.gif" alt="qubit_operation_Quantum_Measurement_1.gif" width="190" height="37" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[2]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_6.gif" alt="qubit_operation_Quantum_Measurement_6.gif" width="193" height="19" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[2]:= MatrixForm=
</p>

<p class="Output">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_7.gif" alt="qubit_operation_Quantum_Measurement_7.gif" width="27" height="57" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[3]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_8.gif" alt="qubit_operation_Quantum_Measurement_8.gif" width="204" height="19" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[3]=
</p>

<p class="Output">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_9.gif" alt="qubit_operation_Quantum_Measurement_9.gif" width="332" height="32" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[4]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_10.gif" alt="qubit_operation_Quantum_Measurement_10.gif" width="182" height="23" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[4]=
</p>

<p class="Output">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_11.gif" alt="qubit_operation_Quantum_Measurement_11.gif" width="140" height="40" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[5]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_12.gif" alt="qubit_operation_Quantum_Measurement_12.gif" width="164" height="24" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[5]=
</p>

<p class="Output">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_13.gif" alt="qubit_operation_Quantum_Measurement_13.gif" width="140" height="40" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[6]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_14.gif" alt="qubit_operation_Quantum_Measurement_14.gif" width="170" height="19" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[6]//MatrixForm=
</p>

<p class="Output">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_15.gif" alt="qubit_operation_Quantum_Measurement_15.gif" width="44" height="61" style="vertical-align:middle" />
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_16.gif" alt="qubit_operation_Quantum_Measurement_16.gif" width="264" height="44" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[8]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_17.gif" alt="qubit_operation_Quantum_Measurement_17.gif" width="403" height="80" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[8]=
</p>

<p class="Output">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_18.gif" alt="qubit_operation_Quantum_Measurement_18.gif" width="359" height="32" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  In[9]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_19.gif" alt="qubit_operation_Quantum_Measurement_19.gif" width="291" height="18" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[9]=
</p>

<table class='Output'>
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span>Probability</span>
    </td>
    
    <td style='text-align: center;'>
      <span>Measurement</span>
    </td>
    
    <td style='text-align: center;'>
      <span>State</span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_20.gif" alt="qubit_operation_Quantum_Measurement_20.gif" width="12" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_21.gif" alt="qubit_operation_Quantum_Measurement_21.gif" width="41" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_22.gif" alt="qubit_operation_Quantum_Measurement_22.gif" width="158" height="40" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_23.gif" alt="qubit_operation_Quantum_Measurement_23.gif" width="12" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_24.gif" alt="qubit_operation_Quantum_Measurement_24.gif" width="41" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_25.gif" alt="qubit_operation_Quantum_Measurement_25.gif" width="183" height="40" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span>Probability</span>
    </td>
    
    <td style='text-align: center;'>
      <span>Measurement</span>
    </td>
    
    <td style='text-align: center;'>
      <span>State</span>
    </td>
  </tr>
</table>

<p class="CellLabel">
  In[10]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_26.gif" alt="qubit_operation_Quantum_Measurement_26.gif" width="309" height="18" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[10]=
</p>

<table class='Output'>
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span>Probability</span>
    </td>
    
    <td style='text-align: center;'>
      <span>Measurement</span>
    </td>
    
    <td style='text-align: center;'>
      <span>State</span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_27.gif" alt="qubit_operation_Quantum_Measurement_27.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_28.gif" alt="qubit_operation_Quantum_Measurement_28.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_29.gif" alt="qubit_operation_Quantum_Measurement_29.gif" width="81" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_30.gif" alt="qubit_operation_Quantum_Measurement_30.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_31.gif" alt="qubit_operation_Quantum_Measurement_31.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_32.gif" alt="qubit_operation_Quantum_Measurement_32.gif" width="89" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_33.gif" alt="qubit_operation_Quantum_Measurement_33.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_34.gif" alt="qubit_operation_Quantum_Measurement_34.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_35.gif" alt="qubit_operation_Quantum_Measurement_35.gif" width="81" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_36.gif" alt="qubit_operation_Quantum_Measurement_36.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_37.gif" alt="qubit_operation_Quantum_Measurement_37.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_38.gif" alt="qubit_operation_Quantum_Measurement_38.gif" width="89" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span>Probability</span>
    </td>
    
    <td style='text-align: center;'>
      <span>Measurement</span>
    </td>
    
    <td style='text-align: center;'>
      <span>State</span>
    </td>
  </tr>
</table>

<p class="CellLabel">
  In[11]:=
</p>

<p class="Input">
  <img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_39.gif" alt="qubit_operation_Quantum_Measurement_39.gif" width="444" height="18" style="vertical-align:middle" />
</p>

<p class="CellLabel">
  Out[11]=
</p>

<table class='Output'>
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span>Probability</span>
    </td>
    
    <td style='text-align: center;'>
      <span>Measurement</span>
    </td>
    
    <td style='text-align: center;'>
      <span>State</span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_40.gif" alt="qubit_operation_Quantum_Measurement_40.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_41.gif" alt="qubit_operation_Quantum_Measurement_41.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_42.gif" alt="qubit_operation_Quantum_Measurement_42.gif" width="59" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_43.gif" alt="qubit_operation_Quantum_Measurement_43.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_44.gif" alt="qubit_operation_Quantum_Measurement_44.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_45.gif" alt="qubit_operation_Quantum_Measurement_45.gif" width="67" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_46.gif" alt="qubit_operation_Quantum_Measurement_46.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_47.gif" alt="qubit_operation_Quantum_Measurement_47.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_48.gif" alt="qubit_operation_Quantum_Measurement_48.gif" width="59" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_49.gif" alt="qubit_operation_Quantum_Measurement_49.gif" width="19" height="32" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_50.gif" alt="qubit_operation_Quantum_Measurement_50.gif" width="65" height="19" style="vertical-align:middle" /></span>
    </td>
    
    <td style='text-align: center;'>
      <span><img src="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement_51.gif" alt="qubit_operation_Quantum_Measurement_51.gif" width="67" height="19" style="vertical-align:middle" /></span>
    </td>
  </tr>
  
  <tr style='vertical-align: baseline;'>
    <td style='text-align: center;'>
      <span>Probability</span>
    </td>
    
    <td style='text-align: center;'>
      <span>Measurement</span>
    </td>
    
    <td style='text-align: center;'>
      <span>State</span>
    </td>
  </tr>
</table>

* * *

For those of you who have Mathematica Installed <a href="http://aaditya.info/research/quantum/qubit_operation_Quantum_Measurement.nb" title="Qubit Operation and Quantum Measurement" target="_blank">here is the Notebook File</a>

Repeat Caveat, this is certainly non-exhaustive and is meant to be minimal. José himself has lot of sample notebooks and youtube tutorials which you may want to checkout for indepth study.

 [1]: http://homepage.cem.itesm.mx/lgomez/quantum/installation.pdf "Instructions to Install Quantum Package for Mathematica"