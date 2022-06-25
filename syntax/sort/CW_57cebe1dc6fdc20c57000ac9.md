# [CW_57cebe1dc6fdc20c57000ac9](https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9)

* en

  ```en
  Given a string of words, return the length of the shortest word(s).
  ```

* tc

  ```tc
  Input: "bitcoin take over the world maybe who knows perhaps"
  Output: 3
  ```

## Solution

* r

  ```r
  find_short <- function(s){
    min(nchar(unlist(strsplit(s, " "))))
  }
  ```
