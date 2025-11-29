import requests

# Parameters
owner = "sanand0"
repo = "tools-in-data-science-public"
sha = "95224924d73f70bf162288742a555fe6d136af2d"
path_prefix = "project-1/"
extension = ".md"

# Fetch GitHub tree
url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{sha}?recursive=1"
print(f"Fetching: {url}")
response = requests.get(url)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

data = response.json()

# Count matching files
count = 0
matching_files = []
for item in data.get('tree', []):
    path = item.get('path', '')
    if path.startswith(path_prefix) and path.endswith(extension):
        count += 1
        matching_files.append(path)

print(f"\nFound {count} files matching:")
print(f"  - Path starts with: {path_prefix}")
print(f"  - Extension: {extension}")
print("\nMatching files:")
for f in matching_files:
    print(f"  - {f}")

# Calculate offset and answer
email = "24ds1000070@ds.study.iitm.ac.in"
email_length = len(email)
offset = email_length % 2

answer = count + offset

print(f"\n{'='*50}")
print(f"Count: {count}")
print(f"Email length: {email_length}")
print(f"Offset (email_length mod 2): {offset}")
print(f"{'='*50}")
print(f"ANSWER: {answer}")
print(f"{'='*50}")