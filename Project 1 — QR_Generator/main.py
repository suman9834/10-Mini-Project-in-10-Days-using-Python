import qrcode

data = input("Enter text or URL to generate QR code: ")

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")

