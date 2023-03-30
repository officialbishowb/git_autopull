import json
import os
import subprocess
from plyer import notification


# ============ VARIABLE ============
pull_count = 0





def load_config():
    '''Load config.json file and return it as a dictionary'''
    with open("config.json") as f:
        return json.load(f)

def notify(title, message):
    '''Send notification to the user using plyer with the given title and message'''
    notification.notify(
        title=title,
        message=message,
        timeout=2,
    )
    
    
def pull_from_repo_folder(folder_path):
    '''Pull from all repositories inside given folder'''
    list_folder = os.listdir(folder_path)
    for folder in list_folder:
        if os.path.isdir(folder_path + "/" + folder):
            os.chdir(folder_path + "/" + folder)
            
            # Check if the folder is a git repository
            if not os.path.exists(".git"):
                continue
            
            # Check if the folder is the same folder as the script
            if os.path.abspath(folder_path + "/" + folder) == os.path.abspath(os.getcwd()):
                continue
            
            output = subprocess.check_output(["git", "pull"]).decode("utf-8")
            if "Already up to date" not in output:
                pull_count += 1
            
            
def pull_from_repo_list(repo_list):
    '''Pull from all repositories in the given list'''
    for repo in repo_list:
        
        os.chdir(repo)
        # Check if the folder is a git repository
        if not os.path.exists(".git"):
            continue
        
        # Check if the folder is the same folder as the script
        if os.path.abspath(repo) == os.path.abspath(os.getcwd()):
            continue
        
        output = subprocess.check_output(["git", "pull"]).decode("utf-8")
        if "Already up to date" not in output:
            pull_count += 1
            
            


def main():
    config = load_config()
    print("==== Pulling from repositories ====")
    
    
    if config.get('repositories_folder_path', None):
        pull_from_repo_folder(config.get('repositories_folder_path'))
        
    if config.get('repositories_path', None):
        pull_from_repo_list(config.get('repositories_path'))
        
    message = "No new updates" if pull_count <= 0 else f"Successfully pulled {pull_count} repositories."
    
    notify("Git Pull", message)
    
    print(message)
    quit()
    
    
if __name__ == "__main__":
    main()