---
title: ''
author: aaditya prakash
layout: page
dsq_thread_id: []
---
[**CV [pdf]**](http://www.cs.brandeis.edu//~aprakash/CV.pdf)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✉ aprakash[at]brandeis.edu - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Public PGP](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/pgp_public_aaditya.txt)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="http://bitcoinsymbol.org/i/old-bitcoin-logo.svg" width="20px" height="20px" /> 19a2dDQDh3EDpHs5bhDyHnoGLMTwqjoEVv 



* * *



### <a name="biography" id="biography"></a>Biography



I am a PhD Student at [Brandeis University](http://www.brandeis.edu/), Boston. My research focus is in application of [deep learning in problems of computer vision]({{site.baseurl}}/notes/research/). Before joining grad school I was a Senior Systems Engineer at [Infosys Limited](https://www.infosys.com/). I am from Kathmandu, [**Nepal**](https://media.gadventures.com/media-server/image_library/Nepal-Himalaya-Mountains-Annapurna-Pokhara-Prayer-Flags-IS-027332084-Lg-RGB.jpg). My [name means "Sun"]({{site.baseurl}}/notes/name/), and it is pronounced as "aaa--Dee--ti--ya". Other than research, I love [rock climbing]({{site.baseurl}}/notes/climbing/), running, [playing chess]({{site.baseurl}}/notes/chess/) and listening to classical Indian songs. 



## News

* <font color="red"><strong>[New]</strong></font> Paper on **image compression using CNN** accepted to Data Compression Conference. [[Code]](https://github.com/iamaaditya/image-compression-cnn) [[PDF]](https://arxiv.org/pdf/1612.08712v1.pdf)

* <font color="red"><strong>[New]</strong></font> Paper on **condensed memory networks** accepted to AAAI 2017. [[PDF]](https://arxiv.org/pdf/1612.01848v1.pdf) [[Slides]](https://docs.google.com/presentation/d/1NSGEBYJmYEa5zsPJBocYcyRVZLKG0y274Wib_BlRX-U/edit?usp=sharing)

* Paper on **Neural Paraphrase Generation** accepted to COLING 2016. [[PDF]](https://arxiv.org/pdf/1610.03098v3.pdf) [[Poster]](https://www.dropbox.com/s/ju09291jukvtg50/coling_poster.pdf?dl=0)

* Won **Honrable Mention Prize** for Visual Question Answering Challenge [[Video]](https://www.youtube.com/watch?v=Fc2v_-VTRSY&index=14&list=PL_bDvITUYucC0r43EXIHkQE_fHVXlmboH) [[PDF](http://gpgpu.cs-i.brandeis.edu/highway.pdf) [[Slides]](https://docs.google.com/presentation/d/1EvYlvwXa7mjiQ2YjFmFs9LigOI8XFiYcd4jOqnprZyQ/edit?usp=sharing) [[Poster]](https://docs.google.com/presentation/d/1S5eVgDddkG4HaMLDBV5KaaDwPO_rDgMyNzOfq4LiJS0/edit?usp=sharing)

* Accepted to **Deep Learning Summer School** at University of Montrel [25% acceptance rate]

* Started summer internship at AI Labs at **Philips Research** 

* Our paper 'Highway Networks for Visual Question Answering' accepted for CVPR VQA workshop.





## Current Research

* * *

### Semantic image compression using CNN

<center> <img src="https://raw.githubusercontent.com/iamaaditya/image-compression-cnn/master/girl_msroi.png"> </center>

* __Problem__: Add semantic knowledge to image compression Semantic Image Compression

* __Our method__: Use CNN to generate a map that covers all the 'semantic objects' and weighs them based on importance. Use variable scaling JPEG to encode the information.
For more details :

* [[Code]](https://github.com/iamaaditya/image-compression-cnn) [[PDF]](https://arxiv.org/pdf/1612.08712v1.pdf)

* Supervisor - Prof. [James Storer](http://www.cs.brandeis.edu/~storer/)



### - Visual Question Answering 


<img src="http://visualqa.org/static/img/teaser_small.jpg" height="85%" width="85%" />
  


* __Problem__: Given a color image of arbitrary size and question of arbitrary length, come up with the most reasonable answer (ground truth obtained from 10 amazon-turks responses)

* __Our approach__: 

Use of Highway networks to attain implicit attention and learn deeper feature representations. [See this]({{site.baseurl}}/research/vqa/)  for more details

* Supervisor - Prof. [James Storer](http://www.cs.brandeis.edu/~storer/)



### - Transfer learning

 

* We are investigating ideas for improving content based image retrieval through transfer learning. 

* We are currently exploring ways to retrieve [MIT Places](http://places.csail.mit.edu/) (scene recognition database) using deep residual image models like [ResNet - 2015 ImageNet challenge winner](http://research.microsoft.com/en-us/um/people/kahe/ilsvrc15/ilsvrc2015_deep_residual_learning_kaiminghe.pdf). Our goal is to do ablation study on the 152 layers of ResNet for image retrieval task. 

* [Literature survey]({{site.baseurl}}/research/vector_quantization/) for compressing deep convolutional neural networks using vector quantization.



## Past Research

* * *



### - Computational Fact Checking [Summer 2014] 



* We investigated applications of computational fact checking on a database with retrospections.

* Implemented a fact checking application for database with weekly Music Billboards.

* [One page summary](https://drive.google.com/open?id=0Bw852LkIy1pXaG1ZN0l2R0M2Zms) &nbsp;&nbsp;&nbsp;&nbsp;-----&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Detailed Report](https://drive.google.com/open?id=0Bw852LkIy1pXWEF5Nkt6aUp2UVk)

* Supervisor - [Prof. Liuba Shrira](http://www.cs.brandeis.edu/~liuba/)



### - Self Organizing maps for large unstructured data [2013] - [Infosys Labs](http://www.infosysblogs.com/infosys-labs/bloggers.html) 

<br />

<img src="https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/som_image.png" height="60%" width="60%" />





* Formulated and designed a novel way to visualize self-organizing maps for unstructured big data.<br />

* Compared various forms of visual representation along with radar graphs and default visualization of self-organizing maps from most of the common packages in R and Matlab.<br />

* See Publication section for Abstract and PDF of the published work.





### - Distributed Simulated Annealing [2012] - [Infosys Labs](http://www.infosysblogs.com/infosys-labs/bloggers.html) 



* Studied industry scaled distributed simulated annealing and issues that arise when dealing with large scale optimization.

* Presented fault tolerance techniques for such a system designed for MapReduce infrastructure running on Apache Hadoop.

* See Publication section for Abstract and PDF of the published work.





## Projects

* * *



* [Detecting fallacy in sentences](https://github.com/gekonwi/brandeis.semantics.final_project) - A computational semantics project in Haskell. Collaborators - [Amin](https://github.com/amsa) & [Shlomo](https://github.com/gekonwi)

* [Social Travel guide](https://github.com/edenzik/elastiCity). Elastic Search project for travel search guide. Collaborators [Eden](https://github.com/edenzik), [Dimos](https://github.com/dimstamat) & Zhenyu.

* [Clipboard to Email](https://github.com/iamaaditya/Clipboard_to_Email). Send Code from clipboard to email automatically.







## Publications

* * *





### Published



*   Prakash, A. & Storer, J (2016) Highway Networks for Visual Question Answering, CVPR Workshop (VQA). [PDF](http://gpgpu.cs-i.brandeis.edu/highway.pdf)



*   Prakash, A. (2013). Reconstructing Self Organizing Maps as Spider Graphs for better visual interpretation of large unstructured datasets. _Infosys Lab Briefings, Infosys._ Vol 11(1). _Jan 2013_ <br />

    | [[Abstract]](http://aaditya.info/research/abstract_graph.txt) [[Full-pdf]](http://aaditya.info/research/graph.pdf) [[INFY]](http://www.infosys.com/infosys-labs/publications/infosyslabs-briefings/Pages/bigdata-challenges-opportunities.aspx) [[slides]](http://aaditya.info/research/slides_graph.pdf) |



*   Prakash, A. (2012). Measures of Fault Tolerance in Distributed Simulated Annealing. _Proceedings of International Conference on Perspective of Computer Confluence with Sciences._ Vol 1 pp 111-114\.<br />

    | [[Abstract]](http://aaditya.info/research/abstract_fault.txt) [[Full-pdf]](http://aaditya.info/research/fault.pdf) [[arXiv]](http://arxiv.org/abs/1212.3295) [[slides]](http://aaditya.info/research/slides_fault.pdf) |



*   Prakash, A., & Jha, R. K. (2012). New Interface Protocol to Connect Multiple Bank Networks from a Single Outlet. _International Journal of Computer Applications, NY, USA_ Vol. 55(1) pp 1-9.<br />

    | [[Abstract]](http://aaditya.info/research/abstract_protocol.txt) [[Full-pdf]](http://aaditya.info/research/protocol.pdf) [[IJCA]](http://www.ijcaonline.org/archives/volume55/number12/8804-3034) [[slides]](http://aaditya.info/research/slides_protocol.pdf) |







* * *



[Quora](http://www.quora.com/Aaditya-Prakash) - [Wikipedia](http://en.wikipedia.org/wiki/User:Iamaaditya) - [Google+](https://plus.google.com/u/0/100303074762902184969?rel=author) - [Twitter](http://twitter.com/aaditya_prakash) - [Linkedin](https://in.linkedin.com/in/aaditya-prakash-68453338) - [Academia.edu](http://infosys.academia.edu/aadityaprakash) - [SlideShare](http://www.slideshare.net/aadityaprakash/) - [GitHub](https://github.com/iamaaditya)



