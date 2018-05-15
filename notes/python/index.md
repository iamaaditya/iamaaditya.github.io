---
title: Python Hacks
author: aaditya prakash
layout: page
dsq_thread_id:
- 
---

## Awesome one-liners (or little more)
  * Breaking list into sublists (useful in files) 
     - group consecutive
     z = [1,11,111, 2, 22, 222, 3, 33, 333]
       zip(*[iter(z)]*3)
       [(1, 11, 111), (2, 22, 222), (3, 33, 333)]

     - group by position
       [z[i::3] for i in range(3)]
       [[1, 2, 3], [11, 22, 33], [111, 222, 333]]

  * Most common item in the list
    - Using Collections Counter
    ` from collections import Counter
    Counter(lst).most_common(1)[0][0] `

    - Without using Counter Credit http://stackoverflow.com/a/1518632/1189865
    ` def most_common(lst):
    return max(set(lst), key=lst.count) `

  * Invert python dictionary

  `ans_to_ix = {v: k for k, v in dataset[u'ix_to_ans'].items()} `

  * Good Numpy Tutorial <http://www.scipy-lectures.org/intro/numpy/numpy.html>





