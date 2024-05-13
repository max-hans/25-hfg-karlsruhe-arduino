# Variables
# Variables are used to store data values
# You can assign a value to a variable using the "=" operator

# Example 1: Assigning a string to a variable
name = "Alice"
print("Hello, " + name + "!")
# Output: Hello, Alice!

# Example 2: Assigning a number to a variable
age = 25
print("Alice is " + str(age) + " years old.")
# Output: Alice is 25 years old.

# Task: Create a variable called "favorite_color" and assign your favorite color to it.
# Then, print a sentence using the variable.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# If Statements
# If statements are used to execute code based on a condition
# The code inside the if block will only run if the condition is True

# Example 1: Checking if a number is positive
number = 10
if number > 0:
    print(str(number) + " is a positive number.")
# Output: 10 is a positive number.

# Example 2: Checking if a person is old enough to vote
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote yet.")
# Output: You are not old enough to vote yet.

# Task: Create a variable called "score" and assign a number to it.
# Write an if statement that prints "You passed!" if the score is greater than or equal to 60.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# While Loops
# While loops are used to repeatedly execute a block of code as long as a condition is True

# Example 1: Printing numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3
# 4
# 5

# Example 2: Guessing a secret number
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
print("Congratulations! You guessed the secret number.")

# Task: Write a while loop that prints the even numbers from 0 to 10.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# For Loops
# For loops are used to iterate over a sequence (such as a list or string)

# Example 1: Printing each letter in a word
word = "hello"
for letter in word:
    print(letter)
# Output:
# h
# e
# l
# l
# o

# Example 2: Calculating the sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("The sum is:", sum)
# Output: The sum is: 15

# Task: Create a list of your favorite fruits and use a for loop to print each fruit.
