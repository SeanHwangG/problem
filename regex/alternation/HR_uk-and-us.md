# [HR_uk-and-us](https://www.hackerrank.com/challenges/uk-and-us)

For some spelling, US uses -se, while UK uses -ze
Given text, find # occurence from sentence either of them

```txt
Input:
2
hackerrank has such a good ui that it takes no time to familiarise its environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize

Output: 2
```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  string americanize(string s) {
    if (s.length() >= 2) s[s.length() - 2] = 'z';
    return s;
  }

  int main() {
    string s;
    regex wp{"\\b\\w*[zs]e\\b"};
    smatch sm;
    vector<string> allwords;
    int sc;
    cin >> sc >> ws;
    while (sc--) {
      getline(cin, s);
      while (regex_search(s, sm, wp)) {
        allwords.push_back(americanize(sm.str()));
        s = sm.suffix();
      }
    }
    getline(cin, s); // Ignore this line
    while(getline(cin, s)) {
      int matches = 0;
      for (auto w : allwords) if (w == s) matches++;
      cout << matches << endl;
    }
    return 0;
  }
  ```

* go

  ```go
  package main

  import (
    "fmt"
    "regexp"
    "bufio"
    "os"
    "strings"
  )


  func main() {
    var n, t int
    fmt.Scan(&n)
    scanner := bufio.NewScanner(os.Stdin)
    txt := ""
    for i:=0; i<n; i++ {
      scanner.Scan()
      txt += " " + scanner.Text()
    }
    scanner.Scan()
    fmt.Sscan(scanner.Text(), &t)

    for i:=0; i<t; i++ {
      scanner.Scan()
      word := scanner.Text()
      re := regexp.MustCompile(`\b`+strings.Replace(word, "our", "ou?r", -1)+`\b`)
      fmt.Println(len(re.FindAllString(txt, -1)))
    }
  }
  ```

* py

  ```py
  import re

  text = '\n'.join(input() for _ in range(int(input())))
  for n in range(int(input())):
    e = input()
    print(len(re.findall(f"{e[:len(e)-2]}[sz]e", text)))
  ```
