# [LC_tenth-line](https://leetcode.com/problems/tenth-line)

```en
Print 10th line
```

```txt
Input:
123
52
2lk
sdlkfj
werkljla
sdkfjlw
wer
we
qw
10th line
sdfk

Output: 10th line
```

## Solution

* sh

  ```sh
  awk 'NR == 10' file.txt
  ```
