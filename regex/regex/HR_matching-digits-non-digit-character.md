# [HR_matching-digits-non-digit-character](https://www.hackerrank.com/challenges/matching-digits-non-digit-character)

You have a test string . Your task is to match the pattern XXxXXxXX
Here x denotes a digit character, and X denotes a non-digit character.



```txt
Input: 06-11-2015
Output: True

Input: 0-10-2015
Output: False
```

## Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  string s, b;
  regex p{"\\d{2}\\D\\d{2}\\D\\d{4}"};
  getline(cin, s);
  cout << boolalpha << regex_search(s, p) << endl;
  return 0;
}
```

```py
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"   # Do not delete 'r'.
```
