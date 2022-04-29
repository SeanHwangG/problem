# [LC_maximum-profit-in-job-scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling)

Given n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i]
Given startTime, endTime and profit arrays, return max profit ST there are no overlapping jobs
If you choose a job that ends at time X you will be able to start another job that starts at time X

```txt
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120  # [1-3]+[3-6]
```

## Solution

* Time: O(NlogN)
* Space: O(N)

* cpp

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

* java

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

* py

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
