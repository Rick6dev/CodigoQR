import qrcode

def generate_qr_code(data):
    qrcode_image = qrcode.make(data)

    return qrcode_image


if __name__ == "__main__":
    data = "https://www.python.org/downloads/"
    qr_code = generate_qr_code(data)

    qr_code.save("qrpython_code.png")