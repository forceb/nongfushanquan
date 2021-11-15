# 1. 打开文件到一个文件对象，比如f

f = open('abc.txt')

# 2. 把所有的行都读到一个列表当汇总
lines = f.readlines()

# 3. 用一个循环来遍历每一行
for x in lines:
    print(x)