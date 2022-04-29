# [LC_minimum-remove-to-make-valid-parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)

Given a string s of '(' , ')' and lowercase English characters
Remove the minimum number of parentheses ( '(' or ')', in any positions )
So that the resulting parentheses string is valid and return any valid string

```txt
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
```

## Solution

* cpp

  ```cpp
  string minRemoveToMakeValid(string s) {
    stack<int> st;
    for (auto i = 0; i < s.size(); ++i) {
      if (s[i] == '(') st.push(i);
      if (s[i] == ')') {
        if (!st.empty()) st.pop();
        else s[i] = '*';
      }
    }
    while (!st.empty()) {
      s[st.top()] = '*';
      st.pop();
    }
    s.erase(remove(s.begin(), s.end(), '*'), s.end());
    return s;
  }
  ```
