# [HR_matching-same-text-again-again](https://www.hackerrank.com/challenges/matching-same-text-again-again)

* en

  ```en
  S must be of length: 20
  1 character: lowercase letter
  2 character: word character
  3 character: whitespace character
  4 character: non word character
  5 character: digit
  6 character: non digit
  7 character: uppercase letter
  8 character: letter (either lowercase or uppercase)
  9 character: vowel (a, e, i , o , u, A, E, I, O or U)
  10 character: non whitespace character
  11 character: should be same as 1st character
  12 character: should be same as 2nd character
  13 character: should be same as 3rd character
  14 character: should be same as 4th character
  15 character: should be same as 5th character
  16 character: should be same as 6th character
  17 character: should be same as 7th character
  18 character: should be same as 8th character
  19 character: should be same as 9th character
  20 character: should be same as 10th character
  ```

* tc

  ```tc
  Input: ab #1?AZa$ab #1?AZa$
  Output: False
  ```

## Solution

* cpp

  ```cpp
  #include <bits/stdc.h++>
  using namespace std;

  int main() {
    string s;
    regex p{R"(([a-z]\w\s\W\d\D[A-Z][[:alpha:]][aeiouAEIOU]\S)\1)"};
    getline(cin, s);
    cout << boolalpha << regex_match(s, p) << endl;
    return 0;
  }
  ```

* py

  ```py
  import re

  pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-z,A-Z][aieouAEIOU]\S)\1$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
