{% tabs %}{% tab title='LC_1098.md' %}

| book_id | name               | available_from |
| ------- | ------------------ | -------------- |
| 1       | "Kalila And Demna" | 2010-01-01     |
| 2       | "28 Letters"       | 2012-05-12     |
| 3       | "The Hobbit"       | 2019-06-10     |
| 4       | "13 Reasons Why"   | 2019-06-01     |
| 5       | "The Hunger Games" | 2008-09-21     |

| order_id | book_id | quantity | dispatch_date |
| -------- | ------- | -------- | ------------- |
| 1        | 1       | 2        | 2018-07-26    |
| 2        | 1       | 1        | 2018-11-05    |
| 3        | 3       | 8        | 2019-06-11    |
| 4        | 4       | 6        | 2019-06-05    |
| 5        | 4       | 5        | 2019-06-20    |
| 6        | 5       | 9        | 2009-02-02    |
| 7        | 5       | 8        | 2010-04-13    |

* reports books that have sold less than 10 copies in last year
* excluding books that have been available for less than 1 month from today. Assume today is 2019-06-23

| book_id | name               |
| ------- | ------------------ |
| 1       | "Kalila And Demna" |
| 2       | "28 Letters"       |
| 5       | "The Hunger Games" |

{% endtab %}{% tab title='LC_1098.sql' %}

```sql
SELECT book_id, name FROM Books
  WHERE available_from < subdate('2019-06-23',interval 1 month) AND
    book_id not in (SELECT book_id FROM Orders
    WHERE dispatch_date between subdate('2019-06-23',interval 1 year) and '2019-06-23'
    GROUP BY book_id
    HAVING SUM(quantity) >= 10)
```

{% endtab %}{% endtabs %}
