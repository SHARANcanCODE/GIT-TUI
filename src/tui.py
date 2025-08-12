import urwid
from git_utils import (
    clone_repo,
    git_status,
    stage_file,
    commit_changes,
    push_changes,
    git_log,
)

class GitTUIApp:
    def __init__(self):
        self.repo_path = None  # Current repo path
        self.status_text = urwid.Text("Welcome to Git TUI Client! Please clone a repo to begin.")
        self.output_box = urwid.Text("")
        self.input_edit = urwid.Edit("Input: ")
        self.stage_list = urwid.SimpleFocusListWalker([])
        self.log_list = urwid.SimpleFocusListWalker([])
        
        # Menu buttons
        menu = urwid.Columns([
            urwid.Button("Clone Repo", on_press=self.clone_repo_prompt),
            urwid.Button("Status", on_press=self.show_status),
            urwid.Button("Stage File", on_press=self.stage_file_prompt),
            urwid.Button("Commit", on_press=self.commit_prompt),
            urwid.Button("Push", on_press=self.push_changes),
            urwid.Button("Git Log", on_press=self.show_log),
            urwid.Button("Quit", on_press=lambda button: raise_exit()),
        ])

        #  Header, Menu, Output, Input
        header = urwid.AttrMap(urwid.Text("Git TUI Client", align="center"), "header")
        self.menu = urwid.AttrMap(menu, "menu")
        self.output = urwid.LineBox(urwid.ListBox(self.log_list), title="Output")
        self.input = urwid.LineBox(self.input_edit, title="Input")

        self.main_frame = urwid.Frame(
            header=header,
            body=urwid.Pile([self.menu, self.output, self.input]),
            footer=urwid.AttrMap(self.status_text, "status"),
        )

    def run(self):
        print("Launching UI loop...")
        palette = [
            ("header", "white,bold", "dark blue"),
            ("menu", "light cyan", "black"),
            ("status", "yellow", "black"),
            ("reversed", "standout", ""),
        ]
        loop = urwid.MainLoop(self.main_frame, palette, unhandled_input=self.handle_input)
        loop.run()

    def handle_input(self, key):
        if key in ("q", "Q", "esc"):
            raise urwid.ExitMainLoop()

    def clone_repo_prompt(self, button):
        self.status_text.set_text("Enter repository URL to clone:")
        self.input_edit.set_edit_text("")
        self.input_edit.set_caption("Repo URL: ")
        self.set_input_callback(self.clone_repo_execute)

    def clone_repo_execute(self, text):
        url = text.strip()
        if not url:
            self.status_text.set_text("Error: URL cannot be empty")
            return
        self.status_text.set_text(f"Cloning repo from: {url} ...")
        result = clone_repo(url)
        self.status_text.set_text(result)
        if "Cloned" in result or "already exists" in result:
            self.repo_path = url.split("/")[-1].replace(".git", "")
        self.clear_input_callback()

    def show_status(self, button):
        if not self.repo_path:
            self.status_text.set_text("No repo cloned yet!")
            return
        self.status_text.set_text(f"Git status for: {self.repo_path}")
        status_output = git_status(self.repo_path)
        self.output.original_widget = urwid.Text(status_output)

    def stage_file_prompt(self, button):
        if not self.repo_path:
            self.status_text.set_text("No repo cloned yet!")
            return
        self.status_text.set_text("Enter filename to stage:")
        self.input_edit.set_edit_text("")
        self.input_edit.set_caption("File to stage: ")
        self.set_input_callback(self.stage_file_execute)

    def stage_file_execute(self, text):
        filename = text.strip()
        if not filename:
            self.status_text.set_text("Filename cannot be empty")
            return
        result = stage_file(self.repo_path, filename)
        self.status_text.set_text(result)
        self.clear_input_callback()

    def commit_prompt(self, button):
        if not self.repo_path:
            self.status_text.set_text("No repo cloned yet!")
            return
        self.status_text.set_text("Enter commit message:")
        self.input_edit.set_edit_text("")
        self.input_edit.set_caption("Commit message: ")
        self.set_input_callback(self.commit_execute)

    def commit_execute(self, text):
        message = text.strip()
        if not message:
            self.status_text.set_text("Commit message cannot be empty")
            return
        result = commit_changes(self.repo_path, message)
        self.status_text.set_text(result)
        self.clear_input_callback()

    def push_changes(self, button):
        if not self.repo_path:
            self.status_text.set_text("No repo cloned yet!")
            return
        self.status_text.set_text(f"Pushing to origin from {self.repo_path} ...")
        result = push_changes(self.repo_path)
        self.status_text.set_text(result)

    def show_log(self, button):
        if not self.repo_path:
            self.status_text.set_text("No repo cloned yet!")
            return
        log_output = git_log(self.repo_path)
        self.output.original_widget = urwid.Text(log_output)
        self.status_text.set_text(f"Git log for {self.repo_path}")

    def set_input_callback(self, callback):
        def on_key_press(input_widget, key):
            if key == "enter":
                callback(input_widget.edit_text)
                return True
            return False
        self.input_edit.keypress = on_key_press

    def clear_input_callback(self):
        self.input_edit.set_caption("Input: ")
        self.input_edit.set_edit_text("")
        self.input_edit.keypress = urwid.Edit.keypress

def raise_exit():
    raise urwid.ExitMainLoop()
