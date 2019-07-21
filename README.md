# game-of-greed
**Author**: Raven W. Robertson
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
I'll be creating a dice game to play in my command line. For class01 I'll be implementing the following features:
Application should simulate rolling between 1 and 6 dice, allow user to set aside dice each roll, should ask user to enter score per roll, allow “banking” current score or rolling again.
Application should keep track of total score and it should keep track of current round.

## Getting Started
I'll be writing this code in python in a pipenv. 

## Architecture
I built this application using python3 and with import sys

## API
I'm not using an API for this application. 

## Change Log
10:00pm - features all working but a little buggy. Can't get dict to hold onto infor for longer that one roll of dice? Check with JB ot James tomorrow  7/8/19
11:44pm - worked out most bugs. Trying to build a tally score function to over write user input for score. I built a test for the function. I'm able to get the user input into the function and stored in a dictionary, but the actual tally isn't working and I just need to sleep. 7/9/19
11:55pm - able to get scoring function to pass all tests. Also have a function built to bring in alternate score from a text file. Still working out bugs, really need to refactor. Still need to add classes. 7/11/19
1240am - build up a class for default and alternate rules. I tried to replace scores directly in my function with attributes from the class object, but I received the error, "'Rules' object is not subscriptable". I was, however able to replace the values in my dictionary to a reference of the class and it is still functioning. 
3:00pm 7/19/2019: passing all tests, - 
[x] Application should encapsulate the rule set in a custom class that is used within game to assign points.
- [x] passing all tests
- [x] handling errors
- [x] Application should should allow for custom rule set
- [x]particular custom rules should override corresponding default
- [x] Application should print out games score to scores.txt file
- [x]Application should simulate rolling between 1 and 6 dice
- [x]Application should allow user to set aside dice each roll
- [x]Application should allow “banking” current score or rolling again