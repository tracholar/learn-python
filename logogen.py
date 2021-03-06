# coding:gbk

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageColor
import sys

if len(sys.argv)<2:
	sys.exit()
if len(sys.argv)>=3:
	fout = sys.argv[2] + '.jpg'
else:
	fout = 'out.jpg'
	
img = Image.open(sys.argv[1])
base_size = tuple(int(i/1.0/max(img.size)*100) for i in img.size)

def binarize(i):
	if i>100:
		return 255
	return 0

new_img = img.convert('L').point(binarize).resize(base_size).filter(ImageFilter.BLUR)

#print new_img.getpixel((5,5))

out_img = Image.new("RGB",(base_size[0]*14,base_size[1]*14),(255,255,255))
draw = ImageDraw.Draw(out_img)
for i in range(base_size[0]):
	for j in range(base_size[1]):
		size = 10-int(new_img.getpixel((i,j))/255.0*10)
		if size==0:
			continue
		#print size,
		draw.rectangle([(i*14+(7-size/2),j*14+(7-size/2)),(i*14+(7+size/2),j*14+(7+size/2))],fill='hsl(%d,100%%,50%%)' % int(i/1.0/base_size[0]*180))
out_img.save(fout)
