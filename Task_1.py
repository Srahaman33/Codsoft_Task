import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        labox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = labox.curselection()
    if selected_task_index:
        labox.delete(selected_task_index)

def update_task():
    selected_task_index = labox.curselection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            labox.delete(selected_task_index)
            labox.insert(selected_task_index[0], updated_task)
            entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create GUI components
frame = tk.Frame(app)
frame.pack(pady=10)

labox = tk.Listbox(frame, selectmode=tk.SINGLE)
labox.pack(side=tk.LEFT, padx=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT)

add_button = tk.Button(app, text="Add Task", width=20, command=add_task)
add_button.pack()

remove_button = tk.Button(app, text="Remove Task", width=20, command=remove_task)
remove_button.pack()

update_button = tk.Button(app, text="Update Task", width=20, command=update_task)
update_button.pack()

app.mainloop()
