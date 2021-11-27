{% tabs %}{% tab title='LC_1507.go' %}

```go
func reformatDate(date string) string {
  month := map[string]string{
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
  }
  if len(date) == 12 { date = "0" + date }
  return date[9:] + "-" + month[date[5:8]] + "-" + date[:2]
}
```

{% endtab %}{% tab title='LC_1507.js' %}

```js
reformatDate(date) => {
  new Date(Date.parse(date.replace(/.. /, ''))).toISOString().slice(0, 10);
}
```

{% endtab %}{% tab title='LC_1507.py' %}

```py
def reformatDate(self, date: str) -> str:
  return datetime.datetime.strptime(re.sub(r"(st|th|rd|nd)", "", date), "%d %b %Y").strftime("%Y-%m-%d")
```

{% endtab %}{% endtabs %}
