from datetime import datetime, timedelta, date

#global variable, constants and lists initialized, to be used and updated in various functions
choice = 2
tasks = []
completed_tasks = []
TODO_FILE = "list.txt"
COMPLETED_FILE = "completed.txt"
ERROR_MESSAGE = "Invalid input! Try Again."
H = "high"
M = "medium"
L = "low"












#Function to display menu options
def display_options():
    print("\nMenu\n")
    print("1. Exit Application")
    print("2. Display To-Do List")
    print("3. Display Completed Tasks List")
    print("4. Add task to To-Do List")
    print("5. Mark a task as 'Completed'")
    print("6. Remove task from To-Do List")
    print("7. Remove task from Completed Tasks List")
    print("8. Display tasks due today") 
    print("9. Display High Priority Tasks")
    print("10. Display Medium Priority Tasks")
    print("11. Display Low Priority Tasks")
    print("12. Display Sorted To-Do List (Date-wise)")
    print("13. Display Sorted To-Do List (Priority-wise)")
    












#Function to fetch data from a file and store it in a global list.
#This function takes file name as a string argument, fetches data from that file and stores it in a temporary list.
#The temporary list is returned and stored in a global list.
def fetch_data(file_name):
    temp_list = []
    with open(file_name, "rt") as file:
        while True:#loop runs infinite times
            task = file.readline() 
            if not task:
                break#loop terminated
            due_date = file.readline() 
            priority = file.readline() 
            file.readline()
            file.readline()
            temp_list.append((f"{task}", f"{due_date}", f"{priority}\n"))#task specifics added to list

    return temp_list












#Function to display a list using for loop to iterate over tbe elements
#The list is provided as an argument
def display_tasks(title, task_list):
    heading(title)
    for i in range(len(task_list)):
       print (f"{i+1}. {task_list[i][0]}   {task_list[i][1]}   {task_list[i][2]} ")





    






#Function to mark a task from to do list as completed.
#This function calls get_index_from_user() function and stores the result in 'index'
#The element at 'index' is appended to completed_tasks list
#This function calls add_task() function to add task to completed tasks file
#This function calls remove_task() function to remove the task from to do list file and stores the new list in 'tasks'
def mark_task_as_complete():
    global tasks, completed_tasks 
    index = get_index_from_user("Which task would you like to mark as completed?", tasks)
    
    completed_tasks = add_task(COMPLETED_FILE, tasks[index][0], tasks[index][1], f"{tasks[index][2]}", completed_tasks)
    tasks = remove_task(TODO_FILE, tasks, index, "Task has been marked completed!")
    











#This function takes file name and task specifics as string arguments and stores task in relevant file
def add_task(file_name, task_to_add, due_date, priority, temp_list):
    
    file = open(file_name, "at")
    file.write(f"{task_to_add}{due_date}{priority}\n")
    file.close()
    temp_list.append((task_to_add, due_date, priority))
    return temp_list
     











#This function displays relevant list, takes input from user of the index of specific element(task) and returns index
def get_index_from_user(message, temp_list):
    display_tasks("",temp_list)
    task_to_remove = int(input(f"{message}(select the number from the list)\n"))-1
    while (task_to_remove < 0 or task_to_remove > (len(temp_list)-1)):
        task_to_remove = int(input(f"{ERROR_MESSAGE} \n{message}(select the number from the list)\n"))-1
    return task_to_remove 













#This function takes relevant file name, relevant list, index of element in list and appropriate output message as arguments
#It removes that particular task(at index) from list, rewrites tasks in relevant file and displays output message on screen
#It returns modified list
def remove_task(file_name, temp_list, task_to_remove, message):
    temp_list.pop(task_to_remove)
    
    file = open(file_name, "wt")
    for task in temp_list:
        file.write(task[0])
        file.write(task[1])
        file.write(task[2])
        file.write("\n")

    file.close()
        
    print(message) 
    return temp_list












#Function to identify tasks that are due today and return their list
#This function compares due date of each task with today's date, adds the task to a list if the dates match and returns that list
def due_today():
    date_today = f"{date.today()}"
    
    tasks_due_today = []
    for task in tasks:
        date_of_task = task[1].replace("Due date: ", "").strip()
        if date_of_task == date_today:
            tasks_due_today.append(task)
    return tasks_due_today












#Function to format text as simple underlined heading
def heading(title):
    print()
    print(title.upper())
    print("-" * len(title))
    print()












#Function to fetch and display all tasks of certain priority
def fetch_priority_tasks(pr): 
    priority = f"Priority: {pr}\n\n"
    
    priority_tasks = []
    for task in tasks: 
        if priority == task[2]:
            priority_tasks.append(task) 
    return priority_tasks

#Function to display all tasks of certain priority
def display_priority_tasks(priority): 
    priority_tasks = fetch_priority_tasks(priority)
    display_tasks(f"{priority} priority tasks", priority_tasks)


    








#Function to sort and display all tasks based on priority
def sort_by_priority():
    sorted_by_priority = fetch_priority_tasks(H) + fetch_priority_tasks(M) + fetch_priority_tasks(L)
    display_tasks("sorted to do list(priority-wise)", sorted_by_priority)


    
    







#Function to sort and display all tasks based on due date
def sort_by_date(): 
    due_dates = []
    for task in tasks:
        due_date = task[1].replace("Due date: ", "").strip()
        #datetime.strptime(due_date, "%Y-%m-%d")
        due_dates.append(due_date)
    
    due_dates.sort()
    
    sorted_by_date = []
    for i in range(len(due_dates)):
        due_dates[i] = f"Due date: {due_dates[i]}\n"
        for task in tasks:
            if task[1] == due_dates[i]:
                sorted_by_date.append(task)
    display_tasks("sorted to do list(date-wise)", sorted_by_date)











    
print("To-Do List Application")

#fetch_data() function is called and the lists returned are stored in tasks and completed_tasks lists
tasks = fetch_data(TODO_FILE)
completed_tasks = fetch_data(COMPLETED_FILE) 

#User driven program
#loops keeps running till user decides to exit program by entering 1
while(choice != 1): 
 
    display_options()

    while True:
        try:
            choice = int(input("\nWhat would you like to do(1-13)?")) 
            if choice < 1 or choice > 13:
                print(ERROR_MESSAGE)
            else:
                break
            
        except ValueError:
            print("Please enter a valid number!")

    
    if choice == 1:
        break
    
    elif choice == 2: 
        display_tasks("to do list", tasks)
        
    elif choice == 3:  
        display_tasks("completed tasks list", completed_tasks) 
        
    elif choice == 4:
        while True:
            task_to_add = input("Enter Task: ").strip()
            if task_to_add:
                break
        task_to_add = f"Task: {task_to_add}\n"
        
        datee = False
        while not datee:
            due_date_input = input("Enter due date(YYYY-MM-DD): ").strip() 
            try:
                datetime.strptime(due_date_input, "%Y-%m-%d")
                datee = True
            except ValueError:
                print(ERROR_MESSAGE)
                datee = False
            due_date = f"Due date: {due_date_input}\n"
        
            
            
        while True:
            priority = input(f"Enter priority({H}, {M}, {L}): ").strip().lower() 
            if priority in[H, M, L]:
                break
            else:
                print(ERROR_MESSAGE) 
        priority = f"Priority: {priority}\n\n"
        
        tasks = add_task(TODO_FILE, task_to_add, due_date, priority, tasks)
        
    elif choice == 5:
        mark_task_as_complete()
        
    elif choice == 6:
        task_to_remove = get_index_from_user("Which task would you like to remove?", tasks)
        tasks = remove_task(TODO_FILE, tasks, task_to_remove, "Task has been removed successfully!")

    elif choice == 7:
        task_to_remove = get_index_from_user("Which task would you like to remove?", completed_tasks)
        completed_tasks = remove_task(COMPLETED_FILE, completed_tasks, task_to_remove, "Task has been removed successfully!")

    elif choice == 8: 
        tasks_due_today = due_today()
        display_tasks("tasks due today", tasks_due_today)

    elif choice == 9:
        display_priority_tasks(H) 

    elif choice == 10:
        display_priority_tasks(M)

    elif choice == 11:
        display_priority_tasks(L)

    elif choice == 12:
        sort_by_date()

    elif choice == 13:
        sort_by_priority()
    
