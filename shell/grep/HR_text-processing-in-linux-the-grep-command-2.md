# [HR_text-processing-in-linux-the-grep-command-2](https://www.hackerrank.com/challenges/text-processing-in-linux-the-grep-command-2)

Use grep to display all those lines that contain the word the in them, case insensitive

```txt
Input:
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,

Output:
But as the riper should by time decease,
Thou that art now the world's fresh ornament,
```

## Solution

* sh

  ```sh
  # -i, --ignore-case
  # Perform case insensitive matching.  By default, grep is case sensitive.
  # -w, --word-regexp
  # The expression is searched for as a word
  grep -iw "the"
  ```
