#!/usr/bin/python3
"""Takes in GitHub credentials (username, password) and uses the
    GitHub API to display the 'id'.
"""


if __name__ == "__main__":
    from sys import argv
    from requests.auth import HTTPBasicAuth
    import requests

    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]

    auth = HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
