import orekit
import numpy

vm = orekit.initVM()

from org.orekit.orbits import KeplerianOrbit, PositionAngle
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants
from org.orekit.frames import FramesFactory
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir()

# To activate once if a problem of orekit.Exception appears. (.getUtc())
# orekit.pyhelpers.download_orekit_data_curdir()


utc = TimeScalesFactory.getUTC()

ra = 400 * 1000         #  Apogee
rp = 500 * 1000         #  Perigee
i = numpy.radians(87.0)      # inclination
# FIXME: Use Hipparchus Library instead of numpy
omega = numpy.radians(20.0)   # perigee argument
raan = numpy.radians(10.0)  # right ascension of ascending node
lv = numpy.radians(0.0)    # True anomaly

epochDate = AbsoluteDate(2020, 1, 1, 0, 0, 00.000, utc)

a = (rp + ra + 2 * Constants.WGS84_EARTH_EQUATORIAL_RADIUS) / 2.0
e = 1.0 - (rp + Constants.WGS84_EARTH_EQUATORIAL_RADIUS) / a

# Inertial frame where the satellite is defined
inertialFrame = FramesFactory.getEME2000()

# Orbit construction as Keplerian
initialOrbit = KeplerianOrbit(24464560.0, 0.7311, 0.122138, 3.10686, 1.00681,
                                    0.048363, PositionAngle.MEAN,
                                    FramesFactory.getEME2000(), epochDate, Constants.GRS80_EARTH_MU);

print(initialOrbit)

