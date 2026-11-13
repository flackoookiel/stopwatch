import tkinter as tk
import theme

# Make the stopwatch window and set its title and size.
root = tk.Tk()
root.title("Stopwatch")
root.geometry("360x220")
root.configure(bg=theme.BG)
root.resizable(False, False)

# These variables keep track of whether the stopwatch is running,
# how much time has already passed, and when the current run started.
running = False
elapsed = 0
start_time = 0

def update():
    # Update the display while the stopwatch is running.
    if running:
        total = elapsed + (int(root.tk.call('clock', 'milliseconds')) - start_time)

        minutes    = total // 60000
        seconds    = (total // 1000) % 60
        hundredths = (total % 1000) // 10

        time_label.config(
            text="{:02d}:{:02d}:{:02d}".format(minutes, seconds, hundredths)
        )

    root.after(50, update)

def start():
    global running, start_time
    if not running:
        start_time = int(root.tk.call('clock', 'milliseconds'))
        running = True

def stop():
    global running, elapsed
    if running:
        elapsed += int(root.tk.call('clock', 'milliseconds')) - start_time
        running = False

def reset():
    global running, elapsed
    running = False
    elapsed = 0
    time_label.config(text="00:00:00")

def toggle():
    """Start if stopped, stop if running — used by the Space shortcut."""
    if running:
        stop()
    else:
        start()

def make_button(parent, text, command, bg, fg):
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
        cursor="hand2",
        takefocus=0,     # keep keyboard focus off buttons — we bind globally
    )

# Time display.
time_label = tk.Label(
    root,
    text="00:00:00",
    font=theme.FONT_TIME,
    bg=theme.BG,
    fg=theme.FG,
    pady=theme.PAD_OUTER,
)
time_label.pack(fill="x")

# Button row.
btn_frame = tk.Frame(root, bg=theme.BG)
btn_frame.pack(pady=(0, theme.PAD_OUTER))

start_btn = make_button(btn_frame, "Start", start, theme.BTN_START_BG, theme.BTN_START_FG)
stop_btn  = make_button(btn_frame, "Stop",  stop,  theme.BTN_STOP_BG,  theme.BTN_STOP_FG)
reset_btn = make_button(btn_frame, "Reset", reset, theme.BTN_RESET_BG, theme.BTN_RESET_FG)

start_btn.pack(side="left", padx=4)
stop_btn.pack(side="left", padx=4)
reset_btn.pack(side="left", padx=4)

# Keyboard shortcuts.
def on_space(event):
    toggle()
    return "break"

def on_reset(event):
    reset()
    return "break"

root.bind("<space>", on_space)
root.bind("<r>", on_reset)
root.bind("<R>", on_reset)

update()
root.mainloop()
