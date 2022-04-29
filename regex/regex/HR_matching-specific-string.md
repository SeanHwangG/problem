# [HR_matching-specific-string](https://www.hackerrank.com/challenges/matching-specific-string)

Count hackerrank in string

```txt
Input: hackerrank team makes hackerrank platform which let engineers to hone their skills

Output: 2
```

## Solution

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
  regex r("hackerrank");
  string s;
  getline(cin, s);

  cout << "Number of matches : " << distance(sregex_iterator(s.begin(), s.end(), r), sregex_iterator()) << endl;
  return 0;
}
```

```py
import re
print(str(re.match(r"...\....\....\....", input()) is not None).lower())
```
