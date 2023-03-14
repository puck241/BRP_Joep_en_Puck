import numpy as np
from os import listdir

import functionfile as FF

path = '/home/puck/Documents/BRP/data'

#The images containing weird artifacts that make them useless
weird_names = np.array(['2MASSJ11320835-5803199', '2MASSJ12041439-6418516', 
                        '2MASSJ12123577-5520273', '2MASSJ12192161-6454101', 
                        '2MASSJ12205449-6457242', '2MASSJ12472196-6808397',
                        '2MASSJ12582559-7028490', '2MASSJ13032904-4723160'])

#2MASSJ13032904-4723160 is star without flux image

#The binaries we found in our initial search
bin1 = np.array(['2MASSJ11555771-5254008', '2MASSJ12560830-6926539', 
                 '2MASSJ13015435-4249422', '2MASSJ13130714-4537438', 
                 'CD-43_3604', 'CVSO_751', 'Gaia_EDR3_3008386787098934144',
                 'HD_283629', 'HD_284266', 'HD_286179', 'UCAC4_454-011718', 
                 'UCAC4_475-014428', 'UCAC4_495-030196','UCAC4_501-011878'])

#The binaries we found in our second searcg
bin2 = np.array(['2MASSJ10065573-6352086','2MASSJ11272881-3952572',
                 '2MASSJ11445217-6438548','2MASSJ11452016-5749094',
                 '2MASSJ12163007-6711477','2MASSJ12185802-5737191',
                 '2MASSJ12210808-5212226','2MASSJ12234012-5616325',
                 '2MASSJ13055087-5304181','2MASSJ13103245-4817036',
                 '2MASSJ13174687-4456534','2MASSJ13335481-6536414',
                 'CoRoT_102718810','Gaia_EDR3_3014970387847972096',
                 'IRAS_08131-4432','RX_J2302.6+0034','UCAC4_127-038351',
                 'UCAC4_134-015937','UCAC4_406-011818','UCAC4_461-018326',
                 'UCAC4_482-118442','UCAC4_496-013657','UCAC4_519-042115',
                 'V1319_TAU'])

bin_names = np.append(bin1, bin2)

#Array containing the names of all stars
all_stars = np.array(sorted(listdir(path)))

#Array with the names of single stars
sin_names = all_stars[(FF.mask_stars(bin_names, all_stars)*
                       FF.mask_stars(weird_names, all_stars))]

#Prints the amount of stars in every category
#print('Single stars:',len(sin_names),'\nBinary stars:',len(bin_names),
#      '\nWeird stars:',len(weird_names))

#Prints the stars for which we have more than 1 epoch.
#mask_dates = np.array([len(listdir(f'{path}/{all_stars[i]}'))!= 1 for i 
#                       in range(len(all_stars))])
#more_dates = all_stars[mask_dates]
#print(more_dates)

#Array with flux data for all single stars
sin_data = FF.star_data(sin_names)

#Array with flux data for all binary stars
#bin_data = FF.star_data(bin_names)

#Array with calibrated data for all single stars
sin_data_cal = np.array([FF.calibration(sin_data[i]) 
                         for i in range(len(sin_names))])
