{% tabs %}{% tab title='LC_1.md' %}

* Find two index that sums up to target

```txt
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

{% endtab %}{% tab title='LC_1.go' %}

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
