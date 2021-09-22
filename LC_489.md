{% tabs %}{% tab title='LC_489.md' %}

* Use robot to clean the entire room, with four given APIs can move forward, turn left or right (Each turn is 90 degrees)
* When robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell

```txt
Input: room =
[[1,1,1,1,1,0,1,1],
 [1,1,1,1,1,0,1,1],
 [1,0,1,1,1,1,1,1],
 [0,0,0,1,0,0,0,0],
 [1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms

Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms
```

{% endtab %}{% tab title='LC_489.py' %}

```py
def cleanRoom(self, robot):
  path = set()
  def dfs(x, y, dx, dy):
    robot.clean()
    path.add((x, y))

    for _ in range(4):
      if (x + dx, y + dy) not in path and robot.move():
        dfs(x + dx, y + dy, dx, dy)
      robot.turnLeft()
      dx, dy = -dy, dx

    robot.turnLeft(); robot.turnLeft()
    robot.move()
    robot.turnLeft(); robot.turnLeft()

  dfs(0, 0, 0, 1)
```

{% endtab %}{% endtabs %}
