# [LC_guess-the-word](https://leetcode.com/problems/guess-the-word)

Given unique strings where wordlist[i] is 6 letters, and 1 word in this list is chosen as secret
Master.guess(word): guessed word must be from original list with 6 lowercase letters
  returns int, representing # exact matches (value and position) of guess to secret word
  Also, if guess is not in given wordlist, it will return -1 instead
For each test case, have exactly 10 chances to guess word

```txt
Input: secret = "acckzz", wordlist = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
Output: Success
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.  # Success
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
```

## Solution

* py

  ```py
  def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    def match(w1, w2):
      return sum(i == j for i, j in zip(w1, w2))

    n = 0
    while n < 6:
      count = [Counter(w[i] for w in wordlist) for i in range(6)]
      guess = max(wordlist, key = lambda w: sum(count[i][c] for i, c in enumerate(w)))
      n = master.guess(guess)
      wordlist = [w for w in wordlist if match(w, guess) == n]
  ```
