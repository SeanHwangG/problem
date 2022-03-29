```cpp
class MRUQueue {
public:
  int step = 16;
  list<int> l;
  vector<list<int>::iterator> skip;
  MRUQueue(int n) {
    for (auto i = 0; i <= n; ++i) {
      auto it = l.insert(end(l), i);
      if (i % step == 0) skip.push_back(it);
    }
  }
  int fetch(int k) {
    auto it = skip[k / step];
    if (k % step == 0 && next(it) != end(l))    skip[k / step] = next(it);
    for (int slow = k % step; slow > 0; --slow) ++it;
    l.splice(end(l), l, it);
    for (auto i = k / step + 1; i < skip.size(); ++i)
      skip[i] = next(skip[i]);
    return *it;
  }
};
```
