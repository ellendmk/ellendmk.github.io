---
layout: post
title: Taking the confusion out of confusion matrices
date: 2023-06-23 14:29:00
---

Confusion matrices can at times be confusing and so can all the metrics that go along with them. Here we'll try to break down intuitively what their purpose is and what each of the metrics mean.


# Why do we need confusion matrices?


Confusion matrices are a useful way to summarise model perfromance when dealing with classification tasks. Not only do they apply to the binary classifcation task but can also be used when dealing with more than two classes.

You might be thinking we have a simple way to evaluate model performance already - lets see how accurate our predictions are? What proportion of our predicted labels match the actual labels? Lets look at an example to see why accuracy is not a great metric.

Say we have a dataset made up of 100 cricket players from UK cricket clubs. Our target variable is a boolean value *opening_batsman*  which indicates if a player is an opener (1) or isn't (0). Our target is only 5% of our data (meaning 5 of the players in our data are opening bastmen).

If we predict all players are *not* opening batsmen our accuracy would be 95% because just by predicting everything as our dominant class (not an opening batsman) we get 95% of labels correct. 95% sounds great but if we were hoping to identify new up and coming opening batsmen this would not work at all and our accuracy measure is giving the wrong impression. Here the class we actually care about getting right (even though its only 5% of all labels) are the opening batsman.

A confusion matrix allows us to dig deeper into our results and look at each target class to judge performance.

# What is a confusion matrix?

Lets look at a slightly smaller dataset below where only the target variable is shown in green for *opening_batsman* $=1$ and red for *opening_bastman* $=0$.

We've built a model that predicts the class for the below samples and this is given on the right. The colour of the predicted blocks shows the models predicted class and the outline of these predictions is either black when correct or the colour of the correct label when we misclassify.

To construct a confusion matrix we have predictions as our rows and actual labels as our columns. In each set of labels we can have values of positive (1) and negative (0). This gives us a 4x4 matrix as shown below.



|                   |           |           |           |                   |
|:-:                |:-:        |:-:        |:-:        |:-:                |
|                   |           | **Actual**           ||                   |
|                   |           |   **1**   |  **0**    | Total Predicted   |
|  **Predicted**    |  **1**    | <img src="../assets/img/tp.png" alt="drawing" style="width:50px;"/>       | <img src="../assets/img/fp.png" alt="drawing" style="width:50px;"/>         |  7                |
|                   |  **0**    | <img src="../assets/img/fn.png" alt="drawing" style="width:50px;"/>        | <img src="../assets/img/tn.png" alt="drawing" style="width:50px;"/>        | 11                |
|  Total Actual     |           | 6         | 12        | *18*              |


