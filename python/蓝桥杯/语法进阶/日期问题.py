import datetime


def judge(y, m, d):
    if y >= 60:
        y += 1900
    if y < 60:
        y += 2000
    try:
        date = datetime.date(y, m, d)
        return date
    except:
        return


def sortDates(datesList):
    split_up = datesList.split('-')

    return int(split_up[0]), int(split_up[1]), int(split_up[2])


string = input()
numbers = []

number = ""
for ch in string:
    if ch.isdigit():
        number = number + ch
    if ch == "/":
        numbers.append(number)
        number = ""
numbers.append(number)

dates = []
dates.append(judge(int(numbers[0]), int(numbers[1]), int(numbers[2])))
dates.append(judge(int(numbers[2]), int(numbers[0]), int(numbers[1])))
dates.append(judge(int(numbers[2]), int(numbers[1]), int(numbers[0])))
dates = list(set(dates))

final_date = []
for date in dates:
    if date != None:
        final_date.append(str(date))

result = sorted(final_date, key=sortDates)
for date in result:
    print(date)
