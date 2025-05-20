# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# ----------------------------FUNCTION----------------------------


def test(param1, param2="default"):
    print(f"test {param1}, {param2}")
    return 1


test("hello")
test(param2="hello", param1="world")
print("1", "2", "3", "4", sep="|")


def add(*args):
    total = 0
    print(type(args))  # tupple
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4, 5))


def print_address(**kwargs):
    print(type(kwargs))  # dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(name="John", age=30, city="New York")

print(" -----------------------------shipping_label------------------------------")


def shipping_label(*args, **kwargs):

    for arg in args:
        print(arg, end=" / ")
    print(">>>")
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" - ")
        print(" >>")
        print(f"{kwargs.get('city')}")


shipping_label("John", "Doe", city="New York", state="NY", zip="10001")


# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# ----------------------------37.list comprehensions----------------------------

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

doubles_2 = [x * 2 for x in range(1, 11)]
print(doubles_2)

fruits_cpmps = ["apple", "banana", "cherry"]
fruits_comp = [fruit.upper() for fruit in fruits_cpmps]
print(fruits_comp)

fruits_chars = [fruit[0] for fruit in fruits_cpmps]
print(fruits_chars)

numbers_1 = [1, -2, 3, -4, 5, -6]
positve_numbers = [num for num in numbers_1 if num >= 0]
negative_numbers = [num for num in numbers_1 if num < 0]
print(positve_numbers)

# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# ----------------------------38.match-case statements----------------------------


def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6 | 7:
            return "Weekend"
        case _:
            return "Invalid day"


print(day_of_week(1))
