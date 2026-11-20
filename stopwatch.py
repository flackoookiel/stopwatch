import tkinter as tk
import theme
import laps

# Make the stopwatch window and set its title and size.
root = tk.Tk()
root.title("Stopwatch")
root.geometry("360x340")
root.configure(bg=theme.BG)
root.resizable(False, False)

# Stopwatch state.
running = False
elapsed = 0
start_time = 0
last_lap_at = 0        # total time (ms) when the last lap was recorded

# Lap storage.
lap_tracker = laps.LapTracker()


def current_total():
    """Total milliseconds elapsed — works whether running or stopped."""
    if running:
        return elapsed + (int(root.tk.call('clock', 'milliseconds')) - start_time)
    return elapsed


def update():
    # Update the display while the stopwatch is running.
    if running:
        total = current_total()
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
    global running, elapsed, last_lap_at
    running = False
    elapsed = 0
    last_lap_at = 0
    lap_tracker.clear()
    time_label.config(text="00:00:00")
    render_laps()


def lap():
    global last_lap_at
    if not running:
        return
    total = current_total()
    lap_tracker.add(total - last_lap_at)
    last_lap_at = total
    render_laps()


def toggle():
    if running:
        stop()
    else:
        start()


def render_laps():
    laps_list.delete(0, "end")
    for i, ms in enumerate(lap_tracker, start=1):
        laps_list.insert("end", f"Lap {i:>2}    {lap_tracker.format(ms)}")
    laps_list.see("end")


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
        takefocus=0,
    )


# --- Layout ---
time_label = tk.Label(
    root,
    text="00:00:00",
    font=theme.FONT_TIME,
    bg=theme.BG,
    fg=theme.FG,
    pady=theme.PAD_OUTER,
)
time_label.pack(fill="x")

btn_frame = tk.Frame(root, bg=theme.BG)
btn_frame.pack(pady=(0, theme.PAD_INNER))

start_btn = make_button(btn_frame, "Start", start, theme.BTN_START_BG, theme.BTN_START_FG)
stop_btn  = make_button(btn_frame, "Stop",  stop,  theme.BTN_STOP_BG,  theme.BTN_STOP_FG)
reset_btn = make_button(btn_frame, "Reset", reset, theme.BTN_RESET_BG, theme.BTN_RESET_FG)
lap_btn   = make_button(btn_frame, "Lap",   lap,   theme.BTN_RESET_BG, theme.BTN_RESET_FG)

start_btn.pack(side="left", padx=3)
stop_btn.pack(side="left", padx=3)
reset_btn.pack(side="left", padx=3)
lap_btn.pack(side="left", padx=3)

# Lap list below the buttons.
laps_list = tk.Listbox(
    root,
    height=6,
    font=(theme.FONT_FAMILY, 10),
    bg=theme.BG,
    fg=theme.FG,
    selectbackground=theme.BTN_RESET_BG,
    borderwidth=0,
    highlightthickness=0,
    activestyle="none",
    takefocus=0,
)
laps_list.pack(fill="x", padx=theme.PAD_OUTER, pady=(0, theme.PAD_OUTER))


# --- Keyboard shortcuts ---
def on_space(event):
    toggle()
    return "break"

def on_reset(event):
    reset()
    return "break"

def on_lap(event):
    lap()
    return "break"

root.bind("<space>", on_space)
root.bind("<r>", on_reset)
root.bind("<R>", on_reset)
root.bind("<l>", on_lap)
root.bind("<L>", on_lap)


update()
root.mainloop()
