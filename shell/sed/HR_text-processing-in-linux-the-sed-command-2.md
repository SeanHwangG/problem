# [HR_text-processing-in-linux-the-sed-command-2](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-2)

* en

  ```en
  Transform all occurrences of word 'thy' with 'your'
  ```

* tc

  ```tc
  Input: Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,

  Output:
  Feed'st your light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  ```

## Solution

* sh

  ```sh
  # g : global
  # i : insensitive
  sed 's/thy/your/ig'
  ```
