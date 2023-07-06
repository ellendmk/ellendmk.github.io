---
layout: post
title: Is deep learning an RG flow?
date: 2020-07-01 20:29:00
comments: true
toc: true
---


This post is aimed at exploring some key ideas presented in the paper
<a href="https://arxiv.org/abs/1906.05212#:~:text=Deep%20learning%20performs%20a%20sophisticated,directly%20relevant%20to%20deep%20learning.">"Is Deep
Learning a Renormalization Group Flow?"</a> which I co-authored
with Prof. Robert de Mello Koch and Prof. Ling Cheng.

# Part 1 - A look into $ \langle vh \rangle $ correlators
# What is learning?
Humans are pretty good at learning new things. From the time that we
are babies we become sponges who soak up (not only lots of food and
parents energy but) all sorts of information, from learning to walk
to the way we speak. But how exactly does this learning take place?
The answer to this question is not well defined.
    
Deep learning algorithms are inspired by the connections between
neurons in our brains. These algorithms perform remarkably well
(often better than our human brains can) at a wide range of tasks.
But how and why do these networks learn so well? A number of people
have suggested that deep learning is performing a type of coarse
graining (averaging out the unimportant information to be left with
a subset of important information). The renormalization group in
physics defines a coarse graining scheme which may help in
understanding deep learning algorithms.
    
The paper mentioned above looks into this link and develops methods
to compare the renormalization group (RG) and restricted Boltzmann
machine (RBM) networks. For this study configurations of the 2D
Ising model are used as training data. The Ising model is a model of
a magnet consisting of discrete spins arranged on a square lattice.
Spins can take values of $ \pm 1 $. This data is well suited for
training RBMs because it consists of only two values. Another reason
why the Ising model is attractive to study stems from the fact that
neighboring spins are coupled. This is similar to an image where
nearby pixels will have similar values.

Before we jump into the comparison, let's review the transformations
we compare. In a discrete version of RG (variational RG) we average
blocks of 4 spins to arrive at a coarse grained output spin.
Locality is thus a key characteristic of this coarse graining
scheme. When we consider an RBM there is a chance that all input
nodes will contribute to a single output node. The weights determine
which inputs will influence a given output. These weights are
determined during training. It is thus not obvious whether the RBM
would be performing a coarse graining related to RG but is
definitely an interesting question to explore. Below very brief
summaries are given of each transformation. We will start by looking
at the RBM coarse graining.

# RBM coarse graining

An RBM produces a set of output vectors $ \{\bf h\} $ given a set of
input vectors $ \{\bf v\} $ using the following equation
$ h_a = \tanh(\sum_i W_{ia} v_i+b_a^{(h)}) $
where the parameters of the model determined by training are

<ul><li>\( b_a^{(h)} \) - the hidden bias and </li>
    <li>\( W_{ia} \) - the weight matrix.</li>
</ul>
The subscripts $i$ and $a$ refer to specific nodes of a given
input/output vector.
Using the trained weights we can get to a set of hidden vectors
(outputs) from the set of visible (input) training vectors.
<div style='text-align:center;'>
<img style="padding-top: 2em; padding-bottom: 2em; width: 650px;
    max-width:100%; margin: 0 auto;left: 50%; top: 50%;"
    src="{{site.baseurl}}/assets/img/dl_as_rg/rbm.png"  alt="image">
</div>

As mentioned earlier we train the networks on 2D Ising model
configurations. Each configuration is a set of values of $\pm 1$
arranged in a square.
We transform the configurations from matrices of size $ L_v \times L_v $ into vectors of length $ L_v\times L_v$ by concatenating the
rows as shown in the below image.
<div style='text-align:center;'>
<img style="padding-top: 2em; padding-bottom: 2em; width: 650px;
    max-width:100%; margin: 0 auto;"
    src="{{site.baseurl}}/assets/img/dl_as_rg/smaller_finite_concat.webp"  alt="image">
    </div>

# Variational RG coarse graining
    
In variational RG one performs a local average of neighboring spins. RG
acts on the original matrix of $ \pm 1 $ values, rather than a vector,
as is the case for the RBM. We can represent the RG average as follows $s\'_{k,j}$

$ = \frac{1}{4}s_{k,j}+s_{k+1,j}$

$ + s_{k,j+1} + s_{k+1,j+1})$ where $s_{i,j}$ denotes a spin in the input lattice ($v_i$ above)
and $s'_{i,j}$ denotes a coarse grained spin present in the output
lattice ($h_a$ above).
This averaging is performed on blocks of 4 spins at a time and these
blocks do not overlap. Thus each block of 4 spins translates into a
single output spin and we have a quarter of the number of input spins in
the output. (The RBMs are constructed so they too reduce the input to
one quarter of the number of input nodes.)

<div style='text-align:center;'>
    <img style="padding-top: 2em; padding-bottom: 2em; width:
        450px;max-width:100%;" src="{{site.baseurl}}/assets/img/dl_as_rg/rg.png"  alt="image">
</div>

# Comparing RG and RBMs

We can see from the equations above that it is not obvious whether these
two transformations are acting in the same way. We can see that both
take a linear combination of the inputs to produce an output.

The input/output configurations are arranged in a grid of size
$ L_v\times L_v $/ $ L_h\times L_h$ (where here for ease of explanation
$ L_v=4$ and $L_h=2 $ ) spins. From the diagrams above you should have
noticed that RG acts on these configurations in their original matrix
form, but the RBM accepts them as a vector.

To probe the transformations we introduce a correlation function between
the inputs and outputs (where the inputs and outputs are arranged in the
grid form rather than as vectors). We want to determine which input
nodes hidden node 1 has learnt are important, which we can phrase as:
which input nodes are correlated to this output node?
To calculate the correlation between a given input node and output node
we use the following
$\langle v_ih_a \rangle = \frac{1}{N_s} \sum_{k=1}^{N_s}
v_i^{(k)}h_a^{(k)}$

The correlations are calculated by summing over all pairs of inputs and
outputs. We label the inputs (v) and outputs (h) using the convention
below:

<div style='text-align:center;'>
<img style="padding-top: 2em; padding-bottom: 2em; width:
    200px; max-width:100%; margin: 0 auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/vlabels.png"  alt="image">
<img style="padding-top: 2em; padding-bottom: 2em; width: 200px;
    max-width:100%; margin: 0 auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/hlabels.png" alt="image">
</div>

For the inputs and outputs depicted here we have input matrices which
consists of 16 values and output matrices which consist of 4 values.
Lets break down the $\langle vh \rangle$ sum using some made up
input/output pairs.

Lets assume we have the following inputs
<div style='text-align:center;'>

<img style="padding-top: 2em; padding-bottom: 2em; width:
200px;max-width:100%; margin: auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/in1.png"  alt="image">
<img style="padding-top: 2em; padding-bottom: 2em; width:
200px;max-width:100%; margin: auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/in2.png"  alt="image">
</div>

which are fed through a transformation and produce the following outputs
(pairs given by the color coding)
<div style='text-align:center;'>

<img style="padding-top: 2em; padding-bottom: 2em; width: 150px;
max-width:100%;margin: auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/out1.png"  alt="image">
<img style="padding-top: 2em; padding-bottom: 2em; width: 150px;
max-width:100%;margin: auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/out2.png"  alt="image">
</div>

We calculate the correlator $\langle v_1h_1 \rangle$ by taking the
product of nodes $v_1$ and $h_1$ for each pair of inputs and outputs. These
products are averaged so we sum the products and divide by the number of
input/output pairs (which here is equal to 2 and so we only sum two
terms per $\langle v_ih_a \rangle$) i.e.
<div style='text-align:center; padding-top:2em; padding-bottom:2em;'>
<p>
\(\langle v_1h_1 \rangle = \frac{1}{2}(\)<mark style=
    'background-color: #d0f8d0;'>\(v_1 h_1\)</mark> \(+\) <mark
    style='background-color:#e2d0f8;'>\(v_1h_1\)</mark>\( )=
\frac{1}{2}(\)<mark style= 'background-color: #d0f8d0;'>\(1
    \times 1\)</mark> \(+\) <mark
    style='background-color:#e2d0f8;'>\(1 \times 1\)</mark>\(
)=1\)
</p>
</div>

For one more example lets look at $\langle v_{16} h_4 \rangle$ (The
bottom left most visible and hidden nodes)

<div style='text-align:center;padding-top:2em; padding-bottom:2em;'>
\(\langle v_{16}h_{4} \rangle = \frac{1}{2}(\)<mark style=
    'background-color: #d0f8d0;'>\(v_{16} h_4\)</mark> \(+\)
<mark style='background-color:#e2d0f8;'>\(v_{16}h_{4}\)</mark>\(
)= \frac{1}{2}(\)<mark style= 'background-color: #d0f8d0;'>\(1
    \times -1\)</mark> \(+\) <mark
    style='background-color:#e2d0f8;'>\(-1 \times -1\)</mark>\(
)=0\)
</div>


For each output node we obtain a grid of values which is the same size
as the input. Here we see an image of what would be the $\langle
v_i h_1 \rangle$ correlators. For the inputs/outputs shown above we would
get 4 matrices of values (because we have 4 hidden nodes) just like the
one shown below.

<div style='text-align:center;'>
<img style="padding-top: 2em; padding-bottom: 2em; width:
350px;max-width:100%; margin: auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/vhlabeled.png"  alt="image">

<img style="padding-top: 2em; padding-bottom: 2em; width: 200px;max-width:100%; margin: auto;" src="{{site.baseurl}}/assets/img/dl_as_rg/vh_set.png"  alt="image">
</div>
<br/>

Great! So now we can encode the patterns of thousands of input and output
pairs into a neat statistical measure of $\langle vh \rangle$. Each
hidden node now has a matrix of $\langle vh \rangle$ values associated
with it. These values tell us important information about which input
nodes each hidden node is correlated to. But we may still have hundreds
of these matrices to understand depending on the number of hidden nodes
in the transformation.

Below are examples of the $\langle vh \rangle$ patterns we observe in
each coarse graining scheme. The dark patches show a patch where the
given hidden node is highly correlated to input nodes. We need a way to
quantify similarities between the schemes. To do this we use spatial
correlators.


<img style='max-width:48%;' src="{{site.baseurl}}/assets/img/dl_as_rg/1024_256_flows_tanh_freq_grid.png">
<img style="max-width: 48%;" src="{{site.baseurl}}/assets/img/dl_as_rg/1024_256_rg_freq_grid.png">
