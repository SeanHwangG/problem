{% tabs %}{% tab title='HR_awk-1.sh' %}

```sh
awk '{if (NF < 4){print "Not all scores are available for "$1}}'
```

{% endtab %}{% endtabs %}
