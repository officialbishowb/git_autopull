# GitHub Auto Pull

This is a simple script that will automatically pull from a folder containing GitHub repositories. It can be set to run on a schedule, or manually.

## Installation
1. Clone this repository to a folder on your computer.
2. Install the requirements with `pip install -r requirements.txt`.
3. Create a file called `config.json` in the same folder as the script. This file should contain the path to the folder containing the repos or the repos themselves. The file should look like this:
```json
{
    "repositories_folder_path": "path/to/folder/containing/repos",
    "repositories_path": [
        "path/to/repo1","path/to/repo2","path/to/repo3"
    ]
    
}
```
4. Run the script with `python3 main.py`. Or, if you want to run on schedule, do the following:
    ### Windows
    1. Create a shortcut to the script.
    2. Open Task Scheduler and create a new task.
    3. Set the trigger to run on a schedule.

    ### Linux
    1. Create a cron job to run the script on a startup.
