import zlib

s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
print len(s)
print len(t)
print zlib.decompress(t)
print zlib.crc32(s)
