# [HR_text-processing-in-linux-the-sed-command-3](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-3)

Use grep to remove all those lines that contain the word 'that'
The search should NOT be sensitive to case


```txt
Input:
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,

Output:
From fairest creatures we desire increase,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
```

## Solution

* highlight all the occurrences of 'thy' by wrapping them up in brace brackets

```sh
# & is captured group
sed -e 's/thy/{&}/gi'
```
