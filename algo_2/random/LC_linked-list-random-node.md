# [LC_linked-list-random-node](https://leetcode.com/problems/linked-list-random-node)

```en
Given a singly linked list, return random node's value from the linked list
```

```txt
Input:
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]

Output:
[null, 1, 3, 2, 2, 3]
```

## Solution

* go

  ```go
  type Solution struct {
    arr []int
  }

  func Constructor(head *ListNode) Solution {
    arr := []int{}
    for head != nil {
      arr = append(arr, head.Val)
      head = head.Next
    }
    return Solution{ arr }
  }

  func (this *Solution) GetRandom() int {
    if len(this.arr) == 0 { return -1 }
    return this.arr[rand.Intn(len(this.arr))]
  }
  ```

* py

  ```py
  def __init__(self, head):
    self.head = head

  def getRandom(self):
    result, node, index = self.head, self.head.next, 1
    while node:
      if random.randint(0, index) is 0:
        result = node
      node = node.next
      index += 1
    return result.val
  ```
