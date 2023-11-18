
Year = int(input("Введіть рік: "))
y = Year

if y % 10 == 1 and y % 100 != 11 and y != 11 or y % 100 == 1 and y % 100 != 11:
    print(y, " rik")
elif 1 < y % 100 < 5 or 1 < y % 10 < 5 and y % 100 > 14:
    print(y, " roki")
else:
    print(y, " rokiv")