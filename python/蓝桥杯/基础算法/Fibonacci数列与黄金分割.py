# 在数据量很庞大的时候需要考虑节省内存

N=int(input())
f=[0,1,1]


if N>200000000:
    print(0.61803399)
else:
    for i in range(3,N+2):
        f.append(f[-1]+f[-2])
        f.pop(0)
        print(f[-1])
    print(format(f[-2]/f[-1],".8f"))
