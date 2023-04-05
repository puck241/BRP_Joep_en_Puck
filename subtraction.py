#Run at vdesk tomorrow 
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

import functionfile as FF
import infofile as IF

#Median YSES star
with fits.open('YSES_median_star.fits') as hdul:
    med_y = hdul[0].data

#Median all star    
with fits.open('all_median_star.fits') as hdul:
    med_all = hdul[0].data
    
arr = IF.almost_all_stars

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
    
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(rest)
    plt.xlim(400, 624)
    plt.ylim(400, 624)
    
    plt.subplot(1,2,2)
    plt.imshow(rest)
    plt.colorbar()
    plt.xlim(500, 524)
    plt.ylim(500, 524)

    plt.suptitle(f'{name}, {date}')
    plt.show()

    
    
    
    
    
    
    
    