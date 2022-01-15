{% tabs %}{% tab title='LC_387.cpp' %}

```cpp
int firstUniqChar(string s) {
  int arr[26] = {0};
  for(int i=0; s[i]; i++)
    arr[s[i]-'a']++;

  for(int i=0; s[i]; i++)
    if(arr[s[i]-'a'] == 1)
      return i;

  return -1;
}
```

{% endtab %}{% tab title='LC_387.py' %}

```py
def firstUniqChar(self, s):
  index=[s.index(l) for l in 'abcdefghijklmnopqrstuvwxyz' if s.count(l) == 1]
  return min(index) if len(index) > 0 else -1
```

{% endtab %}{% endtabs %}
