# [LC_game-play-analysis-v](https://leetcode.com/problems/game-play-analysis-v)

* en

  ```en
  Install date is the first login day of that player
  Day 1 retention of some date X to be # players whose install date is X and they logged back next day
    Divided by # players whose install date is X, rounded to 2 decimal places
  For each install date, # players that installed the game on that day and the day 1 retention
  ```

* tc

  ```tc
  Input:
  | player_id | device_id | event_date | games_played |
  | --------- | --------- | ---------- | ------------ |
  | 1         | 2         | 2016-03-01 | 5            |
  | 1         | 2         | 2016-03-02 | 6            |
  | 2         | 3         | 2017-06-25 | 1            |
  | 3         | 1         | 2016-03-01 | 0            |
  | 3         | 4         | 2016-07-03 | 5            |

  Output:
  | install_dt | installs | Day1_retention |
  | ---------- | -------- | -------------- |
  | 2016-03-01 | 2        | 0.50           |
  | 2017-06-25 | 1        | 0.00           |
  ```

## Solution

* sql

  ```sql
  SELECT a.event_date AS "install_dt",
        COUNT(DISTINCT a.player_id) AS "installs",
        CAST(AVG(CASE WHEN a3.games_played > 0 THEN 1 ELSE 0 END) AS decimal(16,2)) AS "Day1_retention"
    FROM ((SELECT a2.player_id, MIN(a2.event_date) AS "event_date" FROM Activity a2 GROUP BY a2.player_id)) a
      LEFT JOIN Activity a3 ON a3.player_id = a.player_id AND a3.event_date = DATE_ADD(a.event_date, INTERVAL 1 DAY)
    GROUP BY a.event_date
  ```
