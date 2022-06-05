# [LC_basic-calculator-ii](https://leetcode.com/problems/basic-calculator-ii)

```en
Given string s which represents an expression, evaluate this expression and return its value
Int division should truncate toward zero
```

```txt
Input: s = "3+2*2"
Output: 7
```

## Solution

* cpp

  ```cpp
  // O(N) time O(1) space
  int calculate(string s) {
    stringstream ss("+" + s);
    char op;
    int n, last, ans = 0;
    while (ss >> op >> n) {
      if (op == '+' || op == '-') {
        n = op == '+' ? n : -n;
        ans += n;
      } else {
        n = op == '*' ? last * n: last / n;
        ans = ans - last + n; // simulate a stack by recovering last values
      }
      last = n;
    }
    return ans;
  }
  ```
