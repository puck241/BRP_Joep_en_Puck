import infofile as IF
import functionfile as FF

import numpy as np
import matplotlib.pyplot as plt

#Array with all the single stars, shape is (64, 1024, 1024)
sin_names = IF.sin_names
sin_data = FF.star_data(sin_names)

#Array with all the single stars but then masked and normalized
sin_data_copy = sin_data.copy()
sin_clb = np.array([FF.data_reduction(sin_data_copy[i]) 
                    for i in range(len(sin_names))])


#Array with all single stars and everything is masked but the aperture
sin_clb_copy = sin_clb.copy()
sin_aper = np.array([FF.mask_aperture(sin_clb_copy[i]) 
                     for i in range(len(sin_names))])

#sin_rms_sort is the calibrated and apertured data cube of single stars, 
#ordered from best to worst rms. 
rms_idx, sin_rms_sort = FF.arr_sort_rms(sin_aper)

rms_cube = np.empty_like(sin_rms_sort)
for i in range(len(sin_rms_sort)):
    idx_arr = rms_idx[0:i+1]
    rms_cube[i] = FF.rms_image(sin_rms_sort[idx_arr])

for i in range(len(rms_cube)):
    plt.figure()
    plt.title(f'RMS image N = {i+1}')
    plt.imshow(rms_cube[i])
    plt.xlim(482, 542)
    plt.ylim(482, 542)
    plt.colorbar()
    plt.show()





