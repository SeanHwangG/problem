{% tabs %}{% tab title='HR_uk-and-us.md' %}

* For some spelling, US uses -se, while UK uses -ze
* Given text, find # occurence from sentence either of them

```txt
Input:
2
hackerrank has such a good ui that it takes no time to familiarise its environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize

Output: 2
```

{% endtab %}{% tab title='HR_uk-and-us.go' %}

```go
package main

import (
  "fmt"
  "regexp"
  "bufio"
  "os"
  "strings"
)


func main() {
  var n, t int
  fmt.Scan(&n)
  scanner := bufio.NewScanner(os.Stdin)
  txt := ""
  for i:=0; i<n; i++ {
    scanner.Scan()
    txt += " " + scanner.Text()
  }
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &t)

  for i:=0; i<t; i++ {
    scanner.Scan()
    word := scanner.Text()
    re := regexp.MustCompile(`\b`+strings.Replace(word, "our", "ou?r", -1)+`\b`)
    fmt.Println(len(re.FindAllString(txt, -1)))
   }
}
```

{% endtab %}{% tab title='HR_uk-and-us.py' %}

```py
import re

text = '\n'.join(input() for _ in range(int(input())))
for n in range(int(input())):
  e = input()
  print(len(re.findall(f"{e[:len(e)-2]}[sz]e", text)))
```

{% endtab %}{% endtabs %}
