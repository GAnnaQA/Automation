def bank(x, y):
    for i in range(y):
        x = x * 1.10
    return x

result = bank(10000, 4)
print(result)
