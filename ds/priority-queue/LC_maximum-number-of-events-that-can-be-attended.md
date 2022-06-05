# [LC_maximum-number-of-events-that-can-be-attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended)

```en
Given array of events where events[i] = [startDayi, endDayi]
Every event i starts at startDayi and ends at endDayi
Can attend an event i at any day d where startTimei <= d <= endTimei (you can only attend one event at any time d)
Return max number of events you can attend
```

```txt
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
```

## Solution

* py

  ```py
  def maxEvents(self, A):
    A.sort(reverse=1)
    h = []
    res = d = 0
    while A or h:
      if not h: d = A[-1][0]
      while A and A[-1][0] <= d:  # add new events to pq starting on day d
        heapq.heappush(h, A.pop()[1])
      heapq.heappop(h) # greedily attend the event that ends soonest
      res += 1
      d += 1
      while h and h[0] < d:
        heapq.heappop(h)
    return res
  ```
