# [HR_excluding-specific-characters](https://www.hackerrank.com/challenges/excluding-specific-characters)

* en

  ```en
  must be of length 6
  First character should not be a digit
  Second character should not be a lowercase vowel
  Third character should not be b, c, D or F
  Fourth character should not be a whitespace character ( \r, \n, \t, \f or \<space> )
  Fifth character should not be a uppercase vowel
  Sixth character should not be a . or , symbol
  ```

* tc

  ```tc
  Input: think?
  Output: true
  ```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  int main() {
    std::string input;
    std::getline(std::cin, input);
    std::regex re(R"([^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,])");
    std::cout << std::boolalpha << std::regex_match(input, re);
    return 0;
  }
  ```

* py

  ```py
  import re

  pattern = r'^[^\d][^aeiou][^bcDF]\S[^AEIOU][^.,]$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
