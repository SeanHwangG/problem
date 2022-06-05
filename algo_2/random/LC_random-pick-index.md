# [LC_random-pick-index](https://leetcode.com/problems/random-pick-index)

```en
Given an integer array nums with possible duplicates, randomly output the index of a given target number
Assume that the given target number must exist in the array
```

```txt
Input:
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]

Output:
[null, 4, 0, 2]
```

## Solution

* java
  * Reservior sampling

  ```java
  int[] nums;
  Random rnd;

  public Solution(int[] nums) {
    this.nums = nums;
    this.rnd = new Random();
  }

  public int pick(int target) {
    int result = -1;
    int count = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != target)
        continue;
      if (rnd.nextInt(++count) == 0)
        result = i;
    }

    return result;
  }
  ```
