import tkinter as tk
from tkinter import filedialog,messagebox
import qrcode
from PIL import ImageTk

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("600x600")

label_input = tk.Label(root, text="Enter Link or Text:", font=("Arial", 12))
label_input.pack(pady=10)

input_entry = tk.Entry(root, width=40, font=("Arial", 12))
input_entry.pack(pady=5)

generate_button = tk.Button(
    root,
    text="Generate QR Code",
    font=("Arial", 12),
    bg="lightgray",
    fg="black",
    command=lambda: generate_qr()
)
generate_button.pack(pady=15)

save_button = tk.Button(
    root,
    text="Save QR Code",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=lambda: save_qr)
save_button.pack(pady=10)

qr_label = tk.Label(
    root,
    text="Here is the QR Code:",
    font=("Arial", 12),
    width=30,
    height=30,
    relief="solid",
    bg="white"
)
qr_label.pack(pady=90)


def generate_qr():
    user_input = input_entry.get()

    global qr_image
    qr_image = qrcode.make(user_input)

    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo, text="",width="300", height="300")
    qr_label.image = qr_photo


def save_qr():

    # Open a file save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Success", f"QR code saved successfully to {file_path}")
qr_image = None
root.mainloop()