import requests
import json

print('\n ----------------- Making a GET request\n')
url = 'https://jsonplaceholder.typicode.com/users?_limit=3'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print('json_data =', json_data)
else:
    print(f"Error: {response.status_code}")

# Another way to Make a GET request
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print('json_data =', json_data)
else:
    print(f"Error: {response.status_code}")

print('\n ----------------- Making a POST request\n')
url = 'https://jsonplaceholder.typicode.com/posts'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:  # Assuming 201 Created is returned upon successful creation
    result = response.json()
    print('result =', result)
else:
    print(f"Error: {response.status_code}")

print('\n ----------------- Making a PUT request\n')
url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}
response = requests.put(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print('result =', result)
else:
    print(f"Error: {response.status_code}")

print('\n ----------------- Making a PATCH request\n')
data = {
    'title': 'foo',
}
response = requests.patch(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print('result =', result)
else:
    print(f"Error: {response.status_code}")

print('\n ----------------- Making a DELETE request\n')
response = requests.delete(url, headers=headers)

if response.status_code == 200:
    print('Deletion successful.')
else:
    print(f"Error: {response.status_code}")

# Filtering resources
url = 'https://jsonplaceholder.typicode.com/posts?userId=1'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    json_data = response.json()
    print('json_data =', json_data)
else:
    print(f"Error: {response.status_code}")

# Listing nested resources
url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    json_data = response.json()
    print('json_data =', json_data)
else:
    print(f"Error: {response.status_code}")
