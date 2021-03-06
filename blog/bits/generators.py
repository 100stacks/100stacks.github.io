# Python Generators - How, Why, and When to use them
# https://www.youtube.com/watch?v=bD05uGo_sVI

## Simple List
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

sample = [1,2,3,4,5]

#print(square_numbers(sample)) # outputs [1, 4, 9, 16, 25]

# Now using Generators
def square_generator(nums):
    for i in nums:
        yield (i*i)
        
g = square_generator(sample)
print(square_generator(sample)) # returns a generator object, which does to return all the results.
                                # It YIELDS one result at time.  At this point it no results are returned.

print(next(g)) # Syntax for Python 3.x is different from Python 2.7.x
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # Prints 25, for the LAST value in the LIST.
print(next(g)) # Since the LIST is exhausted, the generator throws a `StopIteration` error

# Below shows how we can iteratre through a generator object
for num in g:
    print(num)
    

## Another way to loop through Generator object
print("Another way to loop through Generator object:")
for num in g:
    print(num)
    
## List Comprehension     
print("Using List Comprehension:")

sample2 = [x*x for x in [2,3,5,7,9]]  
print(sample2)

## A Generator using shortcut annotation
print("Generator using shortcut annotation:")

sample3 = (x*x for x in [2,3,5,7,9])
print(sample3) # print the generator object

for num in sample3:
    print(num) # prints 4, 9, 25, 49, 81
 
 ## To print Generator as List
sample3 = (x*x for x in [2,3,5,7,9])
print(sample3) # print the generator object
print (list(sample3))
