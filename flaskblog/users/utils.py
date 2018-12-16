import os
import secrets
from PIL import Image
from flask import current_app


def save_picture(form_picture, source="post"):
    #source=profile头像尺寸125*125，post尺寸最大宽度800
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    i = Image.open(form_picture)
    i_w,i_h = i.size
    if source == "profile":
        output_size = (125,125)
    else:
        output_size = (800, i_h*800/i_w) if i_w>=800 else i.size
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
