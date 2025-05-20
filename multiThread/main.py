import threading
import time


def walk_dog(first):
    print(f"Walking the dog... {first}")
    time.sleep(2)
    print("Dog walked!")


def do_laundry():
    print("Doing laundry...")
    time.sleep(3)
    print("Laundry done!")


def cook_dinner():
    print("Cooking dinner...")
    time.sleep(4)
    print("Dinner cooked!")


# walk_dog()
# do_laundry()
# cook_dinner()

# phai de dau' phay de python hieu la tupple
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()
chore2 = threading.Thread(target=do_laundry)
chore2.start()
chore3 = threading.Thread(target=cook_dinner)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("All chores started!")
