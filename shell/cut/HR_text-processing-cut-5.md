# [HR_text-processing-cut-5](https://www.hackerrank.com/challenges/text-processing-cut-5)

Given tab delimited file with several columns (tsv format) print the first three fields

```txt
Input:
1   New York, New York[10]  8,244,910   1
2   Los Angeles, California 3,819,702   2
3   Chicago, Illinois   2,707,120   3
4   Houston, Texas  2,145,146   4
5   Philadelphia, Pennsylvania[11]  1,536,471   5

Output:
1   New York, New York[10]  8,244,910
2   Los Angeles, California 3,819,702
3   Chicago, Illinois   2,707,120
4   Houston, Texas  2,145,146
5   Philadelphia, Pennsylvania[11]  1,536,471
```

## Solution

* sh

  ```sh
  cut -f1-3
  ```
