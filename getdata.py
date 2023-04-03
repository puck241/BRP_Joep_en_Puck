import infofile as IF
import functionfile as FF

#%%
#----------------------Original flux images-------------------------------

#len(arr_names) x 1024 x 1024
sin = FF.star_data(IF.sin_names) #all single

sin_y = FF.star_data(IF.sin_y_names) #YSES single

sin_wp = FF.star_data(IF.sin_wp_names) #WiSPiT single

bi = FF.star_data(IF.bin_names) #all binaries

bin_y = FF.star_data(IF.bin_y_names) #YSES binaries

bin_wp = FF.star_data(IF.bin_wp_names) #WiSPiT binaires

#%%
#------------Flux images masked around center and normalized-----------------
import numpy as np

sin_copy = sin.copy()
sin_data = np.array([FF.data_reduction(sin_copy[i]) 
                    for i in range(len(IF.sin_names))])

sin_y_copy = sin_y.copy()
sin_y_data = np.array([FF.data_reduction(sin_y_copy[i]) 
                    for i in range(len(IF.sin_y_names))])

sin_wp_copy = sin_wp.copy()
sin_wp_data = np.array([FF.data_reduction(sin_wp_copy[i]) 
                    for i in range(len(IF.sin_wp_names))])

#%%
#-------------------Mask apertures----------------------------------

















