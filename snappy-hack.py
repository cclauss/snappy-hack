#!/usr/bin/env python

import snappy

def out(x):
    print(type(x), len(x), x)

s = 'The quick brown fox jumped over the lazy dog.'
out(s)
compressed = snappy.compress(s)
out(compressed)
try:
    buf = buffer(compressed)
    out(buf)
    buf_d = snappy.decompress(buf)
    out(buf_d)
except NameError:
    print('buffer was removed from Python 3.')
mem = memoryview(compressed)
out(mem)
mem_d = snappy.decompress(mem)
out(mem_d)
