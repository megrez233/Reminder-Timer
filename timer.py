import time
import tkinter as tk
from threading import Thread
from tkinter import messagebox
import winsound


class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder Timer")

        self.total_seconds = 0
        self.running = False

        # Label to display remaining time
        self.time_label = tk.Label(root, text="Time remaining: 00:00:00", font=("Helvetica", 16))
        self.time_label.pack(pady=20)

        # Frame to hold hour, minute, second buttons
        time_frame = tk.Frame(root)
        time_frame.pack(pady=10)

        # Buttons to add time
        self.hour_button = tk.Button(time_frame, text="Add 1 Hour", command=self.add_hour, width=12)
        self.hour_button.grid(row=0, column=0, padx=5)

        self.minute_button = tk.Button(time_frame, text="Add 1 Minute", command=self.add_minute, width=12)
        self.minute_button.grid(row=0, column=1, padx=5)

        self.second_button = tk.Button(time_frame, text="Add 1 Second", command=self.add_second, width=12)
        self.second_button.grid(row=0, column=2, padx=5)

        # Frame to hold start and cancel buttons
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(control_frame, text="Start Timer", command=self.start_timer, width=12)
        self.start_button.grid(row=0, column=0, padx=5)

        # Button to cancel timer
        self.cancel_button = tk.Button(control_frame, text="Cancel Timer", command=self.cancel_timer, width=12)
        self.cancel_button.grid(row=0, column=1, padx=5)

    def update_time_label(self):
        hours, remainder = divmod(self.total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.time_label.config(text=f"Time remaining: {hours:02}:{minutes:02}:{seconds:02}")

    def add_hour(self):
        self.total_seconds += 3600
        self.update_time_label()

    def add_minute(self):
        self.total_seconds += 60
        self.update_time_label()

    def add_second(self):
        self.total_seconds += 1
        self.update_time_label()

    def countdown(self):
        while self.total_seconds > 0 and self.running:
            time.sleep(1)
            self.total_seconds -= 1
            self.update_time_label()
        if self.total_seconds == 0 and self.running:
            self.play_sound()
            self.show_reminder()

    def start_timer(self):
        if self.total_seconds > 0 and not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)  # Disable the Start button after timer starts
            countdown_thread = Thread(target=self.countdown)
            countdown_thread.start()

    def play_sound(self):
        # Play a sound (Windows beep sound)
        winsound.Beep(1000, 1000)  # Frequency 1000Hz, Duration 1000ms

    def show_reminder(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)  # Re-enable the Start button
        messagebox.showinfo("Reminder", "Time's up!")

    def cancel_timer(self):
        self.running = False
        self.total_seconds = 0
        self.update_time_label()
        self.start_button.config(state=tk.NORMAL)  # Re-enable the Start button


# Create the main window
root = tk.Tk()
app = ReminderApp(root)

# Start the main loop
root.mainloop()
