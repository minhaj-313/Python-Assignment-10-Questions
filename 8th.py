try:
    # ask user to input two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # divide the first number by the second number
    result = num1 / num2
    
    # print the result
    print("The result is:", result)

# handle exceptions that may occur
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
except Exception as e:
    print("An error occurred:", e)
    
finally:
    print("Program completed.")
