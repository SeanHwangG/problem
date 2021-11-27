{% tabs %}{% tab title='LC_937.cpp' %}

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

{% endtab %}{% tab title='LC_937.js' %}

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

{% endtab %}{% tab title='LC_937.py' %}

```py
class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def comp(x):
      y = x.split(' ', 1)
      return (0, y[1], y[0]) if y[1][0].isalpha() else (1,)
    return sorted(a, key=comp)
```

{% endtab %}{% endtabs %}
