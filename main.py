import tkinter as tk

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
    fg="black"
)
generate_button.pack(pady=15)

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


qr_image = None
root.mainloop()