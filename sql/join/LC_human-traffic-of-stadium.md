# [LC_human-traffic-of-stadium](https://leetcode.com/problems/human-traffic-of-stadium)

```en
Display records which have 3 or more consecutive rows and the amount of people more than 100
```

```txt
Input:

  | id  | visit_date | people |
  | --- | ---------- | ------ |
  | 1   | 2017-01-01 | 10     |
  | 2   | 2017-01-02 | 109    |
  | 3   | 2017-01-03 | 150    |
  | 4   | 2017-01-04 | 99     |
  | 5   | 2017-01-05 | 145    |
  | 6   | 2017-01-06 | 1455   |
  | 7   | 2017-01-07 | 199    |
  | 8   | 2017-01-08 | 188    |

Output:

  | id  | visit_date | people |
  | --- | ---------- | ------ |
  | 5   | 2017-01-05 | 145    |
  | 6   | 2017-01-06 | 1455   |
  | 7   | 2017-01-07 | 199    |
  | 8   | 2017-01-08 | 188    |
```

## Solution

* join

  ```sql
  SELECT DISTINCT S1.* FROM stadium S1
    JOIN stadium S2 JOIN stadium S3
    ON ((S1.id = S2.id - 1 AND S1.id = S3.id -2) OR
        (S3.id = S1.id - 1 AND S3.id = S2.id -2) OR
        (S3.id = S2.id - 1 AND S3.id = S1.id -2))
  WHERE S1.people >= 100 AND S2.people >= 100 AND S3.people >= 100 ORDER BY S1.id;
  ```

* Window Function

  ```sql
  SELECT ID, visit_date, people
  FROM (
      SELECT ID, visit_date, people
          ,LEAD(people, 1) OVER (ORDER BY id) nxt
          ,LEAD(people, 2) OVER (ORDER BY id) nxt2
          ,LAG(people, 1) OVER (ORDER BY id) pre
          ,LAG(people, 2) OVER (ORDER BY id) pre2
      FROM Stadium
  ) cte
  WHERE (cte.people >= 100 AND cte.nxt >= 100 AND cte.nxt2 >= 100)
      OR (cte.people >= 100 AND cte.nxt >= 100 AND cte.pre >= 100)
      OR (cte.people >= 100 AND cte.pre >= 100 AND cte.pre2 >= 100)
  ```
