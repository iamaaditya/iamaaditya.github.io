---
title: Best Practices
author: aaditya prakash
layout: page
dsq_thread_id:
- 
---


## Google Developers
Source: <https://developers.google.com/machine-learning/rules-of-ml/>
(More details on the link)
   * Don’t be afraid to launch a product without machine learning.
   * First, design and implement metrics.
   * Choose machine learning over a complex heuristic.
   * Keep the first model simple and get the infrastructure right.
   * Test the infrastructure independently from the machine learning.
   * Be careful about dropped data when copying pipelines.
   * Turn heuristics into features, or handle them externally.
   * Know the freshness requirements of your system.
   * Detect problems before exporting models.
   * Watch for silent failures.
   * Give feature columns owners and documentation.
   * Don’t overthink which objective you choose to directly optimize.
   * Choose a simple, observable and attributable metric for your first objective.
   * Starting with an interpretable model makes debugging easier.
   * Separate Spam Filtering and Quality Ranking in a Policy Layer.
   * Plan to launch and iterate.
   * Start with directly observed and reported features as opposed to learned features.
   * Explore with features of content that generalize across contexts.
   * Use very specific features when you can.
   * Combine and modify existing features to create new features in human­-understandable ways.
   * The number of feature weights you can learn in a linear model is roughly proportional to the amount of data you have.
   * Clean up features you are no longer using.
   * You are not a typical end user.
   * Measure the delta between models.
   * When choosing models, utilitarian performance trumps predictive power.
   * Look for patterns in the measured errors, and create new features.
   * Try to quantify observed undesirable behavior.
   * Be aware that identical short-term behavior does not imply identical long-term behavior.
   * The best way to make sure that you train like you serve is to save the set of features used at serving time, and then pipe those features to a log to use them at training time.
   * Importance-weight sampled data, don’t arbitrarily drop it!
   * Beware that if you join data from a table at training and serving time, the data in the table may change.
   * Re-use code between your training pipeline and your serving pipeline whenever possible.
   * If you produce a model based on the data until January 5th, test the model on the data from January 6th and after.
   * In binary classification for filtering (such as spam detection or determining interesting emails), make small short-term sacrifices in performance for very clean data.
   * Beware of the inherent skew in ranking problems.
   * Avoid feedback loops with positional features.
   * Measure Training/Serving Skew.
   * Don’t waste time on new features if unaligned objectives have become the issue.
   * Launch decisions are a proxy for long-term product goals.
   * Keep ensembles simple.
   * When performance plateaus, look for qualitatively new sources of information to add rather than refining existing signals.
   * Don’t expect diversity, personalization, or relevance to be as correlated with popularity as you think they are.


## Nishant G 
Source: <http://forums.fast.ai/t/30-best-practices/12344>
<h3>Data Set</h3>
<ul>
<li>Do as much of your work as you can on a small sample of the data (<a href="https://youtu.be/Th_ckFbc6bI?t=3503" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="137 clicks">137</span></a>)</li>
<li>Public leaderboard of Kaggle is not a replacement for Validation Set. Jeremy showed how he was ranked in 5th in the private leaderboard of Rossmann Competition, whereas he was not in top 300 in public leaderboard. In another example, The test set of public leaderboard (in Iceberg Satellite image Competition) contained mostly of augmented images. (<a href="https://youtu.be/sHcLkfRrgoQ?t=2739" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="23 clicks">23</span></a>)</li>
<li>Look into data. Remove outliers which make sense and there is no other variable to capture those outliers: like in Rossmann Competition, the date&amp;timings for closed stores were not known. There is extra sale before and after close period. So, if you don’t have any data to model the outliers, you need to remove them during training. (<a href="https://youtu.be/sHcLkfRrgoQ?t=2898" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="11 clicks">11</span></a>)</li>
<li>Look into training:  After training the cats vs dogs we could see that some incorrect classified images were mostly misclassified due to cropping. The solution was data augmentation (<a href="https://youtu.be/IPBSB1HLNLo?t=1674" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="9 clicks">9</span></a>)</li>
<li>Data Augmentation: You cannot use all possible types of augmentation. For best results we need to use the right kind of augmentation. (<a href="https://youtu.be/9C06ZPF8Uuc?t=1408" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="34 clicks">34</span></a>)</li>
<li>Test Time Augmentation (TTA): Increases accuracy <a href="https://youtu.be/JNxcznsrRb8?t=3669" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="38 clicks">38</span></a>
</li>
<li>Rossman Notebook: Without expanding your date-time column using <code>add_date_part</code> function of fastai library, you can’t capture any trend/cyclical behavior as a function of time at any of these granularities. We’ll add to every table with a date field.</li>
<li>Rossman Notebook: many models have problems when missing values are present, so it’s always important to think about how to deal with them. In these cases, we are picking an arbitrary signal value that doesn’t otherwise appear in the data.</li>
</ul>
<h3>Learning Rate</h3>
<ul>
<li>Use learning rate finder and select a learning where convergence of loss is steep. Do not select the biggest possible learning rate. (<a href="https://youtu.be/JNxcznsrRb8?t=1320" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="54 clicks">54</span></a>)</li>
<li>When using a pretrained model on some dataset like imagenet, you need to use different learning rates when you are using that model for any new dataset. The initial layers need a smaller learning rate, and the deeper layers need a comparatively larger learning rate. When the new dataset is similar to original dataset (e.g. cats vs dogs is similar to imagenet but iceberg satellite image is not) the weights have a ratio of 10. But when using the imagenet of satellite model the successive weights should have a ratio of 3. (<a href="https://youtu.be/9C06ZPF8Uuc?t=5858" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="13 clicks">13</span></a>)</li>
<li>Cosine annealing: This now supported by default in pytorch <a href="http://pytorch.org/docs/0.3.1/optim.html#torch.optim.lr_scheduler.CosineAnnealingLR" rel="nofollow noopener">0.3.1<span class="badge badge-notification clicks" title="16 clicks">16</span></a> (<a href="https://youtu.be/JNxcznsrRb8?t=2291" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="32 clicks">32</span></a>)</li>
<li>SGD with restarts: 2 setups work very well. (<a href="https://youtu.be/JNxcznsrRb8?t=3272" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="27 clicks">27</span></a>)</li>
<li>To tackle Gradient Explosion we use identity matrix for intialization (<a href="https://youtu.be/sHcLkfRrgoQ?t=7780" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="31 clicks">31</span></a>) Also allows higher learning rate.</li>
</ul>
<h3>Training</h3>
<ul>
<li>bn_freeze = True: In case you are using a deeper network anything greater than resnet34 (like resnext50), bn_freeze = True should be used when you unfreeze and your new dataset is very similar to the original data used in pretrained model (<a href="https://youtu.be/9C06ZPF8Uuc?t=1109" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="20 clicks">20</span></a>) Pytorch is probably the only library which offers this much needed switch.</li>
<li>On the other hand, when the new dataset is not similar to the original dataset, we start with smaller size 64x64, fit in freezed state, unfreeze and fit. And repeat the process with 128x128 and 256x256 (<a href="https://youtu.be/9C06ZPF8Uuc?t=5898" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="8 clicks">8</span></a>)</li>
<li>Kaiming He Initialization: Pytorch has this implemented by default. (<a href="https://youtu.be/J99NV9Cr75I?t=2844" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="19 clicks">19</span></a>)</li>
<li>Adam Optimizer has a better version called AdamW</li>
</ul>
<h3>Activation functions</h3>
<ul>
<li>theoretically softmax and logsoftmax are scaled version of each other, but empirically logsoftmax is better</li>
<li>sigmoid instead of softmax for multi-label classification (<a href="https://youtu.be/9C06ZPF8Uuc?t=4943" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="38 clicks">38</span></a>)</li>
<li>applying sigmoid in the end when you know the min and max of output (eg. highest sale and lowest sale is known in the Rossmann data) relieves the neural network and training is faster.(<a href="https://youtu.be/J99NV9Cr75I?t=4101" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="8 clicks">8</span></a>) This is similar to applying softmax when you know the output should be probability (<a href="https://youtu.be/9C06ZPF8Uuc?t=4498" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="1 click">1</span></a>)</li>
<li>In hidden state to hidden state transition weight matrices tanh is used (<a href="https://youtu.be/sHcLkfRrgoQ?t=6237" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="8 clicks">8</span></a>)</li>
</ul>
<h3>Architectures</h3>
<ul>
<li>In nlp, we have to use slightly different betas in Adam Optimizer (<a href="https://youtu.be/gbceqO8PpBg?t=7175" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="30 clicks">30</span></a>)</li>
<li>In nlp, we use different dropouts all over the place in a specific LSTM model. These dropouts have to be in a certain ratio. (<a href="https://youtu.be/gbceqO8PpBg?t=7206" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="15 clicks">15</span></a>)</li>
<li>In nlp, we use also use gradient clipping. There is no reason why this cannot be used in other models (<a href="https://youtu.be/gbceqO8PpBg?t=7316" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="3 clicks">3</span></a>)</li>
<li>All the NLP models probably need a line of code for regularisation (<a href="https://youtu.be/gbceqO8PpBg?t=7262" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="18 clicks">18</span></a>)</li>
<li>RNN cell is not used nowadays coz of low learning rate constraint due to gradient explosion. We use GRU</li>
<li>In sentiment analysis, transfer learning has outperformed state of the art sentiment analysis models <a href="https://youtu.be/gbceqO8PpBg?t=7738" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="9 clicks">9</span></a>
</li>
<li>Stride 2 convolution has same effect as Max Pool</li>
<li>Batch normalisation allows us to design resilient deeper networks and learning rate can be made higher. It is similar to dropout in the sense that it changes the meaning of the layers, which a kind of regularisation technique like dropout. Therefore, like dropout it is not done in test mode. (<a href="https://youtu.be/H3g26EVADgY?t=5732" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="6 clicks">6</span></a>)</li>
<li>Batch normalisation works best when done after relU</li>
<li>Resnet ensures richer input for first layer. 5by5 convolution is used in start, and stride is set to 1. In subsequent layers stride is 2 and 3by3 convolution is used. Padding is important when your activations are smaller like 4by4. (<a href="https://youtu.be/H3g26EVADgY?t=4972" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="5 clicks">5</span></a>)</li>
<li>Resnet uses something known as Identity training. It has layer-groups. Each layer-group has a bottleneck layer with stride = 2, which causes reduction in activation size. The rest of the layers in the group just try to predict the error through identity training. This concept is yet to be explored in NLP. (<a href="https://youtu.be/H3g26EVADgY?t=6913" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="4 clicks">4</span></a>)</li>
<li>Concatenation of AdaptiveAvg Pooling and AdaptiveMaxPooling is better. (<a href="https://youtu.be/H3g26EVADgY?t=7611" rel="nofollow noopener">source<span class="badge badge-notification clicks" title="20 clicks">20</span></a>)</li>
</ul></div>

