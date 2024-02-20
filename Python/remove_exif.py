import os
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory
from exif import Image


folder_path = askdirectory(title='Select Folder')


jpeg_blob = Path(folder_path).rglob('*.jpg')

jpegs = [pic for pic in jpeg_blob]


images = []

for f in jpegs:
    with open(f, 'rb') as img:

        img_exif = Image(img)

        if img_exif.has_exif:
            print('exif exist')
            img_exif.delete_all()

            with open(f, 'wb') as new_img:
                new_img.write(img_exif.get_file())
                print(f'Exif within Image {os.path.basename(f)} has been removed')