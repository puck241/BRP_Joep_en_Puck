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
arr = IF.sin_wp_names
#%%
data = FF.star_data(arr)
copy = data.copy()
clb_data = np.array([FF.data_reduction(copy[i]) 
                    for i in range(len(arr))])

#%%
star = data[(arr == 'UCAC4_461-018326')].reshape(1024, 1024)
    
#%%
plt.figure()
plt.imshow(star, origin = 'lower')
plt.show()    
    
#%%
plt.figure()
plt.imshow(FF.data_reduction(star))   
plt.xlim(512-200, 512+200)
plt.ylim(512-200, 512+200)
plt.show()  
    
    
    