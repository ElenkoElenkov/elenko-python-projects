from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = Tk()
window.title("Watermark App")
window.geometry("800x600")

img = None
preview = None


def upload_image():
    global img, preview

    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)

    img_resized = img.resize((500, 400))
    preview = ImageTk.PhotoImage(img_resized)

    canvas.create_image(250, 200, image=preview)


def add_watermark():
    global img, preview

    watermark_text = entry.get()

    watermarked = img.copy()
    draw = ImageDraw.Draw(watermarked)

    font = ImageFont.load_default()

    width, height = watermarked.size
    draw.text((width - 120, height - 30), watermark_text, fill="white", font=font)

    img_resized = watermarked.resize((500, 400))
    preview = ImageTk.PhotoImage(img_resized)
    canvas.create_image(250, 200, image=preview)

    watermarked.save("watermarked_image.png")


canvas = Canvas(width=500, height=400)
canvas.pack(pady=20)

upload_btn = Button(text="Upload Image", command=upload_image)
upload_btn.pack()

entry = Entry(width=30)
entry.pack(pady=10)
entry.insert(0, "YourWatermark")

watermark_btn = Button(text="Add Watermark", command=add_watermark)
watermark_btn.pack()

window.mainloop()