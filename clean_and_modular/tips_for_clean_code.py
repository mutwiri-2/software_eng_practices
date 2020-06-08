print(r'''
Tips for writing clean code:
1. Use meaningful names for variables and functions
Using meaningful, descriptive names for variables and functions can help you
explain most of your code without comments

''')

# code without use of meaningful names
s = [88, 92, 79, 93, 85]  # student test scores
print(sum(s) / len(s))  # print mean of test scores

s1 = [x**0.5 * 10 for x in s] # curve scores with square root method and store
# in new list
print(sum(s1) / len(s1)) # print mean of curved test scores

# better code version of the above with use of meaningful names

import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_scores))