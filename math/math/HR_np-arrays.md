# [HR_np-arrays](https://www.hackerrank.com/challenges/np-arrays)

* en

  ```en
  Given single line of input containing space separated numbers.
  Print the reverse NumPy array with type float
  ```

* tc

  ```tc
  Input: 1 2 3 4 -8 -10
  Output: [-10.  -8.   4.   3.   2.   1.]
  ```

## Solution

* py

  ```py
  import numpy

  def arrays(arr):
    return numpy.array(arr[::-1], float)

  arr = input().strip().split(' ')
  result = arrays(arr)
  print(result)
  ```
