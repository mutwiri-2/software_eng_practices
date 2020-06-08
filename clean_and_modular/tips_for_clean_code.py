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

You can also use parts of speech to imply types by using verbs for functions and
nouns for variables

Avoid abbreviations and especially single letters unless the word will be used 
many many times. Exceptions for this rule include names for counters (i), and 
common math variables like x, s, t etc. Choosing when to make this exceptions 
depends on the audience  for your code. Some variables may be common knowledge 
to certain professionals but not others

Long names != descriptive names: long names do not always mean descriptive names
You should be descriptive, yes! But not with more characters than neccessary e.g
# bad
def count_unique_values_of_names_list_with_set(names_list):
    return len(set(names_list))

# better version
def count_unique_values(arr):
    return len(set(arr))

Good function names describe what they do well without including details about 
implementation or highly specific uses

TIP 2 : USE WHITESPACES PROPERLY:
clean code has good and consistent spacing -
PEP-8 guide - https://www.python.org/dev/peps/pep-0008/?#code-lay-out
a) Organize your code with consistent indentation - standard is 4 spaces for each
indent. Make this default in your text editor
b) Separate sections with blank lines to keep your code well organized and
readable
c) Try to limit your lines of code to 79 characters.
https://stackoverflow.com/questions/29968499/vertical-rulers-in-visual-studio-code


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