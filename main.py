import tkinter as tk
import qrcode

# create Tkinter window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

# create label and input field
label_input = tk.Label(root, text="Enter Link or Text:", font=("Arial", 12))
label_input.pack(pady=10)

# create a input entry field
input_entry = tk.Entry(root, width=40, font=("Arial", 12))
input_entry.pack(pady=5)

# Add a button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", font=("Arial", 12), bg="lightgray", fg="black")
generate_button.pack(pady=15)
root.mainloop()


# _input = input("Enter a link or a text:")
#img = qrcode.make(_input)


# Save the image
#img.save('example_qrcode.png')
