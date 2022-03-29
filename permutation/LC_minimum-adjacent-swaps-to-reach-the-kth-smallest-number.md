```cpp
int getMinSwaps(string num, int k) {
  string next = num;
  while (next_permutation(next.begin(), next.end()) && --k);
  int ans = 0;
  for (int i = 0; i < num.length() - 1; i++)
    if (num[i] != next[i]) {
      int j = i + 1;
      while (num[i] != next[j]) j++;
      for (int k = j; k > i; k--){
        swap(next[k], next[k - 1]);
        ans++;
      }
    }
  return ans;
}
```
