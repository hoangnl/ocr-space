import os
import shutil

filename = "foo/bar/baz.txt"
foldername = "backup"
filename = "example_image.png"
os.makedirs(foldername, exist_ok=True)
shutil.move( filename, foldername + "/" + filename)

