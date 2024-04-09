# 这个题只询问了是否有解，并没有询问最小步骤以及解的个数，所以要想一想是否有其他的规律可以直接判断出是否有解

def check(outside, middle, inside):
    for i in range(4):
        numbers = {"G": 0, "R": 0, "Y": 0}
        for n1 in range(i, 12, 4):
            ch = outside[n1]
            numbers[ch] += 1
        for n2 in range(i,8,4):
            ch=middle[n2]
            numbers[ch]+=1
        ch=inside[i]
        numbers[ch]+=1

        if numbers["G"] == 3 and numbers["R"] == 2 and numbers["Y"] == 1:
            continue
        else:
            return False
    return True


T = int(input())

for _ in range(T):
    o = input()
    m = input()
    i = input()
    if check(o, m, i):
        print("YES")
    else:
        print("NO")
