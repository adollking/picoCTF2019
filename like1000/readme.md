#like1000 

This [.tar](1000.tar) file got tarred a lot.


#solution 


```console 
for ((i=1000; i>=1; i--)); do
    7z x "$i.7z" -y
done
```

and get file flag[flag.png](flag.png)





