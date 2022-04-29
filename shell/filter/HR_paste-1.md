# [HR_paste-1](https://www.hackerrank.com/challenges/paste-1)

Join all rows with ;

```txt
Input: Albany, N.Y.
Albuquerque, N.M.
Anchorage, Alaska
Output:
Albany, N.Y.;Albuquerque, N.M.;Anchorage, Alaska
```

## Solution

* sh

```sh
# -d: Use one or more of the provided characters to replace the newline characters instead of the default tab
# -s: Concatenate all of the lines of each separate input file in command line order
paste -sd ';'
```
