```cpp
vector<int> count;
ParkingSystem(int big, int medium, int small) {
  count = {big, medium, small};
}

bool addCar(int carType) {
  return count[carType - 1]-- > 0;
}
```

```go
type ParkingSystem struct {
  s [3]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
  return ParkingSystem{ [3]int{ big, medium, small } }
}

func (this *ParkingSystem) AddCar(carType int) bool {
  if this.s[carType - 1] == 0 { return false }
  this.s[carType - 1]--
  return true
}
```

```java
int[] count;
public ParkingSystem(int big, int medium, int small) {
  count = new int[]{big, medium, small};
}

public boolean addCar(int carType) {
  return count[carType - 1]-- > 0;
}
```

```py
class ParkingSystem:
  def __init__(self, big, medium, small):
    self.A = [big, medium, small]

  def addCar(self, carType):
    self.A[carType - 1] -= 1
    return self.A[carType - 1] >= 0
```
