---
layout: post
title: `pytest` and what it has to offer
date: 2014-08-12 10:18:00
---


# Why test?

Test driven development is a great way to make sure your code is put through its paces before being integrated into a larger code base.

It especially helps when you have a large complex code base where it may be difficult to generate specific scenarios to test each small submodule. 

Test driven development also helps you to think of basic smaller building blocks of functionality which can be built up to arrive at the overall functionality you want. This can guide your logic and the final product will be clean, less buggy code.

# Why test with `pytest`?

The `pytest` framework is a widely used testing framework great for small simple projects but which can also scale to be used in larger complex applications.

The features listed in `pytest`s documentation are

- Detailed info on failing assert statements (no need to remember self.assert* names)
- Auto-discovery of test modules and functions
- Modular fixtures for managing small or parametrized long-lived test resources
- Can run unittest (including trial) and nose test suites out of the box
- Python 3.8+ or PyPy 3
- Rich plugin architecture, with over 800+ external plugins and thriving community

Lets look a little deeper at a few of these.

### assert statements

`pytest` allows you to use standard Python `assert` statement for testing certain expectations are met.
When conditions are not met `pytest` provides details about what the left and right sides values of the assertion were that caused the test to fail which can speed up debugging.

### Auto-discovery of test modules/functions

`pytest` automatically finds all test .py files without the need to specify any paths (although this can be set too).

You can choose to either defined tests outside your application code (see fig 1.) or as part of your application code (see fig 2.).

`pytest` will automatically recurse into directories and search for `test_.*py` or `*_test.py`. It then collects all test items which can be `test` prefixed functions or methods outside of class, `test` prefixed functions or methods inside the `Test` prefixed test classes and methods decorated with `@staticmethod` or `@classmethods`


### Fixtures



# Installation

`pip install selenium`

# Key components



# Top features

