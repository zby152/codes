pownum = []
a = 0
b = 0


def init_pow():
    i = 1
    while i ** 2 < b:
        pownum.append(i ** 2)
        i += 1


def judge(string):
    num = int(string)

    if num in pownum:
        return True
    else:
        return False


(a, b) = map(int, input().split())
init_pow()

for number in pownum:
    if number <= a:
        continue
    number_s = str(number)
    if len(number_s) == 1:
        continue
    for i in range(1, len(number_s)):
        left = ""
        right = ""
        left = number_s[:i]
        right = number_s[i:]
        if judge(number_s) and judge(left) and judge(right):
            print(number)
            break
