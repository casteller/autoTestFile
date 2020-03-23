# coding=utf-8
with open(r'C:\Users\Administrator\Desktop\user.txt','r')as f:
    users = f.readlines()
    for user in users:
        print(user.split(',')[2].split('"')[1])