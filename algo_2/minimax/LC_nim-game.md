# [LC_nim-game](https://leetcode.com/problems/nim-game)

* en

  ```en
  Initially, there is a heap of stones on the table
  You and your friend will alternate taking turns, and you go first
  On each turn, the person whose turn it is will remove 1 to 3 stones from the heap
  The one who removes the last stone is the winner
  ```

* tc

  ```tc
  Input: 4
  Output: false
  ```

## Solution

* cpp

  ```cpp
  bool canWinNim(int n) {
    return (n % 4) != 0;
  }
  ```
