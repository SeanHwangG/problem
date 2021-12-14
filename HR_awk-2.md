{% tabs %}{% tab title='HR_text-processing-awk-2.sh' %}

```sh
awk '{print $1,":", ($2<50||$3<50||$4<50) ? "Fail" : "Pass"}'
```

{% endtab %}{% endtabs %}
