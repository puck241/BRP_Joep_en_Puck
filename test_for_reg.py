# import numpy as np
from regions import Regions
# import pyregion


path = r'C:\Users\joepn\OneDrive\Documenten\BRP\data'

testreg = r'C:\Users\joepn\OneDrive\Documenten\BRP\data\2MASSJ11555771-5254008\2017-04-02\2MASSJ11555771-5254008_2017-04-02.reg'
testreg2 = r'C:\Users\joepn\OneDrive\Documenten\BRP\data\2MASSJ12560830-6926539\2019-01-08\2MASSJ12560830-6926539_2019-01-08.reg'

regread = Regions.read(testreg, format='ds9')
regread2 = Regions.read(testreg2, format='ds9')
# regopen = pyregion.open(testreg)

# reg = open(testreg)
print('string',str(regread))
print(type(regread))
# print(regopen)

x= float(str(regread)[38:47])
y= float(str(regread)[51:60])
print(x,y)

print('string',str(regread2))
x2= float(str(regread2)[38:47])
y2= float(str(regread2)[51:60])
print(x2,y2)
#die godverdomme pyregion wilt niet installeren

# x=540.46633, y=502.95775), radius=6.6979685)>]