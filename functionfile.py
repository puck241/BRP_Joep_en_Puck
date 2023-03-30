import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as f
from os import listdir

# path = '/home/puck/Documents/BRP/data' #Puck
path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data' #Joep

def star_info(star_list, idx):
    ''' Returns the name of the star and date of observation as a tuple. '''
    return star_list[idx], listdir(f'{path}/{star_list[idx]}')[0]

def star_data(star_list):
    ''' Returns the flux data of the stars in star_list in a 3d np.array. '''
    arr = np.empty((len(star_list), 1024, 1024))
    for i in range(len(star_list)):
        name, date = star_info(star_list, i)
        with f.open(f'{path}/{name}/{date}/B_H/calibration/flux/' + 
                    f'{name}_{date}_cube_flux_processed_right.fits') as hdul:
            data = hdul[0].data
        arr[i] = data[0]
    return arr





