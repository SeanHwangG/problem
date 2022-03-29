```py
def total_miles(speeds, times):
  total_miles = 0
  prev_time = 0
  for speed, time in zip(speeds, times):
    total_miles += (time - prev_time) * speed
    prev_time = time
  return total_miles

while n_line := int(input()) != -1:
  speeds, times = [], []
  for _ in range(n_line):
    speed, time = map(int, input().split())
    speeds.append(speed)
    times.append(time)
  print(f'{total_miles(speeds, times)} miles')
```
