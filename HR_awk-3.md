{% tabs %}{% tab title='HR_awk-3.sh' %}

```sh
awk '{avg=($2+$3+$4)/3; print $0, ":", (avg<50)?"FAIL":(avg<80)?"B":"A"}'
```

{% endtab %}{% endtabs %}
