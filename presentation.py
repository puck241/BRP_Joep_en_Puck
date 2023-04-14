import infofile as IF
import functionfile as FF

import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

wd_data = FF.star_data(IF.bin_names)
wd_clb_data = np.array([FF.data_reduction(wd_data[i]) 
                          for i in range(len(IF.bin_names))])

#Median all star    
with fits.open('med_star_all.fits') as hdul:
    med_all = hdul[0].data


for i in range(len(IF.bin_names)):
    rest = FF.subtract_star(wd_clb_data[i], med_all)
    
    name, date = FF.star_info(IF.bin_names, i)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
    ax1.imshow(wd_clb_data[i])
    ax1.set_title('Calibrated image', fontsize = 20)
    ax1.set_xlim(512-100, 512+100)
    ax1.set_ylim(512-100, 512+100)
    
    ax2.imshow(rest)
    ax2.set_title('Subtracted image', fontsize = 20)
    ax2.set_xlim(512-100, 512+100)
    ax2.set_ylim(512-100, 512+100)
    
    #plt.colorbar(ax3.imshow(rest), ax = ax3)
    plt.tight_layout()
    fig.suptitle(f'{name}, {date}, {i}', fontsize = 40, y = 1.05)
    plt.show()
    

#V1319_TAU good example
#2MASSJ13174687-4456534 also good example 

#Show perfect single star

# rest_tau = FF.subtract_star(bin_clb_data[22], med_all)
# name_tau, date_tau = FF.star_info(IF.bin_names, 22)

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (20, 10))
# ax1.imshow(bin_clb_data[22])
# ax1.set_title('Normalized image', fontsize = 20)
# ax1.set_xlim(512-100, 512+100)
# ax1.set_ylim(512-100, 512+100)

# ax2.imshow(rest_tau)
# ax2.set_title('Subtracted image', fontsize = 20)
# ax2.set_xlim(512-100, 512+100)
# ax2.set_ylim(512-100, 512+100)

# #plt.colorbar(ax3.imshow(rest), ax = ax3)
# #plt.tight_layout()
# #fig.suptitle(f'{name_tau}, {date_tau}', fontsize = 20, y = 1.05)
# plt.savefig('presentation2.png')

