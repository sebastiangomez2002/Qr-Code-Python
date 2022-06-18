import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data('Texto d ejemplo') # Informacion que va a ir ene el Qr
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


file = open('Qr Code.png', 'wb') # Nombre y formato del Qr

img.save(file)

file.close()