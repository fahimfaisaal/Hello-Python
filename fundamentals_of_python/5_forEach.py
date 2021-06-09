numbers = [1, 2, 3, 4, 5]

for value in numbers:
    print(value)

sum_of_value = 0

for value in numbers:
    sum_of_value += value

print("total: " + str(sum_of_value))

# sum with sum function
print(sum(numbers))
