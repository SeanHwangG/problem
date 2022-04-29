# [HR_np-dot-and-cross](https://www.hackerrank.com/challenges/np-dot-and-cross)

The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.
Print the matrix multiplication of A and B.

```txt
Input: 2
1 2
3 4
1 2
3 4
Output: [[ 7 10]
 [15 22]]
```

## Solution

```py
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))
```
