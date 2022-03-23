* highlight all the occurrences of 'thy' by wrapping them up in brace brackets

```sh
# & is captured group
sed -e 's/thy/{&}/gi'
```
