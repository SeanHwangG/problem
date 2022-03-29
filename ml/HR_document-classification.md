```py
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer
transformer = HashingVectorizer(stop_words='english')

trains, labels = [], []
with open('trainingdata.txt') as f:
  for i in range(int(f.readline())):
    s = f.readline().rstrip()
    idx = s.find(' ')
    trains.append(s[idx+1:])
    labels.append(int(s[:idx]))
train = transformer.fit_transform(trains)
svm = LinearSVC()
svm.fit(train, labels)
_test = []
for i in range(int(input())):
  s = input().rstrip()
  _test.append(s)
test = transformer.transform(_test)
print(*svm.predict(test), sep='\n')
```
