# [HR_text-processing-tr-1](https://www.hackerrank.com/challenges/text-processing-tr-1)

```en
Replace all parentheses with box brackets
```

```txt
Input: int i=(int)5.8
(23 + 5)*2
Output:
int i=[int]5.8
[23 + 5]*2
```

## Solution

* sh

  ```sh
  tr "()" "[]"
  ```
