from os import listdir
from os.path import isfile, join
import numpy as np
from PIL import Image

path = 'Images/'
resized = path+'resized/'
combined = path+'combined/'
upper_files = [combined + f for f in listdir(combined) if f.startswith('IMG')]
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
