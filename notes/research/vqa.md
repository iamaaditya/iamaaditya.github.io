---
title: Visual Question Answering
author: aaditya prakash
layout: page
dsq_thread_id:
- 
---
## Competition Website 

  * <http://visualqa.org/>
  * <http://mscoco.org/>


## Image Features

### VGG Net

 * Overview <http://www.robots.ox.ac.uk/~vgg/research/very_deep/>
 * Paper <http://arxiv.org/pdf/1409.1556.pdf>


### GoogLeNet

 * Overview <http://googleresearch.blogspot.com/2014/09/building-deeper-understanding-of-images.html>
 * Paper <http://arxiv.org/pdf/1409.4842v1.pdf>


### LSTM

 * Excellent description <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>
 * Paper <http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf>

## Language Features

### Word2Vec

  * Projet website: <https://code.google.com/p/word2vec/>
  * Description:
    This tool provides an efficient implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words. These representations can be subsequently used in many natural language processing applications and for further research.
  * Related Paper:
    [1] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient Estimation of Word Representations in Vector Space. In Proceedings of Workshop at ICLR, 2013.
    [2] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, and Jeffrey Dean. Distributed Representations of Words and Phrases and their Compositionality. In Proceedings of NIPS, 2013.
    [3] Tomas Mikolov, Wen-tau Yih, and Geoffrey Zweig. Linguistic Regularities in Continuous Space Word Representations. In Proceedings of NAACL HLT, 2013.
  * Nice tutorial on Word2Vec <http://multithreaded.stitchfix.com/blog/2015/03/11/word-is-worth-a-thousand-vectors>

### Glove
 
  * Project website: <http://nlp.stanford.edu/projects/glove/>
  * Description: 
    GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space.
  * Paper: GloVe: Global Vectors for Word Representation <http://nlp.stanford.edu/projects/glove/glove.pdf>

### Sense2Vec

  * Description and nice tutorial <https://spacy.io/blog/sense2vec-with-spacy>
  * Paper : <http://arxiv.org/pdf/1511.06388v1.pdf>


### Skip-Thought Vectors

  * Description and intuition about thought-vectors <http://deeplearning4j.org/thoughtvectors>
  * Paper : <http://arxiv.org/abs/1506.06726>
  * Code : <https://github.com/ryankiros/skip-thoughts>

## Datasets

 1. Visual Question Answering (VQA) dataset: Based on images from the COCO dataset,it currently has 360K questions on 120K images. There are plans of releasing questions on the rest of the COCO images and an additional 50K abstract images. All the questions are human-generated, and were specifically designed to stump a "smart robot".

 2. Visual Madlibs: It contains fill-in-the-blank type questions along with standard question-answer pairs. It has 360K questions on 10K images from the COCO dataset. A lot of questions require high-level human cognition, such as describing what one feels on seeing an image.

 3. Toronto COCO-QA Dataset: Automatically generated questions from the captions of the MS COCO dataset. At 115K questions, it is smaller than the VQA dataset. Answers are all one word.

 4. DAQUAR - DAtaset for QUestion Answering on Real-world images: A much smaller dataset, with about 12K questions. This was one of the earliest datasets on image question and answering.


## Other relevant works


### Summer, 2015

* VQA: Visual Question Answering <br /><http://arxiv.org/abs/1505.00468>
* Exploring Models and Data for Image Question Answering <br /><http://arxiv.org/abs/1505.02074>
* Learning to Answer Questions From Image Using Convolutional Neural Network <br /><http://arxiv.org/abs/1506.00333>

### November, 2015 (after deadline of CVPR)

* Deep Compositional Question Answering with Neural Module Networks <br /><http://arxiv.org/abs/1511.02799>
* An attention basedconvolutional neural network for visual question answering <br /><http://arxiv.org/abs/1511.05960>
* Are you talking to a machine? datasetand methods for multilingual image question answering <br /><http://arxiv.org/abs/1505.05612>
* Image question answering using convolutional neural networkwith dynamic parameter prediction <br /><http://arxiv.org/abs/1511.05756>
* Where to look: Focus regions for visual question answering <br /><http://arxiv.org/abs/1511.07394>
* Ask me anything: Free-form visual question answering based on knowledge from external sources <br /><http://arxiv.org/abs/1511.06973>
* Exploring question-guided spatial attention forvisual question answering <br /><http://arxiv.org/abs/1511.05234>
* Stacked attention networks for image questionanswering <br /><http://arxiv.org/abs/1511.02274>
* Simple Baseline for Visual Question Answering <br /><http://arxiv.org/abs/1512.02167>

### 2016
* Dynamic Memory Networks for Visual and Textual Question Answering <br /><http://arxiv.org/abs/1603.01417>
    

### Codes

  * Baseline only, MIT <https://github.com/metalbubble/VQAbaseline/>
  * VQA - VT vision, Virginia Tech <https://github.com/VT-vision-lab/VQA_LSTM_CNN>

### Demo

  * Demo (baseline, MIT) <http://visualqa.csail.mit.edu/>
  * CloudCV, Virginia Tech, <http://cloudcv.org/vqa/>


[Koan on Bias while training Neural Nets](https://en.wikipedia.org/wiki/Hacker_koan#Uncarved_block)    

