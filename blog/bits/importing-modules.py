# Importing Python Modules - shows different ways for importing

import statistics as stats
from statistics import variance as vr, median as med
from statistics import * # import everything using the regex `*` 

sample = [3,7,6,2,10,14,9,5,2,1,5,8,2,4]

print('''
The following shows a some of the available methods of the
built-in statistics module.
Our sample list:
''', sample)
q = stats.mean(sample)
print('mean: ', q)

r = med(sample)
print('median:', r)

s = statistics.mode(sample)
print('mode:', s)

t = statistics.stdev(sample)
print('standard deviation:', t)

u = vr(sample)
print('variance:', u)

'''
Output:
The following shows a some of the available methods of the
built-in statistics module.
Our sample list:
 [3, 7, 6, 2, 10, 14, 9, 5, 2, 1, 5, 8, 2, 4]
mean:  5.571428571428571
median: 5.0
mode: 2
standard deviation: 3.7151309266562604
variance: 13.802197802197803
'''
