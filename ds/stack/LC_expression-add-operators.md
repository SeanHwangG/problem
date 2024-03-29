# [LC_expression-add-operators](https://leetcode.com/problems/expression-add-operators)

* en

  ```en
  Given string num that contains only digits an, an integer target
  return all possibilities to add binary operators '+', '-', or '*' between digits so that result evaluates to target
  ```

* tc

  ```tc
  Input: num = "105", target = 5
  Output: ["1*0+5","10-5"]
  ```

## Solution

* py

  ```py
  def addOperators(self, num: str, target: int) -> List[str]:
    ans, stk = [], [(1, num[0], num[0]=='0')] # next_index, path, has_leading_zero
    while stk:
      i, path, zero = stk.pop()
      if i >= len(num):
        if eval(path) == target:
          ans.append(path)
      else:
        if not zero:
          stk.append((i+1, path+num[i], zero))
        stk.append((i+1, path+'+'+num[i], num[i]=='0'))
        stk.append((i+1, path+'-'+num[i], num[i]=='0'))
        stk.append((i+1, path+'*'+num[i], num[i]=='0'))
    return ans
  ```
