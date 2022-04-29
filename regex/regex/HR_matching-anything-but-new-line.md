# [HR_matching-anything-but-new-line](https://www.hackerrank.com/challenges/matching-anything-but-new-line)

Matches only and exactly strings of form: abc.def.ghi.jkx
where each variable a, b, c, d, e, f, g, h, i, j, k, x can be any single character except the newline

```txt
Input: 123.456.abc.def
Output: True

Input: 123456789.2.2.2
Output: False
```

## Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  std::string input;
  std::getline(std::cin, input);
  std::regex re (R"(...\....\....\....)");
  std::cout << std::boolalpha << std::regex_match(input, re);
  return 0;
}
```

```py
import re
print(str(bool(re.match(r"...\....\....\....", input()))).lower())
```
