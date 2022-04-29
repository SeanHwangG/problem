# [HR_hackerrank-tweets](https://www.hackerrank.com/challenges/hackerrank-tweets)

Print total number of tweets that has hackerrank (case insensitive) in it

```txt
Input:
4
I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
interesting talk by hari, co-founder of hackerrank

Output: 4
```

## Solution

```js
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
  console.log(input.match(/hackerrank/ig).length);
});
```

```py
import re
input_ = ' '.join([input() for _ in range(int(input()))])
print(len(re.findall(r'hackerrank', input_, re.IGNORECASE)))
# print(sum('HACKERRANK' in input().upper() for i in range(int(input()))))
```
