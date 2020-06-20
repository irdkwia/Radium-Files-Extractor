import os, sys
from common import *

def decompress_kfs(data):
    if data[0:4]!=b"KFS!":
        raise Exception("Not a valid KFS file!")

    off_base = value(data[4:8])
    off = off_base
    len_file_table = value(data[8:12])

    lst_files = []
    while off<off_base+len_file_table:
        len_entry = value(data[off:off+2])
        if len_entry==0:
            break
        off += 2
        len_file = value(data[off+len_entry-4:off+len_entry])
        off_file = value(data[off+len_entry-8:off+len_entry-4])
        off_str = 0
        while data[off+off_str]!=0:
            off_str += 1
        file_name = data[off:off+off_str].decode(encoding="ascii")
        file_data = data[off_file:off_file+len_file]
        lst_files.append((file_name, file_data))
        off += len_entry
    return lst_files

arg = sys.argv
if len(arg)>=3:
    # Path to the source
    src = arg[1]

    # Path to the destination
    dst = arg[2]

    with open(src, 'rb') as file:
        data = file.read()
        file.close()
    lst_files = decompress_kfs(data)

    path = dst
    os.makedirs(path, exist_ok=True)

    for i in lst_files:
        dir_name = os.path.dirname(i[0])
        if dir_name!="":
            os.makedirs(path+os.path.sep+dir_name, exist_ok=True)
        with open(path+os.path.sep+i[0], 'wb') as file:
            file.write(i[1])
            file.close()
else:
    print("Usage: "+arg[0]+" in_file out_dir")
