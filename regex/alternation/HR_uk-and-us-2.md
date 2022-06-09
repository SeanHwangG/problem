# [HR_uk-and-us-2](https://www.hackerrank.com/challenges/uk-and-us-2)

* en

  ```en
  For some spelling, US uses or, while UK uses our
  Given UK spelling, find the number of occurence from sentence either of them
  ```

* tc

  ```tc
  Input: 2
  the odour coming out of the leftover food was intolerable
  ammonia has a very pungent odor
  1
  odour

  Output: 2
  ```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  string teaify(string s) {
    regex rp{ "or" };
    return regex_replace(s, rp, "our");
  }

  int main() {
    string s;
    regex wp{"\\b[[:alpha:]]+ou?r[[:alpha:]]*\\b"};
    smatch sm;
    vector<string> allwords;

    int sc;
    cin >> sc >> ws;

    while (sc--) {
      getline(cin, s);
      while (regex_search(s, sm, wp)) {
        allwords.push_back(teaify(sm.str()));
        s = sm.suffix();
      }
    }

    getline(cin, s); // Ignore this line
    while (getline(cin, s)) {
      int matches = 0;
      for (auto w : allwords) if (w == s) matches++;

      cout << matches << endl;
    }

    return 0;
  }
  ```

* py

  ```py
  import re
  text = '\n'.join(input() for _ in range(int(input())))
  for i in range(int(input())):
    s1 = input()
    s2 = s1.replace('our','or')
    print(len(re.findall(rf"\b({s1}|{s2})\b", text)))
  ```
