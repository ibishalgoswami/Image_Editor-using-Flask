##Image Details
import PIL
import tinify
# from PIL import Image,ImageFilter
# Img=Image.open('messi5.jpg')
# print(f"Height of the Image {Img.height}")
# print(f"Width of the Image {Img.width}")
# print(f"Size of the Image {Img.size}") #Size=(width x height)
# print(f"Format of the Image {Img.format}")

##Resizing the Image
# Img=Image.open('messi5.jpg')
# Width=int(input('Mention the Width of the image'))
# Height=int(input('Mention the Height of the image'))
# size=(Width,Height)
# Img=Img.resize(size)
# Img.save('new_image.jpg')
# Img.show()

##Rotating the Image
# Img=Image.open('messi5.jpg')
# rotate=input('In which direction you want to rotate?')
# if rotate=='Down' or rotate=='down':
#     val=180
# elif rotate=='Right' or rotate=='right':
#     val=270
# elif rotate=="Left" or rotate=='right':
#     val=90
# else:
#     val=360
# Img=Img.rotate(val)
# Img.show()

##Filtering the Image
# from PIL import Image
# Img=Image.open('messi5.jpg')
# ##Converting it BLUR
# Img=Img.filter(ImageFilter.BoxBlur(1))
# ##Converting it B & W
# Img=Img.convert('L')
# Img.show()

##Image compressor
from PIL import Image
# img = Image.open('gg.jpg')
# basewidth = img.width
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save('new.jpg')

# Img=Image.open('red-pagoda-temple-3380967.jpg')
# Width=Img.width-8
# Height=Img.height
# size=(Width,Height)
# Img=Img.resize(size)
# Img.save('new_image.jpg')
# Img.show()



