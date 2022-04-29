# [HR_detect-the-domain-name](https://www.hackerrank.com/challenges/detect-the-domain-name)

One line, containing list of detected domains, separated by semi-colons, in lexicographical order
Don't leave any leading/trailing spaces either at ends of line, or before and after the individual domain names

```txt
10
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><b>^
["Train (noun)"](http://www.askoxford.com/concise_oed/train?view=uk).
<i>(definition – Compact OED)</i>. Oxford University Press<span class="reference-accessdate">.
Retrieved 2008-03-18</span>.</span>
<span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.atitle=Train+%28noun%29&rft.genre=article
&rft_id=http%3A%2F%2Fwww.askoxford.com%2Fconcise_oed%2Ftrain%3Fview%3Duk&rft.jtitle=%28definition+%E2%80%93+Compact+OED%29
&rft.pub=Oxford+University+Press&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988">
<span style="display:none;"> </span></span></span></li>
...
</div>

Output: askoxford.com;bnsf.com;hydrogencarsnow.com;mrvc.indianrail.gov.in;web.archive.org
```

## Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  smatch searchResult;
  regex expression(R"(https?://(www.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-\.]+)[/?"])");
  string line, all = "";
  getline(cin, line);

  while (getline(cin, line))
    all += line + " ";

  set<string> output;
  while (regex_search(all, searchResult, expression)) {
    output.insert(searchResult[2]);
    all = searchResult.suffix().str();
  }
  string displayed;
  for(string s : output)
    displayed += s + ";";
  cout << string(displayed.begin(), displayed.end()-1);
  return 0;
}
```

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

```py
import re, sys

page = sys.stdin.read()
re_patt = r"https?:\/\/(?:ww[w\d]\.)?([\w\.-]+\.[a-zA-Z]*)"
print(";".join(sorted(set(re.findall(re_patt, page, re.DOTALL)))))
```
