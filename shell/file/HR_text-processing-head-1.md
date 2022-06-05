# [HR_text-processing-head-1](https://www.hackerrank.com/challenges/text-processing-head-1)

```en
Output first 20 lines
```

```txt
Input:
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
...

Output:
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
...
```

## Solution

* sh
  * Output first 20 lines

  ```sh
  # cat | cut -d$'\n' -f -20
  head -n 20
  ```
