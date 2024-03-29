# [LC_exclusive-time-of-functions](https://leetcode.com/problems/exclusive-time-of-functions)

* en

  ```en
  A function's exclusive time is the sum of execution times for all function calls in the program
  Return exclusive time of each function in array, where value at ith index represents exclusive time for function with ID i


  ```

* tc

  ```tc
  Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
  Output: [3,4]
  ```

## Solution

* cpp

  ```cpp
  class Solution {
  public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
      int lastTime = 0;
      stack<int> stk;
      vector<int> runTime(n, 0);
      for( int i = 0; i < logs.size(); i++ ) {
        string str = logs[i];
        int col_1 = str.find(":"), col_2 = str.find_last_of(":");

        int funcId = stoi(str.substr(0, col_1));
        string type = str.substr(col_1 + 1, col_2 - col_1 - 1);
        int currTime = stoi(str.substr(col_2 + 1));

        if ( type == "start" ) {
          if (stk.size() > 0)
            runTime[stk.top()] += currTime-lastTime;
          stk.push(funcId);
          lastTime = currTime;
        } else {
          runTime[stk.top()] += currTime+ 1 - lastTime;
          stk.pop();
          lastTime = currTime+1;
        }
      }
      return runTime;
    }
  };
  ```

* py

  ```py
  def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    ans, stk = [0]*n, []
    for log in logs:
      f_id, event, time = log.split(':')
      f_id, time = int(f_id), int(time)
      if event=='start':
        if stk:
          ans[stk[-1][0]] += time-stk[-1][1]
        stk.append([f_id, time])
      else:
        popped = stk.pop()
        ans[popped[0]] += time-popped[1]+1
        if stk:
          stk[-1][1] = time+1
    return ans
  ```
