import sys
import urllib.request

def get_user_info(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            print(f"Success! Status code: {status_code}")
    except Exception as err:
        print(f"An error occurred: {err}")
#return response.read()

args = sys.argv
username = args[1]
user_info = get_user_info(username)

if user_info:
    print("")
