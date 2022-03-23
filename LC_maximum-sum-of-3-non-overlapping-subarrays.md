```py
def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
  sub_sum = sum(nums[:k]) #set first k-sized window

  # 3 arrays to store max values at certain indexes (DP)
  take_1 = [[0, []] for _ in range(len(nums))]
  take_2 = [[0, []] for _ in range(len(nums))]
  take_3 = [[0, []] for _ in range(len(nums))]

  for i in range(k - 1, len(nums)):
    sub_sum = sub_sum - nums[i - k] + nums[i]
    take_1[i] = [sub_sum, [i - k + 1]] if sub_sum > take_1[i - 1][0] else take_1[i - 1]
    # max so far if we can only choose one k-sized window

    one_sum, one_idx = take_1[i - k]
    take_2[i] = [sub_sum + one_sum, one_idx + [i - k + 1]] if sub_sum + one_sum > take_2[i - 1][0] else take_2[i - 1]
    # max so far if we can choose 2 windows

    two_sum, two_idx = take_2[i - k]
    take_3[i] = [sub_sum + two_sum, two_idx + [i - k + 1]] if sub_sum + two_sum > take_3[i - 1][0] else take_3[i - 1]
    # answer: max sum if we can choose 3 k-sized windows
  return take_3[-1][1]  # indices are stored at the end of take_3
```
