# [HR_the-trigram](https://www.hackerrank.com/challenges/the-trigram)

Print most frequent trigram in text, first one in case of tie


```txt
Input: I came from the moon. He went to the other room. She went to the drawing room.
Output: went to the
```

## Solution

```py
import sys
from collections import Counter
from functools import reduce
from operator import iconcat

def getTrigrams(sentence):
  words = sentence.split()
  return [" ".join(words[i:i+3]) for i in range(len(words)-2)]

txt = sys.stdin.read()
trigrams = Counter(reduce(iconcat, map(getTrigrams, txt.lower().split('.')), []))
print(max(trigrams, key=trigrams.get))
```
