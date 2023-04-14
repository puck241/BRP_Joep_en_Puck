from astropy.coordinates import SkyCoord as c
import astropy.units as u

import numpy as np
import infofile as IF

yses = IF.y_names

yses_coord = np.empty((len(yses), 2), dtype = 'U30')

for i in range(len(yses)):
      coords = c.from_name(yses[i], parse = True)
      yses_coord[i, 0] = yses[i]
      yses_coord[i, 1] = coords.to_string('hmsdms')

np.savetxt('yses_coordinates.csv', yses_coord, fmt = '%s', delimiter = ',')

