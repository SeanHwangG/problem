# [LC_parallel-courses-ii](https://leetcode.com/problems/parallel-courses-ii)

* en

  ```en
  Given an integer n, which indicates that there are n courses labeled from 1 to n
  Given an array relations where relations[i] = [prev, next]
    representing prerequisite relation between course prev and next: course prev has to be taken before course next
  Also, you are given the integer k.
  In 1 semester, take at most k courses if taken all prerequisites in previous semester for courses you are taking
  Return min number of semesters needed to take all courses, it is always possible to take every course.
  ```

* tc

  ```tc
  Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
  Output: 3

  Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
  Output: 4
  ```

## Solution

* py

  ```py
  class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
      post, pre = defaultdict(list), [0] * n
      for a, b in dependencies:
        pre[b-1] += 1
        post[a-1] += b-1,

      @lru_cache(None)
      def dfs(mask, pre):
        if not mask: return 0

        take = []
        for i in range(n):
          if mask & 1 << i and pre[i] == 0:
            take += i,

        res = inf
        for c in combinations(take, min(k, len(take))):
          m, d = mask, list(pre)
          for a in c:
            m ^= 1 << a
            for b in post[a]:
              d[b] -= 1
          res = min(res, 1 + dfs(m, tuple(d)))
        return res

      return dfs((1 << n) - 1, tuple(pre))
  ```
