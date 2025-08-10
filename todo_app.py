import os
import json
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama for colors
init(autoreset=True)

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

tasks = load_tasks()

def show_tasks():
    if not tasks:
        print(Fore.YELLOW + "\nNo tasks yet.")
        return
    
    total = len(tasks)
    completed = sum(1 for _, done, _ in tasks if done)
    print(Fore.CYAN + f"\nYour To-Do List ({completed}/{total} completed):")
    print(Fore.YELLOW + "-" * 40)
    
    for i, (task, done, added_on) in enumerate(tasks, 1):
        status = Fore.GREEN + "✅" if done else Fore.RED + "❌"
        print(f"{Fore.MAGENTA}{i}. {Fore.WHITE}{task} [{status}{Fore.WHITE}] - Added: {Fore.CYAN}{added_on}")
    print(Fore.YELLOW + "-" * 40)

def add_task():
    task = input(Fore.BLUE + "Enter task: ").strip()
    if task:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append([task, False, timestamp])
        save_tasks()
        print(Fore.GREEN + "✅ Task added!")
    else:
        print(Fore.RED + "❌ Task cannot be empty.")

def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input(Fore.BLUE + "Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1][1] = True
            save_tasks()
            print(Fore.GREEN + "✅ Task marked as done!")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input(Fore.BLUE + "Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            save_tasks()
            print(Fore.GREEN + f"🗑️ Task '{removed_task[0]}' deleted!")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def main():
    while True:
        print(Fore.YELLOW + "\n====== To-Do List Menu ======")
        print(Fore.CYAN + "1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        print(Fore.YELLOW + "=============================")
        
        choice = input(Fore.BLUE + "Choose an option (1-5): ").strip()
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(Fore.MAGENTA + "👋 Goodbye!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
