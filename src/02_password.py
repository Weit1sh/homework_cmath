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
print(z, e, t, h, x, y, q)
