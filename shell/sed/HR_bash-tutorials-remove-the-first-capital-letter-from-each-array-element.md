# [HR_bash-tutorials-remove-the-first-capital-letter-from-each-array-element](https://www.hackerrank.com/challenges/bash-tutorials-remove-the-first-capital-letter-from-each-array-element)

Transform names as described and display entire array of country names with space between each of them

```txt
Input:
Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
NorthKorea
Norway

Output: .amibia .auru .epal .etherlands .ewZealand .icaragua .iger .igeria .orthKorea .orway
```

## Solution

* sh

  ```sh
  sed 's/^[A-Z]/./' | tr '\n' ' '
  ```
