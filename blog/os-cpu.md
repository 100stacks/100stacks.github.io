# Get the number of CPUs and Workers in Python

The article shows a simple example of core level system tools available through Python `os` and `multiprocessing` packages.

## Code Snippet

```py
import os
from multiprocessing import cpu_count

worker_count = (cpu_count() * 2 ) + 1

print("num cpu's:", cpu_count())
print("worker count:", worker_count)
```

This shows how Python can access system level information, such as, `cpu_count`.

### Output:
```
num cpu's: 4
worker count: 9
```
