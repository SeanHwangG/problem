# [LC_game-play-analysis-ii](https://leetcode.com/problems/game-play-analysis-ii)

* en

  ```en
  Reports device that is first logged in for each player
  ```

* tc

  ```tc
  Input:
  * Acitivity

    | player_id | device_id | event_date | games_played |
    | --------- | --------- | ---------- | ------------ |
    | 1         | 2         | 2016-03-01 | 5            |
    | 1         | 2         | 2016-05-02 | 6            |
    | 2         | 3         | 2017-06-25 | 1            |
    | 3         | 1         | 2016-03-02 | 0            |
    | 3         | 4         | 2018-07-03 | 5            |

  Output:
    | player_id | device_id |
    | --------- | --------- |
    | 1         | 2         |
    | 2         | 3         |
    | 3         | 1         |
  ```

## Solution

* sql

  ```sql
  SELECT DISTINCT player_id, first_value(device_id) OVER (PARTITION BY player_id ORDER BY event_date) device_id FROM activity
  ```
