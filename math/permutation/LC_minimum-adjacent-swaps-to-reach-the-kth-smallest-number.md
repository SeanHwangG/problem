# [LC_minimum-adjacent-swaps-to-reach-the-kth-smallest-number](https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number)

* en

  ```en
  Given string num, representing a large integer, and an integer k
  Int is wonderful if it's a permutation of digits in num and is greater in value than num
  Return min number of adjacent digit swaps that needs to be applied to num to reach kth smallest wonderful int
  ```

* tc

  ```tc
  Input: num = "11112", k = 4
  Output: 4
  ```

## Solution

* cpp

  ```cpp
  int getMinSwaps(string num, int k) {
    string next = num;
    while (next_permutation(next.begin(), next.end()) && --k);
    int ans = 0;
    for (int i = 0; i < num.length() - 1; i++)
      if (num[i] != next[i]) {
        int j = i + 1;
        while (num[i] != next[j]) j++;
        for (int k = j; k > i; k--){
          swap(next[k], next[k - 1]);
          ans++;
        }
      }
    return ans;
  }
  ```
