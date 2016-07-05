---
title: Paper Summaries
date: '2016-07-05 18:45:00'
layout: page
draft: true
---
## Wide & Deep Learning for Recommender Systems

### [PDF](http://arxiv.org/abs/1606.07792)

### Summary

This proposes a novel concept of jointly training a deep network along with a shallow network (which they call as 'wide network') for doing recommendation. [Figure 1] They specially look at Apps recommendation on Google Play Store.

Idea behind using two parallel networks is that, while doing recommendation a system needs to balance 'memoriziation' and 'generatlization'. Memorization means that the app being recommended should be very similar to the app off of which the recommendation is being based in. For e.g if you were looking for a single person shooting game, an another game of similar nature. It would be too tangentially to show music apps as recommendation for this scenario. Generatlization refers the ability to deviate from the very specific and exact matches. For the scenario described above if the system recommended another first person shooting game, then the recommendation would be boring. 

They jointly training the network, i.e the learning of weights and loss minimzation happens together for both the networks. They argue that 'wide' network memorises easily while the deep learning generalizes better. For wide network they use simple cross product transformation (product of binary features) whereas for deep network they use learned embeddings and three layers of relu [See figure 4].

They also discuss few engineering details to serve this system in a online learning process so that the user's current search is included in the learning process. They have the emperical result from A/B testing on Google Play that it is better than using traditional Collaborative filtering or just using deep network.
