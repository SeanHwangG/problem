# [HR_text-processing-tr-3](https://www.hackerrank.com/challenges/text-processing-tr-3)

```en
Replace all sequences of multiple spaces with just one space
```

```txt
Input: He  llo
Wor  ld
how  are  you

Output: He llo
Wor ld
how are you
```

## Solution

* sh

  ```sh
  # -s, --squeeze-repeats
  # replace each input sequence of a repeated character that is listed in SET1 with a single occurrence of that character

  tr -s " "
  ```
