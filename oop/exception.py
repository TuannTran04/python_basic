try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid input, please enter a number")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed")
