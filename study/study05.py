import random
a0 = 0
a1 = 0
z = ""
for x in range(100):
    y = random.randint(0b0, 0b1)
    print(y)
    z += str(y)
    print(z)
    if y == 0 :
        a0 += 1
    elif y != 0:
        a1 += 1

print(a0)
print(a1)
print(int(z))

