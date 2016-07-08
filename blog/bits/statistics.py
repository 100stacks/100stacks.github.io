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
