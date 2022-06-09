# [HR_lonely-integer-2](https://www.hackerrank.com/challenges/lonely-integer-2)

* en

  ```en
  First line of input contains number of integers, next contains space-separated integers that form array
  Output, the number that occurs only once
  ```

* tc

  ```tc
  Input: 5
  0 0 1 2 1

  Output: 2
  ```

## Solution

* sh

  ```sh
  read
  tr ' ' '\n' | sort | uniq -u
  ```
