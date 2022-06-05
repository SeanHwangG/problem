# [HR_matching-whitespace-non-whitespace-character](https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character)

```en
You have a test string S. Your task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters, and X denotes non-white space characters
```

```txt
Input: 12 11 15
Output: True

Input: 12 12  123
Output: False
```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;


  int main() {
    string s, b;
    regex p{ "\\S{2}\\s\\S{2}\\s\\S{2}" };
    getline(cin, s);
    cout << boolalpha << regex_search(s, p) << endl;
    return 0;
  }
  ```

* py

  ```py
  import re
  print(str(bool(re.search(r"\S\S\s\S\S\s\S\S", input()))).lower())
  ```
