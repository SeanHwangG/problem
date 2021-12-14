{% tabs %}{% tab title='HR_awk-4.sh' %}

```sh
awk 'ORS=NR%2?";":"\n"'
```

{% endtab %}{% endtabs %}
