# [LC_split-array-into-fibonacci-sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence)

* en

  ```en
  Return any Fibonacci-like sequence split from num, or return [] if it cannot be done
  ```

* tc

  ```tc
  Input: num = "123456579"
  Output: [123,456,579]
  ```

## Solution

* py

  ```py
  def splitIntoFibonacci(self, num: str) -> List[int]:
    def backtrack(s, i, seq, l):
      if i == len(s):
        if len(seq) > 2 and seq[-1] < 1<<31: return seq
        return []
      if len(seq) > 1:
        cur = str(seq[-1] + seq[-2])
        if s[i:i + len(cur)] != cur: return []
        return backtrack(s, i + len(cur), seq + [int(cur)], l)
      if s[i] == '0':
        return backtrack(s, i + 1, seq + [0], l)
      for j in range(i, min(i + 10, l)):
        tmp = backtrack(s, j + 1, seq+[int(s[i: j + 1])], l)
        if tmp: return tmp
      return []
    return backtrack(S, 0, [], len(S))
  ```
