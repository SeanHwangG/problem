# [HR_matching-x-y-repetitions](https://www.hackerrank.com/challenges/matching-x-y-repetitions)

Should begin with 3, 4 or 5 digits
After that, should have 3 or more letters (both lowercase and uppercase)
Then should end with up to 3 symbol(s). You can end with 0 to 3. symbol(s), inclusively

```txt
Input: 3threeormorealphabets.
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
    std::regex re(R"(\d{1,2}[a-zA-Z]{3,100}\.{0,3})");
    std::cout << std::boolalpha << std::regex_match(input, re);
    return 0;
  }
  ```

* py

  ```py
  import re
  pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
