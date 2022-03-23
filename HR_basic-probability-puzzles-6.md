```py
bag_x = ['w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b']
bag_y = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b', 'b', 'b']

total, count = 0, 0
while len(bag_x) != 0:
  ball = bag_x.pop()
  bag_y.append(ball)
  total += len(bag_y)
  count += bag_y.count('b')
  bag_y.pop()

print(f"{counter}/{total}")
```
