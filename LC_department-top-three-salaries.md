```sql
SELECT dep.Name Department, emp.Name Employee, emp.Salary FROM Department dep, Employee emp
  WHERE emp.DepartmentId=dep.Id AND
  (SELECT count(DISTINCT Salary) FROM Employee WHERE DepartmentId=dep.Id AND Salary>emp.Salary) < 3
```
