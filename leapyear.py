# Virginia Link
# CS 362
# 03/05/2021

def calc(num):
    year = int(num)
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

# year = input("Please enter a year")
#
# result = calc(year)
# if result:
#     print("Yes!")
# else:
#     print("No :(")
