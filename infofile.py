import numpy as np
from os import listdir

#Path leading to the data
path = '/home/puck/Documents/brp/data'
#path = '/net/vdesk/data2/rooijakkers/data' #Puck obs
# path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data' #Joep 

#Array containing the names of all stars
all_stars = np.array(sorted(listdir(path)))

#Array containing the names of the stars that are useless because they are 
#weird. 2MASSJ13032904-4723160 is star without flux image.

weird_names = np.array(['2MASSJ11320835-5803199', '2MASSJ11445217-6438548',
                        '2MASSJ11452016-5749094', '2MASSJ11555771-5254008',
                        '2MASSJ12041439-6418516', '2MASSJ12123577-5520273', 
                        '2MASSJ12185802-5737191', '2MASSJ12192161-6454101', 
                        '2MASSJ12205449-6457242', '2MASSJ12234012-5616325',
                        '2MASSJ12393796-5731406', '2MASSJ12472196-6808397',
                        '2MASSJ12510556-5253121', '2MASSJ12582559-7028490',
                        '2MASSJ13032904-4723160', '2MASSJ13055087-5304181',
                        '2MASSJ13121764-5508258', '2MASSJ13233587-4718467'])

#-----------------------------Binaries----------------------------------------

#An array containing the names of all binary stars in the WiSPiT survey.
bin_wp_names = np.array(['CD-43_3604','CVSO_751',
                         'Gaia_EDR3_3008386787098934144',
                         'Gaia_EDR3_3014970387847972096',
                         'HD_283629', 'HD_284266', 'HD_286179',
                         'UCAC4_127-038351', 'UCAC4_134-015937',
                         'UCAC4_200-015587', 'UCAC4_312-058127', 
                         'UCAC4_406-011818', 'UCAC4_454-011718', 
                         'UCAC4_475-014428', 'UCAC4_482-118442', 
                         'UCAC4_495-030196', 'UCAC4_496-013657', 
                         'UCAC4_501-011878', 'V1319_TAU'])


#An array containing the names of all binary stars in the YSES survey.
bin_y_names= np.array(['2MASSJ10065573-6352086', '2MASSJ11272881-3952572',
                       '2MASSJ12160114-5614068', '2MASSJ12210808-5212226', 
                       '2MASSJ12560830-6926539', '2MASSJ13015435-4249422', 
                       '2MASSJ13103245-4817036', '2MASSJ13130714-4537438', 
                       '2MASSJ13174687-4456534', '2MASSJ13335481-6536414'])

#An array containing the names of all binaries. 
bin_names = np.append(bin_wp_names, bin_y_names)
#--------------------------------Single stars---------------------------------

#An array containing the names of all single stars in the WiSPiT survey
sin_wp_names = np.array(['2MASS_J05162151+1147472', '2MASS_J05264348+0143538',
                         '2MASS_J06145339+0003000', 'CoRoT_102718810',
                         'GAIA_DR3_5854897321965963264',
                         'HD_285372', 'HD_285579',
                         'HD_285778', 'HD_285840',
                         'IRAS_08131-4432', 'J_618A',
                         'NSVS_14407747', 'RX_J2302.6+0034',
                         'UCAC4_141-082231', 'UCAC4_280-010722',
                         'UCAC4_319-026529', 'UCAC4_446-032370',
                         'UCAC4_461-018326', 'UCAC4_519-042115',
                         'UCAC4_537-015077', 'V_V1267_CEN',
                         'V_V1346_Tau', 'V_V826_Tau'])


#An array containing the names of all single stars in the YSES survey
sin_y_names = np.array(['2MASSJ10560422-6152054', '2MASSJ11175186-6402056',
                        '2MASSJ11275535-6626046', '2MASSJ11454278-5739285',
                        '2MASSJ12065276-5044463', '2MASSJ12090225-5120410',
                        '2MASSJ12101065-4855476', '2MASSJ12113142-5816533',
                        '2MASSJ12121119-4950081', '2MASSJ12163007-6711477',
                        '2MASSJ12164023-7007361', '2MASSJ12195938-5018404',
                        '2MASSJ12210499-7116493', '2MASSJ12220430-4841248',
                        '2MASSJ12240975-6003416', '2MASSJ12264842-5215070',
                        '2MASSJ12302957-5222269', '2MASSJ12333381-5714066',
                        '2MASSJ12361767-5042421', '2MASSJ12365895-5412178',
                        '2MASSJ12374883-5209463', '2MASSJ12383556-5916438',
                        '2MASSJ12391404-5454469', '2MASSJ12404664-5211046',
                        '2MASSJ12405458-5031550', '2MASSJ12454884-5410583',
                        '2MASSJ12480778-4439167', '2MASSJ12505143-5156353',
                        '2MASSJ13015069-5304581', '2MASSJ13064012-5159386',
                        '2MASSJ13065439-4541313', '2MASSJ13095880-4527388',
                        '2MASSJ13251211-6456207', '2MASSJ13334410-6359345',
                        '2MASSJ13343188-4209305', '2MASSJ13354082-4818124',
                        '2MASSJ13380596-4344564', '2MASSJ13381128-5214251',
                        '2MASSJ13444279-6347495', '2MASSJ13455599-5222255'])

#Array containing the names of all single stars
sin_names = np.append(sin_wp_names, sin_y_names)


#Array with all stars that are not weird
almost_all_stars = np.append(sin_names, bin_names)






