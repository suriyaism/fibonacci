"""
This module is intended to be used to handle
the response output to API GATEWAY in AWS
"""
import json


def json_response(data, message, status, headers={}):
    serialized = json.dumps({'status': status, 'message': message, 'responseOutput': data})
    headers["Content-Type"] = "application/json"
    headers["Access-Control-Allow-Origin"] = "*"
    headers["Access-Control-Allow-Credentials"] = "True"

    for key in headers.keys():
        value = headers.pop(key)
        headers[str(key)] = str(value)

    return {
        'statusCode': status,
        'headers': headers,
        'body': serialized
    }
