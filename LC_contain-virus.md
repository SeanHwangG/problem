```py
def containVirus(self, grid: List[int]) -> int:
  m, n = len(grid), len(grid[0])
  def adj(i,j):
    for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i , j + 1)]:
      if 0 <= ii < m and 0 <= jj < n:
        yield ii,jj

  def get_virus_areas(grid):
    areas, dangers, walls, color = [], [], [], [[0] * n for i in range(m)]

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1 and color[i][j] == 0:
          area, dq = [(i, j)], deque([(i,j)])
          wall, danger = 0, set()
          color[i][j] = 1
          while dq:
            s, t = dq.popleft()
            for ii, jj in adj(s,t):
              if grid[ii][jj] == 1 and color[ii][jj] == 0:
                color[ii][jj] = 1
                dq.append((ii, jj))
                area.append((ii, jj))
              if grid[ii][jj] == 0:
                wall += 1
                danger.add((ii,jj))
          areas.append(area)
          dangers.append(danger)
          walls.append(wall)
    return areas, dangers, walls

  wall_count = 0
  areas, dangers, walls = get_virus_areas(grid)
  while areas:
    n_area = len(areas)
    if sum(len(area) for area in areas) == m * n:
      return wall_count

    dangerest_i = 0
    for i in range(n_area):
      if len(dangers[i]) > len(dangers[dangerest_i]):
        dangerest_i = i

    wall_count += walls[dangerest_i]
    for i, j in areas[dangerest_i]:
      grid[i][j] = -1

    for danger in dangers[:dangerest_i] + dangers[dangerest_i + 1:]:
      for i, j in danger:
        grid[i][j] = 1

    areas, dangers, walls = get_virus_areas(grid)

  return wall_count
```
