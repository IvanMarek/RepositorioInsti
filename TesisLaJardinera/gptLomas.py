import tkinter as tk

def on_resize(event):
    # Adjust column and row weights to make the widgets responsive
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

root = tk.Tk()
root.title("Responsive Window Example")

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

# Create widgets and place them using the grid manager
label = tk.Label(root, text="Responsive Label")
button = tk.Button(root, text="Resize Me!")

label.grid(row=0, column=0, sticky="nsew")
button.grid(row=1, column=0, sticky="ew")

# Make the button expand horizontally, but not vertically
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()