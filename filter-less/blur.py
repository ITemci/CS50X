from PIL import Image, ImageFilter

before = Image.open("images/yard.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out11.bmp")
