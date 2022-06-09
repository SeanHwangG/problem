# [HR_matching-start-end](https://www.hackerrank.com/challenges/matching-start-end)

* en

  ```en
  Must start with a digit and end with . symbol
  Should be characters long only
  ```

* tc

  ```tc
  Input: 0qwer.
  Output: true
  ```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;


  int main() {
    string s;
    regex p{ "^\\d\\w{4}\\.$" };
    getline(cin, s);
    cout << boolalpha << regex_match(s, p) << endl;
    return 0;
  }
  ```

* py

  ```py
  import re

  pattern = r'^\d\w\w\w\w\.$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
