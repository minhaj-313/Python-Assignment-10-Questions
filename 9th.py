# Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Tuples
person = ("John", 30, "Male")

# Sets
colors = {"red", "green", "blue"}

# Dictionaries
person_info = {
    "name": "John",
    "age": 30,
    "gender": "Male"
}

# Accessing elements
print(fruits[0])      # Output: "apple"
print(person[1])      # Output: 30
print(colors)         # Output: {"red", "green", "blue"}
print(person_info["name"])  # Output: "John"

# Modifying elements
fruits[1] = "orange"
person = ("Jane", 25, "Female")
colors.add("yellow")
person_info["age"] = 35

# Iterating through collections
for fruit in fruits:
    print(fruit)
    
for number in numbers:
    print(number)
    
for color in colors:
    print(color)
    
for key, value in person_info.items():
    print(key, value)
