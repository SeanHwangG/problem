{% tabs %}{% tab title='LC_571.sql' %}

```sql
SELECT AVG(Number) 'median' FROM
  (SELECT Number, Frequency, @cum:=@cum+Frequency AS 'cum' FROM Numbers, (SELECT @cum:=0) tmp
    ORDER BY Number) AS N_cum WHERE
  ((SELECT ROUND(SUM(Frequency)/2,0) FROM Numbers) BETWEEN cum-Frequency+1 AND cum) OR
  ((SELECT ROUND(SUM(Frequency)/2+0.5,0) FROM Numbers) BETWEEN cum-Frequency+1 AND cum)
```

{% endtab %}{% endtabs %}
