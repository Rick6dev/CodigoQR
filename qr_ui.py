import flet as ft
import qrcode

def main(page: ft.Page):
    def validate_fields():
        if texto.value or nombre_imagen.value:
            boton.disabled = False
        else:
            boton.disabled = True
    def btn_click(e):
        codigo_qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        codigo_qr.add_data(texto.value)
        image_qr = codigo_qr.make_image(fill_color="black", back_color="white")
        image_qr.save(nombre_imagen.value + ".png")  # Use the provided image name
        imagen_col.controls.append(ft.Image(
            src=f"{nombre_imagen.value}.png",  # Use the provided image name in the src
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN
        ))
        page.update()

    texto = ft.TextField(label="Ingresa tu codigo QR")
    boton = ft.ElevatedButton(text="Generar", on_click=btn_click, disabled=True)
    imagen_col = ft.Column(expand=1, wrap=False, scroll='AUTO')
    nombre_imagen = ft.TextField(label="Nombre de la imagen:")  # Add the image name field
    page.add(nombre_imagen,texto, boton,  imagen_col)  # Add the field to the page

ft.app(target=main)