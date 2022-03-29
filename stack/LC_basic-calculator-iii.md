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
