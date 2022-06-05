# [HR_detect-the-email-addresses](https://www.hackerrank.com/challenges/detect-the-email-addresses)

```en
Print all unique e-mail addresses detected by you, in one line, in lexicographical order, a semi-colon as delimiter
```

```txt
Input:
5
HackerRank is more than just a company, hackers@hackerrank.com
  We are a tight group of hackers, bootstrappers, entrepreneurial thinkers and innovators.
  We are building an engaged community of problem solvers.
  Imagine intelligence and value that a room would hold if it contained hackers/problem solvers from around the world?
  We're building this online.
Hypothesis: Every hacker loves a particular type of challenge presented in a certain set of difficulty.
If we build a large collection of real world challenges in different domains with an engaging interface,
it is going to be incredible! Join us to create history.
Available Positions interviewstreet@hackerrank.com
Product Hacker product@hackerrank.com

Output: hackers@hackerrank.com;interviewstreet@hackerrank.com;product@hackerrank.com
```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  int main() {
    string s;
    set<string> addrs;
    regex emailp{"[[:alnum:]_\\.\\-]+@[[:alnum:]\\._\\-]+[[:alnum:]]+"};
    smatch sm;
    getline(cin, s);
    while (getline(cin, s)) {
      while (regex_search(s, sm, emailp)) {
        addrs.insert(sm.str());
        s = sm.suffix();
      }
    }
    for (set<string>::iterator si = addrs.begin(); si != addrs.end(); ++si) {
      if (si != addrs.begin())
        cout << ";";
      cout << *si;
    }
    cout << endl;
    return 0;
  }
  ```

* py

  ```py
  import re
  N = int(input())
  myStr = " ".join([input() for i in range(N)])
  print(";".join(sorted(set([i for i in re.findall(r"([\w.]+@[\w.]+\w+)", myStr)]))))
  ```
