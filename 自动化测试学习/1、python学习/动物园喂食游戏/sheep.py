class Sheep(object):
    classname = "羊"

    def __init__(self, weight=100):
        self.weight = weight

    def roar(self):
        self.weight -= 5
        print('mie!')
    def feed(self, food):
        if food == 'g':
            self.weight += 10
            print('喂食正确，体重加10斤,目前体重：%s' % (self.weight))
        else:
            self.weight -= 10
            print('喂食错误，体重减10斤,目前体重：%s' % (self.weight))
