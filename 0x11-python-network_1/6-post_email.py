#!/usr/bin/python3
"""Takes a URL and an email address, and sends a POST request to the passed URL
    with the email address as a parameter, and finally displays the body of the
    response.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print("{}".format(response.text))
