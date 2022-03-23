```cpp
string frequencySort(string s) {
  int freq[256] = {};
  for (unsigned char c : s)
    ++freq[c];

  priority_queue<pair<int,char>> most_freq_chars;
  for (int c = 255; c >= 0; --c)
    most_freq_chars.emplace(freq[c], (char)c);

  string ans;
  ans.reserve(s.length());
  while (!most_freq_chars.empty()) {
    auto [n, c] = most_freq_chars.top();
    ans.append(n, c);
    most_freq_chars.pop();
  }
  return ans;
}
```

```go
func frequencySort(s string) string {
  dict := make([]int, 128)
  list := make([]byte, len(s))
  for i := 0; i < len(s); i++ {
      dict[s[i]]++
      list[i] = s[i]
  }
  sort.Slice(list, func (i int, j int) bool {
    if dict[list[i]] == dict[list[j]] {
      return list[i] < list[j]
    }
    return dict[list[i]] > dict[list[j]]
  })
  return string(list)
}
```
