# [LC_course-schedule](https://leetcode.com/problems/course-schedule)

* en

  ```en
  Given jobs and prerequisite, check if all jobs can be done
  ```

* tc

  ```tc
  Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
  Output: false
  ```

## Solution

* py

  ```py
  def canFinish(n, prerequisites):
    G = [[] for i in range(n)]
    degree = [0] * n
    for i, j in prerequisites:
      G[i].append(j)                                                # Take i before j
      degree[j] += 1
    bfs = [i for i in range(n) if degree[i] == 0]
    for i in bfs:
      for j in G[i]:
        degree[j] -= 1
        if degree[j] == 0:
          bfs.append(j)
    return len(bfs) == n
  ```
