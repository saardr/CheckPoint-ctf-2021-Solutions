from PIL import Image

def handle_first_image(filepath = "first_hint.bmp"):
	im = Image.open(filepath)
	rgb_im = im.convert('RGB')

	pixels = list(rgb_im.getdata())
	altered_pixels = []
	for triplet in pixels:
		if triplet != (0, 0, 0):
			altered_pixels.append((255, 255, 255))
		else:
			altered_pixels.append((0,0,0))

	new_image = Image.new(rgb_im.mode, rgb_im.size)
	new_image.putdata(altered_pixels)
	new_image.save("first_hint_altered.png")

def handle_second_image(filepath = "second_hint.bmp"):
	im = Image.open(filepath)	
	rgb_im = im.convert('RGB')

	pixels = list(rgb_im.getdata())
	altered_pixels = []
	for pixel in pixels:
		if pixel[0] % 2 == 0:
			altered_pixels.append((255, 255, 255))
		else:
			altered_pixels.append((0,0,0))
	new_image = Image.new(rgb_im.mode, rgb_im.size)
	new_image.putdata(altered_pixels)
	new_image.save("second_hint_altered.png")
