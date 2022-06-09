# [HR_paste-2](https://www.hackerrank.com/challenges/paste-2)

* en

  ```en
  Restructure file so that 3 consecutive rows are folded into 1 line and are separated by semicolons
  ```

* tc

  ```tc
  Input: Albany, N.Y.
  Albuquerque, N.M.
  Anchorage, Alaska
  Asheville, N.C.
  Atlanta, Ga.
  Atlantic City, N.J.
  Austin, Texas
  Baltimore, Md.
  Baton Rouge, La.
  Output:
  Albany, N.Y.;Albuquerque, N.M.;Anchorage, Alaska
  Asheville, N.C.;Atlanta, Ga.;Atlantic City, N.J.
  Austin, Texas;Baltimore, Md.;Baton Rouge, La.
  ```

## Solution

* sh

  ```sh
  paste - - - -d ';'
  ```
