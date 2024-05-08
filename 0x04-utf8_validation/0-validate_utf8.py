#!/usr/bin/python3

def validUTF8(data):
    nbytes = 0
    for i in data:
        if nbytes == 0:
            if i & 0b10000000:
                nbytes += 1
                b = 0b10000000
                while b & i:
                    nbytes += 1
                    b >>= 1
                if nbytes == 1 or nbytes > 4:
                    return False
            continue
        else:
            if not (i & 0b10000000 and not (i & 0b01000000)):
                return False
            nbytes -= 1
    return nbytes == 0

