import infofile as IF
import functionfile as FF

import astropy.io.fits as fits

import numpy as np
import matplotlib.pyplot as plt


#Median all star    
with fits.open('all_median_star.fits') as hdul:
    med_all = hdul[0].data
    
    
#Want to cut out only the star and subtract that?

#Want to translate the whole image?

#Is there an easy way to automate the locating process so I do not have to 
#look at every single image and determine where the binairy is. 




#ruwe in gaia 
#close to 1.0 --> the star is a singleton 
#but if it is a binary the ruwe 

#have the list of binaries
#have the positions 

#for the binaries where we have two epochs


info = np.array([FF.star_info(IF.almost_all_stars, i) for i in 
                  range(len(IF.almost_all_stars))])

np.savetxt('info.txt', info, fmt='%s')
