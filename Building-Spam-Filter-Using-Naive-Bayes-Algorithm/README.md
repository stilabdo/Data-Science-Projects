# Building a Spam Filter with Naive Bayes
This project is a part of my data science portfolio of projects.

#### -- Project Status: Completed

## Introduction

This dataset consist of 5,572 SMS messages that are already classified by humans. The dataset was put together by Tiago A. Almeida and José María Gómez Hidalgo, and it can be downloaded from the [The UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection). The data collection process is described in more details on [this page](http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/#composition), where you can also find some of the papers authored by Tiago A. Almeida and José María Gómez Hidalgo.

### Technologies
#### Python in jupyter notebook
##### Libiries

* Pandas 
* Regex

### Project Objective
Our objective is to write a program that detects and classifies new messages with an accuracy greater than 80%.


### Project Description

In this project we cleaned the data then we split the data into `training set` and `test set` and later constructed a multinomial Naive Bayes Algorithm from scratch and used the `training set` to train the model then classified the messages included in the `test set` using the algorithm we constructed to with 98.74% accuracy.
 
#### Attributes:

* Label &nbsp; : &nbsp; ham (non-spam) or spam.
* SMS &nbsp; : &nbsp; The message we would like to classify.
