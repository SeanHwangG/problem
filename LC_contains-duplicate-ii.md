{% tabs %}{% tab title='LC_219.go' %}

```go
func containsNearbyDuplicate(nums []int, k int) bool {
  dic := make(map[int]int, len(nums))
  for i, v := range nums{
    if pos, ok := dic[v]; ok && i - pos <= k {
      return true
    }
    dic[v] = i
  }
  return false
}
```

{% endtab %}{% tab title='LC_219.py' %}

```py
def containsNearbyDuplicate(self, nums, k):
  dic = {}
  for i, v in enumerate(nums):
    if v in dic and i - dic[v] <= k:
      return True
    dic[v] = i
  return False
```

{% endtab %}{% endtabs %}
