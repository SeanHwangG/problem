# [CW_5d376cdc9bcee7001fcb84c0](https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0)

* en

  ```en
  You are given a list of numbers. The numbers each repeat a certain number of times
  Remove all numbers that repeat an odd number of times while keeping everything else the same
  ```

* tc

  ```tc
  Input: c(1, 2, 3, 1, 3, 3)
  Output: c(1, 1)
  ```

## Solution

* r

  ```r
  odd_ones_out <- function(numbers){
    t <- table(numbers)
    even <- t[t%%2==0]
    numbers[numbers %in% names(even)]
  }
  ```
