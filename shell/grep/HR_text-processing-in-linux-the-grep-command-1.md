# [HR_text-processing-in-linux-the-grep-command-1](https://www.hackerrank.com/challenges/text-processing-in-linux-the-grep-command-1)

```en
Output only those lines that contain the word 'the'
```

```txt
Input:
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,

Output:
But as the riper should by time decease,
Thou that art now the world's fresh ornament,
```

## Solution

* sh

  ```sh
  grep  " the "
  ```
