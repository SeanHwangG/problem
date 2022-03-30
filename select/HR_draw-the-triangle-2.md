# [HR_draw-the-triangle-2](https://www.hackerrank.com/challenges/draw-the-triangle-2)

Draw triangle when input is 20

```txt
Input: 5
Output:
*
* *
* * *
* * * *
* * * * *
```

## Solution

```sql
SELECT REPEAT('* ', @NUMBER:= @NUMBER + 1) FROM information_schema.tables, (SELECT @NUMBER:=0) t LIMIT 20
```
