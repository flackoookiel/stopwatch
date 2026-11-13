import tkinter as tk
import theme

# Make the stopwatch window and set its title and size.
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x150")
root.configure(bg=theme.BG)

# These variables keep track of whether the stopwatch is running,
# how much time has already passed, and when the current run started.
running = False
elapsed = 0
start_time = 0

def update():
    # Update the display while the stopwatch is running.
    if running:
        # Find the time passed since Start and add time saved before Stop.
        total = elapsed + (int(root.tk.call('clock', 'milliseconds')) - start_time)

        # Change the time from milliseconds into seconds and hundredths.
        seconds = total // 1000
        millis = (total % 1000) // 10

        # Show the time as seconds:hundredths, such as 12:34.
        time_label.config(text="{:02d}:{:02d}".format(seconds, millis))

    # Run this function again after 50 milliseconds to refresh the display.
    root.after(50, update)

def start():
    global running, start_time
    # Start only if the stopwatch is not already running.
    if not running:
        # Save the start time and mark the stopwatch as running.
        start_time = int(root.tk.call('clock', 'milliseconds'))
        running = True

def stop():
    global running, elapsed
    # Stop only if the stopwatch is running.
    if running:
        # Save the time passed so the next Start can continue from here.
        elapsed += int(root.tk.call('clock', 'milliseconds')) - start_time
        running = False

def reset():
    global running, elapsed
    # Stop the stopwatch and clear the saved time.
    running = False
    elapsed = 0
    time_label.config(text="00:00:00")

def make_button(parent, text, command, bg, fg):
    """Create a flat, themed button."""
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=theme.FONT_BTN,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        relief="flat",
        bd=0,
        width=theme.BTN_WIDTH,
        pady=theme.PAD_INNER,
    )

# Make the time display and the three buttons.
time_label = tk.Label(
    root,
    text="00:00:00",
    font=theme.FONT_TIME,
    bg=theme.BG,
    fg=theme.FG,
    pady=theme.PAD_OUTER,
)
start_btn = make_button(root, "Start", start, theme.BTN_START_BG, theme.BTN_START_FG)
stop_btn  = make_button(root, "Stop",  stop,  theme.BTN_STOP_BG,  theme.BTN_STOP_FG)
reset_btn = make_button(root, "Reset", reset, theme.BTN_RESET_BG, theme.BTN_RESET_FG)

# Place the display and buttons in the window from top to bottom.
time_label.pack(fill="x")
start_btn.pack()
stop_btn.pack()
reset_btn.pack()

# Start updating the display and keep the window open for button clicks.
update()
root.mainloop()
