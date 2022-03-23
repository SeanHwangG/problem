* Time: O(NlogN)
* Space: O(N)

```cpp
int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
  int n = startTime.size();
  vector<vector<int>> jobs;
  for (int i = 0; i < n; ++i)
    jobs.push_back({endTime[i], startTime[i], profit[i]});

  sort(jobs.begin(), jobs.end());
  map<int, int> dp = {{0, 0}};
  for (auto& job : jobs) {
    int cur = prev(dp.upper_bound(job[1]))->second + job[2];
    if (cur > dp.rbegin()->second)
      dp[job[0]] = cur;
  }
  return dp.rbegin()->second;
}
```

* Time: O(NlogN)
* Space: O(N)

```java
public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
  int n = startTime.length;
  int[][] jobs = new int[n][3];
  for (int i = 0; i < n; i++)
    jobs[i] = new int[] {startTime[i], endTime[i], profit[i]};

  Arrays.sort(jobs, (a, b) -> a[1] - b[1]);
  TreeMap<Integer, Integer> dp = new TreeMap<>();
  dp.put(0, 0);
  for (int[] job : jobs) {
    int cur = dp.floorEntry(job[0]).getValue() + job[2];
    if (cur > dp.lastEntry().getValue())
      dp.put(job[1], cur);
  }
  return dp.lastEntry().getValue();
}
```

* Time: O(NlogN)
* Space: O(N)

```py
def jobScheduling(self, startTime, endTime, profit):
  jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
  dp = [[0, 0]]
  for s, e, p in jobs:
    i = bisect.bisect(dp, [s + 1]) - 1
    if dp[i][1] + p > dp[-1][1]:
      dp.append([e, dp[i][1] + p])
  return dp[-1][1]
```
