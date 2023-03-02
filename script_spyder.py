import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as f
from os import listdir

#The paths to the directories containing the stars
path_sin = 'data/single_stars'
path_bin = 'data/possible_binaries'

#Lists of names of stars
sin_st = sorted(listdir(path_sin)) 
bin_st = sorted(listdir(path_bin)) 

def star_info(path, idx):
    ''' Returns the name of the star and the date of the observation at index idx as a tuple. '''
    star_names = sorted(listdir(path))
    return star_names[idx], listdir(f'{path}/{star_names[idx]}')[0]

def star_data(path, idx):
    ''' Returns the flux data of the star at the corresponding data at index idx as a 2d numpy array. '''
    name, date = star_info(path, idx)
    with f.open(f'{path}/{name}/{date}/{name}_{date}_cube_flux_processed_right.fits') as hdul:
        data = hdul[0].data
    return data[0]

#Area you want to be left with
A = 200

def mask_but_center(arr):
    ''' Masks everything but the area with size A in a circle around the center. '''
    x = y = np.linspace(-(len(arr))/2, (len(arr))/2, len(arr))
    x_grid, y_grid = np.meshgrid(x, y)
    r_grid = np.sqrt(x_grid**2 + y_grid**2)
    arr[r_grid > np.sqrt(A/np.pi)] = None #np.sqrt(A/np.pi) gives the radius of a circle with size A
    return arr

def normalize(arr):
    ''' Normalizes the array '''
    return arr/np.max(arr)

def calibration(arr):
    norm_arr = normalize(arr)
    return mask_but_center(norm_arr)

def print_stars(path, idx):
    ''' Print the masked and normalised flux image of the star at index idx. '''
    name, date = star_info(path, idx)
    ster = calibration(star_data(path_sin, idx))
    plt.imshow(ster)
    plt.gca().invert_yaxis()
    plt.title(f'{name}, {date}')
    plt.xlim(500, 524)
    plt.ylim(500, 524)
    plt.colorbar
    plt.show()
    
for i in range(len(sin_st)):
    print_stars(path_sin, i)
        
for i in range(len(bin_st)):
    print_stars(path_bin, i)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    