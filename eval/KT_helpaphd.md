```py
n_test = int(input())
for _ in range(n_test):
  line = input()
  if line == 'P=NP':
    print('skipped')
  else:
    print(eval(line))
```