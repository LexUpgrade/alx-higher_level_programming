#!/usr/bin/python3
"""Takes a url as an argument and displays the value of the
    'X-Request-Id' variable found in the header of the response
"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        for h in response.getheaders():
            if h[0] == 'X-Request-Id':
                print(h[1])
                break
