# [LC_duplicate-emails](https://leetcode.com/problems/duplicate-emails)

Find all duplicate emails in a table named Person

```txt
Input:

| Id  | Email   |
| --- | ------- |
| 1   | a@b.com |
| 2   | c@d.com |
| 3   | a@b.com |

Output:

| Email   |
| ------- |
| a@b.com |
```

## Solution

```sql
SELECT email FROM Person
  GROUP BY email HAVING count(*) > 1;
```
