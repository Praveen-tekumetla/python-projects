import qrcode

data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name: ").strip()
qr = qrcode.QRCode(box_size=20, border=8)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(f"few_intresting_projects/{file_name}")
print(f"QR code saved as {file_name}.")