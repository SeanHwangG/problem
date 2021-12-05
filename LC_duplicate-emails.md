{% tabs %}{% tab title='LC_182.md' %}

| Id  | Email   |
| --- | ------- |
| 1   | a@b.com |
| 2   | c@d.com |
| 3   | a@b.com |

* Write a SQL query to find all duplicate emails in a table named Person

| Email   |
| ------- |
| a@b.com |

{% endtab %}{% tab title='LC_182.sql' %}

```sql
SELECT email FROM Person
  GROUP BY email HAVING count(*) > 1;
```

{% endtab %}{% endtabs %}
