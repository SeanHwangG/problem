# [LC_get-highest-answer-rate-question](https://leetcode.com/problems/get-highest-answer-rate-question)

* en

  ```en
  Identify the question which has the highest answer rate
  ```

* tc

  ```tc
  Input:
  | uid | action | question_id | answer_id | q_num | timestamp |
  | --- | ------ | ----------- | --------- | ----- | --------- |
  | 5   | show   | 285         | null      | 1     | 123       |
  | 5   | answer | 285         | 124124    | 1     | 124       |
  | 5   | show   | 369         | null      | 2     | 125       |
  | 5   | skip   | 369         | null      | 2     | 126       |

  Output:
  | survey_log |
  | ---------- |
  | 285        |
  ```

## Solution

* sql

  ```sql
  SELECT clean.question_id AS "survey_log" FROM (
    SELECT s.question_id, SUM(CASE WHEN action = "answer" THEN 1 END)/
        SUM(CASE WHEN action = "show" THEN 1 END) AS "answer_rate" FROM survey_log s
    GROUP BY s.question_id) clean
    ORDER BY clean.answer_rate DESC LIMIT 1
  ```
