{% tabs %}{% tab title='LC_630.py' %}

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

{% endtab %}{% endtabs %}
