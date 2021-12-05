{% tabs %}{% tab title='LC_1204.md' %}

| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |

* The maximum weight the elevator can hold is 1000
* find person_name of the last person who will fit in the elevator without exceeding the weight limit

| person_name       |
+-------------------+
| Thomas Jefferson  |

{% endtab %}{% tab title='LC_1204.sql' %}

```sql
SELECT q1.person_name FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
  GROUP BY q1.turn HAVING SUM(q2.weight) <= 1000
  ORDER BY SUM(q2.weight) DESC
  LIMIT 1
```

{% endtab %}{% endtabs %}
