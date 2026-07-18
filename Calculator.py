import customtkinter as ctk

root = ctk.CTk()
root.title("Simple Calculator")
root.geometry("900x600")

result_var = ctk.StringVar(value="Result")

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20)

entry1 = ctk.CTkEntry(frame, placeholder_text="Enter first number")
entry1.pack(pady=10)

entry2 = ctk.CTkEntry(frame, placeholder_text="Enter second number")
entry2.pack(pady=10)

op_menu = ctk.CTkOptionMenu(frame, values=["+", "-", "*", "/", "^", "%"])
op_menu.pack(pady=10)

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = op_menu.get()
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = a / b
        elif op == '^':
            res = a ** b
        elif op == '%':
            res = a % b
        else:
            res = "Unknown operation"
        result_var.set(str(res))
    except Exception as e:
        result_var.set(f"Error: {e}")

calc_button = ctk.CTkButton(frame, text="Calculate", command=calculate)
calc_button.pack(pady=10)

result_label = ctk.CTkLabel(frame, textvariable=result_var)
result_label.pack(pady=10)

root.mainloop()

