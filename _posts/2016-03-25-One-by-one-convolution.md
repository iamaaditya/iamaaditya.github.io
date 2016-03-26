---
title: One by One [ 1 x 1 ] Convolution - counter-intuitively useful
author: aaditya prakash
layout: post
permalink: /2016/03/
categories:
  - computer science
  - math
tags:
  - convolutional neural network
  - math
  - deep learning
---

Whenever I discuss or show [GoogleNet architecture](http://arxiv.org/pdf/1409.4842v1.pdf), one question always comes up - <br /><br />
**"Why 1x1 convolution ? Is it not redundant ?**

![Convolution with Kernel of size 3x3](http://himal.cs-i.brandeis.edu/ap/conv_arithmetic/gif_/full_padding_no_strides_transposed.gif)
![Convolution with Kernel of size 1x1](http://himal.cs-i.brandeis.edu/ap/conv_arithmetic/gif/full_padding_no_strides_transposed.gif)

left : **Convolution with kernel of size 3x3**               right : **Convolution with kernel of size 1x1**



## Simple Answer

Most simplistic explanation would be that 1x1 convolution leads to dimension reductionality. For example, an image of 200 x 200 with 50 features on convolution with 20 filters of 1x1 would result in size of 200 x 200 x 20.
But then again, is this is the best way to do dimensionality reduction in the convoluational neural network? What about the efficacy vs efficiency?

## Complex Answer

### Feature transformation
Although 1x1 convolution is a 'feature pooling' technique, there is more to it than just sum pooling of features across various channels/feature-maps of a given layer. 
1x1 convolution acts like coordinate-dependent transformation in the filter space[[1](https://plus.google.com/118431607943208545663/posts/2y7nmBuh2ar)]. It is important to note here that this transformation is strictly linear, but in most of application of 1x1 convolution, it is succeeded by a non-linear activation layer like ReLU. This transformation is learned through the (stochastic) gradient descent. But an important distinction is that it suffers with less over-fitting due to smaller kernel size (1x1).

### Deeper Network

One by One convolution was first introduced in this paper titled [Network in Network](http://arxiv.org/pdf/1312.4400v3.pdf). In this paper, the author's goal was to generate a deeper network without simply stacking more layers. It replaces few filters with a smaller perceptron layer with mixture of 1x1 and 3x3 convolutions. In a way, it can be seen as "going wide" instead of "deep", but I think it would a gross oversimplication to say it so naively. Combination of 1x1 (x F) convolution is mathematically equivalent to a multi-layer perceptron.[[2](https://www.reddit.com/r/MachineLearning/comments/3oln72/1x1_convolutions_why_use_them/cvyxood)]. 

In designing such a network, it is important to note that initial convolution kernel should be of size larger than 1x1 to get have a receptive field capable of capturing locally spatial information. According to the NIN paper, 1x1 convolution is equivalent to cross-channel parametric pooling layer. From the paper - "This cascaded cross channel parameteric pooling structure allows complex and learnable interactions of cross channel information".

Cross channel information learning (cascaded 1x1 convolution) is important because human visual cortex have receptive fields (kernels) tuned to different orientation. For e.g 

![different orientation tuned receptive field profiles in the human visual cortex](http://bmia.bmt.tue.nl/education/courses/fev/course/notebooks/RotBundleFiltersListPlot3D.gif)


**Different orientation tuned receptive field profiles in the human visual cortex** [Source](http://bmia.bmt.tue.nl/education/courses/fev/course/notebooks/Convolution.html)


### More Uses

  * 1x1 Convolution can be combined with Max pooling

  ![Pooling with 1x1 convolution](http://himal.cs-i.brandeis.edu/ap/conv_arithmetic/gif/numerical_max_pooling.gif)
   **Pooling with 1x1 convolution**

  * 1x1 Convolution with higher strides leads to even more redution in data, while losing very little non-spatially correlated information

  ![1x1 convolution with strides](http://himal.cs-i.brandeis.edu/ap/conv_arithmetic/gif/no_padding_strides.gif)
   **1x1 convolution with strides**

  * Replace fully connected layers with 1x1 convolutions as Yann LeCun believes they are the same -
> In Convolutional Nets, there is no such thing as "fully-connected layers". There are only convolution layers with 1x1 convolution kernels and a full connection table.
-- [Yann LeCun](https://www.facebook.com/yann.lecun/posts/10152820758292143)

*Images generated using [this wonderful code](https://github.com/vdumoulin/conv_arithmetic)*

*More images on 1x1 convolutions and 3x3 convolutions can be [found here](http://gpgpu.cs-i.brandeis.edu/convolution_images/* 

