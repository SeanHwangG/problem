{% tabs %}{% tab title='LC_1517.sql' %}

```sql
SELECT * FROM Users
  WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9\_\.\-]*@leetcode\.com$'
```

{% endtab %}{% endtabs %}
