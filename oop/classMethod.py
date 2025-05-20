class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    # INSTANCE METHOD
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"


student1 = Student("Alice", 20)
student2 = Student("Bob", 22)


print(Student.get_count())
