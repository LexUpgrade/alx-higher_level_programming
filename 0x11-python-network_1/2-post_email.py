#!/usr/bin/python3
"""Takes in a URL and an email, and sends a POST request to the passed URL
    and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import urllib.parse as parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        html_page = response.read()
        print("{}".format(html_page.decode('utf-8')))
