# 状态压缩动态规划问题
# 对于仅有两个状态的格子问题，可以将分行考虑，将每一行的数据转换成二进制的格式进行处理
# 动态规划的点在于每次考虑当前行时需要保存前两行的状态进行判断，将前面每一行可以出现的次数累加到现在的行上面

suitrow = []


def find_one_col():
    global total
    for i in range(total):
        i_bit = bin(i)[2:].split("0")
        flag = 1
        for s in i_bit:
            if len(s) >= 3:
                flag = 0
        if flag == 1:
            suitrow.append(i)
    return True


(n, m) = map(int, input().split())
total = 2 ** m

find_one_col()
num=len(suitrow)

if n == 1:
    print(num)
else:
    pair = [[0 for _ in range(total)] for _ in range(total)]
    now = [[0 for _ in range(total)] for _ in range(total)]
    for row1 in suitrow:
        for row2 in suitrow:
            pair[row2][row1]=1
    for i in range(2,n):
        for row1 in suitrow:
            for row2 in suitrow:
                for row3 in suitrow:
                    if row1 & row2 & row3==0:
                        now[row3][row2]+=pair[row2][row1]

        pair=now
        now=[[0 for _ in range(total)]for _ in range(total)]

    number=0
    for i in range(total):
        number+=sum(pair[i])
    print(number)
