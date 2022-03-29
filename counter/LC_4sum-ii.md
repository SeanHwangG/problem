```cpp
int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
  int res = 0;
  unordered_map<int, int> AB;
  for (int a : A)
    for (int b : B)
      AB[a + b]++;
  for (int c : C)
    for (int d : D)
      res += AB[-c - d];
  return res;
}
```

```py
def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
  AB = collections.Counter(a+b for a in A for b in B)
  return sum(AB[-c-d] for c in C for d in D)
```
