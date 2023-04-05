import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as f
from os import listdir

#path = '/home/puck/Documents/brp/data'
path = '/net/vdesk/data2/rooijakkers/data' #Puck obs
#path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data' #Joep 


#------------------------Retrieving data---------------------------------
def star_info(star_list, idx):
    """ Returns the name of the star and date of observation
    
    :param star_list: A list of the names of the stars in the directory
    :type star_list: list
    :param idx: The index of the star you want in star_list
    :type idx: int
    :returns: The name of the file at idx and the data of observation 
    :rtype: str, str"""
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


#-------------------First data reduction----------------------------------
def mask_but_center(arr):
    ''' Masks everything but the area with radius r in a circle around the 
    center. '''
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


#--------------Finding the perfect median star------------------------------
def mask_aperture(arr):
    """ Creates a ring in arr between r = 30 and r = 50
    
    :param arr: An image of a star
    :type arr: numpy.ndarray
    :returns: The image where everything is masked but a ring at 30 < r < 50
    :rtype: numpy.ndarray """
    x = y = np.linspace(-(len(arr))/2, (len(arr))/2, len(arr))
    x_grid, y_grid = np.meshgrid(x, y)
    r_grid = np.sqrt(x_grid**2 + y_grid**2)
    arr[r_grid > 50] = None 
    arr[r_grid < 30] = None
    return arr

def arr_sort_rms(arr):
    """ Returns array of star images sorted from best to worst rms
    
    :param arr: Array containing images of stars
    :type arr: numpy.ndarray
    :returns:  array with sorted images and arr sorted from best to worst rms
    :rtype: numpy.ndarray, numpy.ndarray """
    rms_arr = np.nanstd(arr, axis = (1, 2)) #arr with rms of every image
    idx = np.argsort(rms_arr) #indexes sorted from best to worst rms
    return idx, arr[idx]

def median_image(sorted_arr):
    """ Creates a data cube where every ith image is the median of the first 
    i+1 images in sorted_arr and created an array containing the rms of these
    images 
    
    :param sorted_arr: Array containing images of stars sorted from best to 
    worst rms
    :type sorted_arr: numpy.ndarray
    :returns: len(sorted_arr)x1024x1024 array where every ith image is the 
    median of the first i+1 images in sorted_arr and an array with the rms
    of these images. 
    :rtype: numpy.ndarray, numpy.ndarray """
    med_cube = np.zeros([sorted_arr.shape[0]-1, sorted_arr.shape[1], 
                         sorted_arr.shape[2]]) #Cube containing all images. 
    rms_med_im = np.zeros(sorted_arr.shape[0]-1)
    
    for i in range(2, len(sorted_arr)+1):
        print(f'N = {i}')
        N_im = sorted_arr[0:i]
        med = np.median(N_im, axis = 0)
        rms = np.nanstd(med)
        rms_med_im[i-2] = rms
        med_cube[i-2] = med
    
    return med_cube, rms_med_im

#-----------------------Subtract stars---------------------------------------
def subtract_star(im, med_st):
    ''' Subtract the median star from the image and images the results'''
    return im-med_st



