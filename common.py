def value(byte_lst):
    n = 0
    for i, b in enumerate(byte_lst):
        n += b * (256**i)
    return n
