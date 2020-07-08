"""
This module is intended to be used for
the response output to API GATEWAY in AWS
"""

from application.utilities.utils import json_response


# Function to the AWS lambda to serve purpose of server less
def lambda_handler(event, context):
    try:
        n = str(event['queryStringParameters']['n'])
        fibonacci_validators(n)
        calculation_output = calculate_fibonacci(n)
        response_output = json_response(message="Success",
                                        data=calculation_output,
                                        status=200)

    except ValueError:
        response_output = json_response(message="Error",
                                        data="Wrong input value...Value must be an Integer and should not have "
                                             "negative value and should start from 0",
                                        status=400)

    except (IOError, TimeoutError, Exception):
        response_output = json_response(message="Error",
                                        data="Check or pass the input and execution",
                                        status=500)

    return response_output


# Function to validate the input value
def fibonacci_validators(input_value):
    if not int(input_value) or int(input_value) <= 0 or not str(input_value).isdecimal():
        raise ValueError()


# Function which contains the logic to calculate fibonacci
def calculate_fibonacci(n):
    x, y = 0, 1
    n = int(n)
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        for i in range(2, n):
            z = x + y
            x, y = y, z
        return x + y
