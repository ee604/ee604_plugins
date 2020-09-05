import numpy as np
import subprocess

assignment_no_list = [0]
task_no_list = [3]
def download_dataset(assignment_no=0, task_no=3):
    if (assignment_no in assignment_no_list) and (task_no in task_no_list):
        url = "https://github.com/ee604/ee604_assignments/raw/master/assignment_" + str(assignment_no) + "/data/task_" + str(task_no) + ".zip"
        subprocess.check_output(["wget", "-O", "data.zip", url])
        subprocess.check_output(["unzip", "-o", "data.zip", "-d", "./data/"])
        print("Download Complete!")
    else:
        print("No dataset available for assignment", assignment_no, ", task no", task_no)
