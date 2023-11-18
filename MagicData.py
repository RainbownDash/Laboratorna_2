day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if day * month == year:
    print("Це магічна дата")
else:
    print("Це звичайна дата.")