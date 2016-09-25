# ---------------------------------------------------------------------------
# Compares the observed mass of exoplanets vs the calculated mass
# Written with Python 3.5 (Anaconda)
#
# Modul:   AST241
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------
from __future__ import division
import csv
import math
import matplotlib.pyplot as plt
from decimal import *
from sympy import symbols
from sympy import Pow

# Constants
GRAVITATIONAL_CONSTANT = 6.67408e-11

# Correction factors to get SI dimensions
MASS_FACTOR = 1.898e27
ORBITAL_PERIOD_FACTOR = 86400
SEMI_MAJOR_AXIS_FACTOR = 149597870700

# Dimensions
kg, M_jup, M_solar, s, day, AU, m, G = symbols("kg M_jup M_solar s day AU m G")
M_jup = MASS_FACTOR * kg
M_solar = 1047.56 * M_jup
day = ORBITAL_PERIOD_FACTOR * s
AU = SEMI_MAJOR_AXIS_FACTOR * m
G = GRAVITATIONAL_CONSTANT * m**3 * kg**-1 * s**-2

# Calculates the mass given the formula from the lectures and returns it
def CalcMassFromOrbit(row):
    global GRAVITATIONAL_CONSTANT
    global MASS_FACTOR5
    global ORBITAL_PERIOD_FACTOR
    global SEMI_MAJOR_AXIS_FACTOR

    orbital_period = float(row["orbital_period"]) * day
    semi_major_axis = float(row["semi_major_axis"]) * AU

    # This is where the magic happens
    mass = 4 * math.pow(math.pi,2) * semi_major_axis**3 / (G * orbital_period**2)
    return float(mass / M_solar)
 
# Gets the data for the figure
def GetData(reader):
    calculatedMasses = []
    givenMasses = []

    for row in reader:
        if (row["orbital_period"] != "" and row["semi_major_axis"] != "" and row["star_mass"] != ""):
            calculatedMasses.append(CalcMassFromOrbit(row))
            givenMasses.append(float(row["star_mass"]))

    return calculatedMasses, givenMasses

# Creates and renders the plot using the given data
def CreatePlot(data):
    x, y = GetData(data)
    plt.scatter(x, y)
    plt.xlabel("Calculated host star mass [$M_Sol$]")
    plt.ylabel("Host star mass given by data [$M_Sol$]")
    plt.ylim(0,5)
    plt.xlim(0,5)
    plt.show()

# Entry point
if __name__ == '__main__':
    with open('exoplanet.eu_catalog.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        CreatePlot(reader)