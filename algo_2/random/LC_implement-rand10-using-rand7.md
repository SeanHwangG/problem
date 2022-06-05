# [LC_implement-rand10-using-rand7](https://leetcode.com/problems/implement-rand10-using-rand7)

```en
Print rand10() given rand7()
```

```txt
Input: n = 2
Output: [2, 8]
```

## Solution

* cpp

  ```cpp
  int rand10() {
    int rand40 = 40;
    while (rand40 >= 40)
      rand40 = (rand7() - 1) * 7 + rand7() - 1;

    return rand40 % 10 + 1;
  }
  ```

* py

  ```py
  def rand10(self):
    rand40 = 40
    while rand40 >= 40:
      rand40 = (rand7() - 1) * 7 + rand7() - 1
    return rand40 % 10 + 1
  ```
