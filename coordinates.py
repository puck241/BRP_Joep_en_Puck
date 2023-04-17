import numpy as np

file = 'coordinates_ruwe.csv'

#data_type = np.dtype([('name', 'U29'), ('type', 'U1'),('ra', 'U12'), 
#                      ('dec', 'U12'), ('ruwe', 'float'), ('gaia_id', 'U28')])

data_type = np.dtype([('name', 'U29'), ('type', 'U1'), ('ruwe', 'f')])

data = np.loadtxt(file, dtype = data_type, skiprows = 1,
                  delimiter = ',', usecols = (0, 1, 4))

        
single = data[(data['type'] == 's')]
binary = data[(data['type'] == 'b')]

av_ruwe_bin = np.mean(binary['ruwe'])
std_ruwe_bin = np.std(binary['ruwe'])

av_ruwe_sin = np.mean(single['ruwe'])
std_ruwe_sin = np.std(single['ruwe'])


good = data[(data['ruwe'] <= 1.4)]
bad = data[(data['ruwe'] > 1.4)]
#%%
