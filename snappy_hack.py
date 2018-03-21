#!/usr/bin/env python

import snappy

fmt = '{:>9} {:14} {} {}'

def out(name, x):
    print(fmt.format(name, type(x), len(x), x))

s = 'The quick brown fox jumped over the lazy dog.'
out('s', s)
compressed = snappy.compress(s)
out('compressed', compressed)
try:
    buf = buffer(compressed)
    out('buf', buf)
    buf_d = snappy.decompress(buf)
    out('buf_d', buf_d)
except NameError:
    print('buffer was removed from Python 3.')
mem = memoryview(compressed)
out('mem', mem)
mem_d = snappy.decompress(mem)  # <-- TypeError: argument 1 must be string or read-only buffer, not memoryview
out('mem_d', mem_d)
