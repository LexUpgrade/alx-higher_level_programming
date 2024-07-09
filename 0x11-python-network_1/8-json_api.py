#!/usr/bin/python3
"""Takes in a letter and send a POST request to a URL with the letter
    as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_dict = response.json()
        if json_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_dict["id"], json_dict["name"]))
    except ValueError:
        print("Not a valid JSON")
