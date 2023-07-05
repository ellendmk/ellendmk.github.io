---
layout: post
title: Practical advice for optimising SQL queries
date: 2023-06-24
comments: true
---


SQL optimisations can save oodles of time and they are really intuitive and easy to identify once you know what to look for.


# Practical advice for optimising SQL queries

- Case whens
 Make sure no aggregate operations happen within a case statement.

- Distinct & group by
if you're joins are correct there shouldn't be a need for a distinct


- Join conditions and where clauses


- 