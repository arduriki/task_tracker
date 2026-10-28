import sys

# Get all the CLI arguments.
arg_list = sys.argv

# If the user doesn't enter any action.
try:
    action = arg_list[1]
except IndexError:
    print("unknown action")
    sys.exit(1)

if action == "add":
    if len(arg_list) > 3:
        print("Use quotation marks as a description of the task.")
        sys.exit(1)

    try:
        # Store the task in a variable
        added_task = arg_list[2]
        print(f"Task added: {added_task}.")
    except IndexError:
        print("No task to add.")
        sys.exit(1)

elif action == "update":
    if len(arg_list) > 4:
        print("Use quotation marks as a description of the task to be updated.")
        sys.exit(1)

    try:
        # Select the number and convert it into a number
        number_task = int(arg_list[2])

        try:
            description_task = arg_list[3]
            print(f"Description of the task updated as: {description_task}")
        except IndexError:
            print("Enter a description for the task to be updated.")
    except IndexError:
        print("No task to update selected")
    except ValueError:
        print("Enter a task number to update.")

elif action == "delete":
    if len(arg_list) > 3:
        print("Enter just ONE number in order to delete the task.")
        sys.exit(1)

    try:
        # Select the number of task to delete.
        number_task = int(arg_list[2])
        print(f"Task to delete: {number_task}")
    except IndexError:
        print("No task to delete selected")
    except ValueError:
        print("Enter a task number to delete.")

elif action == "mark-in-progress":
    if len(arg_list) > 3:
        print("Enter just ONE number in order to mark the task as in progress.")
        sys.exit(1)
    
    try:
        # Select the number of task to update status.
        number_task = int(arg_list[2])
        print(f"Task {number_task} has been marked as in progress.")
    except IndexError:
        print("No task number has been selected to be marked in progress.")
    except ValueError:
        print("Enter a task number to update its status as in progress.")

elif action == "mark-done":
    if len(arg_list) > 3:
        print("Enter just ONE number in order to mark the task as done.")
        sys.exit(1)
        
    try:
        # Select the number of task to update status.
        number_task = int(arg_list[2])
        print(f"Task {number_task} has been marked as done.")
    except IndexError:
        print("No task number has been selected to be marked as done.")
    except ValueError:
        print("Enter a task number to update its status as done.")

elif action == "list":
    if len(arg_list) > 3:
        print("Enter an appropriate status to be listed under quotation marks.")
        sys.exit(1)

    try:
        status = arg_list[2]

        match status:
            case "done":
                print("done")
            case "todo":
                print("todo")
            case "in-progress":
                print("in progress")
            case _:
                print("unknown status")
    except IndexError:
        print("listing all tasks")

else:
    print("unknown action")
