import os
import json
import csv

file_path = "stuff/test.txt"
file_path_output = "stuff/output.txt"
file_path_json = "stuff/output.json"
file_path_csv = "stuff/output.csv"

txt_data = "hello pizza"

employees = ["John", "Jane", "Doe"]

employee = {
    "name": "Sam",
    "age": 30,
    "job": "developer",
}

employees_csv = [
    ["Name", "Age", "Job"],
    ["John", 25, "developer"],
    ["Jane", 28, "designer"],
    ["Doe", 22, "tester"],
]

if os.path.exists(file_path):
    print(f"{file_path} exists")
    if os.path.isfile(file_path):
        print(f"{file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory")
else:
    print("that location does not exist")


# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# ----------------------------60. w file----------------------------

# >> write (overwrite) file
# with open(file=file_path_output, mode="w") as file:
#     file.write(txt_data)

# >> write but file not exist
# try:
#     with open(file=file_path_output, mode="x") as file:
#         file.write(txt_data)
# except FileExistsError:
#     print(f"{file_path_output} already exists")

# >> append
# try:
#     with open(file=file_path_output, mode="a") as file:
#         for employee in employees:
#             file.write("\n" + employee)
# except FileExistsError:
#     print(f"{file_path_output} already exists")

# >> try:
#     with open(file=file_path_json, mode="w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"{file_path_json} json created")
# except FileExistsError:
#     print(f"{file_path_json} already exists")

try:
    with open(file=file_path_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        for employee in employees_csv:
            writer.writerow(employee)
        print(f"{file_path_csv} json created")
except FileExistsError:
    print(f"{file_path_csv} already exists")
