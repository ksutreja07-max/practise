#join()
#strip()
#lstrip()
#rstrip()
#isalpha()
#isdigit()
#islower()
#isupper()
#isspace()
#[::-1]
#reversed()
#reverse()
#list()
#len()
#if / else
#for loop
#input()
#\n
#\t
#\"
#\'
#\\
    
    
#1. Join Strings — City Names =============

cities = ["Junagadh", "Rajkot", "Ahmedabad"]

result = " - ".join(cities)

print(result)


#2. Join Strings — Programming Languages==========

languages = ["Python", "Java", "C++", "JavaScript"]

result = " | ".join(languages)

print(result)


#3. Strip=============================================

name = "   Kuldip   "

result = name.strip()

print(result)


#4. Lstrip===============================================

name = "   Kuldip   "

result = name.lstrip()

print(result)


#5. Rstrip ================================================

name = "   Kuldip   "

result = name.rstrip()

print(result)


#6. Remove Non-Alphabetic Characters========================

text = "Hello123@World!"

result = ""

for char in text:
    if char.isalpha():
        result = result + char

print(result)


#7. Keep Only Numbers==================================

text = "abc123xyz456"

result = ""

for char in text:
    if char.isdigit():
        result = result + char

print(result)

#8. String Checking ====================================

text1 = "Hello"
text2 = "12345"
text3 = "hello"
text4 = "HELLO"
text5 = "     "

print(text1.isalpha())
print(text2.isdigit())
print(text3.islower())
print(text4.isupper())
print(text5.isspace())

#9. Reverse String — Slicing ======================

text = "Python"

result = text[::-1]

print(result)

#10 ================================================

text = "Python"

result = "".join(reversed(text))

print(result)


#11================================================

text = "Python"

letters = list(text)

letters.reverse()

result = "".join(letters)

print(result)

#12 ==============================================

text = input("Enter a string: ")

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    
    
#13 =============================================

num = input("Enter a number: ")

if num == num[::-1]:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
    
    
#14 ============================================

print("Hello\nWorld")

print("Hello\tWorld")

print("He said \"Hello\"")

print("It's a good day")

print("C:\\Python")


#15 ==============================================

text = input("Enter a string: ")

text = text.strip()

new_text = ""

for char in text:
    if char.isalpha():
        new_text = new_text + char

print("Clean string:", new_text)

print("Length:", len(new_text))

reverse = new_text[::-1]

print("Reverse:", reverse)

if new_text.lower() == reverse.lower():
    print("It is a palindrome")
else:
    print("It is not a palindrome")