{% tabs %}{% tab title='LC_1784.go' %}

```go
func checkOnesSegment(s string) bool {
  return !strings.Contains(s, "01")
}
```

{% endtab %}{% tab title='LC_1784.py' %}

```py
def checkOnesSegment(self, s: str) -> bool:
  return "01" not in s
```

{% endtab %}{% endtabs %}
