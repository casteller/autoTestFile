def getName(srcStr):
    return srcStr.split('the name is ')
a = getName("A girl come in, the name is Jack, level 955;")
b = getName("A old lady come in, the name is Mary, level 94454;")
c = getName("A pretty boy come in, the name is Patrick, level 194;")
print(a,b,c)