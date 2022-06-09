# [LC_course-schedule-iii](https://leetcode.com/problems/course-schedule-iii)

* en

  ```en
  There are n different courses numbered from 1 to n
  courses[i] = [durationi, lastDayi] indicate that ith course should be taken continuously
    for durationi days and must be finished before or on lastDayi
  Return max number of courses that you can take
  ```

* tc

  ```tc
  Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
  Output: 3
  ```

## Solution

* py

  ```py
  def scheduleCourse(self, courses: List[List[int]]) -> int:
    pq = []
    start = 0
    for t, end in sorted(courses, key = lambda course: course[1]):
      start += t
      heapq.heappush(pq, -t)
      while start > end:
        start += heapq.heappop(pq)
    return len(pq)
  ```
