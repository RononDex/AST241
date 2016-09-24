# ---------------------------------------------------------------------------
# Compares the observed mass of exoplanets vs the calculated mass
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

# Constants
GRAVITATIONAL_CONSTANT = Decimal(6.67408e-11)

# Correction factors to get SI dimensions
MASS_FACTOR = Decimal(1.898e27)
ORBITAL_PERIOD_FACTOR = Decimal(86400)
SEMI_MAJOR_AXIS_FACTOR = Decimal(149597870700)

# Calculates the mass given the formula from the lectures and returns it
def CalcMassFromOrbit(row):
    global GRAVITATIONAL_CONSTANT
    global MASS_FACTOR5
    global ORBITAL_PERIOD_FACTOR
    global SEMI_MAJOR_AXIS_FACTOR

    orbital_period = row["orbital_period"]
    semi_major_axis = row["semi_major_axis"]

    # What a long formula. Due to the syntax of python it's not possible to break it into several lines (wihtout doing more steps)
    # well I guess I need to buy a new widescreen monitor
    mass = Decimal(8) * Decimal(math.pow(Decimal(math.pi),3)) * Decimal(math.pow(Decimal(semi_major_axis) * SEMI_MAJOR_AXIS_FACTOR, 3)) / (GRAVITATIONAL_CONSTANT * Decimal(math.pow(Decimal(orbital_period) * ORBITAL_PERIOD_FACTOR, 3)))
    return float(mass / MASS_FACTOR)
 
# Gets the data for the figure
def GetData(reader):
    calculatedMasses = []
    givenMasses = []

    for row in reader:
        if (row["orbital_period"] != "" and row["semi_major_axis"] != "" and row["mass"] != ""):
            calculatedMasses.append(CalcMassFromOrbit(row))
            givenMasses.append(float(row["mass"]))

    return calculatedMasses, givenMasses

# Creates and renders the plot using the given data
def CreatePlot(data):
    x, y = GetData(data)
    plt.scatter(x, y)
    plt.xlabel("Calculated Mass [$\M_Jup]")
    plt.ylabel("Mass given by data [$\M_Jup]")
    plt.show()

# Entry point
if __name__ == '__main__':
    with open('exoplanet.eu_catalog.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        CreatePlot(reader)