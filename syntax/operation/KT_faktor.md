# [KT_faktor](https://open.kattis.com/problems/faktor)

Impact factor of a scientific journal is a measure reflecting the average number of citations to articles published in science journals.
For this task we are using a simplified formula for calculating the impact factor:

(Total sum of all citations articles published in the journal recived)/(Total number of articles published)

Rounding is always preformed up.
For example the impact factor of the “Journal for ore research and time wasting” that published 38 articles quoted 894 times is 894 / 38 = 23.53 rounding up to 24.

You are the editor of one scientific journal.
You know how much article you are going to publish and the owners are pushing you to reach a specific impact factor.
You are wondering how many scientists you will have to bribe to cite your article to meet the owners demands.
Since money is tight you want to bribe the minimal amount of scientists.


```txt
Input: 38 24
Output: 875
```

## Solution

```py
a, b = map(int, input().split())
print((b - 1) * a + 1)
```
