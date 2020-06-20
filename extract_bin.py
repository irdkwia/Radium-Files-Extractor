import os, sys
from PIL import Image
from common import *

def extract_bin(data):

    width = value(data[2:4])
    height = value(data[4:6])
    tiles = value(data[6:8])

    
    pal_bin = data[-0x200:]
    pal = b''
    for i, b in enumerate(pal_bin):
        if i%2==0:
            t = b
        else:
            t += b*256
            r = t%32
            g = (t>>5)%32
            b = (t>>10)%32
            pal += bytes([r*8, g*8, b*8])
    im = Image.frombytes(mode="P", size=(8, tiles*8), data=data[8:8+tiles*64])
    im.putpalette(pal)

    off = 8+tiles*64
    im_map = Image.new(mode="RGB", size=(width*8, height*8))

    add_val = 0
    for y in range(height):
        for x in range(width):
            tile_val = value(data[off:off+2])+add_val
            # Not sure; maybe it's like some other games where the last bits determine the tile property (horizontal flip, vertical flip)
            tile = im.crop((0, 8*tile_val, 8, 8*tile_val+8))
            im_map.paste(tile, (x*8, y*8))
            if tile_val==0x3ff: # That's odd, after it reaches this value, 
                add_val += 0x400
                print("Reached!")
            off += 2
    return im, im_map

arg = sys.argv
if len(arg)>=3:
    # Path to the source
    src = arg[1]

    # Path to the destination
    dst = arg[2]
    
    with open(src, 'rb') as file:
        data = file.read()
        file.close()
    im, im_map = extract_bin(data)

    im_map.save(dst, "PNG")
else:
    print("Usage: "+arg[0]+" in_file out_file")
