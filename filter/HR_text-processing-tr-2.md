# [HR_text-processing-tr-2](https://www.hackerrank.com/challenges/text-processing-tr-2)

Delete all lowercase characters

```txt
Input: Hello
World
how are you

Output: H
W
```

## Solution

```sh
tr -d a-z  # tr -d [:lower:]
```
