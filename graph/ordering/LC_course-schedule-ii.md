# [LC_course-schedule-ii](https://leetcode.com/problems/course-schedule-ii)

* en

  ```en
  There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1
  Array prerequisites where prerequisites[i] = [ai, bi] indicates that take course bi first before course ai
  Return any ordering of courses to finish all courses (if impossible, return an empty array)
  ```

* tc

  ```tc
  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0,2,1,3]
  ```

## Solution

* Time; O(V + E)
* Space; O(V + E)

* py

  ```py
  def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
    G = [[] for i in range(n)]
    degree = [0] * n
    for i, j in prerequisites:
      G[i].append(j)  # Take i before j
      degree[j] += 1
    bfs = [i for i in range(n) if degree[i] == 0]
    for i in bfs:
      for j in G[i]:
        degree[j] -= 1
        if degree[j] == 0:
          bfs.append(j)
    return reversed(bfs) if len(bfs) == n else []
  ```
