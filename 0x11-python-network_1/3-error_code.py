#!/usr/bin/python3
"""Takes in a URL, and sends a request to the URL and displays the body of the
    response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html_page = response.read()
            print("{}".format(html_page.decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
