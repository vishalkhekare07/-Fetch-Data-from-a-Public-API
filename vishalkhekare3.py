#3 Task 7: Fetch Data from a Public API

import requests

def fetch_data_from_api(url):
    response = requests.get(url)
    return response.json()

# Example Usage:
url = "https://jsonplaceholder.typicode.com/posts/1"
data = fetch_data_from_api(url)
print(data)  
