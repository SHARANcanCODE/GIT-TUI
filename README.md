# Git TUI Client

A terminal-based Git client built with Python and the `urwid` library, providing a Text User Interface (TUI) for common Git operations.

## Features

- Clone a Git repository
- View current Git status
- Stage files for commit
- Commit changes with a message
- Push changes to GitHub or remote origin
- View recent Git logs

## How the TUI Works

The application uses the `urwid` Python library to build an interactive terminal interface composed of buttons, text inputs, and output areas. Users interact with the program through keyboard input and menu buttons to execute Git commands under the hood.

## folder structure 

git-tui-client/
│
├── src/
│ ├── main.py # Entry point
│ ├── tui.py # TUI interface definition
│ ├── git_utils.py # Git command helpers
│ └── config.py # Configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Prerequisites

- Python 3.8 or above
- Git installed and available in your system PATH

## Use the menu buttons or keyboard shortcuts:

- Select "Clone Repo" to enter a repository URL to clone
- Use "Status" to see current git status of the repo
- "Stage File" to stage changes by entering filename
- "Commit" to commit staged changes with a message
- "Push" to push commits to origin remote
- "Git Log" to display last 10 commit messages
- "Quit" or press `q` or `esc` to exit