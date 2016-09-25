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
from sympy import symbols
from sympy import Pow

# Constants
GRAVITATIONAL_CONSTANT = 6.67408e-11

# Correction factors to get SI dimensions
MASS_FACTOR = 1.898e27
ORBITAL_PERIOD_FACTOR = 86400
SEMI_MAJOR_AXIS_FACTOR = 149597870700

# Dimensions
kg, M_jup, s, day, AU, m, G = symbols("kg M_jup s day AU m G")
M_jup = MASS_FACTOR * kg
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

    # What a long formula. Due to the syntax of python it's not possible to break it into several lines (wihtout doing more steps)
    # well I guess I need to buy a new widescreen monitor
    mass = 4 * math.pow(math.pi,2) * semi_major_axis**3 / (G * orbital_period**2)
    return float(mass / M_jup)
 
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