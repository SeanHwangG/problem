# [LC_article-views-ii](https://leetcode.com/problems/article-views-ii)

```en
Find all authors that viewed at least one of their own articles, sorted in ascending order by their id
```

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

| article_id | author_id | viewer_id | view_date  |
| ---------- | --------- | --------- | ---------- |
| 1          | 3         | 5         | 2019-08-01 |
| 3          | 4         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |

* Find all the people who viewed more than one article on the same date, sorted in ascending order by their id

| id  |
| --- |
| 5   |
| 6   |

* sql

  ```sql
  SELECT DISTINCT viewer_id AS id#, count(DISTINCT article_id) AS total FROM views
    GROUP BY viewer_id, view_date HAVING Count(DISTINCT Article_id) > 1 ORDER by 1
  ```
