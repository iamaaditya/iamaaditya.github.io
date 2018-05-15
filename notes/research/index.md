---
title: Research
author: aaditya prakash
layout: page
dsq_thread_id:
- 
---
## Sub-pages
 * [Visual Question Answering]( {{site.baseurl}}/notes/research/vqa/ )
 * [Convolutional Neural Network ]({{site.baseurl}}/notes/research/cnn/ ) 
 * [Transfer Learning]({{site.baseurl}}/notes/research/transfer/ )

## Currently thinking about 

 * How to add Network in Network for Visual Question Answering Models
 * Distributed representation (of features)
   > Can you learn X, Y and detect X + Y ?
 * Can you tell the difference between an artificially generated image and a real image ? (Generative image models : <http://arxiv.org/abs/1506.05751> )
 * Saliency map and guided backpropagation <https://github.com/Lasagne/Recipes/blob/master/examples/Saliency%20Maps%20and%20Guided%20Backpropagation.ipynb>

## Papers reading currently
 * How transferable are features in deep neural networks? <http://arxiv.org/abs/1411.1792>
 * On Learning to Think: Algorithmic Information Theory for Novel Combinations of Reinforcement Learning Controllers and Recurrent Neural World Models <http://arxiv.org/abs/1511.09249>
 * Generating images from captions with attention <http://arxiv.org/pdf/1511.02793v1.pdf>
 * Neural Program interpreters <http://www-personal.umich.edu/~reedscot/iclr_project.html>

## Recently read papers
 * Exploring Person Context and Local Scene Context for Object Detection <http://arxiv.org/pdf/1511.08177.pdf>
 * DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition <http://arxiv.org/pdf/1310.1531v1.pdf>
 * On Learning Where To Look <http://www.cs.toronto.edu/~ranzato/publications/ranzato_arxiv14.pdf>

## Papers of interest
 * Human-level concept learning through probabilistic program induction <http://science.sciencemag.org/content/350/6266/1332.abstract>
 * Ask Me Anything: Dynamic Memory Networks for Natural Language Processing <http://arxiv.org/pdf/1506.07285v3.pdf>
 * Object detectors emerge in deep scene cnns <http://arxiv.org/pdf/1412.6856v2.pdf>
 * 21 hottest papers from ICCV 2015 <http://www.computervisionblog.com/2015/12/iccv-2015-twenty-one-hottest-research.html>
 * Memory Networks <http://arxiv.org/abs/1410.3916>
 * Mechanisms Gating the Flow of Information in the Cortex: What They Might Look Like and What Their Uses may be <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3025648/>
 * Bridging the Gaps Between Residual Learning, Recurrent Neural Networks and Visual Cortex <http://arxiv.org/abs/1604.03640v1>

## Libraries currenty of interest
 * <https://github.com/karpathy/neuraltalk2>
 * <https://github.com/HyeonwooNoh/DPPnet>

## Articles 
 * Bayesian Methods for Neural Networks <http://www.cs.cmu.edu/afs/cs/academic/class/15782-f06/slides/bayesian.pdf>
 * Crash course in learning theory <https://blogs.princeton.edu/imabandit/2015/10/13/crash-course-on-learning-theory-part-1/>

## Sources of Paper
 * Arxiv (Deep) Learning <http://arxiv.org/list/cs.LG/recent>
 * Arxiv Machine Learning  <http://arxiv.org/list/stat.ML/recent>
 * Arixv Computer Vision and Pattern Recognition <http://arxiv.org/list/cs.CV/recent>
 * Subreddit Deep Learning Papers <https://www.reddit.com/r/DeepLearningPapers>
 * Arxiv Sanity Preserver (by Karpathy) <http://www.arxiv-sanity.com/top>

## Notes

### Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning <http://arxiv.org/abs/1511.06342>
    Instead of using a fresh network for each game, this team combined deep multitask reinforcement learning with deep-transfer learning to be able to use the same deep neural network across different types of games. This leads not only to a single instance that can succeed in multiple different games, but to one that also learns new games better and faster because of what it remembers about those other games. For example, it can learn a new tennis video game faster because it already gets the concept — the meaningful abstraction of hitting a ball with a paddle — from when it was playing Pong [Source](http://futureoflife.org/2015/12/29/the-top-a-i-breakthroughs-of-2015/)

### Bridge Correlational Neural Networks for Multilingual Multimodal Representation Learning <http://arxiv.org/abs/1510.03519>
    Joint embeddings to support the confluence of multiple meaningfully related mappings at once, across different modalities and different languages. As these embeddings get more sophisticated and detailed, they can become workhorses for more elaborate AI techniques

### Learning semantic relationships for better action retrieval in images <http://web.eecs.umich.edu/~jiadeng/paper/RamanathanEtAl_CVPR2015.pdf>
    Create a system that learns a meaningful schema of relationships between different types of actions from a set of photographs and a dictionary.

### DEEP MANIFOLD TRAVERSAL: CHANGING LABELS WITH CONVOLUTIONAL FEATURES <http://arxiv.org/pdf/1511.06421v1.pdf>
     Uses a dimensionality reduction of a deep net’s weights to form a surface of convolutional features that can simply be slid along to meaningfully, automatically, photorealistically alter particular aspects of photographs, e.g., changing people’s facial expressions or their ages, or colorizing photos.

### Expressing an Image Stream with a Sequence of Natural Sentences <http://www.cs.cmu.edu/~gunhee/publish/nips15_stream2text.pdf>
    **Video summarizing** Novel architecture called a coherent recurrent convolutional network, applying it to creating novel and fluid textual stories from sequences of images.

### Open Areas in Deep Learning (by Yoshua Bengio) 
   Every researcher has their opinion on this, which is a good thing. Here are some I see:
  * Unsupervised learning that would really kick ass
    * generative models that generate crisp images and sounds over a wide set of variations covering natural images and sounds
    * semi-supervised learning that makes a difference even when the labeled dataset is not tiny
    * learning a two-way transformation of the data into a space where variables are disentangled (or mostly independent)
    * bringing (iterative) inference back in deep learning to handle non-factorial posteriors over the latent variables
  * Introducing more reasoning abilities in our models
  * Natural language understanding and knowledge representation on a large scale
  * Models of really long-term dependencies in sequential data and having learners that discover a hierarchical representation at multiple time scales
  * Understand better (and fix) the optimization issues that sometimes arise (for example in unsupervised learning or recurrent nets with long-term dependencies)
  * Train models that incorporate planning (playing out what-if scenarios, maybe stochastically via a generative component) as part of the learning procedure (and also to actually take decisions)
  * Scaling up reinforcement learning to large action spaces
  * Maximum likelihood has known deficiencies (such as a mismatch between training and test conditions) and we need to go around them (maybe ditching maximum likelihood altogether)
  * Bridging the gap between deep learning and biology
  * Ramping up our theoretical understanding of deep learning (optimization issues being one aspect, but expressive / statistical aspects being also in need of more theory)
  * Building specialized hardware that will allow us not just to build consumer products from models trained offline, but maybe more importantly from a scientific point of view, to train much larger models which capture much more knowledge, so as to open the way towards human-level AI
  * Many applications which are under-explored, and in particular I would like to see much more work in the area of health (with some specific issues like missing values and being to exploit data from small studies via transfer learning)

    
