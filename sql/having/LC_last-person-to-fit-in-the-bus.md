# [LC_last-person-to-fit-in-the-bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus)

```en
Maximum weight elevator can hold is 1000
Find person_name of last person who will fit in elevator without exceeding weight limit
```

```txt
Input:

| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |

Output:

| person_name       |
+-------------------+
| Thomas Jefferson  |
```

## Solution

* sql

  ```sql
  SELECT q1.person_name FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
    GROUP BY q1.turn HAVING SUM(q2.weight) <= 1000
    ORDER BY SUM(q2.weight) DESC
    LIMIT 1
  ```
