# units
from pint import UnitRegistry

ureg = UnitRegistry()

# Mass
kg = ureg.kg
g = ureg.g

# Time
d = ureg.d
s = ureg.s
us = ureg.us

# Distance
m = ureg.m
cm = ureg.cm
mm = ureg.mm
um = ureg.um
ft = ureg.ft

# Volume
bbl = ureg.oil_bbl

# Pressure
Pa = ureg.Pa
kPa = ureg.kPa
MPa = ureg.MPa
GPa = ureg.GPa
psi = ureg.psi
bar = ureg.bar

# Temperature
K = ureg.kelvin
R = ureg.rankine
oC = ureg.degC
oF = ureg.degF

# Force
kgf = ureg.kgf
N = ureg.N
daN = ureg.daN
kN = ureg.kN
MN = ureg.MN
GN = ureg.GN

# Permeability
D = ureg.darcy
mD = 0.001 * D
ureg.define("mD = 0.001 * darcy")

# Viscosity
P = ureg.poise
cP = ureg.cP

# Energy
J = ureg.J
W = ureg.W
