#%%
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

import functionfile as FF
import infofile as IF
#%%

#Median all star    
with fits.open('med_star_all.fits') as hdul:
    med_all = hdul[0].data


#%%    
arr = IF.sin_y_names
#%%
data = FF.star_data(arr)
copy = data.copy()
clb_data = np.array([FF.data_reduction(copy[i]) 
                    for i in range(len(arr))])
    
for i in range(len(arr)):
    rest = FF.subtract_star(clb_data[i], med_all)
    name, date = FF.star_info(arr, i)
    #     plt.title(f'{name}, {date}')
    #     plt.imshow(rest)
    #     plt.colorbar()
    #     plt.xlim(500, 524)
    #     plt.ylim(500, 524)
    #     plt.show()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
    ax1.imshow(clb_data[i])
    ax1.set_title('Normalized image', fontsize = 20)
    ax1.set_xlim(512-100, 512+100)
    ax1.set_ylim(512-100, 512+100)
    
    ax2.imshow(rest)
    ax2.set_title('Subtracted image', fontsize = 20)
    ax2.set_xlim(512-100, 512+100)
    ax2.set_ylim(512-100, 512+100)
    
    #plt.colorbar(ax3.imshow(rest), ax = ax3)
    plt.tight_layout()
    fig.suptitle(f'{name}, {date}', fontsize = 40, y = 1.05)
    plt.show()

    
    
    
    
    
    
    
    