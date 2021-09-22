{% tabs %}{% tab title='LC_1981.md' %}

* You are given an m x n integer matrix mat and an integer target
* Choose 1 int from each row in matrix such that absolute difference between target and sum of chosen elements is minimized
* Return the minimum absolute difference
* The absolute difference between two numbers a and b is the absolute value of a - b

```txt
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0   # abs(13 - (1 + 5 + 7))

Input: mat = [[1],[2],[3]], target = 100
Output: 94  # abs(100 - (1 + 2 + 3))

Input: mat = [[1,2,9,8,7]], target = 6
Output: 1   # abs(7 - 6)
```

{% endtab %}{% tab title='LC_1981.py' %}

```py
def minimizeTheDifference(self, mat, target):
  nums = {0}
  for row in mat:
    nums = {x + i for x in row for i in nums}
  return min(abs(target - x) for x in nums)
```

{% endtab %}{% endtabs %}
