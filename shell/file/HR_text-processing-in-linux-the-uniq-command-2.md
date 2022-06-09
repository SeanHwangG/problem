# [HR_text-processing-in-linux-the-uniq-command-2](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2)

* en

  ```en
  Count each character
  ```

* tc

  ```tc
  Input:
  00
  00
  01
  01
  00
  00
  02
  02
  03
  aa
  aa
  aa

  Output:
  2 00
  2 01
  2 00
  2 02
  1 03
  3 aa
  ```

## Solution

* sh

  ```sh
  uniq -c | sed "s/^[[:space:]]*//g"
  ```
