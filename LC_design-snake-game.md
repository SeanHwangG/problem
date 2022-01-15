{% tabs %}{% tab title='LC_353.py' %}

```py
class SnakeGame:
  def __init__(self, width: int, height: int, food: int):
    self.snake = collections.deque([[0,0]])    # snake head is at the front
    self.width, self.height = width, height
    self.food = collections.deque(food)
    self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

  def move(self, direction: str) -> int:
      newHead = [self.snake[0][0]+self.direct[direction][0], self.snake[0][1]+self.direct[direction][1]]

      # newHead can be equal to self.snake[-1]
      if (newHead[0] < 0 or newHead[0] >= self.height)\
        or (newHead[1] < 0 or newHead[1] >= self.width)\
        or (newHead in self.snake and newHead != self.snake[-1]): return -1

      if self.food and self.food[0] == newHead:
        self.snake.appendleft(newHead)
        self.food.popleft()
      else:
        self.snake.appendleft(newHead)
        self.snake.pop()

      return len(self.snake) - 1
```

{% endtab %}{% endtabs %}
