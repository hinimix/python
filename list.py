#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/4/14 下午8:31
# @Author : hinimix
# @File : list.py
# @Software: PyCharm

import copy

# 定义链表结构
class LIST:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


# 遍历链表
def showList(l):
    while 1:
        if l.next != None:
            print(l.data)
            l = l.next
        else:
            print(l.data)
            break


# 生成链表
def generateList(l):
    for i in range(0, 10):
        insertList(l, LIST(i))


# 插入链表首部
def insertList(l, value):
    postNode = l.next
    l.next = value
    value.next = postNode


# 插入链表尾部
def appendList(l, value):
    # tmpList = copy.copy(l)
    # while 1:
    #     if tmpList.next is not None:
    #         tmpList = tmpList.next
    #     else:
    #         break
    # tmpList.next = value
    while 1:
        if l.next != None:
            l = l.next
        else:
            break
    l.next = value


# 求链表长度
def getLengthList(l):
    count = 0
    while 1:
        if l.next != None:
            count += 1
            l = l.next
        else:
            break
    return count


# 单链表反转
def reverseList(l):
    result = LIST(1)
    while 1:
        tmp_node = LIST(1)
        if l.next != None:
            l = l.next
            tmp_node.data = l.data
            tmp_node.next = None
            insertList(result, tmp_node)
        else:
            break
    return result


# 链表中环的检测
def loopCheckList(l):
    nextSet = list()
    while 1:
        if l.next != None:
            l = l.next
            if l in nextSet:
                return True
            else:
                nextSet.append(l)
        else:
            break
    return False


# 两个有序的链表合并
def mergeList(l1, l2):

    # tmpNode=copy.deepcopy(l2)
    # while 1:
    #     if tmpNode.next != None:
    #         tmpNode = tmpNode.next
    #         appendList(l1,tmpNode)
    #         break
    #     else:
    #         break
    while 1:
        if l2.next != None:
            l2 = l2.next
            appendList(l1,l2)
            break
        else:
            break


# 删除链表倒数第 n 个结点
def deleteNNode(l, n):
    realDeleteNo = 0
    if n>=0:
        realDeleteNo = n
    else:
        realDeleteNo = getLengthList(l) + n

    for i in range(0,realDeleteNo):
        if l.next != None:
            l = l.next
        else:
            break
    postNode = l.next
    postNode = postNode.next
    l.next = postNode


# 求链表的中间结点
def getMiddleNode(l):
    lengh = getLengthList(l)
    middle = int(lengh/2 + lengh%2)

    for i in range(0,middle):
        l = l.next

    print("middle node index is: ", middle)
    print("middle node value", l.data)


if __name__ == '__main__':
    t1 = LIST(1)

    t2 = LIST(100)
    insertList(t1, t2)
    generateList(t1)
    # showList(t1)
    # # generateList()
    # l1 = getLengthList(t1)
    # # print(l1)
    # print("-----")
    t4 = reverseList(t1)
    # showList(t4)
    # t5 = loopCheckList(t4)
    # print(t5)
    # t6 = LIST(1)
    # t7 = LIST(2)

    # t8 = LIST(3)
    # t6.next = t7
    # t7.next = t8
    # t8.next = t6
    # t9 = loopCheckList(t6)
    # print(t9)
    # t10 = mergeList(t1, t4)
    # showList(t10)
    # t11 = LIST(111)
    # appendList(t1,t11)
    # mergeList(t1,t4)

    # deleteNNode(t1, -1)
    # showList(t1)
    # getMiddleNode(t1)
    # t12 = LIST(543)
    # appendList(t1,t12)
    # showList(t1)
    mergeList(t1,t4)
    showList(t1)

