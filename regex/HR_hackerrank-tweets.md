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
