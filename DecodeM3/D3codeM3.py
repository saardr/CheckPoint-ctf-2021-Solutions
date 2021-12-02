#!/usr/bin/env python3

from base64 import b64decode
from binascii import unhexlify
from itertools import cycle

s_b32 = "WFKZLTABVKWVLXGMASVPYVP2ZRTKVHKV6XGBJKVEKX44YCVKXBK4XTBDVKSVL2WMACVLOVPEZQJ2VHCV"

s_hex = "b1 55 95 cc 01 aa ad 55 dc cc 04 aa fc 55 fa cc 66 aa 9d 55 f5 cc 14 aa a4 55 f9 cc 0a aa b8 55 cb cc 23 aa a5 55 ea cc 00 aa b7 55 e4 cc 13 aa 9c 55"

s_hex = s_hex.replace(' ', '')

s_decoded = unhexlify(s_hex)
print(s_decoded)

xor_key = unhexlify("CC55AA")
# xor_key = b"CC55AA"

def byteXor(plaintext, key):
	return bytes(bytearray([b^key for b in plaintext]))

def repeatingKeyXor(plaintext, key):
  return bytes(bytearray([a^b for a,b in zip(plaintext, cycle(key))]))

res = repeatingKeyXor(s_decoded, xor_key)
print(res)
res = res.replace(b'\x00', b'')
print(res)

# '}?TavQ0P3Q_AhS_tavi@U{NFP'

# after rot13 we get:

# }?GniD0C3D_NuF_gniv@H{ASC

# reverse it and replace } & { to get:

# CSA{H@ving_FuN_D3C0DinG?}
