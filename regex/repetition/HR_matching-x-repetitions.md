# [HR_matching-x-repetitions](https://www.hackerrank.com/challenges/matching-x-repetitions)

Must be of length equal to 45
First characters should consist of letters(both lowercase and uppercase), or of even digits
Last characters should consist of odd digits or whitespace characters

```txt
Input: 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
Output: true
```

## Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  regex p{"[[:alpha:]02468]{40}[13579\\s]{5}"};
  getline(cin, s);
  cout << boolalpha << regex_match(s, p) << endl;
  return 0;
}
```

```py
import re
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'  # Do not delete 'r'.
print(str(bool(re.search(pattern, input()))).lower())
```
