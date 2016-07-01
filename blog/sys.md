# Python `sys` Library

Used to access system functions.

Here's the code snippet we will breakdown.
```
import sys

sys.stderr.write('this is stderr output stream\n') # stderr is unbuffered, should use for errors only
sys.stderr.flush() # flush buffer
sys.stdout.write('this is the stdout output stream\n\n') # should use for everything except errors

# sys `argv` command
print("\nsystem arguments (notice it returns a LIST):")
print(sys.argv) # all the arguments in a (0-based) LIST, remember the 1st argument is the file name

dsize = sys.getsizeof({}) # overhead of an empty dictionary
lsize = sys.getsizeof([]) # number bytes of an empty list
ssize = sys.getsizeof(set()) # num bytes of an empty set
print("\n-empty dictionary {} bytes\n-empty list {} bytes\n-empty set {} bytes\n".format(dsize, lsize, ssize))
```

## `Stderr` and `Stdout`
Standard Error output is unbuffered, so we run `sys.stderr.flush()` to flush the buffer.
```
import sys

sys.stderr.write('this is stderr output stream\n') # stderr is unbuffered, should use for errors only
sys.stderr.flush() # flush buffer
sys.stdout.write('this is the stdout output stream\n\n') # should use for everything except errors
```
Output:
```
this is stderr output stream

this is the stdout output stream
```

## `sys.argv` command
Returns all the command-line arguments passed in as a (0-based) LIST.  **Remember** the 0th (1st) argument is the file name.

```
print("\nsystem arguments (notice it returns a LIST):")
print(sys.argv) # all the arguments in a (0-based) LIST, remember the 1st argument is the file name
```
Output:
```
system arguments (notice it returns a LIST):
['/opt/conda/lib/python3.5/site-packages/ipykernel/__main__.py', '-f', '/home/jovyan/.local/share/jupyter/runtime/kernel-24640232-2bba-487f-b37a-f3efec8c17b9.json']
```
## `sys.getsizeof(object)` command
Gets the size in `bytes` of the `object`.

```
dsize = sys.getsizeof({}) # overhead of an empty dictionary
lsize = sys.getsizeof([]) # number bytes of an empty list
ssize = sys.getsizeof(set()) # num bytes of an empty set

print("\n-empty dictionary {} bytes\n-empty list {} bytes\n-empty set {} bytes\n".format(dsize, lsize, ssize))
```
Output:
```
-empty dictionary 288 bytes
-empty list 64 bytes
-empty set 224 bytes
```
