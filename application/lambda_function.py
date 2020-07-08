"""
This module is intended to be used for
the response output to API GATEWAY in AWS
"""

from application.utilities.utils import response_builder


# Function to the AWS lambda to serve purpose of server less
def lambda_handler(event, context):
    try:
        n = str(event['queryStringParameters']['n'])
        fibonacci_validators(n)
        output = calculate_fibonacci(n)
        response = response_builder(data=output, message="Success", status=200)

    except ValueError:
        response = response_builder(data="Wrong input value...Value must be an Integer and should not have "
                                         "negative value and should start from 0", message="Error", status=400)

    except (IOError, TimeoutError, Exception):
        response = response_builder(data="Check the input and execution", message="Error", status=500)

    return response


# Function to validate the input value
def fibonacci_validators(input_value):
    if not int(input_value) or input_value <= 0 or not str(input_value).isdecimal():
        raise ValueError()


# Function which contains the logic to calculate fibonacci
def calculate_fibonacci(n):
    x, y = 0, 1

    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        for i in range(2, n):
            z = x + y
            x, y = y, z
        return x + y
