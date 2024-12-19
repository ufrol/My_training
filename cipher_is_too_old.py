import random

a = [n for n in range(0, 20)]
b = random.randint(3, 20)
result = []
for i in range(1, b):
    for j in range(1, b):
        y = b * b
        x = int(a[i] + a[j])
        if y == x:
            break
        if x != 0 and a[i] < a[j] and b % x == 0:
            result.append(a[i])
            result.append(a[j])
        continue
    continue
print(b)
print(''.join(str(el) for el in result))
