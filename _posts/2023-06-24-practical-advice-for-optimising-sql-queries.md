---
layout: post
title: Practical advice for optimising SQL queries
date: 2023-06-24
comments: true
toc: true
---


SQL optimizations can save oodles of time and they are really intuitive and easy to identify once you know what to look for.



Optimizing SQL queries comes down to two simple principles

1. Use as little data as necessary
2. Limit how many times you need to perform any operation


I'll break down these tips into subsections so they'll be easy to skim through.

## Use as little data as necessary

Restrict the tables to the filtered data you are interested in earlier rather than later. Less joins and less operations on rows we don't need will give better performance.

## Avoid computation within joins

Rather create a new column in relevant tables before joining than performing computations in the join condition. Each time a record is checked against another there will be additional unnecessary computations. By including a column in the tables being joined you limit this to one computation per entry.

## Include conditions in joins rather than in where conditions

Join conditions are executed before where conditions. Applying filters within a where will result in all records first being joined before the filtering happens. By including lal filters in the where you limit the number of joins that need to occur.

## Avoid distinct and group by

Always ensure you are performing the correct join on only the necessary rows rather than using a distinct or group by. Only use these operations when aggregating or when completely necessary.

## Avoid computations and aggregations within a case when

Including computations/aggregations within a case when condition may result in the computation/aggregation being computed multiple times. For example if we have
~~~~sql
    ...
    CASE WHEN SUM(TOTAL) < 100 then SUM(TOTAL) 
        ELSE 100 
    END AS TOTAL_SUM
~~~~

the condition requires the aggregation of _TOTAL_ and if the condition is true we need to perform the aggregation a second time.

Including this as a column in an intermediate step would be better where we could then just rely on the column values rather than an aggregation within the condition checks.

~~~~sql
    ...
    CASE WHEN TOTAL_SUM < 100 then TOTAL_SUM 
        ELSE 100 
    END AS TOTAL_SUM
    FROM (
        SELECT SUM(TOTAL) as TOTAL_SUM, --aggregate before using within a condition
            ...
    )
    ...
~~~~

## Where to practice what you've learnt?
