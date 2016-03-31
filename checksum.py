from checksumdir import dirhash

if __name__ == '__main__':
    line = "hash(./test) = <{}>".format(dirhash('test', 'sha1'))
    print (line)
