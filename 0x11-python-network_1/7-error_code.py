#!/usr/bin/pytho3
"""Takes a URL and sends a request to the URL and displays the body of the 
    respinse.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.reason))
