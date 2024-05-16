import struct 

integers = [ 1096770097 ,1952395366 ,1600270708 ,
        1601398833 ,1716808014 ,1734291511 ,960049251 ,1681089078
]

def int_to_chars(n):
    return struct.pack("<I", n)

flag = ''.join(int_to_chars(x).decode('ascii') for x in integers)
print(flag)