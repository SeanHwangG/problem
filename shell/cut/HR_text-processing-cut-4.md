# [HR_text-processing-cut-4](https://www.hackerrank.com/challenges/text-processing-cut-4)

```en
First three tab seperated columns
```

```txt
Input:
1   New York, New York[10]  8,244,910   1
2   Los Angeles, California 3,819,702   2

Output:
1   New York, New York[10]  8,244,910
2   Los Angeles, California 3,819,702
```

## Solution

* sh

  ```sh
  # by default seperator is tab
  cut -f-3
  ```
