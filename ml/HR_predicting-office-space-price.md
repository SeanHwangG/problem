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
