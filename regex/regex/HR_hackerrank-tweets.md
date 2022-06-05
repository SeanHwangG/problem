# [HR_hackerrank-tweets](https://www.hackerrank.com/challenges/hackerrank-tweets)

```en
Print total number of tweets that has hackerrank (case insensitive) in it
```

```txt
Input: 4
I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
interesting talk by hari, co-founder of hackerrank

Output: 4
```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  int main() {
    string s;
    regex hrp{"hackerrank", regex_constants::icase};
    int matches = 0;
    getline(cin, s);
    while(getline(cin, s))
      if (regex_search(s, hrp)) matches++;
    cout << matches << endl;
    return 0;
  }
  ```

* js

  ```js
  process.stdin.resume();
  process.stdin.setEncoding("ascii");
  _input = "";
  process.stdin.on("data", function (input) {
      _input += input;
  });

  process.stdin.on("end", function () {
    console.log(input.match(/hackerrank/ig).length);
  });
  ```

* py

  ```py
  import re
  input_ = ' '.join([input() for _ in range(int(input()))])
  print(len(re.findall(r'hackerrank', input_, re.IGNORECASE)))
  # print(sum('HACKERRANK' in input().upper() for i in range(int(input()))))
  ```
