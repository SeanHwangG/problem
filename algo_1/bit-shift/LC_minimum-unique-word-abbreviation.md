# [LC_minimum-unique-word-abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation)

* en

  ```en
  String can be abbreviated by replacing any number of non-adjacent substrings with their lengths
  For example, a string such as "substitution" could be abbreviated as (not limited to):
    "sub4u4" ("sub stit u tion") / "12" ("substitution") / "su3i1u2on" ("su bst i t u ti on")
  Given target string target and an array of strings dictionary, return any shortest abbreviation of target
  ST it is not an abbreviation of any string in dictionary
  ```

* tc

  ```tc
  Input: target = "apple", dictionary = ["blade"]
  Output: "a4"

  Input: target = "apple", dictionary = ["blade","plain","amber"]
  Output: "1p3"
  ```

## Solution

* py
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
