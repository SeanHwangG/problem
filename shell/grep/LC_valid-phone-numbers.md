# [LC_valid-phone-numbers](https://leetcode.com/problems/valid-phone-numbers)

* en

  ```en
  Output following valid phone numbers:
  ```

* tc

  ```tc
  Input:
  987-123-4567
  123 456 7890
  (123) 456-7890

  Output:
  987-123-4567
  (123) 456-7890
  ```

## Solution

* sh

  ```sh
  grep -e "^\([0-9]\{3\}-\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$" telephone.txt
  ```
