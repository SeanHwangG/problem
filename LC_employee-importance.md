{% tabs %}{% tab title='LC_690.py' %}

* Time; O(n)
* Space; O(n)

```py
class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    emps = {employee.id: employee for employee in employees}
    dfs = lambda id: sum(dfs(sub_id) for sub_id in emps[id].subordinates) + emps[id].importance
    return dfs(id)
```

{% endtab %}{% endtabs %}
