import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_qr_code(data, filename, background_color="white", qr_color="black", logo=None, logo_size=None, logo_position=None, logo_border=False):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=background_color)

    if logo:
        logo_img = Image.open(logo)
        if logo_size:
            logo_img = logo_img.resize(logo_size)

        if logo_border:
            border_width = img.size[0] // 10
            img.paste(logo_img, logo_position, logo_img)
        else:
            img.paste(logo_img, logo_position, logo_img)

    img.save(filename)

def main():
    data = input("Enter the data you want to encode in QR code: ")
    filename = input("Enter the filename to save the QR code (with extension): ")
    background_color = input("Enter background color (default is white): ") or "white"
    qr_color = input("Enter QR code color (default is black): ") or "black"
    include_logo = input("Do you want to include a logo? (yes/no): ").lower() == "yes"

    if include_logo:
        logo_path = input("Enter logo path (with extension): ")
        logo_size = tuple(map(int, input("Enter logo size (width height): ").split()))
        logo_position = tuple(map(int, input("Enter logo position (x y): ").split()))
        logo_border = input("Do you want a border around the logo? (yes/no): ").lower() == "yes"

        generate_qr_code(data, filename, background_color, qr_color, logo_path, logo_size, logo_position, logo_border)
    else:
        generate_qr_code(data, filename, background_color, qr_color)

if __name__ == "__main__":
    main()
