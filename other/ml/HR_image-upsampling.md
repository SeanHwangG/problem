# [HR_image-upsampling](https://www.hackerrank.com/challenges/image-upsampling)

* en

  ```en
  Upsample given image
  ```

* tc

  ```tc
  Input:
  3 3 2
  6 6
  0,0,200 0,0,10 10,0,0
  90,90,50 90,90,10 255,255,255
  100,100,88 80,80,80 15,75,255

  Output:
  0,0,200 0,0,105 0,0,10 5,0,5 10,0,0 10,0,0
  45,45,125 45,45,68 45,45,10 89,86,69 132,128,128 132,128,128
  90,90,50 90,90,30 90,90,10 172,172,132 255,255,255 255,255,255
  95,95,69 90,90,57 85,85,45 110,125,150 135,165,255 135,165,255
  100,100,88 90,90,84 80,80,80 48,78,168 15,75,255 15,75,255
  100,100,88 90,90,84 80,80,80 48,78,168 15,75,255 15,75,255
  ```

## Solution

* py

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
