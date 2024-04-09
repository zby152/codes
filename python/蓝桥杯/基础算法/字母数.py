i = 2023
while True:
    flag = 1
    i_hex = hex(i)[2:]
    for ch in i_hex:
        if ch.isdigit():
            flag = 0
            break
    if flag == 1:
        break
    i += 1

print(i)
