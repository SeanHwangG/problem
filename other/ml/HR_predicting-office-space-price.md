# [HR_predicting-office-space-price](https://www.hackerrank.com/challenges/predicting-office-space-price)

The prices per square foot, are (approximately) a polynomial function of the features in the observation table
This polynomial always has an order less than 4

```txt
Input:
2 100
0.44 0.68 511.14
0.99 0.23 717.1
0.84 0.29 607.91
0.28 0.45 270.4
0.07 0.83 289.88
0.66 0.8 830.85
0.73 0.92 1038.09
0.57 0.43 455.19
0.43 0.89 640.17
0.27 0.95 511.06
Output:
4
0.05 0.54
0.91 0.91
0.31 0.76
0.51 0.31
180.38
1312.07
440.13
343.72
```

## Solution

* py

  ```py
  from sklearn.linear_model import LinearRegression
  from sklearn.preprocessing import PolynomialFeatures
  import numpy as np

  F, N = map(int, input().split())
  featuresList, targets = [], []
  for _ in range(N):
    fields = list(map(float, input().split()))
    featuresList.append(fields[:-1])
    targets.append(fields[-1])

  poly = PolynomialFeatures(degree=3)

  regression = LinearRegression()
  regression.fit(poly.fit_transform(np.array(featuresList)), targets)

  for _ in range(int(input())):
    features = np.array(list(map(float, input().split()))).reshape(1, -1)
    fit = poly.fit_transform(features)
    print(regression.predict(fit)[0])
  ```
