#1
students = ["Rahul", "Amit", "Karan", "Riya", "Neha"]

name = input("Enter student name: ")

if name in students:
    print("Name exists in the list")
else:
    print("Name does not exist")
    
    
#2
numbers = [10, 15, 22, 31, 40, 47]

for number in numbers:
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")
        
        
#3
marks = (65, 32, 78, 45, 25)

for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
    else:
        print(mark, "Fail")
        
        
#4
numbers = [25, 78, 12, 90, 45]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number is:", largest)


#5
numbers = []

if numbers:
    print("List is not empty")
else:
    print("List is empty")
    
    
#6
numbers = [10, 20, 30, 40, 50]

index = int(input("Enter index: "))

if index >= 0 and index < len(numbers):
    value = int(input("Enter new value: "))
    numbers[index] = value
    print(numbers)
else:
    print("Invalid index")
    
    
#7
numbers = (10, 20, 30, 40, 50)

value = int(input("Enter value: "))

if value in numbers:
    print("Value exists")
    print("Index:", numbers.index(value))
else:
    print("Value does not exist")
    
    
#8
numbers = [10, 20, 30]

numbers[0] = 100

print("List:", numbers)

marks = (50, 60, 70)

print("Tuple:", marks)

print("List can be modified")
print("Tuple cannot be modified")


#9
data = [10, 20, 30]

if type(data) == list:
    print("It is a List")
elif type(data) == tuple:
    print("It is a Tuple")
else:
    print("It is something else")
    
    
#10
numbers = [x for x in range(1, 21) if x % 2 == 0]

print(numbers)


#11
numbers = [x for x in range(1, 21) if x % 2 != 0]

print(numbers)


#12
numbers = [x for x in range(1, 51) if x % 3 == 0]

print(numbers)


#13
marks = [25, 45, 67, 32, 80, 39, 55]

passed = [mark for mark in marks if mark >= 40]

print(passed)


#14
numbers = [5, 12, 25, 48, 55, 60, 35, 8]

result = [x for x in numbers if x > 10 and x < 50]

print(result)


#15
names = ["Rahul", "Amit", "Karan", "Sanjay", "Priyanka", "Rakesh"]

result = [name for name in names if len(name) > 5]

print(result)



# =============== LAB WORK ================
#16
marks = [75, 68, 82, 55, 71]

total = 0

for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

    total = total + mark

percentage = total / 5

print("Total:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Pass")
else:
    print("Fail")
    
    
#17
products = ["Shirt", "Shoes", "Watch", "Bag"]
prices = [800, 1500, 2500, 900]

product = input("Enter product name: ")

if product in products:
    index = products.index(product)
    price = prices[index]

    print("Product available")
    print("Original price:", price)

    if price > 1000:
        discount = price * 10 / 100
        final_price = price - discount
        print("Discount:", discount)
        print("Final price:", final_price)
    else:
        print("No discount")
        print("Final price:", price)

else:
    print("Product not available")
    
    
    
# =============== SELF EXERCISE ===============
    
#18
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate elements:", duplicates)


#19
numbers = [10, -5, 0, 8, -2, 0, 15, -7]

positive = []
negative = []
zero = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zero.append(number)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)


#20
numbers = [25, 10, 75, 5, 90, 40]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)


#21
numbers = [5, 12, 8, 20, 3, 15, 25]

result = []

for number in numbers:
    if number >= 10:
        result.append(number)

print(result)


#22
numbers = [5, 10, 12, 15, 21, 25, 30, 33, 40]

even = []
odd = []
divisible_by_5 = []

for number in numbers:

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    if number % 5 == 0:
        divisible_by_5.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Divisible by 5:", divisible_by_5)


#23
names = ["Amit", "Rahul", "Ankit", "Riya", "Ajay"]

for name in names:
    if name.startswith("A"):
        print(name)
        
        
#24
students = ("Rahul", "Amit", "Karan", "Riya", "Neha")
marks = (65, 75, 82, 55, 70)

for i in range(len(students)):
    if marks[i] >= 70:
        print(students[i], "scored", marks[i])
        
        
#25
ages = [8, 15, 25, 45, 65, 12, 18, 70]

for age in ages:

    if age < 13:
        print(age, "Child")

    elif age <= 19:
        print(age, "Teenager")

    elif age <= 59:
        print(age, "Adult")

    else:
        print(age, "Senior Citizen")
        

# ========== END ==========