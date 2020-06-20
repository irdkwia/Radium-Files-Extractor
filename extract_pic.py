import os, sys
from PIL import Image
from common import *

def extract_pic(data, pal=None):

    width = value(data[0:2])
    height = value(data[2:4])
    
    if pal==None:
        im = Image.frombytes(mode="L", size=(width, height), data=data[4:])
    else:
        im = Image.frombytes(mode="P", size=(width, height), data=data[4:])
        im.putpalette(pal)
    return im

arg = sys.argv
if len(arg)>=3:
    # Path to the source
    src = arg[1]

    with open(src, 'rb') as file:
        data = file.read()
        file.close()

    if len(arg)>=4:
        # Path to the source pal
        src_pal = arg[2]
        with open(src_pal, 'rb') as file:
            pal = file.read()
            file.close()
            
        # Path to the destination
        dst = arg[3]
    else:
        pal = None
        # Path to the destination
        dst = arg[2]
    
    im = extract_pic(data, pal)

    im.save(dst, "PNG")
else:
    print("Usage: "+arg[0]+" in_file_pic [in_file_act] out_file")

