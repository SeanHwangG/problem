# [HR_s10-weighted-mean](https://www.hackerrank.com/challenges/s10-weighted-mean)

* en

  ```en
  Given values and weights, printed weighted mean
  ```

* tc

  ```tc
  Input: 5
  10 40 30 50 20
  1 2 3 4 5

  Output: 32.0
  ```

## Solution

* r

  ```r
  data<-readLines(con="/dev/stdin",n=-1)
  nums<-as.numeric(unlist(strsplit(data[2]," ")))
  weights<-as.numeric(unlist(strsplit(data[3]," ")))
  cat(format(round(weighted.mean(nums, weights), 1), nsmall=1))
  ```

* py

  ```py
  size = int(input())
  numbers = list(map(int, input().split()))
  weighted = list(map(int, input().split()))
  sum_items = sum(numbers[i] * weighted[i] for i in range(size))

  print(round(sum_items / sum(weighted), 1))
  ```
