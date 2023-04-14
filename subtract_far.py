import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

import infofile as IF
import functionfile as FF

#Star to subtract 
with fits.open('med_star_all.fits') as hdul:
    med_all = hdul[0].data

#%%
#Import far binaries
arr = IF.bin_f_names
data = FF.star_data(arr)
copy = data.copy()
clb_data = np.array([FF.data_reduction(copy[i]) 
                    for i in range(len(arr))])

#%%
#Choose binary
binary = clb_data[0]
#%%
#Plot star for which you want to determine the position of the binary
dx = 100
plt.figure()
plt.imshow(binary)
plt.colorbar()
plt.xlim(512-dx, 512+dx)
plt.ylim(512-dx, 512+dx)
plt.show
#%%
#Subtract star first time
rest = FF.subtract_star(binary, med_all)

dx = 100
plt.figure()
plt.imshow(rest)
plt.colorbar()
plt.xlim(512-dx, 512+dx)
plt.ylim(512-dx, 512+dx)
plt.show

#%%
#Zoom in on binary to determine position
rest = FF.subtract_star(binary, med_all)
x = 512
y = 512
a = 20

dx = 100
plt.figure()
plt.imshow(rest)
plt.xlim(x_1-a_1, y_1+a_1)
plt.ylim(x_1-a_1, y_1+a_1)
plt.colorbar()
plt.show
#%%
#Cut out this part of the sky
rest_copy = rest.copy()
new_rest = rest_copy[y-a:y+a, x-a:x+a] 

plt.figure()
plt.imshow(new_rest)
plt.colorbar()
plt.show()

#%%
#Subtract the median star from the binary
mid = 512
changed_bin = np.nanmax(new_rest)*med_all[mid-a:mid+a, mid-a:mid+a]

rest_new = FF.subtract_star(new_rest, changed_bin)

plt.figure()
plt.imshow(rest_new, origin = 'lower')
plt.colorbar()
plt.show()

#%%
#If there is another binary, zoom in on this one
plt.figure()
plt.imshow(rest_new, origin = 'lower')
plt.colorbar()
plt.xlim(15, 30)
plt.ylim(5, 17)
plt.show()

#%%
x_2 = 22
y_2 = 13
a_2 = 10
rest_new_copy = rest_new.copy()
rest_bin_2 = rest_new_copy[y_2-a_2:y_2+a_2, x_2-a_2:x_2+a_2]

plt.figure()
plt.imshow(rest_bin_2, origin = 'lower')
plt.colorbar()
plt.show()

#%%
#Also subtract the median star from this binary
mid = 512
changed_bin_2 = np.nanmax(rest_bin_2)*med_all[mid-a_2:mid+a_2, mid-a_2:mid+a_2]

rest_bin_3 = FF.subtract_star(rest_bin_2, changed_bin_2)

plt.figure()
plt.imshow(rest_bin_3, origin = 'lower')
plt.colorbar()
plt.show()
