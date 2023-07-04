---
layout: post
title: Taking the confusion out of confusion matrices
date: 2023-06-23 14:29:00
---

Confusion matrices can at times be confusing and so can all the metrics that go along with them. Here we'll try to break down intuitively what their purpose is and what each of the metrics mean.


# What is a confusion matrix?


Confusion matrices are a useful way to summarise model perfromance when dealing with classification tasks. Here we consider the binary classifcation task as an example but we can use confusion matrices when there are more than two classes.

You might be thinking we have a simple way to evaluate model performance already - lets see how accurate our predictions are? What proportion of our predictions match the actual labels?

Lets look at an example to see why accuracy is not a great metric.

Say we have a list of dataset made up of 100 cricket players from UK cricket clubs. Our target variable is a boolean value *opening_batsman*  which indicates if a player is an opener (1) or isn't (0). Our target is only 5% of our data (meaning 5 of the cricket players in our list are opening bastmen).

If we predict all players are ~not~ opening batsmen our accuracy would be 95% because just by predicting everything as our dominant class (not an opening batsman) we get 95% of labels correct.

If we were hoping to identify new up and coming opening batsmen this would not work at all and the 95% accuracy is giving us the wrong impression because the class we actually care about getting right (even though its only 5% of all labels) are the opening batsman.

A confusion matrix alows us to dig deeper into our results and look at both target categories to judge its performance.

Lets look at a slightly smaller dataset below where only the target variable is shown in green for opening_batsman=1 and red for opening_bastman=0.

We've built a model that predicts the class for the below samples and this is given on the right. We can see the outline of these predictions is either black when correct otherwise or the colour of the correct label when we misclassify.

To construct a confusion matrix we have predictions as our rows and actual labels as our columns.



|    |  |**actual**|      |
|----|----|-----|-----|
| ||1|0|-----|
|  **predicted**  |  1  |   |   |
|    |  0 |   |   |
