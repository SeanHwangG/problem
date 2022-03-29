```sql
DELETE p1 FROM Person p1, Person p2 WHERE p2.Email = p1.Email AND p2.Id < p1.Id;
```
