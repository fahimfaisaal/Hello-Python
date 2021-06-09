# Odd Numbers
odd_number = int(input("Enter your number for Odd: "))

for i in range(0, odd_number + 1):
    if i % 2 != 0:
        print(i)

# Even number
even_number = int(input("Enter your number for even: "))

for i in range(0, even_number + 2):
    if i % 2 == 0:
        print(i)