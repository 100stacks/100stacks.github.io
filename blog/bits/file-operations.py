# Simple example writing to a file

test = 'this is a string\nthat is written to a file`

saveFile = open('test.txt', 'w') # w - (over)write to file, r - read from file, a - append to file

# if text.txt exists, it will delete all content and write our `test` string to it
saveFile.write(test)

# MAKE SURE TO ALWAYS CLOSE THE FILE
saveFile.close()

# Append to a file
saveFile = open('test.txt', 'a') # append

saveFile.write(test)
saveFile.close()

# Read from a file
readFile = open('test.txt', 'r').read()
print(readFile)

# Read contents into a Python List
readFile = open('text.txt', 'r').readlines()
print(readFile)
