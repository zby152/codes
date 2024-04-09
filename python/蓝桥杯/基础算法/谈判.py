# 使用二分搜索维护一个有序数组，减少时间消耗

res = 0


def insert_c(number):
    global people
    l = 0
    r = len(people) - 1
    while l <= r:
        mid = (l + r) // 2
        if people[mid] < number:
            l = mid + 1
        elif people[mid] > number:
            r = mid - 1
        else:
            l=mid
            break
    if l>len(people)-1:
        people.append(number)
    else:
        people.insert(l, number)


n = int(input())
people = list(map(int, input().split()))

people = sorted(people)
while len(people) > 1:
    a = people.pop(0)
    b = people.pop(0)
    c = a + b
    res = res + c

    insert_c(c)


print(res)
