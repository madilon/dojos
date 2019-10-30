def sum_of_divs (n):
    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum = sum + i
    return sum
def is_perfect (n):
    if sum_of_divs(n) == n:
        return 1
    else: 
        return 0

list_of_perfect_numbers = []
for i in range (1, 1001):
      if(is_perfect(i) == 1):
          list_of_perfect_numbers.append(i)

print(list_of_perfect_numbers)