# List manipulation

sample = [3,7,8,10,22,1,7,-4]

print("initial list:", sample)

# Now let's APPEND to the list
sample.append(23)
print("after append:", sample)

# INSERT at a specific location in the 0-based list
sample.insert(4, 99) # index `4` is 22
print("after insert:", sample)

'''
Output:
initial list: [3, 7, 8, 10, 22, 1, 7, -4]
after append: [3, 7, 8, 10, 22, 1, 7, -4, 23]
after insert: [3, 7, 8, 10, 99, 22, 1, 7, -4, 23]

'''

# REMOVE the first occurrence from list, will throw an ERROR if not found
sample.remove(6) # will generate an error

'''
Output:

ValueErrorTraceback (most recent call last)
<ipython-input-6-80a5dc861761> in <module>()
     14 
     15 # REMOVE the first occurrence from list, will throw an ERROR if not found
---> 16 sample.remove(6)

ValueError: list.remove(x): x not in list

'''
