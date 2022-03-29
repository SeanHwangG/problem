```sql
SELECT clean.question_id AS "survey_log" FROM (
  SELECT s.question_id, SUM(CASE WHEN action = "answer" THEN 1 END)/
       SUM(CASE WHEN action = "show" THEN 1 END) AS "answer_rate" FROM survey_log s
  GROUP BY s.question_id) clean
  ORDER BY clean.answer_rate DESC LIMIT 1
```
