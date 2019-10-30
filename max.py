numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
n = len(numbers)
max = min = numbers[0]
i = 1
while i < n:
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]
    i = i + 1 
print(max,min)

sum = 0
for num in numbers:
    sum = sum + int(num)
print(sum/n)