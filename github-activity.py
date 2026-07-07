import sys
import urllib.request
import json

def get_user_info(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

args = sys.argv
username = args[1]
user_info = get_user_info(username)

#test 123 bla bla bla

if user_info:
    for event in user_info:
        print(json.dumps(event, indent=4))
