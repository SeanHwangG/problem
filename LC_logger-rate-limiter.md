{% tabs %}{% tab title='LC_359.cpp' %}

```cpp
class Logger {
 public:
  Logger() {}

  bool shouldPrintMessage(int timestamp, string message) {
    if (timestamp < m[message]) return false;
    m[message] = timestamp + 10;
    return true;
  }

 private:
  unordered_map <string ,int > m;
};
```

{% endtab %}{% endtabs %}
