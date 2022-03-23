```py
import numpy as np

r, c, N = map(int, input().split()) # rows, columns, downsampling coef
R, C = map(int, input().split()) # rows, columns in the original image
o = np.empty((R, C, 3)) # original image
o.fill(np.nan)

for i in range(r):
  current = input().split(' ')
  for j in range(c):
    o[i*N, j*N,:] = map(int, current[j].split(','))

def interpolate(data):
  nan_ind = np.isnan(data)
  not_nan_ind = np.logical_not(nan_ind)
  interpolated = np.interp(nan_ind.nonzero()[0], not_nan_ind.nonzero()[0], data[not_nan_ind])
  data[nan_ind] = interpolated
  return data

good_rows = range(0, R, N)
o[good_rows] = np.apply_along_axis(interpolate, 1, o[good_rows])
o = np.apply_along_axis(interpolate, 0, o)

# printing output
for i in range(R):
  for j in range(C):
    print(','.join(map(str, map(int, o[i,j,:]))), sep=' ')
  print()
```
