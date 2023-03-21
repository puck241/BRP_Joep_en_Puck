import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as f
from os import listdir

# path = '/home/puck/Documents/BRP/data'
path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data'

def mask_stars(arr, star_list):
    ''' Makes a mask the size of star_list with False where the entry 
    of star_names matches arr. '''
    mask = np.ones_like(star_list, dtype = bool)
    for i in arr:
        idx = np.where(star_list == i)
        mask[idx] = False
    return mask

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

def mask_but_center(arr):
    ''' Masks everything but the area with radius r in a circle 
    around the center. '''
    x = y = np.linspace(-(len(arr))/2, (len(arr))/2, len(arr))
    x_grid, y_grid = np.meshgrid(x, y)
    r_grid = np.sqrt(x_grid**2 + y_grid**2)
    arr[r_grid > 100] = None 
    return arr

def normalize(arr):
    ''' Normalizes the array '''
    arr = np.array(arr,dtype=np.float64)
    return arr/np.nanmax(arr)

def calibration(arr):
    ''' Masks and then normalizes the array. '''
    mask_arr = mask_but_center(arr)
    norm_arr = normalize(mask_arr)
    return norm_arr

def print_stars(cal_data, star_list, idx):
    ''' Print the masked and normalised flux image of the star at index idx. '''
    name, date = star_info(star_list, idx)
    star = cal_data[idx]
    
    plt.subplot(1, 2, 1)
    plt.imshow(star)
    plt.gca().invert_yaxis()
    plt.xlim(400, 624)
    plt.ylim(400, 624)

    plt.subplot(1, 2, 2)
    plt.imshow(star)
    plt.gca().invert_yaxis()
    plt.xlim(500, 524)
    plt.ylim(500, 524)

    plt.suptitle(f'{name}, {date}', y = 0.8)
    plt.show()








