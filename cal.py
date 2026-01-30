import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result.set(num1 + num2)
        elif operation == "sub":
            result.set(num1 - num2)
        elif operation == "mul":
            result.set(num1 * num2)
        elif operation == "div":
            if num2 == 0:
                result.set("Error")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid Input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")
root.resizable(False, False)

# Variables
result = tk.StringVar()

# Labels & Entries
tk.Label(root, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", width=20, command=lambda: calculate("add")).pack(pady=5)
tk.Button(root, text="Subtract", width=20, command=lambda: calculate("sub")).pack(pady=5)
tk.Button(root, text="Multiply", width=20, command=lambda: calculate("mul")).pack(pady=5)
tk.Button(root, text="Divide", width=20, command=lambda: calculate("div")).pack(pady=5)

tk.Button(root, text="Clear", width=20, command=clear).pack(pady=5)

# Result
tk.Label(root, text="Result").pack(pady=5)
tk.Entry(root, textvariable=result, state="readonly").pack()

root.mainloop() 