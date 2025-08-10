import os
import yaml
import requests

GITHUB_API = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {os.environ['GH_TOKEN']}",
    "Accept": "application/vnd.github+json"
}

def create_milestone(repo, title, description, due_on):
    url = f"{GITHUB_API}/repos/{repo}/milestones"
    payload = {
        "title": title,
        "description": description,
        "due_on": due_on
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["number"]

def create_issue(repo, title, labels, milestone_number=None):
    url = f"{GITHUB_API}/repos/{repo}/issues"
    payload = {
        "title": title,
        "labels": labels
    }
    if milestone_number:
        payload["milestone"] = milestone_number
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()

def sync_milestones():
    milestone_dir = "project-config/milestones"
    for file in os.listdir(milestone_dir):
        if file.endswith(".yml"):
            repo_name = file.replace(".yml", "")
            with open(os.path.join(milestone_dir, file)) as f:
                data = yaml.safe_load(f)
                for milestone in data["milestones"]:
                    milestone_number = create_milestone(
                        repo=repo_name,
                        title=milestone["title"],
                        description=milestone["description"],
                        due_on=milestone["due_on"]
                    )
                    for issue in milestone["issues"]:
                        create_issue(
                            repo=repo_name,
                            title=issue["title"],
                            labels=issue["labels"],
                            milestone_number=milestone_number
                        )

def sync_epics():
    with open("project-config/epics.yml") as f:
        data = yaml.safe_load(f)
        for epic in data["epics"]:
            for repo in epic["repos"]:
                create_issue(
                    repo=repo,
                    title=f"[EPIC] {epic['title']}",
                    labels=epic["labels"]
                )

if __name__ == "__main__":
    sync_milestones()
    sync_epics()