# [LC_employee-importance](https://leetcode.com/problems/employee-importance)

Employee have id, importance, subordinate (list of the IDs of the direct subordinates of the ith employee)
Given integer id, return total importance value of this employee + their direct subordinates

```txt
Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3

Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
```

## Solution

* Time; O(n)
* Space; O(n)

```py
class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    emps = {employee.id: employee for employee in employees}
    dfs = lambda id: sum(dfs(sub_id) for sub_id in emps[id].subordinates) + emps[id].importance
    return dfs(id)
```
