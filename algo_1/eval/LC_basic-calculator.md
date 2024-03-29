# [LC_basic-calculator](https://leetcode.com/problems/basic-calculator)

* en

  ```en
  Implement eval, consists of digits, '+', '-', '(', ')', and ' '
  ```

* tc

  ```tc
  Input: s = "1 + 1"
  Output: 2

  Input: s = "(1+(4+5+2)-3)+(6+8)"
  Output: 23
  ```

## Solution

* Push result and sign when openning a braces and pop both when closing a brace

* py

  ```py
  def calculate(self, s: str) -> int:
    res, num, sign, stack = 0, 0, 1, []
    for ss in s:
      if ss.isdigit():
        num = 10 * num + int(ss)
      elif ss in ["-", "+"]:
        res += sign * num
        num = 0
        sign = [-1, 1][ss == "+"]
      elif ss == "(":
        stack.extend([res, sign])
        sign, res = 1, 0
      elif ss == ")":
        res += sign * num
        res = res * stack.pop() + stack.pop()
        num = 0
    return res + num * sign
  ```
