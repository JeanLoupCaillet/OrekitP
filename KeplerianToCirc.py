import orekit
import os
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "data.json")

vm = orekit.initVM()
from orekit.pyhelpers import setup_orekit_curdir
from org.orekit.orbits import KeplerianOrbit, PositionAngle
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.utils import Constants
from org.orekit.frames import FramesFactory
from org.orekit.propagation.analytical import KeplerianPropagator

# Setup the Orekit environment.
setup_orekit_curdir()
# In case of failure for utc dates
# orekit.pyhelpers.download_orekit_data_curdir()

"""
Creation of KeplerianElements' class. 
It will be the base of space mechanics calculations.
"""


class KeplerianElements:

    def __init__(self, a, e, i, w, gom, anomaly, position_angle, frame, current_date, mu):
        self.a = a
        self.e = e
        self.i = i
        self.w = w
        self.gom = gom
        self.anomaly = anomaly
        self.position_angle = position_angle
        self.frame = frame
        self.current_date = current_date
        self.mu = mu

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    # Initialisation of Keplerian orbital elements
    def init_keplerian_elements(self):
        return KeplerianOrbit(self.a, self.e, self.i,
                              self.w, self.gom, self.anomaly, self.position_angle,
                              self.frame, self.current_date, self.mu)


class Propagator:
    def __init__(self, initial_orbit, initial_date, shifted_date):
        self.shifted_date = shifted_date
        self.initial_orbit = initial_orbit
        self.initial_date = initial_date

    def __str__(self):
        return str(self.__dict__)

    def propagate_keplerian_elements(self):
        propagator = KeplerianPropagator(self.initial_orbit)
        return propagator.propagate(self.initial_date, self.shifted_date)


if __name__ == "__main__":
    instance = KeplerianElements(24464560.0, 0.7311, 0.122138, 3.10686, 1.00681,
                                 0.048363, PositionAngle.MEAN,
                                 FramesFactory.getEME2000(),
                                 AbsoluteDate(2020, 1, 1, 0, 0, 00.000, TimeScalesFactory.getUTC()),
                                 Constants.GRS80_EARTH_MU)
    k = instance.init_keplerian_elements()
    init_date = AbsoluteDate(2020, 1, 1, 0, 0, 00.000, TimeScalesFactory.getUTC())
    shift = init_date.shiftedBy(3600.0 * 48)
    kp = Propagator(k, init_date, shift)
    kp.propagate_keplerian_elements()
    print(k)
    print(kp)
