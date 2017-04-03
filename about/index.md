---
title: ''
author: aaditya prakash
layout: page
dsq_thread_id: []
---
<img src="https://www.shareicon.net/data/128x128/2016/11/22/854973_email_512x512.png" height="20px" width="20px" /> aprakash[at]brandeis.edu &nbsp; [<img src="https://github.com/favicon.ico" height="20px" width="20px"> iamaaditya](https://github.com/iamaaditya)&nbsp;&nbsp;&nbsp;[<img src="https://upload.wikimedia.org/wikipedia/vi/b/bf/PGP_Icon.png" height="20px" width="20px"> Public PGP](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/pgp_public_aaditya.txt)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<img src="http://bitcoinsymbol.org/i/old-bitcoin-logo.svg" width="20px" height="20px" /> Address](https://blockchain.info/address/19a2dDQDh3EDpHs5bhDyHnoGLMTwqjoEVv) &nbsp;&nbsp; [<img src="https://www.twitter.com/favicon.ico" height="20px" width="20px" />@aaditya_prakash](https://twitter.com/aaditya_prakash) &nbsp;&nbsp; [<img src="https://www.quora.com/favicon.ico" height="20px" width="20px" />Quora](https://www.quora.com/profile/Aaditya-Prakash)

* * *

Table of Contents &nbsp;&nbsp;&nbsp; [Biography](#biography) &nbsp;&nbsp;&nbsp; [Highlights](#highlights) &nbsp;&nbsp;&nbsp; [Research](#current-research) &nbsp;&nbsp;&nbsp; [Projects](#projects) &nbsp;&nbsp;&nbsp; [Publications](#publications) 


## <a name="biography" id="biography"></a>Biography

I am a PhD Student at [Brandeis University](http://www.brandeis.edu/), Boston. My research focus is in application of [deep learning in problems of vision and language]({{site.baseurl}}/notes/research/). Before joining grad school I was a Senior Systems Engineer at [Infosys Limited](https://www.infosys.com/). I am from Kathmandu, [**Nepal**](https://media.gadventures.com/media-server/image_library/Nepal-Himalaya-Mountains-Annapurna-Pokhara-Prayer-Flags-IS-027332084-Lg-RGB.jpg). My [name means "Sun"]({{site.baseurl}}/notes/name/), and it is pronounced as "aaa--Dee--ti--ya". Other than research, I love [rock climbing]({{site.baseurl}}/notes/climbing/), running, [playing chess]({{site.baseurl}}/notes/chess/) and listening to classical Indian songs. 


## Highlights

* <img src="https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/new.jpg" /> Gave five lecture series on Deep Learning, Convolutional Neural Networks, Recurrent Neural Networks, Object localization/detection and Memory Networks. [[Slides]](http://iamaaditya.github.io/notes/CS175/)

* <img src="https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/new.jpg" /> Paper on **image compression using CNN** accepted to Data Compression Conference. [[Code]](https://github.com/iamaaditya/image-compression-cnn) [[PDF]](https://arxiv.org/pdf/1612.08712v1.pdf)

* Paper on **Condensed Memory Networks** accepted to AAAI 2017. [[PDF]](https://arxiv.org/pdf/1612.01848v1.pdf) [[Slides]](https://docs.google.com/presentation/d/1NSGEBYJmYEa5zsPJBocYcyRVZLKG0y274Wib_BlRX-U/edit?usp=sharing)  [[Poster]](https://github.com/iamaaditya/research-papers-slides-posters/raw/master/aaai_2017/aaai_poster.pdf)

* Paper on **Neural Paraphrase Generation** accepted to COLING 2016. [[PDF]](https://arxiv.org/pdf/1610.03098v3.pdf) [[Poster]](https://www.dropbox.com/s/ju09291jukvtg50/coling_poster.pdf?dl=0)

* Won **Honrable Mention Prize** for Visual Question Answering Challenge. [[Video]](https://www.youtube.com/watch?v=Fc2v_-VTRSY&index=14&list=PL_bDvITUYucC0r43EXIHkQE_fHVXlmboH) [[Slides]](https://docs.google.com/presentation/d/1EvYlvwXa7mjiQ2YjFmFs9LigOI8XFiYcd4jOqnprZyQ/edit?usp=sharing) [[Poster]](https://docs.google.com/presentation/d/1S5eVgDddkG4HaMLDBV5KaaDwPO_rDgMyNzOfq4LiJS0/edit?usp=sharing)

* Accepted to **Deep Learning Summer School** at University of Montrel. [25% acceptance rate]

* Started summer internship at AI Labs at **Philips Research**. 

* Paper on **'Highway Networks for Visual Question Answering'** accepted for CVPR VQA workshop. [[PDF]](http://gpgpu.cs-i.brandeis.edu/highway.pdf)



## Research

* * *

### - Condensed Memory Networks

<center> <img src="https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/cmemnn_for_about.png" height="85%" width="85%"> </center>

* __Problem__: Improve the memory networks for large scale NLP tasks

* __Our method__: Add an alternate memory state which is condensed with previous hop values exponentially fewer slots.

* [[PDF]](https://arxiv.org/pdf/1612.01848v1.pdf) [[Slides]](https://docs.google.com/presentation/d/1NSGEBYJmYEa5zsPJBocYcyRVZLKG0y274Wib_BlRX-U/edit?usp=sharing)

* Blog post describing the project coming soon.

* * *

### - Semantic image compression using CNN

<center> <img src="https://raw.githubusercontent.com/iamaaditya/image-compression-cnn/master/girl_msroi.png" height="85%" width="85%"> </center>

* __Problem__: Add semantic knowledge to image compression Semantic Image Compression

* __Our method__: Use CNN to generate a map that covers all the 'semantic objects' and weighs them based on importance. Use variable scaling JPEG to encode the information.
For more details :

* [[Code]](https://github.com/iamaaditya/image-compression-cnn) [[PDF]](https://arxiv.org/pdf/1612.08712v1.pdf) [[Slides]](https://github.com/iamaaditya/research-papers-slides-posters/raw/master/dcc_2017/dcc_slides.pdf)

* Supervisor - Prof. [James Storer](http://www.cs.brandeis.edu/~storer/)

* * *

### - Neural Paraphrase generation using Residual Stacked LSTM

<center> <img src="https://github.com/iamaaditya/iamaaditya.github.io/raw/master/images/residual_lstm.png" height="45%" width="45%"> </center>

* __Problem__: Generate paraphrases using a 'neural' model.

* __Our method__: We take inspiration from ResNet and apply the same techniques to LSTM. We believe this helpes to maintain the semantics of the paraphrases.

* Work done during internship at Philips Research.

* Shown below are samples using our method on three different datasets.

<center> <img src="https://github.com/iamaaditya/iamaaditya.github.io/raw/master/images/paraphrase_samples.png" height="85%" width="85%"> </center>



* * *

### - Visual Question Answering 


<center> <img src="http://visualqa.org/static/img/teaser_small.jpg" height="90%" width="90%" /> </center>
  

* __Problem__: Given a color image of arbitrary size and question of arbitrary length, come up with the most reasonable answer (ground truth obtained from 10 amazon-turks responses)

* __Our approach__: Use of Highway networks to attain implicit attention and learn deeper feature representations. [See this]({{site.baseurl}}/research/vqa/)  for more details

* Supervisor - Prof. [James Storer](http://www.cs.brandeis.edu/~storer/)


* * *


### - Transfer learning


* We are investigating ideas for improving content based image retrieval through transfer learning. 

* We are currently exploring ways to retrieve [MIT Places](http://places.csail.mit.edu/) (scene recognition database) using deep residual image models like [ResNet - 2015 ImageNet challenge winner](http://research.microsoft.com/en-us/um/people/kahe/ilsvrc15/ilsvrc2015_deep_residual_learning_kaiminghe.pdf). Our goal is to do ablation study on the 152 layers of ResNet for image retrieval task. 

* [Literature survey]({{site.baseurl}}/research/vector_quantization/) for compressing deep convolutional neural networks using vector quantization.



## Pre-Grad Research

* * *

### - Computational Fact Checking [Summer 2014] 



* We investigated applications of computational fact checking on a database with retrospections.

* Implemented a fact checking application for database with weekly Music Billboards.

* [One page summary](https://drive.google.com/open?id=0Bw852LkIy1pXaG1ZN0l2R0M2Zms) &nbsp;&nbsp;&nbsp;&nbsp;-----&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Detailed Report](https://drive.google.com/open?id=0Bw852LkIy1pXWEF5Nkt6aUp2UVk)

* Supervisor - [Prof. Liuba Shrira](http://www.cs.brandeis.edu/~liuba/)



* * *

### - Self Organizing maps for large unstructured data [2013] - [Infosys Labs](http://www.infosysblogs.com/infosys-labs/bloggers.html) 

<br />

<center> <img src="https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/som_image.png" height="60%" width="60%" /> </center>





* Formulated and designed a novel way to visualize self-organizing maps for unstructured big data.<br />

* Compared various forms of visual representation along with radar graphs and default visualization of self-organizing maps from most of the common packages in R and Matlab.<br />

* See Publication section for Abstract and PDF of the published work.



* * *



### - Distributed Simulated Annealing [2012] - [Infosys Labs](http://www.infosysblogs.com/infosys-labs/bloggers.html) 



* Studied industry scaled distributed simulated annealing and issues that arise when dealing with large scale optimization.

* Presented fault tolerance techniques for such a system designed for MapReduce infrastructure running on Apache Hadoop.

* See Publication section for Abstract and PDF of the published work.

* * *

## Projects

* * *


* [Detecting fallacy in sentences](https://github.com/gekonwi/brandeis.semantics.final_project) - A computational semantics project in Haskell. Collaborators - [Amin](https://github.com/amsa) & [Shlomo](https://github.com/gekonwi)

* [Social Travel guide](https://github.com/edenzik/elastiCity). Elastic Search project for travel search guide. Collaborators [Eden](https://github.com/edenzik), [Dimos](https://github.com/dimstamat) & Zhenyu.

* [Clipboard to Email](https://github.com/iamaaditya/Clipboard_to_Email). Send Code from clipboard to email automatically.


## Publications

* * *

### In Review

* Garber, Solomon et al. "Static Visual Lecture Summary using Local Intensity Correlation".

### Published


* * *
Prakash, Aaditya, et al. "Semantic Perceptual Image Compression using Deep Convolution Networks." DCC (2017). <br />
<details> <summary><a>Abstract</a></summary>
It has long been considered a significant problem to improve the visual quality of lossy image and video compression. Recent advances in computing power together with the availability of large training data sets has increased interest in the application of deep learning cnns to address image recognition and image processing tasks. Here, we present a powerful cnn tailored to the specific task of semantic image understanding to achieve higher visual quality in lossy compression. A modest increase in complexity is incorporated to the encoder which allows a standard, off-the-shelf jpeg decoder to be used. While jpeg encoding may be optimized for generic images, the process is ultimately unaware of the specific content of the image to be compressed. Our technique makes jpeg content-aware by designing and training a model to identify multiple semantic regions in a given image. Unlike object detection techniques, our model does not require labeling of object positions and is able to identify objects in a single pass. We present a new cnn architecture directed specifically to image compression, which generates a map that highlights semantically-salient regions so that they can be encoded at higher quality as compared to background regions. By adding a complete set of features for every class, and then taking a threshold over the sum of all feature activations, we generate a map that highlights semantically-salient regions so that they can be encoded at a better quality compared to background regions. Experiments are presented on the Kodak PhotoCD dataset and the MIT Saliency Benchmark dataset, in which our algorithm achieves higher visual quality for the same compressed size.
</details>
[[PDF]](https://arxiv.org/pdf/1612.08712v1.pdf) [[Code]](https://github.com/iamaaditya/image-compression-cnn) 

* * *

Prakash, Aaditya, et al. "Condensed Memory Networks for Clinical Diagnostic Inferencing." AAAI (2017). <br />
<details> <summary><a>Abstract</a></summary>
Diagnosis of a clinical condition is a challenging task, which often requires significant medical investigation. Previous work related to diagnostic inferencing problems mostly consider multivariate observational data (e.g. physiological signals , lab tests etc.). In contrast, we explore the problem using free-text medical notes recorded in an electronic health record (EHR). Complex tasks like these can benefit from structured knowledge bases, but those are not scalable. We instead exploit raw text from Wikipedia as a knowledge source. Memory networks have been demonstrated to be effective in tasks which require comprehension of free-form text. They use the final iteration of the learned representation to predict probable classes. We introduce condensed memory neural networks (C-MemNNs), a novel model with iterative condensation of memory representations that preserves the hierarchy of features in the memory. Experiments on the MIMIC-III dataset show that the proposed model outperforms other variants of memory networks to predict the most probable diagnoses given a complex clinical scenario.
</details>
[[PDF]](https://arxiv.org/pdf/1612.01848v1.pdf) [[Slides]](https://docs.google.com/presentation/d/1NSGEBYJmYEa5zsPJBocYcyRVZLKG0y274Wib_BlRX-U/edit?usp=sharing)  [[Poster]](https://github.com/iamaaditya/research-papers-slides-posters/raw/master/aaai_2017/aaai_poster.pdf)

* * *

Prakash, Aaditya, et al. "Neural Paraphrase Generation with Stacked Residual LSTM Networks." COLING (2016). <br />
<details> <summary><a>Abstract</a></summary>
n this paper, we propose a novel neural approach for paraphrase generation. Conventional paraphrase generation methods either leverage handwritten rules and thesauri-based alignments, or use statistical machine learning principles. To the best of our knowledge, this work is the first to explore deep learning models for paraphrase generation. Our primary contribution is a stacked residual LSTM network, where we add residual connections between LSTM layers. This allows for efficient training of deep LSTMs. We experiment with our model and other state-of-the-art deep learning models on three different datasets: PPDB, WikiAnswers and MSCOCO. Evaluation results demonstrate that our model outperforms sequence to sequence, attention-based and bi-directional LSTM models on BLEU, METEOR, TER and an embedding-based sentence similarity metric.
</details>
[[PDF]](https://arxiv.org/pdf/1610.03098v3.pdf) [[Poster]](https://github.com/iamaaditya/research-papers-slides-posters/raw/master/coling_2016/coling_poster.pdf)

* * *

Prakash, A. & Storer, J (2016) Highway Networks for Visual Question Answering, CVPR Workshop (VQA). <br />
<details> <summary><a>Abstract</a></summary>
We propose a version of highway network designed for the task of Visual Question Answering. We take inspiration from recent success of Residual Layer Network and Highway Network in learning deep representation of images and fine grained localization of objects. We propose variation in gating mechanism to allow incorporation of word embedding in the information highway. The gate parameters are influenced by the words in the question, which steers the network towards localized feature learning. This achieves the same effect as soft attention via recurrence but allows for faster training using optimized feed-forward techniques.  We are able to obtain state-of-the-art1 results on VQA dataset for Open Ended and Multiple Choice tasks with current model.
</details>
[[PDF]](http://gpgpu.cs-i.brandeis.edu/highway.pdf) [[Slides]](https://docs.google.com/presentation/d/1nrc-kOmDn1Msp41q8gwiiDFrXa0uKoBatlk1plmo8GM/edit?usp=sharing) [[Poster]](https://github.com/iamaaditya/research-papers-slides-posters/raw/master/cvpr_2016/cvpr_poster.pdf)

* * *


### Pre grad school

*   Prakash, A. (2013). Reconstructing Self Organizing Maps as Spider Graphs for better visual interpretation of large unstructured datasets. _Infosys Lab Briefings, Infosys._ Vol 11(1). _Jan 2013_ <br />

    | [[Abstract]](http://aaditya.info/research/abstract_graph.txt) [[Full-pdf]](http://aaditya.info/research/graph.pdf) [[INFY]](http://www.infosys.com/infosys-labs/publications/infosyslabs-briefings/Pages/bigdata-challenges-opportunities.aspx) [[slides]](http://aaditya.info/research/slides_graph.pdf) |



*   Prakash, A. (2012). Measures of Fault Tolerance in Distributed Simulated Annealing. _Proceedings of International Conference on Perspective of Computer Confluence with Sciences._ Vol 1 pp 111-114\.<br />

    | [[Abstract]](http://aaditya.info/research/abstract_fault.txt) [[Full-pdf]](http://aaditya.info/research/fault.pdf) [[arXiv]](http://arxiv.org/abs/1212.3295) [[slides]](http://aaditya.info/research/slides_fault.pdf) |



*   Prakash, A., & Jha, R. K. (2012). New Interface Protocol to Connect Multiple Bank Networks from a Single Outlet. _International Journal of Computer Applications, NY, USA_ Vol. 55(1) pp 1-9.<br />

    | [[Abstract]](http://aaditya.info/research/abstract_protocol.txt) [[Full-pdf]](http://aaditya.info/research/protocol.pdf) [[IJCA]](http://www.ijcaonline.org/archives/volume55/number12/8804-3034) [[slides]](http://aaditya.info/research/slides_protocol.pdf) |

* * *

[Quora](http://www.quora.com/Aaditya-Prakash) - [Wikipedia](http://en.wikipedia.org/wiki/User:Iamaaditya) - [Google+](https://plus.google.com/u/0/100303074762902184969?rel=author) - [Twitter](http://twitter.com/aaditya_prakash) - [Linkedin](https://in.linkedin.com/in/aaditya-prakash-68453338) - [Academia.edu](http://infosys.academia.edu/aadityaprakash) - [SlideShare](http://www.slideshare.net/aadityaprakash/) - [GitHub](https://github.com/iamaaditya) - [ResearchGate](https://www.researchgate.net/profile/Aaditya_Prakash3)

<details>
  <summary><a>Thank you!</a></summary>
  (づ｡◕‿‿◕｡)づ
</details>
