# File Operations - showing simple file operations in Python

test = 'this is a string\nthat is written to a file'

saveFile = open('test.txt', 'w') # w - (over)write to file, r - read from file, a - append to file

# if text.txt exists, it will delete all content and write our `test` string to it
saveFile.write(test)

# MAKE SURE TO ALWAYS CLOSE THE FILE
saveFile.close()

# Let's see if we can read in what we just saved....
readFile = open('test.txt', 'r').read()
print(readFile)

# Read contents into a Python List
readFile = open('test.txt', 'r').readlines()
print(readFile)

# Now let's APPEND to the file
test2 = 'Yet more content.\nChecking to see if we need an newline here.\n'

saveFile = open('test.txt', 'a') # append

saveFile.write(test2)
saveFile.close()

# Let's see if we can read in what we just APPENDED....
readFile = open('test.txt', 'r').read()
print(readFile)

# Read contents into a Python List
readFile = open('test.txt', 'r').readlines()
print(readFile)

'''
Output:
this is a string
that is written to a file
['this is a string\n', 'that is written to a file']
this is a string
that is written to a fileYet more content.
Checking to see if we need an newline here.

['this is a string\n', 'that is written to a fileYet more content.\n', 'Checking to see if we need an newline here.\n']

'''
