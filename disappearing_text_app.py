import tkinter as tk

TIME_LIMIT = 5000  # 5 seconds (in milliseconds)

timer = None


def reset_timer(event=None):
    global timer
    window.after_cancel(timer)
    timer = window.after(TIME_LIMIT, delete_text)


def delete_text():
    text_box.delete("1.0", tk.END)
    status_label.config(text="💀 Too slow... text deleted!", fg="red")


window = tk.Tk()
window.title("Disappearing Writing App")
window.config(padx=20, pady=20)

title = tk.Label(text="Keep typing...", font=("Arial", 18))
title.pack()

text_box = tk.Text(width=50, height=15, font=("Arial", 14))
text_box.pack()
text_box.bind("<KeyPress>", reset_timer)

status_label = tk.Label(text="Start typing!", font=("Arial", 12))
status_label.pack(pady=10)

timer = window.after(TIME_LIMIT, delete_text)

window.mainloop()