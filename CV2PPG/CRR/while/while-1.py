n = 15
i = 2
c = 0
while i < 15:
    if n % 2:
        print(i)
        c = c + i
    n = n + 1
    i=i+1
print(c)