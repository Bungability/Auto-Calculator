import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7',), ('8',), ('9',), ('/',),
    ('4',), ('5',), ('6',), ('*',),
    ('1',), ('2',), ('3',), ('-',),
    ('0',), ('.',), ('=', '+'), ('+',),
    ('C', clear)
]

row_num = 1
col_num = 0

for button in buttons:
    btn_text = button[0]
    btn_func = button[1] if len(button) > 1 else lambda x=btn_text: entry.insert(tk.END, x)
    tk.Button(root, text=btn_text, width=5, command=btn_func).grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


root.mainloop()
