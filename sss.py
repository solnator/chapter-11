def print_pyramid(n):
    if n % 2 == 0 or n < 1 or n > 999:
        print()
        return
    
    for i in range(1, n+1, 2):
        print( '*' * i)


# Input: An odd integer between 1 and 999
n = int(input("Enter odd number between 1 and 999: "))
print_pyramid(n)
