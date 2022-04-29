# [LC_evaluate-boolean-expression](https://leetcode.com/problems/evaluate-boolean-expression)

Evaluate the boolean expressions in Expressions table in any order

```txt
Input: 

Variables

| name | value |
| ---- | ----- |
| x    | 66    |
| y    | 77    |

Expressions

| left_operand | operator | right_operand |
| ------------ | -------- | ------------- |
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |

Output:

| left_operand | operator | right_operand | value |
| ------------ | -------- | ------------- | ----- |
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
```

## Solution

```sql
SELECT e.left_operand, e.operator, e.right_operand,
    CASE WHEN operator = '>' THEN IF(v1.value > v2.value, 'true', 'false')
      WHEN operator = '<' THEN IF(v1.value < v2.value, 'true', 'false')
      ELSE IF(v1.value = v2.value, 'true', 'false')
    END AS value
  FROM Expressions e
  JOIN Variables v1 ON v1.name = e.left_operand
  JOIN Variables v2 ON v2.name = e.right_operand;
```
