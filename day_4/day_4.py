import hashlib


key = 'yzbqklnj'

#Problem 1
i = 1
while True:
    h = hashlib.md5(key)
    h.update(str(i))
    if h.hexdigest()[0:5] == '00000':
        break
    i += 1

print(i)
print(hashlib.md5('%s%d' % (key, i)).hexdigest())


#Problem 2
i = 1
while True:
    h = hashlib.md5(key)
    h.update(str(i))
    if h.hexdigest()[0:5] == '00000':
        break
    i += 1

print(i)
print(hashlib.md5('%s%d' % (key, i)).hexdigest())
