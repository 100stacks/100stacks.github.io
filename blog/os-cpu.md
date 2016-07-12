# Get the number of CPUs and Workers

## Code Snippet

```py
import os
from multiprocessing import cpu_count
worker_count = (cpu_count() * 2 ) + 1

print("num cpu's:", cpu_count())
print("worker count:", worker_count)
```

### Output
```
num cpu's: 4
worker count: 9
```
