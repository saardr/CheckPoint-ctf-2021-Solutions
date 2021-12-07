#!/usr/bin/env python3
import string
from PIL import Image
from math import inf

IMAGE_PATH = "source/challenge.bmp" 
FLAG_START = "CSA{"

bin2b64_dict = {i : c for i, c in enumerate(
    string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
)}

bin2b32_dict = {i : c for i, c in enumerate(
    string.ascii_uppercase + '234567'
)}

def get_pixel_list(image_path):
    return list(Image.open(image_path).getdata())

def triangular_series_generator(start = 0, limit = inf):
    n = start
    while n*(n+1)//2 < limit:
        yield n*(n+1)//2
        n += 1

def get_triangular_sublist(lst):
    triangular_sublist = []
    for n in triangular_series_generator(0, len(lst)):
        triangular_sublist.append(lst[n])
    return triangular_sublist

def extract_lsbits_from_num_list(lst): # grayscale image is a 0-255 numbers list
    return [num & 1 for num in lst]

def bitlist_to_byte_list(bitlist, bits_per_byte = 8):
    byte_list = []
    for i in range(0, len(bitlist), bits_per_byte):
        current_bits = bitlist[i:i+bits_per_byte]
        byte = 0
        power_of_two = 1
        for bit in reversed(current_bits):
            byte += power_of_two*bit
            power_of_two *= 2
        byte_list.append(byte)
    return byte_list
        

def extract_lsbits_from_image(image_path):
    pixel_lst = get_pixel_list(image_path)
    lsbits = extract_lsbits_from_num_list(pixel_lst)
    return lsbits

def get_triangular_lsbits_from_image(image_path):
    """I am almost certain this is the correct approach.
    the issue is a can't find out what to do next. see notes.txt"""
    lsbits = extract_lsbits_from_image(image_path)
    return get_triangular_sublist(lsbits)


def get_divider_pairs(num):
    return [(i, num // i) for i in filter(lambda k: num % k == 0, range(1, num))]

def decipher_bytes(triangular_bytes):
    for n,size in enumerate(get_divider_pairs(len(triangular_bytes))):
        im = Image.frombytes('L', size, bytes(triangular_bytes))
        im.save(f"img{n}.bmp")


def decipher_bitlist(bitlist):
    """takes in the triangular lsbits and deciphers the flag from them"""


def main():
    triangular_lsbits = get_triangular_lsbits_from_image(IMAGE_PATH)
    result = decipher_bitlist(triangular_lsbits)



    # lsbits = extract_lsbits_from_image(IMAGE_PATH)
    # extracted_bytes = bitlist_to_byte_list(lsbits)
    # triangular_bytes = get_triangular_sublist(extracted_bytes)
    # decipher_bytes(triangular_bytes)



def log(file, text):
    with open(file, "a") as f:
        f.write("\n" + "-"*80 + '\n')
        f.write(text)
        f.write('\n' + '-'*80 + '\n')
    


if __name__ == "__main__":
    main()
