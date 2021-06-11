# Xarg rechive multilple args as a tuple
def addition(*numbers):
    return sum(numbers)

print(addition(1, 2, 5, 10, 2))


# XXarg rechive parameters like dictionary
def get_result(**details):
    return f"Hello {details['name']} {'Congratulation you have passed' if details['result'] else 'you have failed'}"

print(get_result(name="fahim", result=True))