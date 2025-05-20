import json
import csv

file_path = "stuff/test.txt"
file_path_output = "stuff/output.txt"
file_path_json = "stuff/output.json"
file_path_csv = "stuff/output.csv"


try:
    with open(file=file_path, mode="r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission denied")

try:
    with open(file=file_path_json, mode="r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission denied")

try:
    with open(file=file_path_csv, mode="r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)
            print()
            print(row[0])

except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission denied")
