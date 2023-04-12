# Cloudkaptan Selenium Python Test Framework

Here is a brief about the framework and some detailed steps which you need to follow to set it up in your system. Kindly follow the document thoroughly.

The contents of the journey are:

- [Introduction](https://github.com/vivek-ck/ck-selenium-python/tree/main#introduction)

- [Framework Features](https://github.com/vivek-ck/ck-selenium-python/tree/main#framework-features)

- [Installation](https://github.com/vivek-ck/ck-selenium-python/tree/main#installation)

- [Test Case](https://github.com/vivek-ck/ck-selenium-python/tree/main#test-cases)

- [Contributing](https://github.com/vivek-ck/ck-selenium-python/tree/main#contributing)

- [Conclusion](https://github.com/vivek-ck/ck-selenium-python/tree/main#conclusion)




## Introduction

Welcome to our *Selenium Python Test Framework*! This repository contains a collection of test cases for web applications developed by [CloudKaptan Consultancy Services Pvt Ltd](https://cloudkaptan.com/). Our goal is to provide a reliable and comprehensive set of test cases that cover all aspects of our web applications.




## Framework Features

This framwork provides the following features:

1) [Seleniumbase](https://seleniumbase.io/): It is highly recommended to go through this documentation.

2) UI testing

3) API Testing




## Installation

To get started, you'll need to have [Python 3](https://www.python.org/downloads/) and [venv](https://docs.python.org/3/library/venv.html) installed.

Now follow along:

#### 1) Cloning the repository: [ck-selenium-python](https://github.com/vivek-ck/ck-selenium-python)

1) Open a terminal in your project folder.

2) Use the following command to clone the repository and go into it:

```terminal

git clone https://github.com/vivek-ck/ck-selenium-python

cd selenium-python-tests

```

#### 2) Creating a virtual environment for dependencies

1) Create a virtual environment:

```terminal

python -m venv

```

2) Activate the virtual environment:

```terminal

source venv/bin/activate

```

#### 3) Project setup and dependency download

All the requirements are present in the [setup.py](https://github.com/vivek-ck/ck-selenium-python/tree/main/setup.py)

Trigger the setup:

```terminal

pip install -e .

```




## Test Cases

Our tests are designed to be modular and reusable, making it easy to build out test suites for specific applications. We've included examples for common tasks like user authentication, data input and output, and navigating between pages.

In addition to the test cases, we've also included utility functions and helper classes to simplify test case creation and management.




#### Behave BDD Testing

We will use [behave](https://behave.readthedocs.io/en/stable/) for triggering our feature files.

```terminal

behave **salesforce/*.feature

```




## Contributing

As a private company, this repository is only accessible to authorised team members and collaborators. However, we welcome contributions from our team members and encourage developers to submit their own test cases and improvements.




To contribute to the repository, you'll need to:




1) Fork the repository

2) Create a new branch for your changes

3) Make your changes and commit them

4) Push your changes to your forked repository

5) Open a pull request from your branch to the main repository

6) We'll review your changes and merge them into the main repository if they meet our standards and requirements.




## Conclusion

Thank you for your interest in our Selenium Python test repository! We're committed to maintaining this repository and keeping it up-to-date with the latest best practices for Selenium testing. If you have any questions or feedback, please feel free to reach out to our team.
