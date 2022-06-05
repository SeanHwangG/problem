# [HR_text-processing-tr-2](https://www.hackerrank.com/challenges/text-processing-tr-2)

```en
Delete all lowercase characters
```

```txt
Input: Hello
World
how are you

Output: H
W
```

## Solution

* sh

  ```sh
  tr -d a-z  # tr -d [:lower:]
  ```
