---
title: Visual Question Answering Literature Survey
author: aaditya prakash
layout: page
dsq_thread_id:
  - 
---

# List of papers


* [[01VQA](<http://arxiv.org/abs/1505.00468>)] VQA: Visual Question Answering 
* [[02EMD](<http://arxiv.org/abs/1505.02074>)] Exploring Models and Data for Image Question Answering 
* [[03LAQ](<http://arxiv.org/abs/1506.00333>)] Learning to Answer Questions From Image Using Convolutional Neural Network 
* [[04DCQ](<http://arxiv.org/abs/1511.02799>)] Deep Compositional Question Answering with Neural Module Networks 
* [[05ABC](<http://arxiv.org/abs/1511.05960>)] An attention based convolutional neural network for visual question answering 
* [[06ATM](<http://arxiv.org/abs/1505.05612>)] Are you talking to a machine? datasetand methods for multilingual image question answering 
* [[07DPP](<http://arxiv.org/abs/1511.05756>)] Image question answering using convolutional neural networkwith dynamic parameter prediction 
* [[08WTL](<http://arxiv.org/abs/1511.07394>)] Where to look: Focus regions for visual question answering 
* [[09AMA](<http://arxiv.org/abs/1511.06973>)] Ask me anything: Free-form visual question answering based on knowledge from external sources 
* [[10V7W](<http://arxiv.org/abs/1511.03416>)] Visual7W: Grounded Question Answering in Images 
* [[11AAA](<http://arxiv.org/abs/1511.05234>)] Ask, Attend and Answer: Exploring question-guided spatial attention for visual question answering 
* [[12SAN](<http://arxiv.org/abs/1511.02274>)] Stacked attention networks for image questionanswering 
* [[13BOW](<http://arxiv.org/abs/1512.02167>)] Simple Baseline for Visual Question Answering 
* [[14ICV](<http://arxiv.org/abs/1603.02814>)] Image Captioning & Visual Question Answering Based on Attributes & External Knowledge 
* [[15DMN](<http://arxiv.org/abs/1603.01417>)] Dynamic Memory Networks for Visual and Textual Question Answering 
* [[16CMV](<http://arxiv.org/abs/1511.05676>)] Compositional Memory for Visual Question Answering  
* [[17LCN](<http://arxiv.org/abs/1601.01705>)] Learning to Compose Neural Networks for Question Answering

# Results

## VQA Dataset
(as self-published by authors- not verified)

Results below are for testdev-2015, except the final column which is for test-standard

**Method** |**All**| **Y/N**| **Other**| **Num**| **Test-Std[All]**
:------|:------:|:------:|:------:|:------:|:------:|
~~~~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~
Image| 28.1| 64.0| 3.8| 0.4| -
Question| 48.1| 75.7| 27.1| 36.7| -
Q+I| 52.6| 75.6| 37.4| 33.7| -
LSTM Q+I| 53.7| 78.9| 36.4| 35.2| 54.1
[16CMV]| 52.6| 78.3| 35.9| 34.4| -
[09AMA]| 55.7| 79.2| 40.1| 36.1| 56.0
[13BOW]| 55.7| 76.5| 42.6| 35.0| 55.9
[07DPP]| 57.2| 80.7| 41.7| 37.2| 57.4
[17LCN]| 57.9| 80.5| 43.1| 37.4| 58.0
[15AAA]| 57.9| 80.8| 43.2| 37.3| 58.2
[12SAN]| 58.7| 79.3| 46.1| 36.6| 58.9
[15DMN]| 60.3| 80.5| 48.3| 36.8| 60.4

# WordCloud

* To get a quick sense of where most of the models are headed in terms of architecture, it suffices to see the word cloud (after removing stop-words)

![word cloud](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/word_cloud_vqa_relative.png)

# Image Features

## GoogleNet vs VGGNet
 * Googlenet
   * [16CMV]
   * [13BOW]
   * [14ICV]
   * [06ATM]
   * [11AAA]
   * [12SAN]
 * VGGNet
   * [12SAN]
   * [06ATM]
   * [01VQA]
   * [14ICV]
   * [04DCQ]
   * [09AMA]

 * Some over lap is because they experimented with both the kind of features
 * Some of them experimented with Alexnet, e.g [06ATM], [16CMV], [09AMA] but for all of them it was underforming model
 * No one yet is using ResNet, yet.

# Memory

## LSTM vs GRU

 * Only [15DMN] and [07DPP] are using GRU whereas others are using LSTM. 
 * However, it should be noted that [15DMN] uses bi-directional GRU whereas [07DPP] uses single directional GRU.

## No bidirectinal LSTM

 * While several of them have reported either [02EMD]'s numbers on Bi-directional LSTM (model 2-VIS+BLSTM), no one has used bi-directional LSTM in their main model.

## Attention models vs non-attention models

 * Following papers use Attention Models
   * [15DMN] - Attention gates using modified GRUs
   * [04CDQ]
   * [11AAA] - Spatial attention with two hop model
   * [05ABC]
   * [12SAN]
   * [10V7W]
 * Following papers do not use any attention models, but believe that using attention would improve their model's performance
   * [07DPP]
   * [02EMD]
   * [06ATM]


# Episodic memory vs Semantic memory

 * [16CMV] claims to have used "declarative memory" which is combination of both semantic and episodic memory.
 * [15DMN] uses episodic memory modules explicitly. 
 * For reference: Tulving, Endel. "Episodic and semantic memory 1." Organization of Memory. London: Academic 381.4 (1972).


# Activation functions used
 
 * Sigmoid
   * [15DMN]  - Also uses ReLU & TanH
   * [06ATM]  - Also uses TanH
 * ReLU
   * [11AAA]
   * [03LAQ]
   * [04DCQ] 
   * [08WTL]
 * TanH
   * [12SAN]
   * [14ICV]
   * [10V7W]
   * [01VQA]
   * [05ABC]
   * [16CMV]


# Use of Batch Normalization

 * Only [07DPP] and [08WTL] have used batch-normalization for their training, even though most of the other deep learning research fields have extensively used the process.
 * For reference: Ioffe, Sergey, and Christian Szegedy. "Batch normalization: Accelerating deep network training by reducing internal covariate shift." arXiv preprint arXiv:1502.03167 (2015).


