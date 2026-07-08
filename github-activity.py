import sys
import urllib.request
import json
import datetime

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
    json_cache = load_cache(username)
    if json_cache:
        return json_cache
    else:
        url = f"https://api.github.com/users/{username}/events"
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read())
                save_cache(username, data)
                return data
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

def print_user_info(info):
    print("=========== User Activity ===========")
    for event in info:
        result = format_event(event)
        if result:
            print(result)

def format_event(event):
    event_type = event["type"]
    repo_name = event["repo"]["name"]
    payload = event["payload"]

    if event_type == "PushEvent":
        return f"- Pushed to {repo_name}"
    elif event_type == "CommitCommentEvent":
        return f"- Commented on a commit in {repo_name}"
    elif event_type == "CreateEvent":
        ref_type = payload["ref_type"]
        ref = payload.get("ref", "")
        if ref:
            return f"- Created {ref_type} '{ref}' in {repo_name}"
        else:
            return f"- Created {ref_type} in {repo_name}"
    elif event_type == "DeleteEvent":
        ref_type = payload["ref_type"]
        ref = payload["ref"]
        return f"- Deleted {ref_type} '{ref}' in {repo_name}"
    elif event_type == "DiscussionEvent":
        action = payload["action"]
        return f"- {action.capitalize()} a discussion in {repo_name}"
    elif event_type == "ForkEvent":
        return f"- Forked {repo_name}"
    elif event_type == "GollumEvent":
        return f"- Updated wiki in {repo_name}"
    elif event_type == "IssueCommentEvent":
        issue_title = payload["issue"]["title"]
        return f"- Commented on issue '{issue_title}' in {repo_name}"
    elif event_type == "IssuesEvent":
        action = payload["action"]
        return f"- {action.capitalize()} an issue in {repo_name}"
    elif event_type == "MemberEvent":
        action = payload["action"]
        member = payload["member"]["login"]
        return f"- {action.capitalize()} member '{member}' in {repo_name}"
    elif event_type == "PublicEvent":
        return f"- Made {repo_name} public"
    elif event_type == "PullRequestEvent":
        action = payload["action"].capitalize()
        number = payload["number"]
        return f"- {action} pull request #{number} in {repo_name}"
    elif event_type == "PullRequestReviewEvent":
        state = payload["review"]["state"]
        return f"- {state.capitalize()} a pull request review in {repo_name}"
    elif event_type == "PullRequestReviewCommentEvent":
        return f"- Commented on a pull request review in {repo_name}"
    elif event_type == "ReleaseEvent":
        action = payload["action"]
        tag = payload["release"]["tag_name"]
        return f"- {action.capitalize()} release '{tag}' in {repo_name}"
    elif event_type == "WatchEvent":
        return f"- Starred {repo_name}"
    else:
        return None

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
            if event["type"].lower() == command.lower():
                print(format_event(event))
                output_check = True
        if not output_check:
            print("No activity found")

def save_cache(username, data):
    cache = {
        "timestamp": datetime.datetime.now().isoformat(),
        "data": data
    }
    with open(f"cache_{username}.json", "w") as f:
        json.dump(cache, f, indent=4)

def load_cache(username):
    try:
        with open(f"cache_{username}.json", "r") as f:
            cache = json.load(f)
        
        cached_time = datetime.datetime.fromisoformat(cache["timestamp"])
        now = datetime.datetime.now()
        diff = now - cached_time

        if diff.total_seconds() < 300:
            return cache["data"]
        else:
            return None

    except FileNotFoundError:
        return None  
    except json.JSONDecodeError:
        return None


if __name__ == "__main__":

    print_activity()


    
