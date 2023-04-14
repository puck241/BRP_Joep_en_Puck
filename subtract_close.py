import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

import infofile as IF
import functionfile as FF

#Star to subtract 
with fits.open('med_star_all.fits') as hdul:
    med_all = hdul[0].data
    
#%%
#Import close binaries
arr = IF.bin_c_names
data = FF.star_data(arr)
copy = data.copy()
clb_data = np.array([FF.data_reduction(copy[i]) 
                    for i in range(len(arr))])

#%%
#Choose binary
binary = clb_data[0]

#%%
#Plot star for which you want to determine the position of the binary
dx = 10
plt.figure()
plt.imshow(binary)
plt.colorbar()
plt.xlim(512-dx, 512+dx)
plt.ylim(512-dx, 512+dx)
plt.show

#%%
#Determine positions
p_1 = (510, 512)
p_2 = (514, 510)
#%%
#Cut out binary
cut_bin = binary[p_1[1]-dx:p_1[1]+dx, p_1[0]-dx:p_1[0]+dx]

plt.figure()
plt.imshow(cut_bin)
plt.colorbar()
plt.show()

#%%
#Subtract median star from binary 1
r = 10
med = med_all[512-r:512+r, 512-r:512+r]

rest = FF.subtract_star(cut_bin, med)


plt.figure()
plt.imshow(rest, origin = 'lower')
#plt.xlim(x_1-a_1, y_1+a_1)
#plt.ylim(x_1-a_1, y_1+a_1)
plt.colorbar()
plt.show
#%% 
#Subtract median star from binary 2
med_norm = np.nanmax(rest)*med_all
p_3 = (14, 9)
#%%
#Cut out binary
dx = 5
cut_bin_2 = rest[p_3[1]-dx:p_3[1]+dx, p_3[0]-dx:p_3[0]+dx]

plt.figure()
plt.imshow(cut_bin_2)
plt.colorbar()
plt.show()

#%%
#Subtract median star from binary 1
r = 5
med_norm = med_norm[512-r:512+r, 512-r:512+r]

rest_2 = FF.subtract_star(cut_bin_2, med_norm)


plt.figure()
plt.imshow(rest_2, origin = 'lower')
#plt.xlim(x_1-a_1, y_1+a_1)
#plt.ylim(x_1-a_1, y_1+a_1)
plt.colorbar()
plt.show






















