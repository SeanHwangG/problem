* Create diff-number whose bits tell me which of the word's letters differ from the target
* Check 2^m abbreviations, represented as number from 0 to 2m-1, bits representing which letters of target are in abbreviation

```py
def minAbbreviation(self, target: str, dic: List[str]) -> str:
  m = len(target)
  diffs = {sum(2 ** i for i, c in enumerate(w) if target[i] != c) for w in dic if len(w) == m}
  if not diffs:
    return str(m)
  bits = max((i for i in range(2 ** m) if all(d & i for d in diffs)),
              key = lambda bits: sum((bits >> i) & 3 == 0 for i in range(m - 1)))
  s = ''.join(target[i] if bits & 2 ** i else '#' for i in range(m))
  return re.sub('#+', lambda m: str(len(m.group())), s)
```
