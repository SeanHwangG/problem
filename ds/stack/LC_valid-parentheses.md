# [LC_valid-parentheses](https://leetcode.com/problems/valid-parentheses)

```en
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if input is valid

```

```txt
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

## Solution

* java

  ```java
  public boolean isValid(String s) {
    Stack<Character> stack = new Stack<Character>();
    for (char c : s.toCharArray()) {
      if (c == '(')
        stack.push(')');
      else if (c == '{')
        stack.push('}');
      else if (c == '[')
        stack.push(']');
      else if (stack.isEmpty() || stack.pop() != c)
        return false;
    }
    return stack.isEmpty();
  }
  ```
