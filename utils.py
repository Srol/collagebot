from PIL import Image
from slacker import Slacker
import urllib.request
# import io
import requests

# Insert API Key here
api_key = "API key here"
slack = Slacker(api_key)

def collage_it(to_collage, channel, userName, force):
	downloaded_files = []
	x = 1
	# this downloads the files sent into the request to the local machine
	for url in to_collage:
		url = url[1:-1]
		print(url)
		r = urllib.request.urlopen(url)
		image_data = r.read()
		f = open("file" + str(x)+ ".jpg", "wb")
		f.write(image_data)
		f.close()
		downloaded_files.append("file" + str(x)+ ".jpg")
		x += 1
	# A basic two-photo collage with no restraints. The height and width of the smaller photo will be used. 
	if force == False:
		image1 = Image.open(downloaded_files[0])
		image2 = Image.open(downloaded_files[1])
		width1, height1 = image1.size
		width2, height2 = image2.size
		result = Image.new('RGB',(min(width1,width2) + min(width1,width2), min(height1,height2)))
		resultw, resulth = result.size
		result.paste(image1, (0,0))
		result.paste(image2, (resultw//2,0))
		result.save('result.jpg')
		f_upload = slack.files.upload("result.jpg", channels=channel)
		print(f_upload)
	# This forces a two-image collage to resize and crop itself to a 48 x 27, no greater than  2400 x 1350.
	# This image will be resized by height then centered by width.
	elif force == True:
		image1 = Image.open(downloaded_files[0])
		image2 = Image.open(downloaded_files[1])
		width1, height1 = image1.size
		width2, height2 = image2.size
		smollest = min(width1,width2,height1,height2)
		if smollest == width1 or smollest == height1:
			new_dimensions = frame_it(width1, height1)
		else:
			new_dimensions = frame_it(width2, height2)
		result = Image.new('RGB', (new_dimensions[0], new_dimensions[1]))
		resultw, resulth = result.size
		wpercent1 = (resulth/float(image1.size[1]))
		hsize1 = int((float(image1.size[0])*float(wpercent1)))
		image1 = image1.resize((hsize1,resulth), Image.ANTIALIAS)
		wpercent2 = (resulth/float(image2.size[1]))
		hsize2 = int((float(image2.size[0])*float(wpercent2)))
		image2 = image2.resize((hsize2,resulth), Image.ANTIALIAS)
		width1, height1 = image1.size
		width2, height2 = image2.size
		left_one = (width1 - resultw/2)/2
		right_one = (width1 + resultw/2)/2
		new_one = image1.crop((left_one, 0, right_one, height1))
		left_two = (width2 - resultw/2)/2
		right_two = (width2 + resultw/2)/2
		new_two = image2.crop((left_two,0,right_two, height2))
		result.paste(new_one, (0,0))
		result.paste(new_two, ((resultw//2),0))
		result.save('result.jpg')
		f_upload = slack.files.upload("result.jpg", channels=channel)
		print(f_upload)
	else:
		slack.chat.post_message(channel, "Something went wrong, @patrick.hogan can you come here and check it out?")

#this is the function used to determine the best aspect ratio for a collage, going by the smallest dimension of the smallest photo of the two.
def frame_it(width, height):
	widths = [[2400,1350],[2000,1107],[1600,891],[1200,675],[800,432],[400,216]]
	def get_key(item):
		if width < height:
			return item[0]
		else:
			return item[1]
	widths.append([width,height])
	order_widths = sorted(widths, key=get_key)
	if order_widths.index([width,height]) != 0:
		return order_widths[order_widths.index([width,height]) - 1]
	else:
		return order_widths[1]


