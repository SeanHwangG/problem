# [LC_minimum-initial-energy-to-finish-tasks](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks)

You are given an array tasks where tasks[i] = [actuali, minimumi]:
Actuali is the actual amount of energy you spend to finish the ith task
Minimumi is the minimum amount of energy you require to begin the ith task
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task
However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it
You can finish the tasks in any order you like
Return min initial amount of energy you will need to finish all the tasks

```txt
Input: tasks = [[1,2],[2,4],[4,8]]
Output: 8
```

## Solution

* py

  ```py
  def minimumEffort(self, tasks: List[List[int]]) -> int:
    sort = sorted(tasks, key = lambda x : x[1] - x[0])[::-1]
    res = 0; curr = 0
    for i, n in enumerate(sort):
      if curr < n[1]:
        res += n[1] - curr
        curr = n[1]
      curr -= n[0]
    return res
  ```
