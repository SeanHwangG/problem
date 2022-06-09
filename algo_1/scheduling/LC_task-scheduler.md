# [LC_task-scheduler](https://leetcode.com/problems/task-scheduler)

* en

  ```en
  Given characters array tasks, representing tasks CPU needs to do, where each letter represents different task
  Each task is done in one unit of time. For each unit of time, CPU could complete either one task or just be idle
  However, there is non-negative int n that represents cooldown period between two same tasks
  Return least number of units of times that the CPU will take to finish all the given tasks
  ```

* tc

  ```tc
  Input: tasks = ["A","A","A","B","B","B"], n = 2
  Output: 8
  ```

## Solution

* py

  ```py
  def leastInterval(self, tasks: List[str], n: int) -> int:
    tasks_count = list(collections.Counter(tasks).values())
    max_count = max(tasks_count)
    max_count_tasks = tasks_count.count(max_count)
    return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)
  ```
