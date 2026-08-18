# units
from pint import UnitRegistry

ureg = UnitRegistry()

# Mass
kg = ureg.kg
g = ureg.g
mg = ureg.mg
lb = ureg.lb
lbm = ureg.lb

# Time
d = ureg.d
h = ureg.h
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

# Compressibility
sip = 1.0 / ureg.psi
rab = 1.0 / ureg.bar
microsip = sip / 1e6
microrab = rab / 1e6
usip = microsip
urab = microrab

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
lbf = ureg.lbf

# Permeability
D = ureg.darcy
mD = 0.001 * D
ureg.define("mD = 0.001 * darcy")

# Viscosity
P = ureg.poise
cP = ureg.cP

# Energy
J = ureg.J
kJ = ureg.kJ
MJ = ureg.MJ
GJ = ureg.GJ
W = ureg.W
kW = ureg.kW
MW = ureg.MW
GW = ureg.GW


def psi_to_Pa(value):
    """Convert psi to Pa."""
    return (value * psi).to(Pa)


def psi_to_kPa(value):
    """Convert psi to kPa."""
    return (value * psi).to(kPa)


def psi_to_MPa(value):
    """Convert psi to MPa."""
    return (value * psi).to(MPa)


def psi_to_GPa(value):
    """Convert psi to GPa."""
    return (value * psi).to(GPa)


def Pa_to_psi(value):
    """Convert Pa to psi."""
    return (value * Pa).to(psi)


def kPa_to_psi(value):
    """Convert kPa to psi."""
    return (value * kPa).to(psi)


def MPa_to_psi(value):
    """Convert MPa to psi."""
    return (value * MPa).to(psi)


def GPa_to_psi(value):
    """Convert GPa to psi."""
    return (value * GPa).to(psi)


def psi_to_bar(value):
    """Convert psi to bar."""
    return (value * psi).to(bar)


def sip_to_1_per_Pa(value):
    """Convert 1/psi to 1/Pa."""
    return (value * sip).to(1 / Pa)


def sip_to_1_per_kPa(value):
    """Convert 1/psi to 1/kPa."""
    return (value * sip).to(1 / kPa)


def sip_to_1_per_MPa(value):
    """Convert 1/psi to 1/MPa."""
    return (value * sip).to(1 / MPa)


def sip_to_1_per_GPa(value):
    """Convert 1/psi to 1/GPa."""
    return (value * sip).to(1 / GPa)


def usip_to_1_per_Pa(value):
    """Convert 1/usip to 1/Pa."""
    return (value * usip).to(1 / Pa)


def usip_to_1_per_kPa(value):
    """Convert 1/usip to 1/kPa."""
    return (value * usip).to(1 / kPa)


def usip_to_1_per_MPa(value):
    """Convert 1/usip to 1/MPa."""
    return (value * usip).to(1 / MPa)


def usip_to_1_per_GPa(value):
    """Convert 1/usip to 1/GPa."""
    return (value * usip).to(1 / GPa)
