import qrcode

_input = input("Enter a link or a text:")
img = qrcode.make(_input)


# Save the image
img.save('example_qrcode.png')
