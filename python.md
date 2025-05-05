# Python Basics

## Introduction to Python Code

Python code works like a recipe that the computer follows step-by-step, from top to bottom. When you run a Python program, the computer reads and executes each line in order. For example, if you write `x = 5` and then `print(x)`, the computer first creates a variable named 'x' with the value 5, and only then prints it. Comments are notes for humans that Python ignores - they start with a `#` symbol. Everything after the `#` on that line is ignored by Python. Comments help explain what your code does, making it easier for you and others to understand. For instance:

```python
# This is a comment explaining what happens next
player_score = 10  # This sets the player's score to 10
player_score = player_score + 5  # Adding 5 points
# The line below will show the score on screen
print(f"Your score is: {player_score}")  # Output: Your score is: 15
```

In this example, Python only executes the actual code, while the comments (beginning with `#`) provide explanation for human readers.

## Variables

Variables are used to store data values. You can assign a value to a variable using the "=" operator.

### Example 1: Assigning a string to a variable

```python
name = "Alice"
print(f"Hello, {name}!")
# Output: Hello, Alice!
```

### Example 2: Assigning a number to a variable

```python
age = 25
print(f"Alice is {age} years old.")
# Output: Alice is 25 years old.
```

### Example 3: Microcontroller-relevant variable

```python
led_pin = 13
print(f"LED connected to pin {led_pin}")
# Output: LED connected to pin 13
```

### Task 1

Create a variable called "favorite_color" and assign your favorite color to it. Then, print a sentence using the variable.

### Solution:

```python
favorite_color = "blue"
print(f"My favorite color is {favorite_color}.")
# Output: My favorite color is blue.
```

### Task 2

Create variables for temperature and humidity sensor readings (use the values 23.5 and 65). Print both values in a single sentence.

### Solution:

```python
temperature = 23.5
humidity = 65
print(f"The temperature is {temperature}°C and humidity is {humidity}%.")
```

### Task 3

Create variables for three different pin assignments for LEDs: red_led, green_led, and blue_led. Use pin numbers 5, 6, and 7. Print which pin each LED is connected to.

## If Statements

If statements are used to execute code based on a condition. The code inside the if block will only run if the condition is True.

### Example 1: Checking if a number is positive

```python
number = 10
if number > 0:
    print(f"{number} is a positive number.")
# Output: 10 is a positive number.
```

### Example 2: Checking if a person is old enough to vote

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote yet.")
# Output: You are not old enough to vote yet.
```

### Example 3: Using elif for multiple conditions

```python
temperature = 25
if temperature > 30:
    print("It's hot - turn on cooling")
elif temperature < 15:
    print("It's cold - turn on heating")
else:
    print("Temperature is comfortable")
# Output: Temperature is comfortable
```

### Example 4: Microcontroller-relevant if statement

```python
button_pressed = True
if button_pressed:
    print("LED on")
else:
    print("LED off")
# Output: LED on
```

### Task 1

Create a variable called "score" and assign a number to it. Write an if statement that prints "You passed!" if the score is greater than or equal to 60.

### Solution:

```python
score = 75
if score >= 60:
    print("You passed!")
# Output: You passed!
```

### Task 2

Create a variable called "motion_detected" and set it to either True or False. Write an if-else statement that prints "Alarm activated!" if motion is detected, otherwise print "All clear".

### Solution:

```python
motion_detected = True
if motion_detected:
    print("Alarm activated!")
else:
    print("All clear")
```

### Task 3

Create a variable called "battery_level" with a value between 0 and 100. Write an if-elif-else statement that prints:

- "Critical - Please charge now!" if the level is less than 10
- "Low - Consider charging soon" if the level is between 10 and 30
- "Battery OK" if the level is above 30

### Task 4

Create two variables: "button1_pressed" and "button2_pressed" (both True or False). Write an if statement that prints "Special function activated!" only if both buttons are pressed.

## While Loops

While loops are used to repeatedly execute a block of code as long as a condition is True.

### Example 1: Printing numbers from 1 to 5

```python
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
```

### Example 2: Microcontroller-relevant while loop

```python
sensor_value = 0
while sensor_value < 100:
    print(f"Reading sensor: {sensor_value}")
    sensor_value += 20
    # In a real microcontroller, you'd read the actual sensor here
# Output:
# Reading sensor: 0
# Reading sensor: 20
# Reading sensor: 40
# Reading sensor: 60
# Reading sensor: 80
```

### Task 1

Write a while loop that prints the even numbers from 0 to 10.

### Solution:

```python
num = 0
while num <= 10:
    print(num)
    num += 2
# Output:
# 0
# 2
# 4
# 6
# 8
# 10
```

### Task 2

Write a while loop that counts down from 10 to 1, then prints "Blast off!" at the end (after the loop).

### Solution:

```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
```

### Task 3

Write a while loop that simulates waiting for a sensor to reach a threshold. Start with "sensor_reading = 15" and increment it by 5 each iteration. Continue until the reading is at least 50, printing the value each time.

### IGNORE: Task 4

Create a variable called "password_attempt" and set it to "". Inside a while loop, check if password_attempt equals "secret". If not, set password_attempt to "secret" (simulating a user entering the correct password) and continue the loop. Once the correct password is entered, print "Access granted!" and exit the loop.

## For Loops

For loops are used to iterate over a sequence (such as a list or string).

### Example 1: Printing each letter in a word

```python
word = "hello"
for letter in word:
    print(letter)
# Output:
# h
# e
# l
# l
# o
```

### Example 2: Calculating the sum of numbers in a list

```python
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum = sum + number
print(f"The sum is: {sum}")
# Output: The sum is: 15
```

### Example 3: Microcontroller-relevant for loop

```python
pins = [5, 6, 13]
for pin in pins:
    print(f"Initializing pin {pin}")
# Output:
# Initializing pin 5
# Initializing pin 6
# Initializing pin 13
```

### Task 1

Create a list of 3 fruits and use a for loop to print each one.

### Solution:

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# orange
```

### Task 2

Create a list called "led_pins" with the values [9, 10, 11]. Use a for loop to simulate turning on each LED by printing "LED on pin {pin} is now ON".

### Solution:

```python
led_pins = [9, 10, 11]
for pin in led_pins:
    print(f"LED on pin {pin} is now ON")
```

### Task 3

Create a list of temperatures [22.5, 19.8, 25.1, 23.4]. Use a for loop to print each temperature, and beside it print "Too hot!" if the temperature is over 23, otherwise print "Comfortable".

### Task 4

Create a list of 5 numbers. Use a for loop to calculate and print the square of each number (number \* number).

### Task 5

Use a for loop with the range() function to print numbers from 1 to 5. Hint: You can use "for i in range(1, 6):" to create a loop that runs 5 times.

## Advanced Challenges

### Challenge Task 1: Temperature Monitor System

Create a program that simulates a temperature monitoring system. Use the following requirements:

- Create a list of temperature readings: [18.5, 19.2, 22.1, 25.7, 27.3, 26.8, 24.5, 23.9, 25.6, 28.2]
- Use a for loop to analyze each temperature
- Keep track of how many readings are "Normal" (18-24), "Warning" (24-27), and "Critical" (above 27)
- After analyzing all readings, print a status report showing counts of each category
- If any Critical readings are found, print "Alert: Critical temperature detected!"

```python
# Sample partial solution to get you started:
temperatures = [18.5, 19.2, 22.1, 25.7, 27.3, 26.8, 24.5, 23.9, 25.6, 28.2]
normal_count = 0
warning_count = 0
critical_count = 0

# Your code here
```

### Challenge Task 2: LED Pattern Generator

Create a program that generates different LED blinking patterns for a microcontroller:

- Create a list called `patterns` containing three patterns: "blink", "alternate", "fade"
- Create a variable `selected_pattern` and set it to one of the patterns
- Use if/elif/else statements to handle each pattern:
  - For "blink": Use a while loop to simulate an LED turning on and off 5 times
  - For "alternate": Use a for loop with a list of LED pins [5, 6, 7] to turn each pin on and off in sequence
  - For "fade": Simulate a brightness fade using a while loop that increases a value from 0 to 100 in steps of 10
- For each pattern, print descriptive messages showing what the LED(s) would be doing

### Challenge Task 3: Sensor Data Analyzer

Create a program that analyzes simulated sensor data:

- Create three variables: `min_threshold` = 30, `max_threshold` = 70, and `danger_zone` = 85
- Create a list `sensor_data` with values [42, 65, 28, 91, 50, 35, 69, 72, 86, 55]
- Use a for loop to process each reading and print one of these messages:
  - "Too low" if below min_threshold
  - "Optimal" if between min_threshold and max_threshold
  - "Too high" if between max_threshold and danger_zone
  - "DANGER!" if at or above danger_zone
- Keep count of readings in each category
- After processing all readings, calculate and print the average value of all readings
- Use an if statement to provide a final system status: "System OK" if no DANGER readings, otherwise "System Failure"

## Interesting Stuff

### Random values

You can generate random values to use in your program. These always range from 0 to 1.
Anything beyond that needs to be done by you by multiplication etc.

```python
import random


while True:
    variable = random.random() * 100

    if variable < 10:
        print("low")
    elif variable < 50:
        print("medium")
    elif variable < 80:
        print("medium2")
    else:
        print("high")
```
