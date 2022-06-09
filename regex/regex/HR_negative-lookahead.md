# [HR_negative-lookahead](https://www.hackerrank.com/challenges/negative-lookahead)

* en

  ```en
  Match all characters which are not immediately followed by that same character
  ```

* tc

  ```tc
  Input: gooooo
  Output: 2
  ```

## Solution

* cpp

  ```cpp
  #include <iostream>
  #include <algorithm>
  #include <regex>
  using namespace std;


  int main() {
    string s;
    regex p{"(.)(?!\\1)"};

    getline(cin, s);
    auto matchcount = distance(sregex_iterator(s.begin(), s.end(), p), sregex_iterator());
    cout << "Number of matches : " << matchcount << endl;

    return 0;
  }
  ```

* py

  ```py
  import re

  Test_String = input()
  pattern = r"(.)(?!\1)"
  match = re.findall(pattern, Test_String)

  print("Number of matches :", len(match))
  ```
