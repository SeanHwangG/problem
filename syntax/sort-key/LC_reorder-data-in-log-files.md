# [LC_reorder-data-in-log-files](https://leetcode.com/problems/reorder-data-in-log-files)

* en

  ```en
  letter-logs come before all digit-logs
  letter-logs are sorted lexicographically by their contents
  If their contents are the same, then sort them lexicographically by their identifiers
  digit-logs maintain their relative ordering
  ```

* tc

  ```tc
  Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
  Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
  ```

## Solution

* cpp

  ```cpp
  bool comp(string s1, string s2){
    int i1 = s1.find(' ') + 1, i2 = s2.find(' ') + 1;
    if (!isdigit(s1[i1]) && !isdigit(s2[i2]))
      return s1.substr(i1) < s2.substr(i2);
    else
      return !isdigit(s1[i1]);
  }
  class Solution {
  public:
    vector<string> reorderLogFiles(vector<string>& logs) {
      stable_sort(logs.begin(), logs.end(), comp);
      return logs;
    }
  };
  ```

* js

  ```js
  const reorderLogFiles = logs =>
    logs.filter(log => /[a-z]$/.test(log))
        .sort((a, b) =>
          ((aId, aWords, _, bId, bWords) =>
            aWords.localeCompare(bWords) || aId.localeCompare(bId))(
            ...a.split(/\s(.+)/),
            ...b.split(/\s(.+)/),
          ),
        ).concat(logs.filter(log => /\d$/.test(log)));
  ```

* py

  ```py
  class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
      def comp(x):
        y = x.split(' ', 1)
        return (0, y[1], y[0]) if y[1][0].isalpha() else (1,)
      return sorted(a, key=comp)
  ```
