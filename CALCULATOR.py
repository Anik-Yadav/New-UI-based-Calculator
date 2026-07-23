import customtkinter as ctk
import math

root = ctk.CTk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(True, True)

entry = ctk.CTkEntry(root, justify="right", font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

result_var = ctk.StringVar(value="")
result_label = ctk.CTkLabel(root, textvariable=result_var, font=("Arial", 18))
result_label.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)

def insert_value(val):
    entry.insert("end", val)

def clear_entry():
    entry.delete(0, "end")
    result_var.set("")

def calculate(event=None):
    try:
        expr = entry.get()
        # Handle equality check separately
        if "=" in expr:
            left, right = expr.split("=", 1)
            left_val = eval(left, {"__builtins__": None}, math.__dict__)
            right_val = eval(right, {"__builtins__": None}, math.__dict__)
            result_var.set(str(left_val == right_val))
        else:
            res = eval(expr, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "abs": abs,
                "pow": pow,
                "log": math.log,
                "pi": math.pi,
                "e": math.e
            })
            result_var.set(str(res))
    except Exception as e:
        result_var.set(f"Error: {e}")

buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("+", 5, 2), ("=", 5, 3),   # "=" for arithmetic/equality
    ("sqrt", 6, 0), ("abs", 6, 1), ("pow", 6, 2), ("log", 6, 3),
    ("Execute", 7, 2), ("C", 7, 0)
]

for (text, r, c) in buttons:
    if text in ("=", "Execute"):
        btn = ctk.CTkButton(root, text=text, command=calculate)
    elif text == "C":
        btn = ctk.CTkButton(root, text=text, command=clear_entry)
    else:
        btn = ctk.CTkButton(root, text=text, command=lambda t=text: insert_value(t))
    btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.bind("<Return>", calculate)

root.mainloop()
