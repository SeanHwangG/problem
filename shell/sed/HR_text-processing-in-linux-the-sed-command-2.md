# [HR_text-processing-in-linux-the-sed-command-2](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-2)

Transform all occurrences of word 'thy' with 'your'

```txt
Input: Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,

Output:
Feed'st your light's flame with self-substantial fuel,
Making a famine where abundance lies,
```

## Solution

```sh
# g : global
# i : insensitive
sed 's/thy/your/ig'
```
