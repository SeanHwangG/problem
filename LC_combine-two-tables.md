{% tabs %}{% tab title='LC_175.sql' %}

```sql
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person
  LEFT JOIN Address ON Person.PersonId = Address.PersonId;
```

{% endtab %}{% endtabs %}
