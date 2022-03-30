* in awk ,$i is the i-th column of the line segmented by Field Separator(default " ")
* NF = Number of Fields, how many pieces of the line we got after segmentation
* END tells what to do after previous expression

```sh
awk '
{
  for (i = 1; i <= NF; i++) {
    if(NR == 1) {
      s[i] = $i;
    } else {
      s[i] = s[i] " " $i;
    }
  }
}
END {
  for (i = 1; s[i] != ""; i++) {
    print s[i];
  }
}' file.txt
```