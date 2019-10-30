x = []
n = int(input("Cate elem are lista"))
i = 0


while (i < n):
    el = int(input("Elementul al " + str(i) + "-ulea: "))
    x.append(el)
    i = i + 1
    
swap = True

while (swap == True):
    i  = 0
    swap = False
    for i in range(n - 1):
        if x[i] > x[i + 1]:
            aux =x[i]
            x[i] = x[i + 1]
            x[i + 1] = aux
            swap = True

print(x)
