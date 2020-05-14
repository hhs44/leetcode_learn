"""
用户管理系统
用户类User:

       属性:用户uid,  用户名name, 密码passwd
管理系统类Manager:【不用考虑数据持久化存储的问题】

        使用列表保存所有用户的信息
        方法有

               1.添加用户

                       注册用户时要求:

                            用户uid 在10000到99999中随机产生,并且要求id不能重复

                            用户名用正则表达式验证规则:必须以字母或者下划线开头,不能包含!@#$%^&*~这些特殊字符,用户名长度为3到12位

                            密码用正则表达式验证规则:必须以大写字母开头,可包含!@#$^&*中的特殊字符,其他的均为数字字母或者下划线,长度为6到12位

               2.按照用户id对用户进行降序排序

               3.根据用户id删除用户
"""
import re
import random

users = []
uids = []


class User():

    def __init__(self):
        self.uid = ""
        self.name = ""
        self.passwd = ""


class Manager():
    def adduser(self):
        user = User()
        username = input("请输入用户名：\n")
        username_check = re.compile('^[a-zA-Z_][a-zA-Z0-9]{3,12}')
        while username_check.match(username) == None:
            username = input("用户名格式错误，请重新输入用户名：\n")
        passwd = input("请输你的密码：\n")
        passwd_check = re.compile('^[A-Z][a-zA-Z0-9!@#$^&*_]{6,12}')
        while passwd_check.match(passwd) == None:
            passwd = input("密码格式错误，请重新输入密码：\n")
        uid = random.randint(10000, 99999)
        while uid in uids:
            uid = random.randint(10000, 99999)
        user.uid = uid
        user.name = username
        user.passwd = passwd
        uids.append(uid)
        users.append(user)

    def orderbyuid(self):
        uids.sort()
        users.sort(key=lambda x: x.uid, reverse=False)
        print(uids)

    def deluser(self):
        uid = input("请输入要删除的用户id：")
        while uid not in uids:
            uid = input("用户id不存在，请重新输入：")
        del_uer = users.pop(uids.index(uid))
        print("uid:{},name{}".format(del_uer.uid, del_uer.name))


manager = Manager()
while True:
    print("####欢迎使用用户管理系统#####")
    print("1.添加新用户")
    print("2.用户排序")
    print("3.删除用户")
    print("##########################")
    num = input("请输入你的操作")
    if num == "1":
        manager.adduser()
    elif num == "2":
        manager.orderbyuid()
    elif num == "3":
        manager.deluser()
    else:
        print("没有该操作")
