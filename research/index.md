---
title: Research
author: aaditya prakash
layout: page
dsq_thread_id:
  - 
---


## Visual Question Answering

Following are the links to my notes on current work. They might be benefitial only if you are also a researcher in the same field.

 * [Visual Question Answering]( {{site.baseurl}}/notes/research/vqa/ ) - contains basic modules and ideas that I am experimenting with.
 * [Python notebook demo and tutorial for VQA]( https://github.com/iamaaditya/VQA_Demo/blob/master/Visual_Question_Answering_Demo_in_python_notebook.ipynb )  - I wrote this tutorial as a gentle introduction to VQA.
 * [Visual Comparision](http://gpgpu.cs-i.brandeis.edu/shankar/submissions_vqa/project_comparison/comparison_mar31.html)  <br/>
   * This a large file ! Load at your risk.  <br />
   * Images are not loaded but a link is provided. <br />

 * __Temporary Results__

    |Model_name | Overall Accuracy |    Others    |    Numbers    | yes/no      |
    |-----------|:------------------:|:------------:|:--------------:|:--------:|
    |___________|_________________|_______________|_______________|_____________|
    |KOR ## dppnet_12                 |57.63 | 42.74 | 36.45 | 80.69|
    |KOR ## dppnet_9                  |57.61 | 42.85 | 36.50 | 80.48|
    |__OUR__ ## model_2               |57.20 | 42.01 | 36.84 | 80.40|
    |__OUR__ ## model_1               |57.15 | 41.85 | 36.34 | 80.57|
    |MIT ## base2                     |55.90 | 42.42 | 35.29 | 77.15|
    |MIT ## base1                     |55.65 | 42.55 | 34.97 | 76.47|
    |VQA ## lstm_mlp_relu             |49.75 | 33.30 | 29.91 | 74.28|
    |__OLD__ ## new_lstm_3            |48.11 | 30.20 | 22.53 | 75.87|


 * __Comparison of results from different models__
    
    Number of unique answers / total number of models  == total questions with those unique answers / Total questions  % percentage of questions with those number of unique answers

    ALL QUESTION <br />
    ------------------------ <br />
    1/9  ==  18073/60864  %  0.297 <br />
    2/9  ==  23593/60864  %  0.388 <br />
    3/9  ==  09611/60864  %  0.158 <br />
    4/9  ==  06378/60864  %  0.105 <br />
    5/9  ==  02557/60864  %  0.042 <br />
    6/9  ==  00593/60864  %  0.01 <br />
    7/9  ==  00059/60864  %  0.001 <br />



    Filtered QUESTION (NO Binary decision questions) <br />
    ------------------------ <br />
    1/9  ==  06438/60864  %  0.106 <br />
    2/9  ==  10172/60864  %  0.167 <br />
    3/9  ==  09136/60864  %  0.15 <br />
    4/9  ==  05566/60864  %  0.091 <br />
    5/9  ==  02121/60864  %  0.035 <br />
    6/9  ==  00500/60864  %  0.008 <br />
    7/9  ==  00054/60864  %  0.001 <br />



    <br />
  * Detailed Analysis of the different Visual Question Answering models
    * Memory
    * Attention models vs non-attention models
    * LSTM vs GRU
    * Episodic memory vs Semantic memory
    * No bidirectinal LSTM
    * Activation functions used
    * Choice of Activations
    * Use of Batch Normalization
    <br />TODO ! - Add Link


## Transfer Learning 

 * [Transfer Learning]({{site.baseurl}}/notes/research/transfer/ )






