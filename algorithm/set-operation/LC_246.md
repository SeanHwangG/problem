{% tabs %}{% tab title='LC_246.md' %}

* Given a string num which represents an integer, return true if num is a strobogrammatic number.
* strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

```txt
Input: num = "69"
Output: true

Input: num = "88"
Output: true

Input: num = "962"
Output: false

Input: num = "1"
Output: true
```

{% endtab %}{% tab title='LC_246.py' %}

```py
def isStrobogrammatic(self, num):
  return set(map(operator.add, num, num[::-1])) <= {'69', '96', '00', '11', '88'}
```

{% endtab %}{% endtabs %}
