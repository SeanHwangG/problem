# [LC_not-boring-movies](https://leetcode.com/problems/not-boring-movies)

* en

  ```en
  Output movies with odd numbered ID and description that is not 'boring'. Order the result by rating
  ```

* tc

  ```tc
  Input:
  | id  | movie      | description | rating |
  | --- | ---------- | ----------- | ------ |
  | 1   | War        | great 3D    | 8.9    |
  | 2   | Science    | fiction     | 8.5    |
  | 3   | irish      | boring      | 6.2    |
  | 4   | Ice song   | Fantacy     | 8.6    |
  | 5   | House card | Interesting | 9.1    |

  Output:
  | id  | movie      | description | rating |
  | --- | ---------- | ----------- | ------ |
  | 5   | House card | Interesting | 9.1    |
  | 1   | War        | great 3D    | 8.9    |
  ```

## Solution

* sql

  ```sql
  SELECT * FROM cinema
    WHERE description != 'boring' AND id % 2 = 1
    ORDER BY rating DESC;
  ```
