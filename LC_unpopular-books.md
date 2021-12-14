{% tabs %}{% tab title='LC_1098.sql' %}

```sql
SELECT book_id, name FROM Books
  WHERE available_from < subdate('2019-06-23',interval 1 month) AND
    book_id not in (SELECT book_id FROM Orders
    WHERE dispatch_date between subdate('2019-06-23',interval 1 year) and '2019-06-23'
    GROUP BY book_id
    HAVING SUM(quantity) >= 10)
```

{% endtab %}{% endtabs %}
