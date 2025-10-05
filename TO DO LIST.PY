import json

# Load existing tasks from a file (if any)
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Not done"
            print(f"{index}. {task['name']} - {status}")

# Add a new task
def add_task(tasks):
    name = input("What task do you want to add? ")
    tasks.append({"name": name, "done": False})
    print("Task added.")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Enter task number to mark as done: "))
        tasks[number - 1]["done"] = True
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Enter task number to delete: "))
        deleted = tasks.pop(number - 1)
        print(f"Deleted task: {deleted['name']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

# The main app loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Please choose a valid option (1 to 5).")

# Start the app
main()
