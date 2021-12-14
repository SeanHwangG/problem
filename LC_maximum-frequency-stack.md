{% tabs %}{% tab title='LC_895.go' %}

```go
import "container/heap"

type Node struct {
  cnt int
  ind int
  x int
}

type maxHeap []*Node

func (h maxHeap) Len() int { return len(h) }

func (h maxHeap) Less(i,j int) bool {
  if h[i].cnt == h[j].cnt {
    return h[i].ind > h[j].ind
  }
  return h[i].cnt > h[j].cnt
}

func (h maxHeap) Swap(i,j int) { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
  *h = append(*h, x.(*Node))
}

func (h *maxHeap) Pop() interface{} {
  n := len(*h) - 1
  res := (*h)[n]
  *h = (*h)[:n]
  return res
}

type FreqStack struct {
  cnt map[int]int
  stack *maxHeap
  ind int
}

func Constructor() FreqStack {
  res := FreqStack{}
  res.ind, res.stack, res.cnt = -1, &maxHeap{}, map[int]int{}
  heap.Init(res.stack)
  return res
}

func (st *FreqStack) Push(x int)  {
  st.ind++
  st.cnt[x]++
  e := Node{st.cnt[x], st.ind, x}
  heap.Push(st.stack, &e)
}

func (st *FreqStack) Pop() int {
  e := heap.Pop(st.stack).(*Node)
  st.cnt[e.x]--
  return e.x
}
```

{% endtab %}{% tab title='LC_895.py' %}

```py
def __init__(self):
  self.freq = collections.Counter()
  self.m = collections.defaultdict(list)
  self.maxf = 0

def push(self, x):
  freq, m = self.freq, self.m
  freq[x] += 1
  self.maxf = max(self.maxf, freq[x])
  m[freq[x]].append(x)

def pop(self):
  freq, m, maxf = self.freq, self.m, self.maxf
  x = m[maxf].pop()
  if not m[maxf]:
    self.maxf = maxf - 1
  freq[x] -= 1
  return x
```

{% endtab %}{% endtabs %}
