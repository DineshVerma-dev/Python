import qrcode

data = 'Learned to make QR'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="blue")
img.save("project/qr.png")

print("QR Code generated and saved as 'qrcode_with_logo.png'")
