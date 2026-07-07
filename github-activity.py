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
    print("===== GitHub User Profile =====")
    print(f"{'Name:':<10} {profile["name"]}")
    print(f"{'Bio:':<10} {profile["bio"]}")
    print(f"{'Location:':<10} {profile["location"]}")
    print(f"{'Repos:':<10} {profile["public_repos"]}")
    print(f"{'Followers:':<10} {profile["followers"]}")
    print(f"{'Blog:':<10} {profile["blog"]}")
    print("================================")


def get_user_info(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except Exception as err:
        print(f"An error occurred: {err}")
        return None



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



if __name__ == "__main__":

    args = sys.argv

    if len(args) < 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = args[1]
    user_info = get_user_info(username)
    user_profile = get_user_profile(username)
    print_user_profile(user_profile)
"""     print(json.dumps(user_profile, indent=4))
    for event in user_profile:
        print(event) """
    
