# [LC_movie-rating](https://leetcode.com/problems/movie-rating)

```en
Find name of user who has rated greatest number of movies. If tie, lexicographically smaller user name
Find movie name with highest average rating in February 2020. If tie, lexicographically smaller movie name
```

```txt
Input:
Movies
  | movie_id | title    |
  | -------- | -------- |
  | 1        | Avengers |
  | 2        | Frozen 2 |
  | 3        | Joker    |

Users
  | user_id | name   |
  | ------- | ------ |
  | 1       | Daniel |
  | 2       | Monica |
  | 3       | Maria  |
  | 4       | James  |

Movie_Rating
  | movie_id | user_id | rating | created_at |
  | -------- | ------- | ------ | ---------- |
  | 1        | 1       | 3      | 2020-01-12 |
  | 1        | 2       | 4      | 2020-02-11 |
  | 1        | 3       | 2      | 2020-02-12 |
  | 1        | 4       | 1      | 2020-01-01 |
  | 2        | 1       | 5      | 2020-02-17 |
  | 2        | 2       | 2      | 2020-02-01 |
  | 2        | 3       | 2      | 2020-03-01 |
  | 3        | 1       | 3      | 2020-02-22 |
  | 3        | 2       | 4      | 2020-02-25 |

Output:
  | results  |
  | -------- |
  | Daniel   |
  | Frozen 2 |
```

## Solution

* sql

  ```sql
  ( SELECT u.name AS results
    FROM Movie_Rating r LEFT JOIN Users u
    ON (r.user_id = u.user_id)
    GROUP BY r.user_id
    ORDER BY COUNT(r.movie_id) DESC, u.name
    LIMIT 1)
  UNION
  ( SELECT m.title AS results
    FROM Movie_Rating r LEFT JOIN Movies m
    ON (r.movie_id = m.movie_id)
    WHERE r.created_at LIKE '2020-02%'
    GROUP BY r.movie_id
    ORDER BY AVG(r.rating) DESC, m.title
    LIMIT 1)
  ```
