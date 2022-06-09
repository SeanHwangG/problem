# [LC_utf-8-validation](https://leetcode.com/problems/utf-8-validation)

* en

  ```en
  A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
  1-byte char, first bit is a 0, followed by its Unicode code.
  n-byte char, first n bits are all 1's, n + 1 bit is 0, followed by n - 1 bytes with most significant 2 bits 10
  ```

* tc

  ```tc
  Input: data = [197,130,1]
  Output: true  # 11000101 10000010 00000001.

  Input: data = [235,140,4]
  Output: false  # data represented the octet sequence: 11101011 10001100 00000100.
  ```

## Solution

* cpp

  ```cpp
  bool validUtf8(vector<int>& data) {
    int count = 0;
    for (auto c : data) {
      if (count == 0) {
        if ((c >> 5) == 0b110) count = 1;
        else if ((c >> 4) == 0b1110) count = 2;
        else if ((c >> 3) == 0b11110) count = 3;
        else if ((c >> 7)) return false;
      } else {
        if ((c >> 6) != 0b10) return false;
        count--;
      }
    }
    return count == 0;
  }
  ```
