{% tabs %}{% tab title='LC_217.go' %}

```go
func containsDuplicate(nums []int) bool {
  m := make(map[int]bool)
  for _, v := range nums {
    if _, ok := m[v]; ok {
      return true
    }
    m[v] = true
  }
  return false
}
```

{% endtab %}{% tab title='LC_217.js' %}

```js
var containsDuplicate = function(nums) {
  return new Set(nums).size < nums.length;
};
```

{% endtab %}{% tab title='LC_217.py' %}

```py
def containsDuplicate(self, nums):
  return len(nums) != len(set(nums))
```

{% endtab %}{% endtabs %}
