# [LC_find-median-given-frequency-of-numbers](https://leetcode.com/problems/find-median-given-frequency-of-numbers)



```txt
Input: 
| Number | Frequency |
| ------ | --------- |
| 0      | 7         |
| 1      | 1         |
| 2      | 3         |
| 3      | 1         |

Output:
| median |
| ------ |
| 0.0000 |
```

## Solution

* sql

  ```sql
  SELECT AVG(Number) 'median' FROM
    (SELECT Number, Frequency, @cum:=@cum+Frequency AS 'cum' FROM Numbers, (SELECT @cum:=0) tmp
      ORDER BY Number) AS N_cum WHERE
    ((SELECT ROUND(SUM(Frequency)/2,0) FROM Numbers) BETWEEN cum-Frequency+1 AND cum) OR
    ((SELECT ROUND(SUM(Frequency)/2+0.5,0) FROM Numbers) BETWEEN cum-Frequency+1 AND cum)
  ```
