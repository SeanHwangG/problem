# [LC_trips-and-users](https://leetcode.com/problems/trips-and-users)

Find cancellation rate of requests with unbanned users (both client and driver)
Dividing # canceled (client/driver) requests with unbanned users by total # requests with unbanned users on day
Return the result table between "2013-10-01" and "2013-10-03". in any order. Round up to two decimal points

```txt
Input:
* Trip

  | Id  | Client_Id | Driver_Id | City_Id | Status              | Request_at |
  | --- | --------- | --------- | ------- | ------------------- | ---------- |
  | 1   | 1         | 10        | 1       | completed           | 2013-10-01 |
  | 2   | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
  | 3   | 3         | 12        | 6       | completed           | 2013-10-01 |
  | 4   | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
  | 5   | 1         | 10        | 1       | completed           | 2013-10-02 |
  | 6   | 2         | 11        | 6       | completed           | 2013-10-02 |
  | 7   | 3         | 12        | 6       | completed           | 2013-10-02 |
  | 8   | 2         | 12        | 12      | completed           | 2013-10-03 |
  | 9   | 3         | 10        | 12      | completed           | 2013-10-03 |
  | 10  | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |

* User

  | Users_Id | Banned | Role   |
  | -------- | ------ | ------ |
  | 1        | No     | client |
  | 2        | Yes    | client |
  | 3        | No     | client |
  | 4        | No     | client |
  | 10       | No     | driver |
  | 11       | No     | driver |
  | 12       | No     | driver |
  | 13       | No     | driver |

Output:
| Day        | Cancellation Rate |
| ---------- | ----------------- |
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |


```

## Solution

* sql

  ```sql
  SELECT Request_at as Day, ROUND(SUM(t.Status != "completed") / COUNT(*), 2) as "Cancellation Rate"
    FROM Trips t
    JOIN Users c ON t.Client_ID = c.Users_ID AND c.Banned = "No"
    JOIN Users d ON t.Driver_ID = d.Users_ID AND d.Banned = "No"
    WHERE Request_at BETWEEN "2013-10-01" AND "2013-10-03"
    GROUP BY Request_at;
  ```
