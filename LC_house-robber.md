```java
public int rob(int[] nums) {
  if (nums.length == 0)   return 0;

  int N_best = 0, Y_best = nums[0];

  for (int i = 1; i < nums.length; i++){
    int temp = N_best;
    N_best = Math.max(N_best, Y_best);
    Y_best = temp + nums[i];
  }
  return Math.max(N_best, Y_best);
}
```
