```py
x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

first = x["Red"] * y["Red"] * z["Black"]
second = x["Red"] * y["Black"] * z["Red"]
third = x["Black"] * y["Red"] * z["Red"]

print(first + second + third)
```
