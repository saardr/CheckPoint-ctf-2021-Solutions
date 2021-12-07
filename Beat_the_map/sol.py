#!/usr/bin/env python3
from PIL import Image
from math import inf

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
        
def decipher_extracted_bytes(lst):
    pass

def extract_lsbits_from_image(image_path):
    pixel_lst = get_pixel_list(image_path)
    lsbits = extract_lsbits_from_num_list(pixel_lst)
    return lsbits

def get_triangular_lsbits_from_image(image_path):
    """I am almost certain this is the correct approach.
    the issue is a can't find out what to do next. see notes.txt"""
    lsbits = extract_lsbits_from_image(image_path)
    triangular_lsbits = get_triangular_sublist(lsbits)
    return triangular_lsbits


IMAGE_PATH = "source/challenge.bmp" 


def main():
    triangular_lsbits = get_triangular_lsbits_from_image(IMAGE_PATH)
    # dat_s = "".join(map(str, triangular_lsbits))
    extracted_bytes = bitlist_to_byte_list(triangular_lsbits, 7)
    dat_s = str(extracted_bytes)
    log("notes.txt", dat_s)
    # open("res.bin", "wb").write(bytes(extracted_bytes))



def log(file, text):
    with open(file, "a") as f:
        f.write("\n" + "-"*80 + '\n')
        f.write(text)
        f.write('\n' + '-'*80 + '\n')
    


if __name__ == "__main__":
    main()
