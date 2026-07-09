# GitHub Activity CLI

A simple command line interface (CLI) to fetch and display the recent activity of any GitHub user directly in the terminal. Built with Python using only the standard library.

## Features

- Display GitHub user profile information
- Fetch and display recent GitHub activity
- Filter activity by event type
- Cache results for 5 minutes to avoid unnecessary API calls

## Installation

Clone the repository:

```bash
git clone https://github.com/I-Martes-I/GitHub-User-Activity-CLI-project.git
cd GitHub-User-Activity-CLI-project
```

## Usage

Run the app using:

```bash
github-activity <username>          # Show user profile and all recent activity
github-activity <username> <event>  # Filter activity by event type
```

## Supported Event Types

|              Event                |               Description             |
|-----------------------------------|---------------------------------------|
| `PushEvent`                       | Commits pushed to a repository        |
| `CreateEvent`                     | Branch or tag created                 |
| `DeleteEvent`                     | Branch or tag deleted                 |
| `ForkEvent`                       | Repository forked                     |
| `WatchEvent`                      | Repository starred                    |
| `IssuesEvent`                     | Issue opened, closed, etc.            |
| `IssueCommentEvent`               | Comment on an issue                   |
| `PullRequestEvent`                | Pull request opened, closed, merged   |
| `PullRequestReviewEvent`          | Pull request review submitted         |
| `PullRequestReviewCommentEvent`   | Comment on a pull request review      |
| `CommitCommentEvent`              | Comment on a commit                   |
| `ReleaseEvent`                    | Release published or updated          |
| `MemberEvent`                     | Repository member added or removed    |
| `PublicEvent`                     | Repository made public                |
| `DiscussionEvent`                 | Discussion created or edited          |
| `GollumEvent`                     | Wiki page created or updated          |

## Caching

Results are cached locally in a `cache_<username>.json` file for 5 minutes. This means repeated calls with the same username won't make unnecessary API requests. After 5 minutes the cache expires and fresh data is fetched from GitHub.

## Examples

Input:
```bash
github-activity AsabenehBlaBlaBla
```
Output:
```bash
User 'AsabenehBlaBlaBla' not found.
```

Input:
```bash
github-activity Asabeneh
```
Output:
```bash
======== GitHub User Profile ========
Name:      Asabeneh
Bio:        🌐 Fullstack Engineer🌱 Educator 📘 Content creator 📈 Data Analyst |
I create jargon-free, easy to read and understand educational material
Location:  Helsinki, Finland
Repos:     192
Followers: 21597
Following: 21
Blog:      https://www.asabeneh.com
=========== User Activity ===========
- Starred wix/react-native-ui-lib
- Pushed to Asabeneh/30-Days-Of-AI-Engineering
- Starred SYSTRAN/faster-whisper
- Pushed to Asabeneh/30-Days-Of-AI-Engineering
- Pushed to Asabeneh/30-Days-Of-AI-Engineering
...
```

Input:
```bash
github-activity Asabeneh BlaBlaBla
```
Output:
```bash
Unknown event type 'BlaBlaBla'.
Valid events: PushEvent, CommitCommentEvent, CreateEvent, DeleteEvent, DiscussionEvent, ForkEvent, GollumEvent, IssueCommentEvent, IssuesEvent, MemberEvent, PublicEvent, PullRequestEvent, PullRequestReviewEvent, PullRequestReviewCommentEvent, ReleaseEvent, WatchEvent
```

Input:
```bash
github-activity Asabeneh PushEvent
```

Output:
```bash
=========== User PushEvent Activity ===========
- Pushed to Asabeneh/30-Days-Of-AI-Engineering
- Pushed to Asabeneh/30-Days-Of-AI-Engineering
- Pushed to Asabeneh/30-Days-Of-AI-Engineering
...
```

Input:
```bash
github-activity Asabeneh CreateEvent
```
Output:
```bash
=========== User CreateEvent Activity ===========
- Created branch 'main' in Asabeneh/30-Days-Of-AI-Engineering
```