#!/usr/bin/env python3

# -*- coding: utf-8 -*-


import json

frindlist = [{"id":"10000", "name": "xiao ming"},
             {"id": "10001", "name": "xiao li"},
             {"id": "10002", "name": "xiao wang"},
             {"id": "10003", "name": "xiao fang"},
             {"id": "10004", "name": "xiao lan"}]

def login(pr=None):

    a = 0
    print("")
    for friend in frindlist:
        a += 1
        print(a,end=" : ")
        print("id:",friend['id'],"name:",friend['name'],sep="  ")

def help1():
    while True:
        print("请选择好友id(退出请输入exit):")
        uids = input()
        if uids == 'exit':
            exit()

        a = -1
        for friend in frindlist:
            a += 1
            if (uids == friend['id']):
                # print(a)
                return a

        print('无此用户，请重新输入id')

def chosefriend():
    a = help1()
    # print(a)
    uids = frindlist[a]['id']
    # print(uids)
    print('您正在与%s聊天' % frindlist[a]['name'], end="\n\n")
    while True:
        print("聊天记录：")
        news = getnews(uids)
        for new in news:
            print(new, end='')
        print("请输入内容（退出请输入exit)")
        str1 = input()
        if str1 == 'exit':
            break
        putnews(uids, str1)
        print('-' * 50,end='\n\n')



def putnews(uids,str1):
    with open('record%s.txt' % uids, 'a') as f:
        f.write(str1+'\n')


def getnews(uids):
    aa1 = open('record%s.txt' % uids, 'a+')
    aa1.close()
    with open('record%s.txt' % uids, 'r+') as f:
        a = f.readlines()
        return a


username = "admin"
password = "123"

print("欢迎使用QQ")
print("请输入用户名")
while True:
    user = input()
    if user != username:
        print("can not find this username, please try again")
    else:
        while True:
            print("请输入密码")
            pword = input()
            if pword != password:
                print("密码错误，请重新输入")
            else:
                print("欢迎")
                while True:
                    login()
                    chosefriend()











