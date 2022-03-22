{% tabs %}{% tab title='LC_574.sql' %}

```sql
SELECT Name
FROM Candidate
WHERE id = (SELECT CandidateId
  FROM Vote
  GROUP BY CandidateId
  ORDER BY COUNT(*) DESC
  LIMIT 1);
```

{% endtab %}{% endtabs %}