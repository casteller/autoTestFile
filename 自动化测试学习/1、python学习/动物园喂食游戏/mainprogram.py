from random import randint
from tiger import Tiger
from sheep import Sheep
from room import Room
import time
print("*********游戏开始*********")
#循环创建实例--10个房间实例--游戏初始化操作
roomList = []
for one in range(0,10):#左含右不含  0----9
    #随机取动物
    if randint(0,1) == 1:#老虎
        ani = Tiger()
    else:#羊
        ani = Sheep()
    room = Room(one,ani)#创建实例
    roomList.append(room)

startTime = time.time()

while True:
    endTime = time.time()
    if endTime - startTime > 10:
        print("*********游戏结束*********")
        for roomNo, room in enumerate(roomList):
            print("房间号:%s  房间里的动物是:%s  动物的体重是:%s" % (roomNo+1, room.animal.classname, room.animal.weight))
        break
    roomNum = randint(0, 9)
    room = roomList[roomNum]
    print("当前房间号：%s,请选择敲门(k)/还是喂食(f)？" % (room.num+1))
    while True:
        userInput = input("您的选择：")

        if userInput == "k":
            room.animal.roar()
            print("当前房间的动物体重减5斤，目前体重：%s" %(room.animal.weight))
            while True:
                food = input('请给房间里面的动物喂食:')
                if food == "m" or food == "g":
                    room.animal.feed(food)
                    break
                else:
                    print("输入错误，只能输入m或者g")
            break
        elif userInput == "f":
            while True:
                food = input('请给房间里面的动物喂食:')
                if food == "m" or food == "g":
                    room.animal.feed(food)
                    break
                else:
                    print("输入错误，只能输入m或者g")
            break
        else:
            print("输入有误，只能输入k或者f")










