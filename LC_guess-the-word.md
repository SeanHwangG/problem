{% tabs %}{% tab title='LC_843.py' %}

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

{% endtab %}{% endtabs %}
