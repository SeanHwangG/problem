{% tabs %}{% tab title='LC_765.py' %}

```py
def minSwapsCouples(self, row: List[int]) -> int:
  n = len(row)
  pair = defaultdict(int)
  for i in range(0, len(row) - 1, 2):
    G[i] = i + 1
    G[i + 1] = i
  ans = 0
  for i in range(0, len(row) - 2, 2): #Traverse the array and swap if not with his/her pair
    if not pair[row[i]] == row[i+1]:
      ans += 1
      temp = row.index(pair[row[i]])
      row[i + 1], row[temp] = row[temp], row[i + 1]
  return ans
```

{% endtab %}{% endtabs %}