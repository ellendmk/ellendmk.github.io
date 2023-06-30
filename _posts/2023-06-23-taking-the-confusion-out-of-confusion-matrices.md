---
layout: post
title: Taking the confusion out of confusion matrices
date: 2023-06-23 14:29:00
---

Confusion matrices can at times be confusing and so can all the metrics that go along with them. Here we'll try to break down intuitively what their purpose is and what each of the metrics mean.


# What is a confusion matrix?


Confusion matrices are a useful way to summarise model perfromance when dealing with binary classification tasks.

You might be thinking we have a simple way to evaluate model performance already - lets see how accurate our predictions are? What proportion of our predictions match the actual labels?

Lets look at an example to see why accuracy is not a great metric.

Say we have a list of 100 cricket players from UK cricket clubs and our target variable is whether the player is an opening batsman or not. Our target is 5% of our data (meaning 5 of the cricket players in our list are opening bastmen).

If we predict all players are ~not~ opening batsmen our accuracy would be 95% because just by predicting everything as our dominant class (not an opening batsman) we get 95% of labels correct. 

If we were hoping to identify new up and coming opening batsmen this would not work at all and the 95% accuracy is giving us the wrong impression because the class we actually care about getting right (even though its only 5% of all labels) are the opening batsman.

