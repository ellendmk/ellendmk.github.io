---
layout: post
comments: true
toc: true
title: Taking the confusion out of confusion matrices
date: 2023-07-03 20:29:00
---

Confusion matrices can at times be confusing and so can all the metrics that go along with them. Here we'll try to break down intuitively what their purpose is and what each of the metrics mean.


# Why do we need confusion matrices?

Confusion matrices are a useful way to summarize model performance when dealing with classification tasks. Not only do they apply to the binary classification task but can also be used when dealing with more than two classes.

You might be thinking *we have a simple way to evaluate model performance already - lets see how accurate our predictions are? What proportion of our predicted labels match the actual labels?* Lets look at an example to understand why accuracy is not always a great metric.

We have a dataset made up of 100 cricket players from UK cricket clubs. Our target variable is a boolean value *opening_batsman*  which indicates if a player is an opener (1) or isn't (0). Our target is only 5 % of our data (meaning 5 of the 100 players in our data are opening batsmen).

If we predict all players are *not* opening batsmen our accuracy would be 95% because just by predicting everything as our dominant class (not an opening batsman) we get 95 % of labels correct. 95 % sounds great but if we were hoping to identify new up and coming opening batsmen this would not work at all and our accuracy measure is giving the wrong impression. Here the class we actually care about getting right (even though its only 5 % of all labels) are when players are an opening batsman.

A confusion matrix allows us to dig deeper into our results and look at each target class to judge performance.

# What is a confusion matrix?

Lets look at a slightly smaller dataset below where only the target variable is shown. Each block represents a labeled sample with orange for *opening_batsman* \\(=1\\) and blue for *opening_batsman* \\(=0\\). This is shown by the first row of blocks below.

We've built a model that predicts the class for the below samples and this is given in the second row of blocks. Correct classifications have a white tick and misclassifications a black cross.

<div style="text-align: center;">
<img src="{{site.baseurl}}/assets/img/samples.png" alt="drawing" style="height: 100px; object-fit: scale-down;padding-bottom:-40px;padding-left:10px;"/>


<img src="{{site.baseurl}}/assets/img/predictions.png" alt="drawing" style="height:100px;object-fit: scale-down;padding-top:-100px;"/>
     <div class="caption" style='text-align:justify;'><b>Figure 1:</b> Top: actual labels (orange meaning opening_batsman = 1 and blue meaning opening_batsman = 0). Bottom: predicted labels (ticks in white show correct classifications and black crosses show misclassifications.).</div>
</div>

## Constructing the matrix

To construct a confusion matrix we have a matrix with predictions as our rows and actual labels as our columns. In each case labels can take values of positive (1 = opening batsman) and negative (0 = not an opening batsman). Each sample will have an actual label and a predicted label and by summing up how many lie in each block we get a 4x4 matrix as shown below. 



<table style = 'max-width:900px; text-align:center;'>
<tr>
     <td style="border-bottom-style: hidden;border-top-style: hidden;border-left-style: hidden;"></td>
     <td style="border-bottom-style: hidden;border-top-style: hidden;border-left-style: hidden;"></td>
     <td colspan="2"> Actual  </td>
     <td style="border-top-style: hidden;border-right-style: hidden;"></td>
</tr>
<tr>
     <td style="border-top-style: hidden;border-left-style: hidden;"></td>
     <td style="border-top-style: hidden;border-left-style: hidden;">  </td>
     <td> 1 </td>
     <td>0</td>
     <td> Predicted totals</td>

</tr>

<tr>
     <td rowspan='2' style='center'>Predicted</td>
     <td >1</td>
     <td > 3 <br />  <img src="{{site.baseurl}}/assets/img/tp.png" alt="drawing" style="width:50px;border:0"
     /> <br />  True positives <br/>(TP) </td>
     <td> 4 <br /> <img src="{{site.baseurl}}/assets/img/fp.png" alt="drawing" style="width:50px;border:0"/> <br /> False positives (FP)  </td>
     <td> 7</td>
</tr>
<tr>
     <td >0</td>
     <td > 3<br /><img src="{{site.baseurl}}/assets/img/fn.png" alt="" style="width:50px;border:0;"/> <br /> False negatives (FN) </td>
     <td> 8<br /><img src="{{site.baseurl}}/assets/img/tn.png" alt="" style="width:50px;border:0;"/> <br /> True negatives (TN) </td>
     <td> 11</td>
</tr>
<tr>
<td style="border-bottom-style: hidden;border-left-style: hidden;"></td>
     <td >Actual Totals</td>
     <td> 6 </td>
     <td> 12 </td>
     <td >18</td>

</tr>
</table>

The terminology we use to label each block of the confusion matrix is either true or false (is our prediction correct i.e. true or incorrect i.e. false) followed by what our prediction was (positive i.e. 1 or negative i.e. 0). 

## Accuracy from the diagonal

The diagonal of a confusion matrix tells us about the correct classifications our model made. Summing these and dividing by the total number of samples will give us the accuracy measure we discussed above. For this dataset we have \\(3+8=11\\) out of 18 predictions that are correct giving us an accuracy of \\(11/18 = 57.9\%\\).  

But we already mentioned that we care more about the performance of our model for predicting a label of 1.


## How good are we at predicting *opening_batsman* \\(= 1\\)?

There are a few intuitive measures to consider when quantifying how well our model performs when looking at a specific class

1. How good are we at finding actual opening batsmen?
2. How often are our predictions correct of who an opening batsmen?
3. A measure that combines the above two metrics: the ability to find real labels as well as have a high hit rate amongst predictions.


#### 1. Recall: How good are we at finding actual opening batsmen?
For the first point we could think of this as trying to see how many actual opening_batsman = 1 labels we managed to catch. This we can get with the ratio between the number of correct predictions for opening_batsman = 1  (TP) and all the actual opening_batsman = 1 labels (TP+FN). This measure is called recall and gives ua an idea of well we can recall the ground truth of our underlying data. Recall has the below formula

$$R=\frac{TP}{TP+FN}$$

In this case we get a recall value of 

$$R = \frac{3}{3+3}=0.5$$

#### 2. Precision: How often are our predictions correct of who an opening batsmen is?

For the second point we are trying to understand how often our positive predictions are actually correct. For this we again need our correct opening_batsman = 1 (TP) as the numerator but for our denominator we now need all predictions where opening_batsman = 1 regardless of whether they were correct or not (TP+FP). This measure tells us how precise we are at predicting and is called precision. The formula is given by

$$P = \frac{TP}{TP+FP}$$

In this case we get a precision of

$$P = \frac{3}{3+4}=0.429$$

#### 3. Combining precision and recall into a single metric with the harmonic mean

If we have two models and we're trying to determine which one is better at predicting opening batsman but one has a better precision an the other a better recall it may get tricky trying to decide which one to use. What we need now is a sensible way of combining these two metrics into a single measure.

A measure exists that combines precision and recall by taking the harmonic mean. This is called the F1-score. So this sounds like some sort of fancy average of the two metrics.

To find the harmonic mean we must find the reciprocal of the arithmetic mean of reciprocals which is given by

$$\frac{1}{H} = \frac{\frac{1}{P}+\frac{1}{R}}{2}$$

$$H = \frac{2PR}{P+R}$$

We know values of precision and recall will fall between 0 and 1 and we can plot what the harmonic mean of these values would be 

<img src="{{site.baseurl}}/assets/img/f1-score.png" alt="drawing" style="width:500px;"/>


The harmonic mean gives us a way of balancing the effects of each individual metric without being penalized for one being very low. It gives us a nonlinear combination which better captures the trade-off between the two metrics and allows us to easily compare two models.