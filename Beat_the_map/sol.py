#!/usr/bin/env python3
from functools import reduce
from PIL import Image

def get_triang_nums(max_range):
    triang_nums = [0]
    num = 1
    while triang_nums[-1]+num < max_range:
        triang_nums.append(triang_nums[-1]+num)
        num += 1
    return triang_nums

def main():
    im = Image.open("challenge.bmp")
    width, height = im.size

    triang_nums = get_triang_nums(width*height)
    pixels = list(im.getdata())

    triang_pixels = [pixels[index] for index in triang_nums]
    triang_lsbits = list(map(lambda x: x&1, triang_pixels))

    print(f"there are {len(triang_lsbits)} extracted bits")
    print(f"the first 64 bits are: " + reduce(lambda a, b: str(a) + str(b), triang_lsbits[:64]))
    
    byte_list = bytearray() 
    for i in range(0, len(triang_lsbits), 8):
        byte_list.append((int(reduce(lambda a, b: str(a) + str(b), triang_lsbits[i:i+8]), 2)))

    print(f"bytes: {bytes(byte_list)}")
    open("log.bmp", "wb").write(byte_list)

if __name__ == "__main__":
    main()