# plumbing 


## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

## solution 

```console
(root㉿DESKTOP)-[picoCTF_2019/plumbing]
└─# nc jupiter.challenges.picoctf.org 7480 | grep pico
picoCTF{digital_plumb3r_06e9d954}
```