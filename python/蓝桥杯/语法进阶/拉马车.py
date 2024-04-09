# 双向队列
from collections import deque

A = []
B = []
desk = deque([])


def judge():
    global A, B, desk
    ch = desk.pop()
    if ch in desk:
        desk.append(ch)
        return True
    else:
        desk.append(ch)
        return False


def roundA():
    global A, B, desk
    flag = 0

    x = A.popleft()
    desk.append(x)
    if judge():
        temp = desk.pop()
        A.append(temp)
        temp = desk.pop()
        while temp != x:
            A.append(temp)
            temp = desk.pop()
        A.append(temp)
        flag = 1
    return flag


def roundB():
    global A, B, desk
    flag = 0

    x = B.popleft()
    desk.append(x)
    if judge():
        temp = desk.pop()
        B.append(temp)
        temp = desk.pop()
        while temp != x:
            B.append(temp)
            temp = desk.pop()
        B.append(temp)
        flag = 1
    return flag


A = deque(input())
B = deque(input())

# A=deque(["K","8","X","K","A","2","A","9","5","A"])
# B=deque(["2","7","K","5","J","5","Q","6","K","4"])


while len(A) > 0 and len(B) > 0:
    flag_A = 1
    flag_B = 1
    while flag_A == 1:
        flag_A = roundA()
    while flag_B == 1 and len(A) > 0:
        flag_B = roundB()

if len(A) == 0:
    print("".join(B))
else:
    print("".join(A))
