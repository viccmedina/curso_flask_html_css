import os 
from PIL import Image
from flask import url_for, current_app


def add_profile_pic(pic_upload, username):
	"""
	Nos permite administrar las fotos de perfiles
	de cada usuario.
	"""
	filename = pic_upload.filename
	ext_type = filename.spli('.')[-1]
	storegae_filename = str(username) + '.' + ext_type
	filepath = os.path.join(current_app.root_path, 'static/profile_pics', storegae_filename)

	output_size = (200, 200)
	pic = Image.open(pic_upload)
	pic.thumbnail(output_size)
	pic.save(filepath)

	return storegae_filename