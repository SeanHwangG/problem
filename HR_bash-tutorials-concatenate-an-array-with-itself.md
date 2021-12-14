{% tabs %}{% tab title='HR_bash-tutorials-concatenate-an-array-with-itself.sh' %}

```sh
tr `$'\n' ' ' | awk '{print $`0 `$0 $`0}'
```

{% endtab %}{% endtabs %}
