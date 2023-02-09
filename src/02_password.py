import random

alphabet = "abcdefghigklmnopqrstuvwxyz"
alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = random.randint(0, 9)
y = random.randint(0, 9)
q = random.randint(0, 9)
z = random.choice(alphabet)
e = random.choice(alphabet)
t = random.choice(alphabet_big)
h = random.choice(alphabet_big)
all = (z + e + t + h + str(x + y + q))
print(all)
