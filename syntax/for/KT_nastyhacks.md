# [KT_nastyhacks](https://open.kattis.com/problems/nastyhacks)

* en

  ```en
  For N lines, print "advertise" or "does not matter" or "do not advertise".
  r is expected revenue if you do not advertise, e is expected revenue if you do advertise, c, is the cost of advertising
  ```

* tc

  ```tc
  Input: 3  # N
  0 100 70  # r, e, c
  100 130 30
  -100 -70 40
  Output: advertise
  does not matter
  do not advertise
  ```

## Solution

* py

  ```py
  for _ in range(int(input())):
    r, e, c = map(int, input().split())
    if r > e - c:
      print('do not advertise')
    elif r == e - c:
      print('does not matter')
    else:
      print('advertise')
  ```
