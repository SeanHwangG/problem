# [HR_text-processing-in-linux-the-uniq-command-3](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-3)

Count each character ignoring case

```txt
Input:
00
00
01
01
00
00
02
02
03
aa
AA
Aa

Output:
2 00
2 01
2 00
2 02
1 03
3 aa
```

## Solution

* sh

  ```sh
  uniq -ci | sed "s/^[[:space:]]*//g"
  ```
