# [LC_number-of-music-playlists](https://leetcode.com/problems/number-of-music-playlists)

Player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip
To avoid boredom, you will create a playlist so that:
  Every song is played at least once.
  A song can only be played again only if k other songs have been played.
Given n, goal, and k, return # possible playlists that you can create, MOD 109 + 7.

```txt
Input: n = 3, goal = 3, k = 1
Output: 6  # [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

Input: n = 2, goal = 3, k = 0
Output: 6  # [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
```

## Solution

* Last song might be new / old
* Time: O((L-K)(N-K))

```py
def numMusicPlaylists(self, N, L, K):
  dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
  for i in range(K + 1, N + 1):
    for j in range(i, L + 1):
      if i == j or i == K + 1:
        dp[i][j] = math.factorial(i)
      else:
        dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
  return dp[N][L] % (10**9 + 7)
```
