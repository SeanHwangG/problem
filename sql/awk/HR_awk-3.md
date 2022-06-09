# [HR_awk-3](https://www.hackerrank.com/challenges/awk-3)

* en

  ```en
  A >=80, B >= 60, C >= 60, FAIL otherwise
  ```

* tc

  ```tc
  Input:
  A 25 27 50
  B 35 37 75
  C 75 78 80
  D 99 88 76

  Output:
  A 25 27 50 : FAIL
  B 35 37 75 : FAIL
  C 75 78 80 : B
  D 99 88 76 : A
  ```

## Solution

* sh

  ```sh
  awk '{avg=($2+$3+$4)/3; print $0, ":", (avg<50)?"FAIL":(avg<80)?"B":"A"}'
  ```
