import tkinter as tk
import time

sample_text = "The quick brown fox jumps over the lazy dog"

start_time = None


def start_test(event):
    global start_time
    if start_time is None:
        start_time = time.time()


def check_result():
    global start_time

    typed_text = entry.get("1.0", tk.END).strip()

    if typed_text == sample_text:
        end_time = time.time()
        time_taken = end_time - start_time

        words = len(sample_text.split())
        wpm = (words / time_taken) * 60

        result_label.config(text=f"Speed: {int(wpm)} Words Per Minute")
    else:
        result_label.config(text="Text doesn't match!")


window = tk.Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

title = tk.Label(text="Typing Speed Test", font=("Arial", 18))
title.pack()

text_label = tk.Label(text=sample_text, wraplength=400)
text_label.pack(pady=10)

entry = tk.Text(height=5, width=50)
entry.pack()
entry.bind("<KeyPress>", start_test)

check_button = tk.Button(text="Check Speed", command=check_result)
check_button.pack(pady=10)

result_label = tk.Label(text="")
result_label.pack()

window.mainloop()