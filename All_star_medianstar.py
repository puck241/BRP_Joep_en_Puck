#%%
#Importing other files and libraries
import infofile as IF
import functionfile as FF

import numpy as np
import matplotlib.pyplot as plt

#%%
#Loading data
sin_data = FF.star_data(IF.sin_names) #all single stars

#bin_data = FF.star_data(IF.bin_names) #all binaries

#%%
#Masking flux images and normalizing them
copy = sin_data.copy()
clb_data = np.array([FF.data_reduction(copy[i]) 
                    for i in range(len(IF.sin_names))])

#%%
#Masking an aperture around the star

copy2 = clb_data.copy()
aper = np.array([FF.mask_aperture(copy2[i])
                     for i in range(len(IF.sin_names))])

#%%
#Determining the rms of the images and sorting them from best to worst
idx_sort, data_sort = FF.arr_sort_rms(aper)

#%%
#Creating the median images and calculating the rms of these images

median_cube, median_rms = FF.median_image(data_sort)

# %%
#Plotting the rms vs the number of images used for the median image
plt.figure()
plt.title('Determining the optimal numer of images using all data')
plt.plot(np.arange(1, len(median_rms)+1), median_rms)
plt.xlabel('N')
plt.ylabel('rms')
plt.savefig('rms_all.pdf')

#%%
#Determining the optimal number of images 
idx_opt_im = idx_sort[0:np.argmin(median_rms)]

#%%
#Making the median image of the star containing the optimal number
opt_median_im_all = np.median(clb_data[idx_opt_im], axis = 0)

#%%
#Plotting the optimal median single star
dx = 30
plt.figure()
plt.title('Optimal median single star using all stars')
plt.imshow(opt_median_im_all)
plt.xlim(512-dx, 512+dx)
plt.ylim(512-dx, 512+dx)
plt.savefig('med_star_all.pdf')

# %%
#Making the median image of apertures containing the optimal number
# opt_median_im_aper_all = np.median(aper[idx_opt_im], axis = 0)

# dx = 50
# plt.figure()
# plt.title('Optimal median single star using all stars')
# plt.imshow(np.log(opt_median_im_aper_all))
# plt.xlim(512-dx, 512+dx)
# plt.ylim(512-dx, 512+dx)
# plt.colorbar()
# plt.savefig('optimal_single_star_aper_all2.pdf')
# #plt.show()

# %%
#Save this star as fits file that I can import later on so I do not have to 
#keep running the code
import astropy.io.fits as fits

fits.writeto('med_star_all.fits', opt_median_im_all)