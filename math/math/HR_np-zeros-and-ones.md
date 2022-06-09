# [HR_np-zeros-and-ones](https://www.hackerrank.com/challenges/np-zeros-and-ones)

* en

  ```en
  First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool

  ```

* tc

  ```tc
  Input: 3 3 3
  Output: [[[0 0 0]
    [0 0 0]
    [0 0 0]]

   [[0 0 0]
    [0 0 0]
    [0 0 0]]

   [[0 0 0]
    [0 0 0]
    [0 0 0]]]
  [[[1 1 1]
    [1 1 1]
    [1 1 1]]

   [[1 1 1]
    [1 1 1]
    [1 1 1]]

   [[1 1 1]
    [1 1 1]
    [1 1 1]]]
  ```

## Solution

* py

  ```py
  import numpy
  nums = tuple(map(int, input().split()))
  print (numpy.zeros(nums, dtype = numpy.int))
  print (numpy.ones(nums, dtype = numpy.int))
  ```
