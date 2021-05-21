# Use this script to demonstrate Exception handling
# Use this site to learn about Exception handling: https://realpython.com/python-exceptions/
# Created by Tao Peng on 05.20.2021

# Exceptions versus Syntax Errors
print( 0 / 0 ))
print( 0 / 0)

# Raising an Exception
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# The AssertionError Exception
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."

# The try and except Block: Handling Exceptions
import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')

# The else and finally Clause
import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')