import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as f
from os import listdir

#path to data
path = 'data'

#list of star names
star_names = np.array(sorted(listdir(path)))

#Show which stars have more than 1 file
mask_dates = np.array([len(listdir(f'data/{star_names[i]}'))!= 1 for i in range(len(star_names))])
more_dates = star_names[mask_dates]
print(more_dates)

mask_weird = np.ones_like(star_names, dtype = bool)
mask_weird[49] = False #2MASSJ13032904-4723160 no flux data 
star_names = star_names[mask_weird]

def star_info(idx):
    ''' Returns the name of the star and the date of the observation at index idx as a tuple. '''
    return star_names[idx], listdir(f'{path}/{star_names[idx]}')[0]

def star_data(idx):
    ''' Returns the flux data of the star at the corresponding data at index idx as a 2d numpy array. '''
    name, date = star_info(idx)
    with f.open(f'{path}/{name}/{date}/B_H/calibration/flux/{name}_{date}_cube_flux_processed_right.fits') as hdul:
        data = hdul[0].data
    return data[0]

def mask_but_center(arr, r):
    ''' Masks everything but the area with radius r in a circle around the center. '''
    x = y = np.linspace(-(len(arr))/2, (len(arr))/2, len(arr))
    x_grid, y_grid = np.meshgrid(x, y)
    r_grid = np.sqrt(x_grid**2 + y_grid**2)
    arr[r_grid > r] = None #np.sqrt(A/np.pi) gives the radius of a circle with size A
    return arr

def normalize(arr):
    ''' Normalizes the array '''
    arr = np.array(arr,dtype=np.float64)
    return arr/np.nanmax(arr)

def calibration(arr, r):
    ''' Masks and then normalizes the array. '''
    mask_arr = mask_but_center(arr, r)
    norm_arr = normalize(mask_arr)
    return norm_arr

def print_stars(idx):
    ''' Print the masked and normalised flux image of the star at index idx. '''
    name, date = star_info(idx)
    star = calibration(star_data(idx), 100)
    
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

    plt.suptitle(f'{name}, {date}, {idx}', y = 0.8)
    plt.show()
    
for i in range(len(star_names)):
        print_stars(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    