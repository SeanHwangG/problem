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
