import sys

"""
sys.arv -> used to get all command-line arguments as a list of strings.
- [0] is the name of the command/app
- [1] is the action
- When listing tasks, [2] is the status
-
"""

# Get all the CLI arguments.
arg_list = sys.argv

# It can't get more than 4 arguments.
if len(arg_list) > 3:
    print("Command not valid")
    sys.exit()

# If the user doesn't enter any action.
try:
    action = arg_list[1]
except IndexError:
    print("unknown action")
    sys.exit()

if action == "add":
    try:
        # Store the task in a variable
        added_task = arg_list[2]
        print(f"Task added: {added_task}.")
    except IndexError:
        print("No task to add.")

if action == "update":
    try:
        # Select the number and convert it into a number
        number_task = int(arg_list[2])
        print(f"Task selected: {number_task}")

        try:
            description_task = arg_list[3]
            print(f"Description of the task updated as: {description_task}")
        except IndexError:
            print("Enter a description for the task to be updated.")
    except IndexError:
        print("No task selected")
    except ValueError:
        print("Enter a task number")

# TODO: continue with update, delete, mark-in-progress, mark-done and list

# try:
#     action = arg_list[1]
#     if action == "list":
#         try:
#             status = arg_list[2]

#             match status:
#                 case "done":
#                     print("done")
#                 case "todo":
#                     print("todo")
#                 case "in-progress":
#                     print("in progress")
#                 case _:
#                     print("unknown status")
#         except IndexError:
#             print("listing all tasks")
#     else:
#         match action:
#             case "add":
#                 print("add")
#             case "update":
#                 print("update")
#             case "delete":
#                 print("delete")
#             case "mark-in-progress":
#                 print("mark in progress")
#             case "mark-done":
#                 print("mark done")
#             case _:
#                 print("wrong action")
