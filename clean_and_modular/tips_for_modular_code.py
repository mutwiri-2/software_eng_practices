print(r'''
Modularization splits your code into logical functions and modules. This allows
you to reuse parts of your code

A few guidelines for Modularization:
1. DRY (Don't Repeat Yourself!) - Generalize and consolidate repeated code in
loops or functions
2. Abstract out logic to improve readability - Abstracting out code into a
function not only makes it less repetitive but also improves the readability
with descriptive function names. Although your code can become more readable 
when you abstract out logic into functions, it is possible to over-engineer this
and have way too many modules, so use your judgement.

3. Minimize the number of entities (functions. classes, modules) - Creating more
modules does not neccessarily result in effective modularization

4. Make sure each function you create is focused on doing one thing - Avoid
having unneccessary side-effects in functions and keep them focused. When 
functions are doing multiple things, they become more difficult to generalize
and reuse
NB: If there is an and in your function, consider refactoring

# example of functions with unneccessary side effect
def flat_curve_and_print_mean(arr, n):
    curved = [i + n for i in arr]
    print(np.mean(curved))
    return curved

def square_root_curve_and_print_mean(arr):
    curved = [math.sqrt(i) * 10 for i in arr]
    print(np.mean(curved))
    return curved

5. Arbitrary variable names can be more effective in certain functions - In
general functions, arbitrary variable names can make the code more clean

6. 

Code to show the above guidelines in practice
# spaghetti code
s = [88, 92, 79, 93, 85]
print(sum(s)/len(s))

s1 = []
for x in s:
    s1.append(x + 5)
print(sum(s1)/len(s1))

s2 = []
for x in s:
    s2.append(x + 10)
print(sum(s2)/len(s2))

s3 = []
for x in s:
    s3.append(x**0.5 * 10)
print(sum(s3)/len(s3))

# clean code - better naming and readable functions
import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_5 = [score + 5 for score in test_scores]
print(np.mean(curved_5))

curved_10 = [score + 10 for score in test_scores]
print(np.mean(curved_10))

curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_sqrt))

# Modularization - abstract out logic to remove repetition
import math
from numpy import mean

def flat_curve(arr, n):
    return [i + n for i in arr]

def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]

test_scores = [88, 92, 79, 93, 85]
print(mean(test_scores))

curved_5 = flat_curve(test_scores, 5)
print(mean(curved_5))

curved_10 = flat_curve(test_scores, 10)
print(mean(curved_10))

curved_sqrt = square_root_curve(test_scores)
print(mean(curved_sqrt))
''')

# spaghetti code
s = [88, 92, 79, 93, 85]
print(sum(s)/len(s))

s1 = []
for x in s:
    s1.append(x + 5)
print(sum(s1)/len(s1))

s2 = []
for x in s:
    s2.append(x + 10)
print(sum(s2)/len(s2))

s3 = []
for x in s:
    s3.append(x**0.5 * 10)
print(sum(s3)/len(s3))

# clean code - better naming and readable functions
import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_5 = [score + 5 for score in test_scores]
print(np.mean(curved_5))

curved_10 = [score + 10 for score in test_scores]
print(np.mean(curved_10))

curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_sqrt))

# Modularization - abstract out logic to remove repetition
import math
from numpy import mean

def flat_curve(arr, n):
    return [i + n for i in arr]

def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]

test_scores = [88, 92, 79, 93, 85]
print(mean(test_scores))

curved_5 = flat_curve(test_scores, 5)
print(mean(curved_5))

curved_10 = flat_curve(test_scores, 10)
print(mean(curved_10))

curved_sqrt = square_root_curve(test_scores)
print(mean(curved_sqrt))