import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
#store API response in a variable
response_dict=r.json()
print(f"total respositories: {response_dict['total_count']}")

# explore information about the respositories
repo_dicts=response_dict['items']
print(f"respositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"repository: {repo_dict['html_url']}")
    print(f"created: {repo_dict['created_at']}")
    print(f"updated: {repo_dict['updated_at']}")
    print(f"description: {repo_dict['description']}")