# [LC_design-phone-directory](https://leetcode.com/problems/design-phone-directory)

* en

  ```en
  Implement the PhoneDirectory class:
  PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers
  int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available
  bool check(int number) Returns true if the slot number is available and false otherwise
  void release(int number) Recycles or releases the slot number
  ```

* tc

  ```tc
  Input:
  ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
  [[3], [], [], [2], [], [2], [2], [2]]

  Output:
  [null, 0, 1, true, 2, false, null, true]
  ```

## Solution

* py

  ```py
  class PhoneDirectory:
    def __init__(self, maxNumbers):
      self.available = set(range(maxNumbers))

    def get(self):
      return self.available.pop() if self.available else -1

    def check(self, number):
      return number in self.available

    def release(self, number):
      self.available.add(number)
  ```
