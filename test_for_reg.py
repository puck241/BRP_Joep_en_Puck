from regions import Regions

path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data'

testreg = r'C:\Users\joepn\OneDrive\Documenten\BRP\data\2MASSJ11555771-5254008\2017-04-02\2MASSJ11555771-5254008_2017-04-02.reg'
testreg2 = r'C:\Users\joepn\OneDrive\Documenten\BRP\data\2MASSJ12560830-6926539\2019-01-08\2MASSJ12560830-6926539_2019-01-08.reg'

regread = Regions.read(testreg, format='ds9')
regread2 = Regions.read(testreg2, format='ds9')


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



x, y = find_x_y_reg(testreg)
print('xpuck',x)
print('ypuck',y)

print('')

print('regread as string:',str(regread))
print('type:',type(regread))

print('')

x= float(str(regread)[38:47])+1
y= float(str(regread)[51:60])+1
print('xjoep',x)
print('yjoep',y)

# print('string',str(regread2))
# x2= float(str(regread2)[38:47])
# y2= float(str(regread2)[51:60])
# print(x2,y2)

