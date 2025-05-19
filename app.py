import time
import random

print("hello world")

# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# -----------------------------------------------------------

price1 = 3000.141556
price2 = -9870.65
price3 = 1200.34
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# -----------------------------------------------------------

# time.sleep(2)
print("time's up")

# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# -----------------------------------------------------------


fruit = ["apple", "banana", "cherry"]
# print(dir(fruit))
# print(help(fruit))
print(len(fruit))
print("pinalty" in fruit)
# fruit.append("orange")
# fruit.remove("banana")
# fruit.insert(1, "kiwi")
# fruit.sort()
# fruit.reverse()
# fruit.clear()

# print(fruit.index("banana"))
# print(fruit.count("banana"))

print(fruit, end=" ")


fruit_sets = {"apple", "banana", "cherry"}
# fruit_sets.add("orange")
# fruit_sets.remove("banana")
# fruit_sets.pop()
# fruit_sets.clear()

fruit_tup = ("apple", "banana", "cherry", "orange")
print("apple" in fruit_tup)
print(fruit_tup.count("apple"))
print(fruit_tup.index("banana"))


# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# ----------------------------DICTIONARY----------------------------

capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
}
# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))
capitals.update({"Spain": "Madrid"})
capitals.update({"USA": "Madridd"})
# capitals.pop("Germany")
# capitals.popitem()  # xoa phan tu cuoi
# capitals.clear()

keys = capitals.keys()
print(keys)
values = capitals.values()
print(values)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")

print(capitals)

# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# ----------------------------RANDOM----------------------------

number = random.randint(1, 10)
number2 = random.random()

print(number)
print(number2)


options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cart = ["1", "2", "3", "4", "5"]
random.shuffle(cart)
print(cart)
