---
layout: post
title: Fine tuning LLMs
date: 2023-07-27
comments: true
toc: true
---

With the open source release of 🤗 Llama getting your hands dirty with LLMs has become easier. But most of us don't have access to large amounts of costly compute so understanding efficient methods to fine tune LLMs and what their trade-offs are is important. In this post we'll explore commonly used methods, how they work, where the efficiencies come from and what the downsides are.


# Parameter-Efficient Fine-Tuning (PEFT) methods

There are a class of methods grouped together under the banner of PEFT. They include

- LoRA (Low-Rank Adaptation)
- Prefix Tuning
- P-Tuning
- Prompt Tuning
- AdaLoRA
- $(IA)^3$ (few-shot PEFT)


Here we'll summarize key aspects of each method and the pros and cons of each. These are available to use from hugging face 🤗 with the `peft` python library.

## LoRA (Low-Rank Adaptation)

LoRA trains smaller low rank matrices they obtain by rank decomposition of a few pre-trained dense layers. This makes LoRA storage and compute efficient allowing for various low rank matrices to be trained depending on the task at hand. Switching between tasks also becomes easier with these low rank fine tunings.

## Prefix Tuning


## P-Tuning


## Prompt Tuning


## AdaLoRA


## $(IA)^3$ (few-shot PEFT)