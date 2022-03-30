# [LC_rectangle-area-ii](https://leetcode.com/problems/rectangle-area-ii)

Given a list of (axis-aligned) rectangles, each rectangle[i] = [xi1, yi1, xi2, yi2]
Where (xi1, yi1) are coordinates of bottom-left corner, (xi2, yi2) are coordinates of top-right corner of ith rectangle
Find total area covered by all rectangles in plane, return MOD 10^9+7

```txt
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49 # modulo 10^9+7
```

## Solution

```cpp
class Solution {
public:
  int rectangleArea(vector<vector<int>>& rectangles) {
    set<int> xs, ys;
    for (vector<int> &rect : rectangles) {
      xs.insert({rect[0], rect[2]});
      ys.insert({rect[1], rect[3]});
    }
    vector<int> x(xs.begin(), xs.end()), y(ys.begin(), ys.end());
    vector<vector<bool>> visit(x.size() + 1, vector<bool>(y.size() + 1, false));

    for (vector<int> rect : rectangles){
      int xs = lower_bound(x.begin(), x.end(), rect[0]) - x.begin();
      int xe = lower_bound(x.begin(), x.end(), rect[2]) - x.begin();
      int ys = lower_bound(y.begin(), y.end(), rect[1]) - y.begin();
      int ye = lower_bound(y.begin(), y.end(), rect[3]) - y.begin();
      for (int i = xs; i < xe; i++)
        for (int j = ys; j < ye; j++)
          visit[i][j] = true;
    }

    long ret = 0;
    for (int i = 0; i < x.size(); i++){
      for (int j = 0; j < y.size(); j++){
        if (visit[i][j] && i != x.size() - 1 && j != y.size() - 1)
          ret += (x[i + 1] - x[i]) * (long)(y[j + 1] - y[j]);
    return ret % (long)(1e9 + 7);
  }
};
```
