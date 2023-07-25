#!/usr/bin/env python
# coding: utf-8

# # Q1. In Python, what is the difference between a built-in function and a user-defined function? Provide anexample of each.

# A built-in function is a function that comes with Python and can be used without defining it first. For example, print() is a built-in function that prints the given argument to the standard output. A user-defined function is a function that is created by the programmer to perform a specific task. For example, def add_numbers(x, y): is a user-defined function that takes two numbers as parameters and returns their sum.
# Here is an example of using both types of functions in Python:

# In[1]:


# A user-defined function to add two numbers
def add_numbers(x, y):
  sum = x + y
  return sum

# Calling the user-defined function
num1 = 5
num2 = 6
print("The sum is", add_numbers(num1, num2))

# Calling the built-in function
print("The length of 'Hello' is", len("Hello"))


# # Q2. How can you pass arguments to a function in Python? Explain the difference between positionalarguments and keyword arguments.

# You can pass arguments to a function in Python in two ways: positional arguments and keyword arguments.
# 
# Positional arguments are arguments that are passed to a function in a specific order, and the function uses the arguments in the order that they are received. For example, if you have a function that takes two arguments, the first argument will be used as the first parameter, and the second argument will be used as the second parameter. To use positional arguments, you need to pass the arguments in the same order as their respective parameters in the function definition. For example:

# In[2]:


# A function that takes two arguments
def add_numbers(x, y):
  return x + y

# Calling the function with positional arguments
result = add_numbers(3, 4) # 3 is assigned to x, 4 is assigned to y
print(result) # 7


# The difference between positional and keyword arguments is that positional arguments depend on the order of the arguments, while keyword arguments do not. Positional arguments are simpler and more concise, but they can be prone to errors if you mix up the order of the arguments. Keyword arguments are more explicit and clear, but they can be verbose and repetitive.
# 
# You can also use both positional and keyword arguments in a single function call, as long as you follow some rules:
# 
# You must use all the positional arguments before any keyword arguments.
# You cannot use a positional argument after a keyword argument.
# You cannot use the same argument as both positional and keyword.
# For example:

# In[3]:


# A function that takes three arguments
def greet(name, message, punctuation):
  print(f"{message}, {name}{punctuation}")

# Calling the function with both positional and keyword arguments
greet("Alice", "Hello", "!") # All positional
greet("Bob", punctuation = ".", message = "Goodbye") # All keyword
greet("Charlie", "Hi", punctuation = "?") # Two positional, one keyword
greet(name = "David", "Welcome", "!") # Invalid: positional after keyword
greet("Eve", message = "How are you", punctuation = "!") # Invalid: same argument twice


# # Q3. What is the purpose of the return statement in a function? Can a function have multiple returnstatements? Explain with an example.

# The purpose of the return statement in a function is to end the execution of the function and send back a value or values to the caller. The return statement can be used to return any Python object, such as numbers, strings, lists, tuples, dictionaries, etc. The return value can be used for further computation or processing in the program.
# 
# A function can have multiple return statements, but only one of them will be executed depending on the condition or logic of the function. A function can also return multiple values using a single return statement by simply listing the values separated by commas. This method returns a tuple, which is an immutable object that contains one or more items.
# 
# Here is an example of a function that has multiple return statements and returns multiple values:

# In[4]:



def check_number(n):
  if n > 0:
    return "Positive", n # Returns a tuple with two items
  elif n < 0:
    return "Negative", n # Returns a tuple with two items
  else:
    return "Zero", n # Returns a tuple with two items

# Calling the function with different arguments
result1 = check_number(5)
result2 = check_number(-3)
result3 = check_number(0)

# Printing the results
print(result1) # ('Positive', 5)
print(result2) # ('Negative', -3)
print(result3) # ('Zero', 0)


# In this example, the function check_number() takes a number as an argument and returns a tuple with two items: a string that indicates if the number is positive, negative or zero, and the number itself. The function has three return statements, but only one of them will be executed depending on the value of n. The function can return multiple values using commas in the return statement.
# 
# I hope this helps you understand the purpose of the return statement in a function and how to use it to return multiple values or have multiple return statements. 

# # Q4. What are lambda functions in Python? How are they different from regular functions? Provide anexample where a lambda function can be useful.

# Lambda functions are anonymous functions that are defined using the lambda keyword. They can have any number of arguments but only one expression, which is evaluated and returned. Lambda functions are mainly used as a convenient way to create simple and short functions that are not needed later in the code.
# 
# Regular functions are named functions that are defined using the def keyword. They can have any number of arguments and statements, and they can return any Python object. Regular functions are mainly used to create reusable and modular code that can be called multiple times in the code.
# 
# The main differences between lambda functions and regular functions are:
# 
# Lambda functions are anonymous, while regular functions have a name.
# Lambda functions are defined on a single line, while regular functions can span multiple lines.
# Lambda functions can only have one expression, while regular functions can have multiple statements.
# Lambda functions do not support docstrings, while regular functions can have documentation strings.
# Lambda functions cannot use global or nonlocal statements, while regular functions can.
# 
# Here is an example that illustrates the differences between a lambda function and a regular function:

# In[5]:


# Lambda function that adds two numbers
add_lambda = lambda x, y: x + y

# Regular function that adds two numbers
def add_def(x, y):
  """This function adds two numbers and returns the result."""
  return x + y

# Calling both functions with the same arguments
print(add_lambda(2, 3)) # 5
print(add_def(2, 3)) # 5


# # Q5. How does the concept of "scope" apply to functions in Python? Explain the difference between localscope and global scope.

# The concept of scope applies to functions in Python because it determines the visibility and accessibility of variables within a function. Scope defines the region or area where a variable can be used or referenced12
# 
# There are two types of scope in Python: local scope and global scope.
# 
# Local scope is the scope within a function, where variables are created and used only inside that function. Local variables are not accessible from outside the function. Local scope is also known as function scope.
# 
# Global scope is the scope outside of any function, where variables are created and used throughout the program. Global variables are accessible from any function or region of the code. Global scope is also known as module scope.
# 
# The difference between local scope and global scope is that local variables have a limited lifetime and accessibility, while global variables have a longer lifetime and wider accessibility. Local variables are created when a function is called and destroyed when the function ends, while global variables are created when the program starts and destroyed when the program ends. Local variables can only be used within the function where they are defined, while global variables can be used by any function or region of the code.
# 
# 

# # Q6. How can you use the "return" statement in a Python function to return multiple values?

# You can use the return statement in a Python function to return multiple values by simply listing those values separated by commas. This way, the function will return a tuple, which is an immutable object that contains one or more items.
# 
# For example, suppose you have a function that calculates the area and perimeter of a rectangle given its length and width. You can use the return statement to return both values as follows:

# In[12]:


# Define a function that returns the area and perimeter of a rectangle
def rectangle_area_perimeter(length, width):
  # Calculate the area
  area = length * width
  # Calculate the perimeter
  perimeter = 2 * (length + width)
  # Return both values as a tuple
  return area, perimeter

# Call the function with some arguments
result = rectangle_area_perimeter(10, 5)
print(result) # (50, 30)


# In this example, the function rectangle_area_perimeter() returns a tuple with two items: the area and the perimeter of the rectangle. We can assign the result to a variable and print it out.
# 
# Alternatively, we can also use tuple unpacking to assign each value to a separate variable. For example:

# In[13]:


# Call the function with some arguments
area, perimeter = rectangle_area_perimeter(10, 5)
print(area) # 50
print(perimeter) # 30


# In this example, we use tuple unpacking to assign each item of the tuple to a different variable. This way, we can access each value individually.
# 
# I hope this helps you understand how to use the return statement in a Python function to return multiple values.

# # Q7. What is the difference between the "pass by value" and "pass by reference" concepts when it comes to function arguments in Python?

# Pass by value means that when a function is called, the actual values of the arguments are copied and passed to the function. The function then works with these copies, and any changes made to them do not affect the original variables in the caller.
# 
# Pass by reference means that when a function is called, the references or pointers to the arguments are passed to the function. The function then works with these references, and any changes made to them affect the original variables in the caller.
# 
# The difference between pass by value and pass by reference is that pass by value creates a new copy of the argument for the function, while pass by reference shares the same argument with the function. Pass by value is safer and simpler, but it can be inefficient for large or complex data structures. Pass by reference is faster and more flexible, but it can introduce side effects and errors.

# # Q8. Create a function that can intake integer or decimal value and do following operations:
# ## a. Logarithmic function (log x)
# ## b. Exponential function (exp(x))
# ## c. Power function with base 2 (2x)
# ## d. Square root

# To create a function that can intake integer or decimal value and do the following operations, we can use the math module, which provides various mathematical functions.

# In[14]:


# Import the math module
import math

# Define a function that takes a number as an argument
def math_operations(number):
  # Check if the number is positive
  if number > 0:
    # Calculate and print the logarithmic function (log x)
    log_x = math.log(number)
    print(f"log({number}) = {log_x}")

    # Calculate and print the exponential function (exp(x))
    exp_x = math.exp(number)
    print(f"exp({number}) = {exp_x}")

    # Calculate and print the power function with base 2 (2^x)
    power_x = 2 ** number
    print(f"2^{number} = {power_x}")

    # Calculate and print the square root
    sqrt_x = math.sqrt(number)
    print(f"sqrt({number}) = {sqrt_x}")
  else:
    # Print an error message if the number is negative or zero
    print("Invalid input. The number must be positive.")


# This function takes a number as an argument and checks if it is positive. If it is, then it calculates and prints the four mathematical operations using the math module. If it is not, then it prints an error message.
# 
# Here are some examples of calling the function with different inputs:

# In[15]:


# Call the function with an integer value
math_operations(4)


# In[16]:


# Call the function with a decimal value
math_operations(3.14)


# In[17]:


# Call the function with a negative value
math_operations(-2)


# # Q9. Create a function that takes a full name as an argument and returns first name and last name.

# To create a function that takes a full name as an argument and returns first name and last name, you can use the split() method, which splits a string into a list of substrings based on a delimiter. For example:

# In[18]:


# Define a function that takes a full name as an argument
def split_name(full_name):
  # Split the full name by whitespace
  name_list = full_name.split()
  # Check if the name list has at least two elements
  if len(name_list) >= 2:
    # Assign the first element to first name
    first_name = name_list[0]
    # Assign the last element to last name
    last_name = name_list[-1]
    # Return both names as a tuple
    return first_name, last_name
  else:
    # Print an error message if the name list is too short
    print("Invalid input. The full name must have at least two words.")


# This function takes a full name as an argument and splits it by whitespace using the split() method. It then checks if the resulting list has at least two elements, which are the minimum for a valid full name. If it does, then it assigns the first element to the first name and the last element to the last name, and returns them as a tuple. If it does not, then it prints an error message.
# 
# Here are some examples of calling the function with different inputs:

# In[19]:


# Call the function with a valid full name
first, last = split_name("John Smith")
print(f"First name: {first}")
print(f"Last name: {last}")


# In[20]:


# Call the function with another valid full name
first, last = split_name("Mary Jane Watson")
print(f"First name: {first}")
print(f"Last name: {last}")


# In[21]:


# Call the function with an invalid full name
split_name("Alice")


# In[ ]:




