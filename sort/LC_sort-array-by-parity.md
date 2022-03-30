```cpp
class Solution {
public:
  vector<int> sortArrayByParity(vector<int>& A) {
    partition(A.begin (), A.end (), [](auto e) { return e % 2 == 0; });
 return A;
  }
};
```

```py
def sortArrayByParity(self, A):
	return sorted(A, key=lambda x: x % 2)
```
