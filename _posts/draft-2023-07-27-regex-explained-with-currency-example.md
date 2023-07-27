---
layout: post
title: Regex explained with currency example
date: 2023-07-27
---

Regular expressions are a great way to define and check for complex patterns within strings. But often they can look cryptic and are tricky to write. In this post we'll look at an example related to currency to try break down some important principles that you can reuse for other regex tasks.


# Identifying a currency string

We're interested in identifying valid currency strings. For this example we define a valid string as follows

- Must start with the currency which is one of USD, GBP or ZAR
- A space must follow the currency
- The monetary value should follow this 
  - with comma separation 
  - if any decimal points occur exactly two numbers should follow with the first non-zero 
  - no leading zeroes on the left of the decimal point


The below examples should make the above constraints clear

```
USD 27.32 # valid string
USD 27 # valid string
USD 109,627 # valid string
USD 72,109,627 # valid string
ZAR 100,027.32 # valid string
AUD 100,027.32 # not valid string - AUD not accepted
GBP 03.32 # not valid string - leading zero
GBP 1227.32 # not valid string no comma separator for 1000
aZAR 50 # not valid string doesn't start with correct currency
USD 27.02 # not valid string - leading 0 after decimal
```