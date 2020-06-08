print(r'''
Tips for writing clean code:
1. Use meaningful names for variables and functions
Using meaningful, descriptive names for variables and functions can help you
explain most of your code without comments

Guidelines for coming up with meaningful names:
1. Be descriptive and imply type:
When coming up with names for functions and variables, be descriptive and where
possible try implying the type of whatever you are naming e.g
# descriptive and implying type
age_list = [25, 17, 56, 67]

# not descriptive
ages = [25, 17, 56, 67]

For booleans, it is often helpful to prefix the name with words like is or has 
to make it clear that it is a condition


''')

# code without use of meaningful names
s = [88, 92, 79, 93, 85]  # student test scores
print(sum(s) / len(s))  # print mean of test scores

s1 = [x**0.5 * 10 for x in s] # curve scores with square root method and store
# in new list
print(sum(s1) / len(s1)) # print mean of curved test scores

# better code version of the above with use of meaningful names

import math
from numpy import mean
test_scores = [88, 92, 79, 93, 85]
print(mean(test_scores))

curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
print(mean(curved_test_scores))