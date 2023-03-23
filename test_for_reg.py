import functionfile as FF
import infofile as inf
import numpy as np

path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data'

def find_x_y_reg(file):
    ''' Opens the .reg file and returns the x and y coordinate in the file. loc_circle is the number of the line
    where the information on the circle is stored and sep is the thing used for seperating the x and y coord. '''
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
        name, date = FF.star_info(bin_with_reg_list, i)
        regfile = f'{path}/{name}/{date}/' + f'{name}_{date}.reg'
        x,y = find_x_y_reg(regfile)
        arr[i]=x,y
    return arr

print(make_reg_arr(inf.bin_with_reg))

