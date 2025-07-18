# Print Hello World
print("Hello World")
z ="Hello World"
print(z)


# Take input from user and print it
user = int(input("hey user give input:"))
print("the input is:",user)


# Add two numbers input by the user
num1 = int(input("first number:"))
num2 = int(input("second number:"))
add = num1 + num2
print("add these two numbers:", add)

# Find the square of a number
num = int(input("enter a number:"))
square = num **2  
# a = 6
# square = a**2 
print("square of the number is:", square)


# Swap two numbers
a = 5
b = 10
print("a=",a)
print("b=",b)
a, b = b, a
print(f"after swap a ={a} and b={b}")


# Print numbers from 1 to 10 using a loop
for i in range(1,11):
    print(i)



# Calculate the sum of numbers from 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)



# Print all even numbers between 1 and 50
n = int(input("Enter a number: "))
even = 0
odd = 0
print("Even numbers between 1 and", n, "are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")  # print the even number
        even += 1
    else:
        odd += 1
# #another way
# for i in range(2,51,2):
#     print(i)



# Print the reverse of a number
num = int(input("Enter a number: "))
rev = 0
while num != 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)


# Check if a number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Count the number of vowels in a string
s = input("Enter a string: ")
count = sum(1 for char in s.lower() if char in "aeiou")
print("Number of vowels:", count)


# Reverse a string
s = input("Enter a string: ")
print("Reversed:", s[::-1])



# Find the largest number in a list
list =[1,2,3,4,5,6,9]
a = max(list)
print("largest numbers in this list is:", a)


# Remove duplicates from a list
a =[6,6,1,8,3,1,9,5]
print(list(set(a)))


# Sort a list in ascending order
a =[6,8,3,1,9,5]
a.sort()
#a.sort(reverse=True)  #descending
print("sorted list is:", a)



# Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Find the largest of three numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print("Largest number is:", max(a, b, c))



# Calculate the factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)



# Generate a multiplication table for a number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
