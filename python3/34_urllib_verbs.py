# Daniel OUATTARA
# 28 06 2024


import urllib.request
import json
from urllib import request


url = 'https://jsonplaceholder.typicode.com/users?_limit=3'

print('\n ------------------------- # Make a GET request\n')

res = urllib.request.urlopen(url)

# Print the response code
print(f'res.code = {res.code}')  # 200

# Read the response data as bytes
binaries = res.read()  # <class 'bytes'>

# Decode the bytes to a UTF-8 string
data = binaries.decode('utf-8')

# Print the decoded data
print(f'data = {data}')

# Parse JSON data
json_data = json.loads(data)

# Print the JSON data
print(json_data)


print('\n ---------------------- # Make a GET request\n')


# Make a GET request
req = urllib.request.Request(url)

# Perform the request and capture the response
with urllib.request.urlopen(req) as response:
    # Decode the response
    data = response.read().decode('utf-8')
    # Print the data
    print('data = ', data)

    print('-----')

    # Parse JSON data to Python object
    json_data = json.loads(data)
    # Print the JSON data
    print('json_data = ', json_data)


print('\n ----------------------- # Make a POST request\n')

# URL of the API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Headers specifying that the content type is JSON with UTF-8 encoding
headers = {'Content-Type': 'application/json; charset=UTF-8'}

# Data to be sent as the body of the POST request, formatted as a dictionary
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}

# Encode the data to JSON
data = json.dumps(data).encode('utf-8')

# Create a request object
req = urllib.request.Request(url, data=data, headers=headers, method='POST')

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print('result = ', result)
    print('-----')
    print('json.loads(result) = ', json.loads(result))


print('\n ------------------ # Make a PUT request \n')


url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}

# Encode the data to JSON
data = json.dumps(data).encode('utf-8')

# Create a request object
req = urllib.request.Request(url, data=data, headers=headers, method='PUT')

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print('result = ', result)
    print('-----')
    print('json.loads(result) = ', json.loads(result))

print('\n ----------------------- # Make a PATCH request \n')


url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    'title': 'foo',
}

# Encode the data to JSON
data = json.dumps(data).encode('utf-8')

# Create a request object
req = urllib.request.Request(url, data=data, headers=headers, method='PATCH')

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print('result = ', result)
    print('-----')
    print('json.loads(result) = ', json.loads(result))


print('\n ----------------------- # Make a delete request \n')


url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-Type': 'application/json; charset=UTF-8'}

# Create a request object
req = urllib.request.Request(url, headers=headers, method='DELETE')

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print('result = ', result)
    print('-----')
    # print('json.loads(result) = ', json.loads(result))


print('\n ----------------------- # Filtering resources \n')

# This will return all the posts that belong to the first user

url = 'https://jsonplaceholder.typicode.com/posts?userId=1'
headers = {'Content-Type': 'application/json; charset=UTF-8'}

# Create a request object
req = urllib.request.Request(url, headers=headers)

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')
    print('data = ', data)

    print('-----')

    # Parse JSON data to Python object
    json_data = json.loads(data)
    # Print the JSON data
    print('json_data = ', json_data)


print('\n ----------------------- # Listing nested resources \n')

# This is equivalent to /comments?postId=1

url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
headers = {'Content-Type': 'application/json; charset=UTF-8'}

# Create a request object
req = urllib.request.Request(url, headers=headers)

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')
    print('data = ', data)

    print('-----')

    # Parse JSON data to Python object
    json_data = json.loads(data)
    # Print the JSON data
    print('json_data = ', json_data)
