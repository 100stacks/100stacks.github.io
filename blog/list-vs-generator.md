# List vs Generator

* This article shows the difference between `list` and `generator` execution times.
* Of note, the entire `list` object is loaded into memory.
* The `generator` object is lazy (as used) loaded into memory.

## Code Snippet
```py
import sys
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

#print("Memory (Before) for names list: {} bytes".format(sys.getsizeof(names)))
#print("Memory (Before) for majors list: {} bytes".format(sys.getsizeof(majors)))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
    yield person
    
# Using a List        
t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

print('Memory (After) adding 1M list objects to an empty List: {} bytes'.format(sys.getsizeof(people)))
print('Took {} seconds'.format(t2-t1))

# Using a Generator (Reusing `people` list object)
t3 = time.clock()
people = people_generator(1000000)
t4 = time.clock()

print('\nMemory (After) adding 1M list objects to re-typed List object as Generator: {} bytes'.format(sys.getsizeof(people)))
print('Took {} seconds'.format(t4-t3))

# Using a Generator (using a new generator object)
t5 = time.clock()
people1 = people_generator(1000000)
t6 = time.clock()

print('\nMemory (After) adding 1M list objects to a NEW Generator: {} bytes'.format(sys.getsizeof(people1)))
print('Took {} seconds'.format(t6-t5))
```

## Output
```
Memory (After) adding 1M list objects to an empty List: 8697464 bytes
Took 2.540992000000003 seconds

Memory (After) adding 1M list objects to re-typed List object as Generator: 88 bytes
Took 0.11375400000000013 seconds

Memory (After) adding 1M list objects to a NEW Generator: 88 bytes
Took 6.600000000389628e-05 seconds = that's 0.04447 seconds!
```

#### Notice the `generator` object took 0.04447 seconds vs 2.54 seconds for the `list` object.
