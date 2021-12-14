{% tabs %}{% tab title='LC_1.go' %}

```go
func twoSum(nums []int, target int) []int {
  m := make(map[int]int, len(nums))

  for i, num := range nums {
    if idx, ok := m[target - num]; ok {
      return []int{idx, i}
    }
    m[num] = i
  }
  return []int{0, 0}
}
```

{% endtab %}{% tab title='LC_1.py' %}

```py
def twoSum(self, nums, target):
  d = {}
  for i, num in enumerate(nums):
    if target - num in d:
      return d[target - num], i
    d[num] = i
```

{% endtab %}{% endtabs %}
