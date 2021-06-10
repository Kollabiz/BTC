from PIL import Image
from os import listdir
from io import BytesIO

##### Printing all files in dir #####

print(listdir())

##### Changing image format (just in case) #####

def convert_format(ima):
   with BytesIO() as f:
   	ima.save(f, format='PNG')
   	f.seek(0)
   	ima_png = Image.open(f)
   return ima_png
   
##### Inputs and stuff #####

images = input('Images: ')
if images == '*':
	images = listdir()
else:
	images = images.split(',')
loaded = []

##### Loading images #####

for image in images:
	try:
		loaded.append(Image.open(image.strip()))
	except:
		print('There\'s an error with:\n', image, sep='\t')

##### Getting final texture size #####

widht = 0
heights = []
for image in loaded:
	widht += image.size[0]
	heights.append(image.size[1])

height = max(heights)

##### Creating empty image ######

ex = Image.new('RGBA', (widht, height))

##### Converting format (just in case) #####

for image in loaded:
	image = convert_format(image)
	print(image.mode)

##### Putting images in texture #####

step = 0
for image in loaded:
	box = (0, 0, image.size[0], image.size[1])
	region = image.crop(box)
	box = (step, 0, image.size[0] + step, image.size[1])
	ex.paste(region, box)
	step += image.size[0]

##### Saving #####

ex.save('texture.png', 'PNG')