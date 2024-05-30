enemy = [4, 2, 4, 5, 3, 3, 1]
a = max(enemy)
print(a)

enemy.remove(5)
b = max(enemy)
print(b)
enemy.remove(b)

print(enemy)