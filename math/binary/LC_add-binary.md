# [LC_add-binary](https://leetcode.com/problems/add-binary)

```en
Given two binary strings a and b, return their sum as a binary string
```

```txt
Input: a = "11", b = "1"
Output: "100"
```

## Solution

* cpp

  ```cpp
  string addBinary(string a, string b) {
    string s = "";
    int c = 0, i = a.size() - 1, j = b.size() - 1;
    while (i >= 0 || j >= 0 || c == 1) {
      c += i >= 0 ? a[i--] - '0' : 0;
      c += j >= 0 ? b[j--] - '0' : 0;
      s = char(c % 2 + '0') + s;
      c /= 2;
    }
    return s;
  }
  ```

* js

  ```js
  var addBinary = function(a, b) {
    return (BigInt(`0b${a}`) + BigInt(`0b${b}`)).toString(2);
  };
  ```

* py

  ```py
  def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
  ```
