# [LC_text-justification](https://leetcode.com/problems/text-justification)

Full justify line

```txt
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

## Solution

```py
def fullJustify(self, words, maxWidth):
  res, cur, num_of_letters = [], [], 0
  for w in words:
    if num_of_letters + len(w) + len(cur) > maxWidth:
      for i in range(maxWidth - num_of_letters):
        cur[i % (len(cur) - 1 or 1)] += ' '
      res.append(''.join(cur))
      cur, num_of_letters = [], 0
    cur += [w]
    num_of_letters += len(w)
  return res + [' '.join(cur).ljust(maxWidth)]
```
