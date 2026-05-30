import tkinter as tk

def press_key(key):
    # Appends the pressed key to the current text in the display
    current = display_var.get()
    if key =="C":
        display_var.set("")
    elif key == "=":
        try:
            result = str(eval(current))
            display_var.set(result)
        except Exception:
            display_var.set("Error")
            
    else:
        display_var.set(current + str(key))
        
#Main window setup
root = tk.Tk()
root.title("Simple Calc")
root.geometry("300x400")
    
display_var = tk.StringVar()
    
#display screen
screen = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right", bd=10, insertwidth=4)
screen.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)
    
#Button panel layout
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

buttons = [
    ['1', '2', '3', '/'],
    ['4', '5', '6', '*'],
    ['7', '8', '9', '-'],
    ['C', '0', '=', '+']
]

# Loop through our matrix to generate buttons on a grid layout
for row_idx, row in enumerate(buttons):
    for col_index, text in enumerate(row):
        action = lambda x=text: press_key (x)
        btn = tk.Button(button_frame, text=text, font=("Arial", 14), command=action)
        btn.grid(row=row_idx, column=col_index, sticky="nsew", padx=2, pady=2)
        
    #Make buttons expand evenly inside the frame
for i in range(4):
    button_frame.rowconfigure(i, weight=1)
    button_frame.columnconfigure(i, weight=1)
root.mainloop()