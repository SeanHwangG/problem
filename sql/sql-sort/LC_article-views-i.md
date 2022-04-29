# [LC_article-views-i](https://leetcode.com/problems/article-views-i)

Find all authors that viewed at least one of their own articles, sorted in ascending order by their id


```txt
Input:
| article_id | author_id | viewer_id | view_date  |
| ---------- | --------- | --------- | ---------- |
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
Output:
| id  |
| --- |
| 4   |
| 7   |
```

## Solution

```sql
SELECT DISTINCT v.author_id AS "id" FROM Views v
  WHERE v.author_id = v.viewer_id
  ORDER BY v.author_id
```
