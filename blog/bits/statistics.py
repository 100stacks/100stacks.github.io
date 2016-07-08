# Statistics module 

import statistics

sample = [3,7,6,2,10,14,9,5,2,1,5,8,2,4]

print('''
The following shows a some of the available methods of the
built-in statistics module.

Our sample list:
''', sample)
q = statistics.mean(sample)
print('mean: ', q)

r = statistics.median(sample)
print('median:', r)

'''
Output:
The following shows a some of the available methods of the
built-in statistics module.

Our sample list:
 [3, 7, 6, 2, 10, 14, 9, 5, 2, 1, 5, 8, 2, 4]
mean:  5.571428571428571
median: 5.0
'''

