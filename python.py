x = 0
number = 2360
while number > 0:
    y = number % 10
    number = number // 10
    x = x * 10 + y
    print(x)
