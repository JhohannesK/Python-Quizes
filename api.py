# Import the module
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')


# Store API response in a variable
response_dict = r.json()

# Finding the total repos
print(f"Total Repositories: {response_dict['total_count']}")
repo_dict = response_dict['items']

print(f"Repositories returned: {len(repo_dict)}")