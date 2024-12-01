import tkinter as tk

def evaluate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=16, font=('Helvetica', 24), borderwidth=0, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
 
button_colors = {
    '/': '#ff9500',
    '*': '#ff9500',
    '-': '#ff9500',
    '+': '#ff9500',
    '=': '#ff9500',
    '0': '#d4d4d2',
    '.': '#d4d4d2'
}
 
row_val = 1
col_val = 0
 
for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x)
    if button == "=":
        btn = tk.Button(root, text=button, width=4, height=2, command=evaluate, bg=button_colors.get(button, '#505050'), fg='white', font=('Helvetica', 18))
    else:
        btn = tk.Button(root, text=button, width=4, height=2, command=action, bg=button_colors.get(button, '#333333'), fg='white', font=('Helvetica', 18))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.bind('<Return>', evaluate)

root.mainloop()
