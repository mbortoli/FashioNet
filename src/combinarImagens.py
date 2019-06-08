# https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
from os import listdir
from os.path import isfile, join
import numpy as np
from PIL import Image

cropped_upper = 'cropped_upper/'
cropped_bottom = 'cropped_bottom/'
combined = 'combined/'
upper_files = [cropped_upper + f for f in listdir(cropped_upper) if isfile(join(cropped_upper, f))]
bottom_files = [cropped_bottom + f for f in listdir(cropped_bottom) if isfile(join(cropped_bottom, f))]
for u in upper_files:
    upper_image = Image.open(u)
    for b in bottom_files:
        print(u, b)
        bottom_image = Image.open(b)
        combined_image = np.vstack([upper_image, bottom_image])
        #print(combined_image)
        combined_image = Image.fromarray(combined_image)
        combined_image.save(combined + u.split('/', 1)[1] + '-' + b.split('/', 1)[1])
