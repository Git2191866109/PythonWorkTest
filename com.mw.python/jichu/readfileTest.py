f = open("E:\mojiworkspace\PythonWorkTest\com.mw.python\jichu\StrsOp2.py")

lines = f.readlines()
alist = []
for line in lines:
    alist.append(line.strip('\n'))

print lines
print alist
