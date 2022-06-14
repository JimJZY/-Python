try:
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except OSError:
    print('文件出错啦!')
