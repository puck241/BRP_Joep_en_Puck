import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as f
from os import listdir

# path = '/home/puck/Documents/BRP/data' #Puck
path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data' #Joep


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


#--------------------------Data reduction--------------------------------------
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

def data_reduction(arr):
    ''' Masks and then normalizes an array with one image. '''
    mask_arr = mask_but_center(arr)
    norm_arr = normalize(mask_arr)
    return norm_arr

#--------------------Finding the perfect single star---------------------------
def mask_aperture(arr):
    ''' Picks out a ring between radius 20 and 30 around the star and 
    returns this.  '''
    x = y = np.linspace(-(len(arr))/2, (len(arr))/2, len(arr))
    x_grid, y_grid = np.meshgrid(x, y)
    r_grid = np.sqrt(x_grid**2 + y_grid**2)
    arr[r_grid > 30] = None 
    arr[r_grid < 20] = None
    return arr

def arr_sort_rms(arr):
    ''' Returns an array with indexes of the image with the best 
    rms first and the worst rms last and returns the single star array 
    sorted from best to worst rms. '''
    rms_arr = np.nanstd(arr, axis = (1, 2)) 
    idx = np.argsort(rms_arr) 
    return idx, arr[idx]

def rms_image(arr):
    ''' Makes an image with the rms of every pixel '''
    return np.nanstd(arr, axis = 0)

#--------------------Finding the binaries from the reg files-------------------
def find_x_y_reg(file):
    ''' Opens the .reg file and returns the x and y coordinate in the file.'''
    loc_circle = 3
    sep = ','
    with open(file, 'rt') as reg:
        data_reg = reg.readlines()
        data_reg = data_reg[loc_circle]
    
    first, second = data_reg.find(sep), data_reg.rfind(sep)
    return float(data_reg[7:first]), float(data_reg[(first+1):second])

def make_reg_arr(bin_with_reg_list):
    arr = np.empty((len(bin_with_reg_list), 2))
    for i in range(len(bin_with_reg_list)):
        name, date = star_info(bin_with_reg_list, i)
        regfile = f'{path}/{name}/{date}/' + f'{name}_{date}.reg'
        x,y = find_x_y_reg(regfile)
        arr[i]=x,y
    return arr



