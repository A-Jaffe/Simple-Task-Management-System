# Declare global variables for program
not_complete = "No"
task_count = 0

# Import datetime library
from datetime import date
import os


# Define menu choice function
def menu_select():
    
    menu_choice = input('''Please select one of the following options below:
r - Register a new user 
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
vs - View statistics 
e - Exit
: ''').lower()
        
    # For ONLY admin to register new users
    if menu_choice == 'r':
        if user_name == 'admin' and user_password == 'adm1n':
            reg_user()

        else:
            print("\nOnly the admin may register new users. ")

    # For admin/user to add a new task
    elif menu_choice == 'a':
        add_task()

    # For admin/user to view ALL tasks 
    elif menu_choice == 'va':
        view_all()

    # For admin/user to view a USERNAME specific task
    elif menu_choice == 'vm':
        view_mine()

    # For ONLY admin to view statistics
    elif menu_choice == 'vs':
        if user_name == 'admin' and user_password == 'adm1n':
            view_stats()

        else:
            print("\nOnly the admin may view statistics. ")
            menu_select()

    # For ONLY admin to generate report files    
    elif menu_choice == 'gr':
        generate_report()
        
    # Exit the program
    elif menu_choice == 'e':
        print('Thank you and goodbye!')
        exit()

    # When user inputs invalid menu option
    else:
        print("You have made a wrong choice, Please Try again \n")
        menu_select()


# Define register user function
def reg_user():
    new_name = input("Please enter a new username: ")
    new_pass = input("Please enter a new password: ")
    confirm_pass = input("Please confirm your password: ")

    # If user already exists, restart reg_user function
    if new_pass == confirm_pass:
        with open ('user.txt', 'r') as user_file:
            user_check = user_file.read()
            if new_name in user_check:
                print("\nThat username already exists")
                reg_user()

            # Write new user and password to user.txt file
            else:
                with open ('user.txt', 'a') as user_file:
                    save_data = f", {new_name}, {new_pass}"
                    user_file.write(save_data)
                    print("The new username and password have been added to the registry! ")

                    
# Define add task function
def add_task():
    user_task = input("Please enter the username to whom the task is assigned: ")
    task_title = input("Please enter the title of the task: ")
    task_descrip = input("Please enter a description of the task: ")
    due_date = input("Please enter the date this task is due (in the format yyyy-mm-dd): ")
    today_date = date.today()
    task_data = (f"{user_task}, {task_title}, {task_descrip}, {due_date}, {today_date}, {not_complete} ")
    print("Thank you, the task has been added. ")

    # Write new task data to tasks.txt file
    with open('tasks.txt', 'a') as task_file:
        task_file.write("\n" + task_data)

        
# Define view all tasks function
def view_all():
    with open('tasks.txt', 'r') as task_file:
        for line in task_file:
            line.split("\n")
            task_line = line.split(",") 

            # Display all tasks in easy to read manner
            print(f"Assigned to:\t\t  {task_line[0]} \n")
            print(f"Task:\t\t\t {task_line[1]} \n")
            print(f"Description:\t\t {task_line[2]} \n")
            print(f"Due Date:\t\t {task_line[3]} \n")
            print(f"Date assigned:\t\t {task_line[4]} \n")
            print(f"Completed:\t\t {task_line[-1]} \n")
            print("----------------------------------")

            
# Define view my task function
def view_mine():
    task_file = open('tasks.txt', 'r')
    task_count = 0
    task_update = ""
    user_tasks = []
    all_tasks = []
    for line in task_file:
        task_count +=1
        line.split("\n")
        task_line = line.split(",")
        all_tasks.append(task_line)

        # Display tasks assigned to specific user in easy to read manner
        if user_name == task_line[0]:
            user_tasks.append(task_line)
            print(f"Task number {task_count}:")
            print(f"Assigned to:\t\t  {task_line[0]} \n")
            print(f"Task:\t\t\t {task_line[1]} \n")
            print(f"Description:\t\t {task_line[2]} \n")
            print(f"Due Date:\t\t {task_line[3]} \n")
            print(f"Date assigned:\t\t {task_line[4]} \n")
            print(f"Completed:\t\t {task_line[-1]} \n")
            print("----------------------------------")

    # Request task number to edit from user or return to main menu             
    edit_select = int(input("Enter the task number you would like to edit: (or enter -1 to return to menu) \n")) -1
    
    task = all_tasks[edit_select]

    # If user inputs '-1', return to main menu 
    if str(edit_select) == '-2':
        print("\n")
        menu_select()

    # If user selects a specific task, request what type of edit they would like to make    
    edit_choice = int(input("Would you like to mark the task complete (enter: 1) or edit the task(enter: 2)?"))

    # If user chooses to mark a task complete
    if str(edit_choice) == '1' and (task[5] == " No\n") or (task[5] == " No \n"):
        task[5] = "Yes \n"
        for i in range(len(all_tasks)):
            task_update += ', '.join(all_tasks[i])

        # Update task in file from "No" to "Yes"
        with open('tasks.txt','w') as task_file:
            task_file.write(task_update.replace('  ', ' '))
            print("\nThe task has been successfully updated. ")

    # If task already marked complete, tell user
    elif str(edit_choice) == "1" or str(edit_choice) == '2' and (task[5] == " Yes\n") or (task[5] == " Yes \n") \
    or (task[5] == " Yes"):
        print("\nYou can only edit tasks that have not been marked complete. ")

    # If user chooses to edit the task, ask if they would like to change username or due date
    if str(edit_choice) == '2' and (task[5] == " No\n") or (task[5] == " No \n"):
        kind_of_edit = input("Would you like to edit the username(enter: u) or the due-date(enter: d) of the task?").lower()

        # If user chooses to change the username of who task is assigned to
        if kind_of_edit == 'u':
            name_edit = input("Please enter a new username for the task: ")
            task[0] = name_edit
            for i in range(len(all_tasks)):
                task_update += ', '.join(all_tasks[i])

            # Write updated task to task.txt file
            with open('tasks.txt', 'w') as task_file:
                task_file.write(task_update.replace('  ', ' '))
                print("\nThe task has been successfully updated. ")

        # If user chooses to change the duedate of the tasks    
        elif kind_of_edit == 'd':
            duedate_edit = input("Please enter a new due date for the task (in the format yyyy-mm-dd): ")
            task[3] = duedate_edit
            print("\n")
            for i in range(len(all_tasks)):
                task_update += ', '.join(all_tasks[i])

            # Write updated task to task.txt file
            with open('tasks.txt', 'w') as task_file:
                task_file.write(task_update.replace('  ', ' '))
                print("\nThe task has been successfully updated. ")

        
# Define view statistics function, ONLY for admin
def view_stats():
    if user_name == 'admin' and user_password == 'adm1n':

        # If overview files have not yet been generated, call generate_report() function
        generate_report()

        # Display task_overview and user_overview information in an easy to read manner
        print("Task Overview Information ")
        print("------------------------------------------------------------------- \n")
        with open('task_overview.txt', 'r') as task_file:
            for line in task_file:
                print(line.strip("\n"))
        print("\n------------------------------------------------------------------- \n")   
        print("\nUser Overview Information ")
        print("------------------------------------------------------------------- \n")
        with open('user_overview.txt', 'r') as user_file:
            for line in user_file:
                print(line.strip("\n"))
        print("------------------------------------------------------------------- ")

    # If user not admin, display message and return to main menu
    else:
        print("Only the admin may view statistics.")
        menu_select()

        
# Define generate report function
def generate_report():
    task_summary = ""
    user_summary = ""
    user_tasks = []
    all_tasks = []
    due_date = []
    user_dictionary = {}
    complete_dict = {}
    not_complete_dict = {}
    overdue_dict = {}
    a = 0
    b = 0
    overdue = 0
    import datetime

    # If user not admin, display message and return to main menu
    if user_name != 'admin' and user_password != 'adm1n':
         print("\nOnly the admin may generate reports. \n")
         menu_select()
         
    elif user_name == 'admin' and user_password == 'adm1n':

        # Task Overview information
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                line.split("\n")
                task_line = line.split(",")
                all_tasks.append(task_line)

            # Determine which tasks are complete and which tasks are incomplete
            for i in range(len(all_tasks)):
                if " Yes\n" in all_tasks[i]:
                    a += 1
                elif " Yes \n" in all_tasks[i]:
                    a += 1
                elif " Yes" in all_tasks[i]:
                    a +=1
                elif " No\n" in all_tasks[i]:
                    b += 1
                elif " No \n" in all_tasks[i]:
                    b += 1
                elif " No" in all_tasks[i]:
                    b += 1
                
                # Retrieve due dates from each task as well as today's date for overdue check
                due_date.append(all_tasks[i][3])
                due_string = due_date[i].split('-')
                due_year = due_string[0].strip()
                due_month = due_string[1]
                due_day = due_string[2]
                date_now = str(datetime.date.today())
                date_string = date_now.split("-")
                year_now = date_string[0]
                month_now = date_string[1]
                day_now = date_string[2]

                # Determine which tasks are overdue
                if due_year < year_now and " No\n" in all_tasks[i] or " No \n" in all_tasks[i] or " No" in all_tasks[i]:
                    overdue += 1
                    
                elif due_year == year_now and due_month < month_now and " No\n" in all_tasks[i] or " No \n" in all_tasks[i] \
                or " No" in all_tasks[i]:
                    overdue += 1
                    
                elif due_year == year_now and due_month == month_now and due_day < day_now and " No\n" in all_tasks[i] \
                or " No \n" in all_tasks[i] or " No" in all_tasks[i]:
                    overdue += 1

            # Create task overview summary
            task_summary = task_summary + (f"The total number of tasks registered with the task manager is {len(all_tasks)}")
            
            task_summary = task_summary + (f"\nThe total number of completed tasks is {str(a)}.")
            
            task_summary = task_summary + (f"\nThe total number of incomplete tasks is {str(b)}.")
            
            task_summary = task_summary + (f"\nThe total number of tasks that are incomplete and overdue is {overdue}.")

            task_summary = task_summary + (f"\nThe percentage of incomplete tasks is \
{str(round((b / (len(all_tasks))) * 100, 2))}%.")
            
            task_summary = task_summary + (f"\nThe percentage of tasks that are overdue is \
{round((overdue) / (len(all_tasks)) * 100, 2)}%.")

            
            print("\n")
            print("Task overview file has been generated.")
        
        # Write task overview summary to task_overview.txt file
        with open ('task_overview.txt', 'w') as task_overview:
            task_overview.write(str(task_summary))
        
        # User overview information
        user_list = []
        with open('user.txt', 'r') as user_file:
            for line in user_file:
                contents = line.strip()
                contents = contents.split(",")
                for i in range(len(contents)):
                    if i % 2 == 0:
                        user_list.append(contents[i].strip())

        # Create dictionaries for various tallying
        user_dictionary = dict.fromkeys(user_list)
        for key in user_dictionary:
            user_dictionary[key] = 0

        complete_dict = dict.fromkeys(user_list)
        for key in complete_dict:
            complete_dict[key] = 0

        not_complete_dict = dict.fromkeys(user_list)
        for key in not_complete_dict:
            not_complete_dict[key] = 0

        overdue_dict = dict.fromkeys(user_list)
        for key in overdue_dict:
            overdue_dict[key] = 0

    # Read from task.txt file to tally complete, incomplete and overdue tasks        
    with open('tasks.txt', 'r') as task_file:
        for line in task_file:
            line.split("\n")
            line.strip()
            task_line = line.split(",")
            user_tasks.append(task_line)
            
            # Tally each user's task amount
            for word in task_line:
                if word in user_dictionary:
                    user_dictionary[word] = user_dictionary[word] + 1
            
            # Tally complete tasks for each user
            for key in complete_dict:
                if task_line[0] == key and task_line[5].strip() == "Yes":
                    complete_dict[key] = complete_dict[key] + 1

            # Tally incomplete tasks for each user
            for key in not_complete_dict:
                if task_line[0] == key and task_line[5].strip() == "No":
                    not_complete_dict[key] = not_complete_dict[key] + 1
            
            # Retrieve due dates from each task as well as today's date for overdue check
            for i in range(len(user_tasks)):
                due_date.append(user_tasks[i][3])
                due_string = due_date[i].split('-')
                due_year = due_string[0].strip()
                due_month = due_string[1]
                due_day = due_string[2]
                date_now = str(datetime.date.today())
                date_string = date_now.split("-")
                year_now = date_string[0]
                month_now = date_string[1]
                day_now = date_string[2]
                
            # Determine which tasks for each user are both incomplete and overdue
            for key in overdue_dict:
                if task_line[0] == key: 
                    if task_line[5].strip() == "No" and due_year < year_now:
                        overdue_dict[key] = overdue_dict[key] + 1
                    elif task_line[5].strip() == "No" and due_year == year_now and due_month < month_now:
                        overdue_dict[key] = overdue_dict[key] + 1
                    elif task_line[5].strip() == "No" and due_year == year_now and due_month == month_now and due_day < day_now:
                        overdue_dict[key] = overdue_dict[key] + 1

#--------------------------------------------------------------------------------------------------------------------------------------------        

        # Create user overview summary
        user_summary = user_summary + (f"The total number of users registered is {round(user_amount/ 2)}.")

        user_summary = user_summary + (f"\nThe total number of tasks generated and tracked by the task manager is \
{str(len(all_tasks))}.\n")
        user_summary = user_summary + ("\n")

        # For each username in users.txt file, summarize all relevant task information
        for key in list(user_dictionary.keys()):
            user_summary = user_summary + (f"The total tasks assigned to {key} is: {user_dictionary[key]}\n")
            user_summary = user_summary + (f"The percentage of tasks assigned to {key} is: \
{round((user_dictionary[key] / len(all_tasks)) * 100, 2)}% \n")
            user_summary = user_summary + (f"The percentage of completed tasks assigned to {key} is: \
{round(complete_dict[key] / user_dictionary[key] * 100, 2)}% \n")
            user_summary = user_summary + (f"The percentage of tasks not yet completed, assigned to {key} is: \
{round(not_complete_dict[key] / user_dictionary[key] * 100, 2)}% \n")
            user_summary = user_summary + (f"The percentage of incomplete and overdue tasks assigned to {key} is: \
{round(overdue_dict[key] / user_dictionary[key] * 100, 2)}% ")
            user_summary = user_summary + ("\n \n")

        
        print("User overview file has been generated.")
        print("\n")

        # Write user overview summary to user_overview.txt file
        with open('user_overview.txt', 'w') as user_overview:
            user_overview.write(str(user_summary))

# ====Login Section====
# Read usernames and passwords from file
with open('user.txt', 'r') as user_file:
    for line in user_file:
        contents = line.strip()
        contents = contents.split(",")
        user_amount = len(contents)

        for i in range(user_amount):
            user_on_file = str(contents)
   
# Request username and password from user
    login = False
    print("Welcome to the task manager! \n")
    user_name = input("Please enter a username: ")
    user_password = input("Please enter a password: ")

    while login == False:

        # If neither username or password in users.txt
        if user_name not in user_on_file and user_password not in user_on_file:
            print("\nYou have entered an incorrect username and password, please try again \n")
            user_name = input("Please enter a valid username: ")
            user_password = input("Please enter a valid password: ")
            login = False

        # If username is in users.txt but password is not
        elif user_name in user_on_file and user_password not in user_on_file or user_password == "":
            print("\nYou have entered a correct username but an incorrect password, please try again. ")
            user_name = input("Please enter a valid username: ")
            user_password = input("Please enter a valid password: ")
            login = False

        # If username is not in users.txt but password is
        elif user_name not in user_on_file or user_name == "" and user_password in user_on_file:
            print("\nYou have entered an incorrect username and a correct password, please try again. ")
            user_name = input("Please enter a valid username: ")
            user_password = input("Please enter a valid password: ")
            login = False

        # If the user does not enter anything
        elif user_name == "" and user_password == "":
            print("\nYou have not entered anything, please try again \n")
            user_name = input("Please enter a valid username: ")
            user_password = input("Please enter a valid password: ")
            login = False

        # If username and password are in users.txt, allow user to proceed to main menu    
        elif user_name in user_on_file and user_password in user_on_file:
            print("\n")
            menu_select()
