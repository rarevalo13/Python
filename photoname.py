from PIL import Image
from PIL.ExifTags import TAGS
import rawpy


def get_exif(fn):
	exif = {}
	i = Image.open(fn)
	info = i._getexif()
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		exif[decoded] = value
	return exif


def converter(fn):
	import ipdb;ipdb.set_trace()
	image = rawpy.imread(fn)
	rbg = image.postprocess()
	image.save(fn.split('.')[0] + "jpeg", 'rbg')