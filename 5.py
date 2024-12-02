import tkinter as tk
import tkinter.messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("تایمر علی وفائیان")
        self.root.geometry("500x500")

        self.remaining_time = 0
        self.is_running = False

        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48), bg="lightblue", fg="darkblue")
        self.timer_label.pack(pady=50)

        self.entry = tk.Entry(root, width=10, font=("Helvetica", 24))
        self.entry.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        self.start_button = tk.Button(button_frame, text="شروع", command=self.start_timer, bg="green", fg="white", font=("Helvetica", 18))
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(button_frame, text="متوقف کردن", command=self.stop_timer, bg="red", fg="white", font=("Helvetica", 18))
        self.stop_button.pack(side=tk.LEFT, padx=20)

    def start_timer(self):
        try:
            self.remaining_time = int(self.entry.get())
            if self.remaining_time > 0:
                self.is_running = True
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.countdown()
            else:
                tkinter.messagebox.showwarning("خطا", "لطفا یک عدد صحیح وارد کنید.")
        except ValueError:
            tkinter.messagebox.showwarning("خطا", "لطفا یک عدد صحیح وارد کنید.")

    def countdown(self):
        if self.remaining_time > 0 and self.is_running:
            mins, secs = divmod(self.remaining_time, 60)
            timer_format = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=timer_format)
            self.remaining_time -= 1
            self.root.after(1000, self.countdown)
        elif self.remaining_time == 0:
            self.is_running = False
            self.show_alert()
            self.timer_label.config(text="زمان تمام شد!")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def stop_timer(self):
        self.is_running = False
        self.timer_label.config(text="تایمر متوقف شد.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def show_alert(self):
        tkinter.messagebox.showinfo("هشدار", "زمان تمام شد!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
