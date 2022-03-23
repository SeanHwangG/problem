* Only swap operation is needed for Bubble sort, and when N > 1 you can swap two element

```py
def orderlyQueue(self, S, K):
  return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))
```
