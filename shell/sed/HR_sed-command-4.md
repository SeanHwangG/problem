# [HR_sed-command-4](https://www.hackerrank.com/challenges/sed-command-4)

* en

  ```en
  Each line contains a credit card number in the form dddd dddd dddd dddd
  Mask first 12 character
  ```

* tc

  ```tc
  Input:
  1234 5678 9101 1234
  2999 5178 9101 2234
  9999 5628 9201 1232
  8888 3678 9101 1232

  Output:
  **** **** **** 1234
  **** **** **** 2234
  **** **** **** 1232
  **** **** **** 1232
  ```

## Solution

* sh

  ```sh
  sed 's/[0-9]\+ /**** /g'
  ```
