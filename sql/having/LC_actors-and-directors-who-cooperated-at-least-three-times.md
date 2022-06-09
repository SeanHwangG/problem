# [LC_actors-and-directors-who-cooperated-at-least-three-times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times)

* en

  ```en
  Report that provides pairs (actor_id, director_id) where the actor have cooperated with the director at least 3 times
  ```

* tc

  ```tc
  Input:

  | actor_id    | director_id | timestamp   |
  +-------------+-------------+-------------+
  | 1           | 1           | 0           |
  | 1           | 1           | 1           |
  | 1           | 1           | 2           |
  | 1           | 2           | 3           |
  | 1           | 2           | 4           |
  | 2           | 1           | 5           |
  | 2           | 1           | 6           |

  Output:

  | actor_id    | director_id |
  +-------------+-------------+
  | 1           | 1           |
  ```

## Solution

* sql

  ```sql
  SELECT actor_id, director_id FROM ActorDirector
    GROUP BY actor_id, director_id HAVING COUNT(1) >= 3
  ```
