from pyzbar.pyzbar import decode
from PIL import Image
import validators
import qrcode
import webbrowser

def main():
    qr = qrcode.QRCode(
        version = 15,
        box_size = 10,
        border = 5
    )
    data = input(f'Enter text or link: ')
    if not data:
        print(f'Text cannot be empty')
    else:
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image()
        img.save("QRCode_Image.png")
        valid = validators.url(data)
        decodeQR = decode(Image.open('QRCode_Image.png'))
        print(f'Your encoded the following text into your QRCode: {decodeQR[0].data.decode("ascii")}')
        if valid:
            answer = input(f'Do you wish to open your link in browser (Y/n)? ')
            if answer.lower() == 'y':
                webbrowser.open(data, new=0, autoraise=True)


if __name__ == '__main__':
    main()