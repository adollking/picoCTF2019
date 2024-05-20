#c0rrupt

##solution
we saw corupt header in png
```console
 xxd -g 1 mystery | head
00000000: 89 65 4e 34 0d 0a b0 aa 00 00 00 0d 43 22 44 52  .eN4........C"DR
00000010: 00 00 06 6a 00 00 04 47 08 02 00 00 00 7c 8b ab  ...j...G.....|..
00000020: 78 00 00 00 01 73 52 47 42 00 ae ce 1c e9 00 00  x....sRGB.......
00000030: 00 04 67 41 4d 41 00 00 b1 8f 0b fc 61 05 00 00  ..gAMA......a...
00000040: 00 09 70 48 59 73 aa 00 16 25 00 00 16 25 01 49  ..pHYs...%...%.I
00000050: 52 24 f0 aa aa ff a5 ab 44 45 54 78 5e ec bd 3f  R$......DETx^..?
00000060: 8e 64 cd 71 bd 2d 8b 20 20 80 90 41 83 02 08 d0  .d.q.-.  ..A....
00000070: f9 ed 40 a0 f3 6e 40 7b 90 23 8f 1e d7 20 8b 3e  ..@..n@{.#... .>
00000080: b7 c1 0d 70 03 74 b5 03 ae 41 6b f8 be a8 fb dc  ...p.t...Ak.....
00000090: 3e 7d 2a 22 33 6f de 5b 55 dd 3d 3d f9 20 91 88  >}*"3o.[U.==. .

```
change header using hexedit to 
```console
cp mystery fixed.png

hexedit fixed.png

00000000   89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  00 00 06 6A  00 00 04 47  .PNG........IHDR...j...G
00000018   08 02 00 00  00 7C 8B AB  78 00 00 00  01 73 52 47  42 00 AE CE  1C E9 00 00  .....|..x....sRGB.......
00000030   00 04 67 41  4D 41 00 00  B1 8F 0B FC  61 05 00 00  00 09 70 48  59 73 AA 00  ..gAMA......a.....pHYs..
00000048   16 25 00 00  16 25 01 49  52 24 F0 AA  AA FF A5 AB  44 45 54 78  5E EC BD 3F  .%...%.IR$......DETx^..
```

and its still corupt 
lets check using pngcheck

```console 
pngcheck -v fixed.png

File: fixed.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in fixed.png

```
chunk pHY to large change aa to 00

```console 

00000030: 00 04 67 41 4d 41 00 00 b1 8f 0b fc 61 05 00 00  ..gAMA......a...
00000040: 00 09 70 48 59 73 aa 00 16 25 00 00 16 25 01 49  ..pHYs...%...%.I

```
lets check again using pngcheck

```console 
 pngcheck -v fixed.png

File: fixed.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in fixed.png
```
The invalid chunk length (too large) error does not specify a chunk, must begin at the start and check each chunk, withthe format of chunks and each field’s length: 4 bytes (length) - 4 bytes (chunk type) - lengthbytes (data) - 4 bytes (CRC).


change 
```console 
00000050: 52 24 f0 aa aa ff a5 ab 44 45 54 78 5e ec bd 3f  R$......DETx^..?


```
to 

```console
00000050: 52 24 f0 aa aa ff a5 49 44 41 54 78 5e ec bd 3f  R$.....IDATx^..?
```
and get flag picoCTF{c0rrupt10n_1847995}