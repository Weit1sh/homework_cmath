import math
print("Enter the time of year you were born")
year_time = input(">>> ")
print("Enter x")
x = int(input(">>> "))
year_time = year_time.lower ()
if year_time == "winter":
    y = (((math.sin(x) + 23 * x) ** 4) / (math.sqrt(abs(x) ** x - 3)))
    y = round(y, 2)
    print(y)
elif year_time == "spring":
    y = ((2 * math.cos(x) * math.sqrt((888 * (x ** 4) ** 5))) / math.cos (math.pi))
    y = round(y, 2)
    print(y)
elif year_time == "summer":
    y = (((x ** 2) ** math.sqrt(abs(x))) / (math.sin(x) + math.cos(math.pi)))
    y = round(y, 2)
    print(y)
elif year_time == "autumn":
    y = ((math.cos(123 * x) + math.sqrt(4 * abs(x))) / (abs(math.sin(2 ** x) + math.pi)))
    y = round(y, 2)
else:
    print("Sorry, but there is no such time of year")