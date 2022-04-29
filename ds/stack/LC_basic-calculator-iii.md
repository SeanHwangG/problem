# [LC_basic-calculator-iii](https://leetcode.com/problems/basic-calculator-iii)

Implement 1 calculator to evaluate a simple expression string.
Expression string contains non-negative integers, +, -, *, / operators, and open ( and closing parentheses )
Int division should truncate toward zero.
Assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1]

```txt
Input: s = "6-4/2"
Output: 4

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

## Solution

* py

  ```py
  def calculate(self, s: str) -> int:
    s = filter(None, re.split(r'([+\-*/()\$])', (s + '$').replace(' ', '')))
    return self.do_calculate(s)

  def do_calculate(self, s):
    stk, num, sign = [], 0, '+'

    def calculate_top():
      if sign == '+':
        stk.append(num)
      if sign == '-':
        stk.append(-num)
      if sign == '*':
        stk[-1] *= num
      if sign == '/':
        stk[-1] = int(stk[-1] / num)

    for c in s:
      if c.isdigit():
        num = int(c)
      elif c == '(':
        num = self.do_calculate(s)
      elif c in ')$':
        calculate_top()
        return sum(stk)
      elif c in '+-*/':
        calculate_top()
        num, sign = 0, c
  ```
