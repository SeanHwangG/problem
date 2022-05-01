# [HR_text-processing-cut-7](https://www.hackerrank.com/challenges/text-processing-cut-7)

Print characters from thirteenth position to the end

```txt
Input:
How was the math test?
We have a test tomorrow.
I finally passed that test.
test

Output:
math
test
that
test
```

## Solution

* sh

  ```sh
  cut -d' ' -f4
  ```
