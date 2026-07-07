import sys
import urllib.request
import json

def get_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

def print_user_profile(profile):
    print("======== GitHub User Profile ========")
    print(f"{'Name:':<10} {profile['name'] or profile['login']}")
    if profile["bio"]: print(f"{'Bio:':<10} {profile["bio"]}") 
    if profile["location"]: print(f"{'Location:':<10} {profile["location"]}")
    print(f"{'Repos:':<10} {profile["public_repos"]}")
    print(f"{'Followers:':<10} {profile["followers"]}")
    print(f"{'Following:':<10} {profile["following"]}")
    if profile["blog"]: print(f"{'Blog:':<10} {profile["blog"]}")


def get_user_info(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

def print_user_info(info):
    print("=========== User Activity ===========")
    for event in info:
        print(format_event(event))

def format_event(event):
    event_type = event["type"]
    repo_name = event["repo"]["name"]

    if event_type == "PushEvent":
        return f"- Pushed to {repo_name}"
    elif event_type == "IssuesEvent":
        action = event["payload"]["action"]
        return f"- {action.capitalize()} an issue in {repo_name}"
    elif event_type == "WatchEvent":
        return f"- Starred {repo_name}"
    elif event_type == "ForkEvent":
        return f"- Forked {repo_name}"
    elif event_type == "CreateEvent":
        return f"- Created repository {repo_name}"
    elif event_type == "IssueCommentEvent":
        issue_title = event["payload"]["issue"]["title"]
        return f"- Commented on issue '{issue_title}' in {repo_name}"
    elif event_type == "PullRequestEvent":
        action = event["payload"]["action"].capitalize()
        number = event["payload"]["number"]
        return f"- {action} pull request #{number} in {repo_name}"
    elif event_type == "PullRequestReviewEvent":
        state = event["payload"]["review"]["state"]
        return f"- Reviewed pull request in {repo_name}"
    else:
        return f"- {event_type} in {repo_name}"

def print_activity():
    args = sys.argv

    if len(args) < 2:
        print("Usage: github-activity <username>")
        sys.exit(1)
    
    username = args[1]

    if len(args) == 2:
        user_profile = get_user_profile(username)
        user_info = get_user_info(username)
        print_user_profile(user_profile)
        print_user_info(user_info)
        if not user_info:
            print("No activity found")

    elif len(args) == 3:
        command = args[2]
        user_info = get_user_info(username)
        output_check = False
        print(f"=========== User {command} Activity ===========")
        for event in user_info:
            if event["type"] == command:
                print(format_event(event))
                output_check = True
        if not output_check:
            print("No activity found")


if __name__ == "__main__":

    print_activity()
    
