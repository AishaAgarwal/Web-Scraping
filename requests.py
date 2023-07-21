# webscraping is done using requests and beautiful soup library 
# Requests library is used for making HTTP requests to a specific URL and returns the response.

import requests
# GET request 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r)
print(r.content)

print(r.status_code)
