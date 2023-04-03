#%%
#Importing other files and libraries
import infofile as IF
import functionfile as FF
import numpy as np
import matplotlib.pyplot as plt

#%%
#Loading data
sin_data = FF.star_data(IF.sin_wp_names) #WISPIT single

#bin_data = FF.star_data(IF.bin_wp_names) #WISPIT binaries

#%%
#Masking flux images and normalizing them
copy = sin_data.copy()
clb_data = np.array([FF.data_reduction(copy[i]) 
                    for i in range(len(IF.sin_wp_names))])

#%%
#Masking an aperture around the star

copy2 = clb_data.copy()
aper = np.array([FF.mask_aperture(copy2[i])
                     for i in range(len(IF.sin_wp_names))])

#%%
#Determining the rms of the images and sorting them from best to worst
idx_sort, data_sort = FF.arr_sort_rms(aper)

#%%
#Creating the median images and calculating the rms of these images

median_cube, median_rms = FF.median_image(data_sort)


# %%
#Plotting the rms vs the number of images used for the median image
plt.figure()
plt.title('Determining the optimal numer of images using WISPITdata')
plt.plot(np.arange(1, len(median_rms)+1), median_rms)
plt.xlabel('N')
plt.ylabel('rms')
plt.show()

#%%
#Determining the optimal number of images 
idx_opt_im = idx_sort[0:np.argmin(median_rms)]

#%%
#Making the median image of the star containing the optimal number
opt_median_im_wp = np.median(clb_data[idx_opt_im], axis = 0)

#%%
#Plotting the optimal median single star
dx = 30
plt.figure()
plt.title('Optimal median single star using only WISPIT')
plt.imshow(opt_median_im_wp)
plt.xlim(512-dx, 512+dx)
plt.ylim(512-dx, 512+dx)
plt.show()

# %%
