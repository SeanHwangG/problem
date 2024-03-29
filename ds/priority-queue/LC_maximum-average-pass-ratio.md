# [LC_maximum-average-pass-ratio](https://leetcode.com/problems/maximum-average-pass-ratio)

* en

  ```en
  classes[i] = [passi, totali]. You know beforehand that in ith class
    There are totali total students, but only passi number of students will pass exam
  There're another extraStudents brilliant students that are guaranteed to pass exam of any class they're assigned to
  Assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all classes
  ```

* tc

  ```tc
  Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
  Output: 0.78333
  ```

## Solution

* py

  ```py
  def maxAverageRatio(self, A, k):
    h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in A]
    heapify(h)
    for _ in range(k):
      v, a, b = heapq.heappop(h)
      a, b = a + 1, b + 1
      heapq.heappush(h, (-(a + 1) / (b + 1) + a / b, a, b))
    return sum(a / b for v, a, b in h) / len(h)
  ```
