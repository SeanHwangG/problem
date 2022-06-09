# [LC_predict-the-winner](https://leetcode.com/problems/predict-the-winner)

* en

  ```en
  Given an integer array nums. Two players are playing a game with this array: player 1 and player 2
  Player takes one of the numbers from either end of the array, adds chosen number to their score
  If you start first, can you win?
  ```

* tc

  ```tc
  Input: nums = [1,5,2]
  Output: false
  ```

## Solution

* java
  * Time, Space; O(N^2), O(N^2)

  ```java
  public boolean PredictTheWinner(int[] nums) {
    return helper(nums, 0, nums.length-1, new Integer[nums.length][nums.length]) >= 0;
  }
  private int helper(int[] nums, int s, int e, Integer[][] mem){
    if(mem[s][e] == null)
      mem[s][e] = s == e ? nums[e] :
        Math.max(nums[e] - helper(nums, s, e - 1, mem), nums[s] - helper(nums, s + 1, e, mem));
    return mem[s][e];
  }
  ```
