---
title: Visual Question Answering
author: aaditya prakash
layout: page
dsq_thread_id:
  - 
---



## Implicit Attention using modified highway networks

### Conceptual diagram

![diagram](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/residual_vqa.png)

### Extended Abstract

[PDF](http://gpgpu.cs-i.brandeis.edu/highway.pdf)

### Abstract

We propose a version of highway network designed for
the task of Visual Question Answering. We take inspiration
from recent success of Residual Layer Network and Highway
Network in learning deep representation of images and
fine grained localization of objects. We propose variation
in gating mechanism to allow incorporation of word embedding
in the information highway. The gate parameters
are influenced by the words in the question, which steers the
network towards localized feature learning. This achieves
the same effect as soft attention via recurrence but allows
for faster training using optimized feed-forward techniques.
We are able to obtain state-of-the-art1
results on VQA
dataset for Open Ended and Multiple Choice tasks with current
model.

## Best Result

### Open Ended 

Overall Accuracy is: 62.73

Per Answer Type Accuracy is the following:
other : 51.35
number : 38.07
yes/no : 82.58


### Multiple Choice

Overall Accuracy is: 64.81

Per Answer Type Accuracy is the following:
other : 55.82
number : 39.14
yes/no : 82.13

^ Open Ended employed statistical filtering, ie. for every question category (64 category types see VQA Paper by Agrawal et al) answers were choosen to be within 98% of the seen answers from the training set. This increased the accuracy of model by more than a percent.
For Multiple Choice such filtering was not employed becuase it was expected to choose answers from the given 18 choices.

## Features

### Image

 * [ ResNet 200 ](https://github.com/facebook/fb.resnet.torch)
 * [ GoogLeNet ](https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet)
 * [ VGGNet ](http://www.robots.ox.ac.uk/~vgg/research/very_deep/)

### Words

 * [ Glove ](http://nlp.stanford.edu/projects/glove/)
 * [ Word2Vec ](https://spacy.io/)
 * [ConceptNet Numberbatch](https://github.com/LuminosoInsight/conceptnet-numberbatch)
 * [Syntactic Similarity](https://github.com/brmson/dataset-sts)

### Misc
 * [ ConceptNet ]( http://conceptnet5.media.mit.edu/ )
 * [ WordNet ](https://wordnet.princeton.edu/)

### Comparison of results from the VQA Challenge

 * Detailed comparison of results will be published here, once VQA has completed evaluation of the challange.


### Relevant Papers
 * Sukhbaatar, Sainbayar, Jason Weston, and Rob Fergus. "End-to-end memory networks." Advances in Neural Information Processing Systems. 2015.
 * Hinton, Geoffrey, Oriol Vinyals, and Jeff Dean. "Distilling the knowledge in a neural network." arXiv preprint arXiv:1503.02531 (2015).
 * Srivastava, Rupesh Kumar, Klaus Greff, and Jürgen Schmidhuber. "Highway networks." arXiv preprint arXiv:1505.00387 (2015).
 * Glorot, Xavier, and Yoshua Bengio. "Understanding the difficulty of training deep feedforward neural networks." International conference on artificial intelligence and statistics. 2010.
 * He, Kaiming, et al. "Deep Residual Learning for Image Recognition." arXiv preprint arXiv:1512.03385 (2015).
 * For papers related to VQA see [__Literature Survey__]({{site.baseurl}}/research/literature/) 

### Old apporach using end-to-end attention with skip-thought
 * __Our Approach__
   * Use of visual attention model along with end-to-end memory networks which are trained on skip-thought vectors on question tokens, and GoogLeNet dense layer image features. 
   * We are experimenting with application of Neural Turing Machines. We believe having a persistent memory will lead to sharing of knowledge between images where similar questions were asked. 
   * We are also experimenting to see if having spatial information could be useful in answering questions about location and direction. I am coding adaptation of CRF-RNN to extract spatial knowledge to be merged with image features.
 * [__Literature Survey__]({{site.baseurl}}/research/literature/)  - (Almost) exhaustive list of papers tackling the problem and their results and their methodologies, includes survey of techniques and tricks used by various research groups.
 * [__Visual Question Answering Demo__]({{site.baseurl}}/2016/04/visual_question_answering_demo_notebook)  - A ipython notebook demonstration of a simple but yet effective mode for visual question answering inference.
 * [__Github Code of simple demo__](https://github.com/iamaaditya/VQA_Demo) - Code of the aforementioned demo. Also includes standalone code to run inference on a server with pretrained models and weights.
 * [__Visual Question Answering Notes__]( {{site.baseurl}}/notes/research/vqa/ ) - contains basic modules and ideas that I am experimenting with.
 * [__Visual Comparision of Results__](http://gpgpu.cs-i.brandeis.edu/shankar/submissions_vqa/project_comparison/comparison_mar31.html)  <br/>
   * This a large file ! Load at your risk.  <br />
   * Images are not loaded but a link is provided. <br />


 * Obvious negative corrleation between confidence of Amazon Mechanical Turks and the accuracy of the system
 ![correct vs incorrect](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/correct_vs_incorrect.png)

 * __Temporary Results__

**Method** |**All**| **Y/N**| **Other**| **Num**| **Test-Std[All]**
:------|:------:|:------:|:------:|:------:|:------:|
~~~~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~
Image| 28.1| 64.0| 3.8| 0.4| -
Question| 48.1| 75.7| 27.1| 36.7| -
Q+I| 52.6| 75.6| 37.4| 33.7| -
LSTM Q+I| 53.7| 78.9| 36.4| 35.2| 54.1
[[16CMV](<http://arxiv.org/abs/1511.05676>)]| 52.6| 78.3| 35.9| 34.4| -
[[09AMA](<http://arxiv.org/abs/1511.06973>)]| 55.7| 79.2| 40.1| 36.1| 56.0
[[13BOW](<http://arxiv.org/abs/1512.02167>)]| 55.7| 76.5| 42.6| 35.0| 55.9
[[07DPP](<http://arxiv.org/abs/1511.05756>)]| 57.2| 80.7| 41.7| 37.2| 57.4
[[17LCN](<http://arxiv.org/abs/1601.01705>)]| 57.9| 80.5| 43.1| 37.4| 58.0
[[11AAA](<http://arxiv.org/abs/1511.05234>)]| 57.9| 80.8| 43.2| 37.3| 58.2
[[12SAN](<http://arxiv.org/abs/1511.02274>)]| 58.7| 79.3| 46.1| 36.6| 58.9
[[15DMN](<http://arxiv.org/abs/1603.01417>)]| 60.3| 80.5| 48.3| 36.8| 60.4
OUR| 60.4| 81.5| 47.6| 37.2| 60.7


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


