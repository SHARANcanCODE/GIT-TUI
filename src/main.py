from tui import GitTUIApp

def main():
    print("Starting Git TUI Client...") 
    app = GitTUIApp()
    print("GitTUIApp instantiated...")   
    app.run()
    print("App run finished.")            

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error running the app: {e}")



# This code serves as the entry point for the Git TUI application.
# It imports the GitTUIApp class from the tui module and runs the application.
# The main function is called when the script is executed directly.
# This structure allows for easy testing and modularity in the codebase.