#debug
import os

from scipy import ndimage
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Load raw speckle images in .dat format
# Convert .dat to .tiff

# Load .tiff image
# calculate speckle contrast (Dynamic Imaging of Cerebral Blood Flow Using Laser Speckle)


# Add dimensions to image (e.g. 5x4 [mm))








#function for lasca contrast calculation
def lasca(imarray, wsize = 10):
    immean = ndimage.uniform_filter(imarray, size=wsize) 
    im2mean = ndimage.uniform_filter(np.square(imarray), size=wsize)
    imcontrast = np.sqrt(im2mean / np.square(immean) - 1)
    return imcontrast

# make sure file exists
print(os.listdir())
# make sure I'm in the directory I think I'm in
print(os.getcwd())

############ Main
#load test dataset
im = Image.open("./../data/interim/datauint16.tiff")
#taking only 1st frame
#convert to the float for filtering and calculation
imarray = np.array(im).astype(float)

#make contrast with window of 5 pixels
imcontrast05 = lasca(imarray, 5)
#make contrast with window of 10 pixels
imcontrast10 = lasca(imarray, 10)

#finally plot the data and results
plt.figure(figsize=(12,5))
plt.subplot(1,3,1);
plt.imshow(imarray,  cmap=plt.get_cmap("gray"))
plt.colorbar(orientation = 'horizontal',  ticks = np.linspace(500, 2000, 4, endpoint=True))

plt.subplot(1,3,2);
plt.imshow(imcontrast05,  vmin=0.1, vmax=0.4, cmap=plt.get_cmap("jet"))
plt.colorbar(orientation = 'horizontal', ticks = [0.1, 0.2, 0.3, 0.4])

plt.subplot(1,3,3);
plt.imshow(imcontrast10,  vmin=0.1, vmax=0.4, cmap=plt.get_cmap("jet"))
plt.colorbar(orientation = 'horizontal', ticks = [0.1, 0.2, 0.3, 0.4])

#saves figure
plt.savefig('./../data/final/result.jpg', bbox_inches=0, pad_inches=0,dpi=120);
plt.show()
