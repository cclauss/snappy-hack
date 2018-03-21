#!/usr/bin/env python
# coding=utf-8

"""
$ python snappy_hack.py

s          <type 'str'>        45 The quick brown fox jumped over the lazy dog.
compressed <type 'str'>        47 -�The quick brown fox jumped over the lazy dog.
buf        <type 'buffer'>     47 -�The quick brown fox jumped over the lazy dog.
buf_d      <type 'str'>        45 The quick brown fox jumped over the lazy dog.
mem        <type 'memoryview'> 47 <memory at 0x7ffa61147478>
Traceback (most recent call last):
  File "snappy_hack.py", line 23, in <module>
    mem_d = snappy.decompress(mem)  # <-- TypeError: argument 1 must be string or read-only buffer, not memoryview
  File "/home/travis/virtualenv/python2.7.14/lib/python2.7/site-packages/snappy/snappy.py", line 91, in uncompress
    return _uncompress(data)
TypeError: argument 1 must be string or read-only buffer, not memoryview
"""

import six
import snappy

fmt = '{:10} {:19} {} {}'

def out(name, x):
    print(fmt.format(name, str(type(x)), len(x), x))

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
mem_bin_d = snappy.decompress(six.binary_type(mem))
out('mem_bin_d', mem_bin_d)
mem_d = snappy.decompress(mem)  # <-- TypeError: argument 1 must be string or read-only buffer, not memoryview
out('mem_d', mem_d)
