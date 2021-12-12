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
repo_dicts = response_dict['items']

print(f"Repositories returned: {len(repo_dicts)}")

# Exploring first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for x in repo_dict.keys():
    print(x)
    
print("\nSelecting particular information in each repo")

for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['full_name']}")
    print(f"Language: {repo_dict['language']}")
    print(f"Owner: {repo_dict['owner']}")