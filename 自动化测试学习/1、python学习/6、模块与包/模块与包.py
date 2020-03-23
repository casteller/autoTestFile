class Tiger:#老虎--类
    className = 'tiger'#静态属性---类属性--整个类
    __age = 200
    def __init__(self,weight):#初始化方法--构造方法
        self.weight = weight
    #静态方法
    @staticmethod
    def tell():
        print('我是静态方法！')
    def roar(self):
        self.weight -= 5
        print('wow!')
t1 = Tiger(100)
t2 =Tiger(200)
print(t1.weight)