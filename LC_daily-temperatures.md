```cpp
vector<int> dailyTemperatures(vector<int>& T) {
  stack<pair<int,int>> s; // <number, position>
  vector<int> result(T.size(),0);

  for(int i = n - 1; i >= 0; i--) {
    int curr = T[i];
    while (!s.empty() && s.top().first <= curr)   // remove all colder
      s.pop();
    result[i] = s.empty() ? 0 : s.top().second - i; // calculate distance from last index
    s.push({curr,i});
  }

  return result;
}
```

```py
def dailyTemperatures(self, T):
  ans = [0] * len(T)
  stack = []
  for i, t in enumerate(T):             # while iterating forward
    while stack and T[stack[-1]] < t:   # for every lower temperature
      prev_idx = stack.pop()            # update highest
      ans[prev_idx] = i - prev_idx
    stack.append(i)

  return ans
```
