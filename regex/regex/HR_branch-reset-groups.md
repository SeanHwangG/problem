# [HR_branch-reset-groups](https://www.hackerrank.com/challenges/branch-reset-groups)

You have a test string S
Your task is to write a regex which will match , with following condition(s):

S consists of 8 digits.
S must have "---", "-", ".", ":" separator such that str S gets divided in 4 parts, with each part having exactly 2 digits
S string must have exactly one kind of separator
Separators must have integers on both sides

```txt
Valid 
12-34-56-78
12:34:56:78
12---34---56---78
12.34.56.78

Invalid 
1-234-56-78
12-45.78:10
```

## Solution

```cpp
#include <bits/stdc++.h>
using namespace std;


int main() {
  regex reg_pat(R"(^\d\d(---|-|\.|:)(\d\d\1){2}\d\d$)");
  string str;
  cin >> str;
  cout << std::boolalpha << regex_search(str,reg_pat);
  return 0;
}
```

```py
import re
print(str(bool(re.search(r'^\d\d(?|(-)|(:)|(\.)|(---))\d\d\1\d\d\1\d\d$', input()))).lower())
```
