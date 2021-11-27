{% tabs %}{% tab title='HR_detect-the-domain.name.go' %}

```go
package main
import "fmt"
import "os"
import "io/ioutil"
import "regexp"
import "strings"
import "sort"

func main() {
 bytes, _ := ioutil.ReadAll(os.Stdin)
  text := string(bytes)

  r := regexp.MustCompile(`(?m)(?:https?\:\/\/)(?:www\.|ww2\.)*([\w\d\-\.]+\.[a-z]{2,})`)
  find := r.FindAllStringSubmatch(text, -1)
  s := []string{}
  un := make(map[string]struct{})
  for i := range find {
    if _, ok := un[find[i][1]]; !ok {
      un[find[i][1]] = struct{}{}
      s = append(s,find[i][1])
    }
  }
  sort.Strings(s)
  fmt.Println(strings.Join(s,";"))
}
```

{% endtab %}{% tab title='HR_detect-the-domain.name.py' %}

```py
import re, sys

page = sys.stdin.read()
re_patt = r"https?:\/\/(?:ww[w\d]\.)?([\w\.-]+\.[a-zA-Z]*)"
print(";".join(sorted(set(re.findall(re_patt, page, re.DOTALL)))))
```

{% endtab %}{% endtabs %}
