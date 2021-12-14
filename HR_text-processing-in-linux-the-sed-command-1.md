{% tabs %}{% tab title='HR_text-processing-sed-1.sh' %}

```sh
# \< and > in regex world (sed syntax) represents words boundaries
sed -e 's/\<the\>/this/'
```

{% endtab %}{% endtabs %}
