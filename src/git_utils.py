import subprocess
import os

def run_git_command(repo_path, args):
    try:
        process = subprocess.run(
            ["git"] + args,
            cwd=repo_path,
            text=True,
            capture_output=True,
            check=True,
        )
        return process.stdout.strip() or "Success"
    except subprocess.CalledProcessError as e:
        return e.stderr.strip() or "Error running git command"

def clone_repo(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    if os.path.isdir(repo_name):
        return f"Repo {repo_name} already exists."
    try:
        process = subprocess.run(
            ["git", "clone", repo_url],
            text=True,
            capture_output=True,
            check=True,
        )
        return f"Cloned {repo_url} successfully."
    except subprocess.CalledProcessError as e:
        return e.stderr.strip() or "Error cloning repo."

def git_status(repo_path):
    return run_git_command(repo_path, ["status", "--short"])

def stage_file(repo_path, filename):
    full_path = os.path.join(repo_path, filename)
    if not os.path.exists(full_path):
        return f"File {filename} does not exist in repo."
    return run_git_command(repo_path, ["add", filename])

def commit_changes(repo_path, message):
    if not message.strip():
        return "Commit message cannot be empty."
    return run_git_command(repo_path, ["commit", "-m", message])

def push_changes(repo_path):
    return run_git_command(repo_path, ["push"])

def git_log(repo_path, max_entries=10):
    args = ["log", f"-n{max_entries}", "--pretty=format:%h - %an: %s"]
    return run_git_command(repo_path, args)
