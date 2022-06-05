# [HR_text-processing-in-linux-the-sed-command-1](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-1)

```en
For each line in a given input file, transform the first occurrence of the word 'the' with 'this'
Search and transformation should be strictly case sensitive
```

```txt
Input: 
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,

Output:
Thou that art now this world's fresh ornament,
And only herald to this gaudy spring,
```

## Solution

* sh

  ```sh
  # \< and > in regex world (sed syntax) represents words boundaries
  sed -e 's/\<the\>/this/'
  ```
