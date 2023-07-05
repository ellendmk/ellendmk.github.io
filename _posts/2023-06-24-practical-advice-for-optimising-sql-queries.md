---
layout: post
title: Practical advice for optimising SQL queries
date: 2023-06-24
comments: true
---


SQL optimizations can save oodles of time and they are really intuitive and easy to identify once you know what to look for.


# Practical advice for optimizing SQL queries

Optimizing SQL queries comes down to two simple principles

1. Use as little data as necessary
2. Limit how many times you need to perform any operation


I'll break down these tips into subsections so they'll be easy to skim through.

## Use as little data as necessary

Earlier in your query rather than later you should restrict the tables to the filters you are interested in be it dates, a subset of humans or particular records.

For example if we had the below query

~~~~sql
with CTE as (
select col1,
    col2,
    col3,
    date1,
    date2
from table1
)

...

select cola,
    colb,
    col1,
    col2, 
    col3,
    date1,
    date2
from CTE3
where GETDATE() between date1 and date2
~~~~

it would be better to apply the filter to the first CTE as it might be used as a base for other CTEs and we'll be loading and performing operations on more data than necessary.

~~~~sql
with CTE as (
select col1,
    col2,
    col3,
    date1,
    date2
from table1
where GETDATE() between date1 and date2

)

...

select cola,
    colb,
    col1,
    col2, 
    col3,
    date1,
    date2
from CTE3
~~~~


## Avoid computation within joins

## Include conditions in joins rather than in where conditions

## Avoid distinct and group by

## Avoid computations within a case when

## Where to practice what you've learnt?

