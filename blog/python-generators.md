# Python Generators
## How, Why, and Where to use them

## Simple List
```
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

sample = [1,2,3,4,5]

print(square_numbers(sample)) # outputs [1, 4, 9, 16, 25]
```
Outputs:
```
1
4
9
16
25
```

## Now with a Generator

```
# Now using Generators
def square_generator(nums):
    for i in nums:
        yield (i*i)
        
g = square_generator(sample)
print(square_generator(sample)) # returns a generator object, which does NOT return all the results.
                                # It YIELDS one result at time. 
```

Initially the generator object is returned:

```
<generator object square_generator at 0x7f1ab815c308>
```

When we run the following commands, the LIST is iterated over using the YIELD statement:
```
print(next(g)) # Syntax for Python 3.x is different from Python 2.7.x
print(next(g))
print(next(g))
print("go: " next(g))
print(next(g)) # Prints 25, for the LAST value in the LIST.
```
Outputs:
```
<generator object square_generator at 0x7f1ab815c308>
1
4
9
16
25
```
Once the `list` of values is exhausted, we get a....

### `StopIteration` Stack Trace

```
StopIterationTraceback (most recent call last)
<ipython-input-20-93bdddec6e6f> in <module>()
     27 print(next(g))
     28 print(next(g)) # Prints 25, for the LAST value in the LIST.
---> 29 print(next(g)) # Since the LIST is exhausted, the generator throws a `StopIteration` error
     30 

StopIteration: 

```

## Rewrite the Generator as simple FOR loop
```
for num in g:
    print(num)
```

## List Comprehension     
```
print("Using List Comprehension:")

sample2 = [x*x for x in [2,3,5,7,9]]  # notice we wrap in [] to indicate List Comprehension
print(sample2)
```
Outputs:
```
Using List Comprehension:
[4, 9, 25, 49, 81]
```

## A Generator using shortcut annotation
```
print("Generator using shortcut annotation:")

sample3 = (x*x for x in [2,3,5,7,9]) # notice we use () to indicate it's a Generator
print(sample3) # print the generator object

for num in sample3:
    print(num)
```

## Print Generator as a list...
```
sample3 = (x*x for x in [2,3,5,7,9])
print (list(sample3)) # notice the `list` keyword
```
