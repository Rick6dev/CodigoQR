import qrcode
from PIL import Image, ImageFilter

# Ruta al logo
logo_path = "logo.png"

# Carga el logo y redimensionalo
logo = Image.open(logo_path)
logo_resized = logo.resize((50, 50), Image.LANCZOS)

# Crea el QR code con la configuración adecuada
def generate_qr_code_with_logo(data, logo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")

    return qrcode_image, qr.modules_count

# Genera el QR code con el logo
if __name__ == "__main__":
    data = "https://www.python.org/downloads/"
    qr_image, modules_count = generate_qr_code_with_logo(data, logo_resized)

    # Calcula la posición central para colocar el logo
    position = ((modules_count - logo_resized.size[0]) // 50,
                (modules_count - logo_resized.size[1]) // 50)

    # Cambia el modo de color del logo a RGB
    rgb_logo = logo_resized.convert("RGB")

    qr_image.paste(rgb_logo, position)

    qr_image.save("qrpython_code_with_ss.png")