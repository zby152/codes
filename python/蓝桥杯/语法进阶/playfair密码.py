fair = input()
stego = input()
count = 1
maps = [["" for _ in range(5)] for _ in range(5)]
full = 0


def map_append(x):
    global count, maps, full
    i = count // 5
    if count // 5 == count / 5:
        i -= 1
    j = count % 5 - 1
    maps[i][j] = x
    count += 1
    if count == 26:
        full = 1


def find_str(letter):
    global maps
    for i in range(5):
        for j in range(5):
            if maps[i][j] == letter:
                return i, j


def ifin(letter):
    for maps_row in maps:
        if letter in maps_row:
            return True
    return False


# fair="youandme"
# stego="welcometohangzhou"
result = ""
tb = [chr(x) for x in range(97, 123)]

for key in fair:
    map_append(key)
    if full == 1:
        break

for letter in tb:
    if full == 0 and (letter not in fair):
        map_append(letter)

for point1 in range(0, len(stego), 2):
    if point1 == len(stego) - 1:
        result = result + stego[point1]
        continue

    str1 = stego[point1]
    str2 = stego[point1 + 1]
    if str1 == str2:
        result = result + str1 + str2
        continue
    if (not ifin(str1)) or (not ifin(str2)):
        result = result + str1 + str2
        continue

    (x1, y1) = find_str(str1)
    (x2, y2) = find_str(str2)
    if x1 == x2 or y1 == y2:
        result = result + str2 + str1
        continue

    str3 = maps[x1][y2]
    str4 = maps[x2][y1]
    result = result + str3 + str4

print(result)
