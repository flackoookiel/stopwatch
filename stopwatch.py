import tkinter as tk

# Make the stopwatch window and set its title and size.
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x150")

# Make the time display.
time_label = tk.Label(root, text="00:00:00", font=("Arial", 28, "bold"))

# Place the display in the window.
time_label.pack()

# Keep the window open for button clicks.
root.mainloop()
