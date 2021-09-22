{% tabs %}{% tab title='HR_bash-tutorials-filter-an-array-with-patterns.md' %}

* Given list of countries, each on new line. Read them into an array and then filter out names containing 'a' or 'A'

```txt
Input:
Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
NorthKorea
Norway

Output: Niger
```

{% endtab %}{% tab title='HR_bash-tutorials-filter-an-array-with-patterns.py' %}

```sh
grep -vi 'a' || printf "\n"
```

{% endtab %}{% endtabs %}
