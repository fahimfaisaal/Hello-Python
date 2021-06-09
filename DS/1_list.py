# List in python
language = ["C", "C++", "Java", "JavaScript", "goLang", "python"]

# access index by number
print(language[0])
print(language[1])

print(language[2:])
print(language[:-2])

# concat any array by + operator
newLists = language + ["Ruby", "php", "Rust"]
print(newLists)

# len function
print(len(language), len(newLists))

# append function
language.append("Haskel")
print(language)

# insert function in python
language.insert(3, "Scala")
print(language)

# remove function in python
language.remove("C")
print(language)

# sort function in python
numbers = [5, 234, 3, 233, -1, -100, 34, 150]

numbers.sort()
print("Ascending order -> ", numbers) # for ascending

numbers.reverse()
print("Descending order -> ", numbers) # for descending

# pop function
print("pop item -> ", language.pop())
print("After pop -> ", language)

# copy list in immutable way
main_list = ["I", "am", "Main list"]
copy_list = main_list.copy()
copy_list[-1] = "Copy list"

print(main_list, copy_list)

# get item position with index function
python_position = language.index("python")
print("python position ->", python_position)

# count function in python get mode
numbers = [1, 2, 3, 4, 5, 1, 1, 1, 2, 3, 2, 1, 4]

number_of_one = numbers.count(1)
number_of_two = numbers.count(2)
number_of_three = numbers.count(3)
number_of_four = numbers.count(4)
number_of_five = numbers.count(5)

print("number of one = ", number_of_one)
print("number of tow = ", number_of_two)
print("number of three = ", number_of_three)
print("number of four = ", number_of_four)
print("number of five = ", number_of_five)

