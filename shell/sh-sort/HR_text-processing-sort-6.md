# [HR_text-processing-sort-6](https://www.hackerrank.com/challenges/text-processing-sort-6)

Sort data in ascending order of average monthly temperature in January

```txt
Input:
Austin, Texas   50.2    68.3    84.2    70.6    33.65   85  0.9 62 / 58
Baltimore, Md.  32.3    53.2    76.5    55.4    41.94   115 21.5    53
Bismarck, N.D.  10.2    43.3    70.4    45.2    16.84   96  44.3    64

Output:
Bismarck, N.D.  10.2    43.3    70.4    45.2    16.84   96  44.3    64
Baltimore, Md.  32.3    53.2    76.5    55.4    41.94   115 21.5    53
Austin, Texas   50.2    68.3    84.2    70.6    33.65   85  0.9 62 / 58
```

## Solution

* sh

  ```sh
  sort -n -k2 -t$'\t'
  ```
