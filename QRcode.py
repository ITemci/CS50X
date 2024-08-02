import qrcode

image = qrcode.make("https://www.facebook.com/temciuc.ion1")
image.save("code.png", "PNG")
