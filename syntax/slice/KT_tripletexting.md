# [KT_tripletexting](https://open.kattis.com/problems/tripletexting)

* en

  ```en
  Same string are repeated three times and but one of them are wrong
  Print right string
  ```

* tc

  ```tc
  Input: hellohrllohello
  Output: hello
  ```

## Solution

* py

  ```py
  s = input()
  chunk = len(s) // 3
  a = s[:chunk]
  b = s[chunk:chunk * 2]
  c = s[chunk * 2:]
  if b == c:
    print(b)
  else:
    print(a)
  ```
