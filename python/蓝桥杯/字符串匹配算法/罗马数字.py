tab = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
n = int(input())
for _ in range(n):
    string = input()
    chs = [string[0]]
    numbers = [tab[string[0]]]
    num=numbers[0]
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            numbers[-1]=numbers[-1]+tab[string[i]]
            num+=tab[string[i]]
        else:
            chs.append(string[i])
            numbers.append(tab[string[i]])
            if tab[string[i-1]]<tab[string[i]]:
                num+=tab[string[i]]
                num-=2*numbers[-2]
            else:
                num+=tab[string[i]]
    print(num)

