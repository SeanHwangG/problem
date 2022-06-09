# [LC_race-car](https://leetcode.com/problems/race-car)

* en

  ```en
  Car starts at position 0 and speed +1 on an infinite number line, can go into negative positions
  Car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
  When you get an instruction 'A', your car does the following:
    position += speed, speed *= 2
  When you get an instruction 'R', your car does the following:
    If your speed is positive then speed = -1, otherwise speed = 1
  Your position stays the same
  (ex: After commands "AAR", car goes to positions 0 -> 1 -> 3 -> 3, and your speed goes to 1 -> 2 -> 4 -> -1)
  Given a target position target, return length of shortest sequence of instructions to get there.
  ```

* tc

  ```tc
  Input: target = 3
  Output: 2  # AA 0 --> 1 --> 3

  Input: target = 6
  Output: 5  # AAARA 0 --> 1 --> 3 --> 7 --> 7 --> 6
  ```

## Solution

* py
  1. Go pass our target, stop and turn back
      * We take n instructions of A.
      * 1 + 2 + 4 + ... + 2 ^ (n-1) = 2 ^ n - 1
      * Then we turn back by one R instruction.
      * In the end, we get closer by n + 1 instructions.

  2. Go as far as possible before pass target, stop and turn back
      * We take n - 1 instruction of A and one R.
      * Then we take m instructions of A, where m < n

  * Time; O(TlogT)
  * Space; O(T)

  ```py
  @lru_cache(None)
  def racecar(self, t: int) -> int:
    if t == 0:
      return 0
    n = t.bit_length()
    if 2 ** n - 1 == t:
      return n
    else:
      mn = self.racecar(2 ** n - 1 - t) + n + 1
      for m in range(n - 1):
        mn = min(mn, self.racecar(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
    return mn
  ```
