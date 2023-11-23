from PIL import Image

img = Image.open('yourimage.jpeg')
#img.show()
bw_img = img.convert('L')
bw_img.show()
bw_img.save('bw_image.png')