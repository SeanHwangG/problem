# [HR_more-than-75-marks](https://www.hackerrank.com/challenges/more-than-75-marks)

Query the Name of any student in STUDENTS who scored higher than 75 Marks
Order your output by the last three characters of each name
  If student both have name ending in same last three characters (ex: Bobby, Robby), sort them by ascending ID

```txt
Input:
| ID  | Name     | Marks |
| --- | -------- | ----- |
| 1   | Ashley   | 81    |
| 2   | Samantha | 75    |
| 4   | Julia    | 76    |
| 3   | Belvet   | 84    |
```

## Solution

* sql

  ```sql
  SELECT Name FROM Students WHERE Marks > 75
    ORDER BY RIGHT(Name, 3), Id;
  ```
