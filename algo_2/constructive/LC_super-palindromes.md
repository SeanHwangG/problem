# [LC_super-palindromes](https://leetcode.com/problems/super-palindromes)

* en

  ```en
  Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome
  Given 2 positive int left and right represented as strings, return # of super-palindromes int in inclusive range [left, right]
  ```

* tc

  ```tc
  Input: left = "4", right = "1000"
  Output: 4
  ```

## Solution

* py

  ```py
  def superpalindromesInRange(self, left: str, right: str) -> int:
    def generate_palindromes():
      yield from range(1, 10)
      for i in range(1, 10000):
        yield int(f"{i}{str(i)[::-1]}")
        yield from [int(f"{i}{j}{str(i)[::-1]}") for j in range(10)]

    left, right = int(left), int(right)
    count = 0
    for n in generate_palindromes():
      sq = n*n
      if left <= sq and sq <= right and str(sq) == str(sq)[::-1]:
        count += 1

    return count
  ```
