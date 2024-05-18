# la cifra de

## Solution: 

decompile apk using web [decompiler](https://www.decompiler.com)
di file MainActivity ada button 
```java
public void buttonClick(View view) {
     this.text_bottom.setText(FlagstaffHill.getFlag(this.text_input.getText().toString(), this.ctx));
 }
```
dan function getFlag()
```java
 public static String getFlag(String input, Context ctx) {
     if (input.equals(ctx.getString(R.string.password))) {
         return fenugreek(input);
     }
     return "NOPE";
 }
```
R.string.password mengambil dari R.java

```java
public static final int password = 2131427375;
```

untuk password sendiri ada di Resources > resources.arsc > res > values > strings.xml

```xml

<string name="password">opossum</string>
```

maka mendapatkan password opossum di insert ke app one.apk

[file](flag.jpeg)

The flag: `picoCTF{pining.for.the.fjords}`.