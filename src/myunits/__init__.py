# %%          UNITS
############# UNITS #########################################################################

__version__ = "0.10.2"

from pint import UnitRegistry

ureg = UnitRegistry()

# Mass
kg = ureg.kg
g = ureg.g
mg = ureg.mg
lb = ureg.lb
lbm = ureg.lb

# Time
year = ureg.year
d = ureg.d
h = ureg.h
minute = ureg.minute
minutes = ureg.minute
s = ureg.s
ms = ureg.ms
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

# %%          CONVERSIONS
############# CONVERSIONS #########################################################################

#####################################################################################
# %           Pressure
#####################################################################################


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


#####################################################################################
# %           Compressibility
#####################################################################################


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


def perMPa_to_perPa(value):
    """Convert 1/MPa to 1/Pa."""
    return (value * (1 / MPa)).to(1 / Pa)


def perGPa_to_perPa(value):
    """Convert 1/GPa to 1/Pa."""
    return (value * (1 / GPa)).to(1 / Pa)


def perGPa_to_perMPa(value):
    """Convert 1/GPa to 1/MPa."""
    return (value * (1 / GPa)).to(1 / MPa)


def perGPa_to_perkPa(value):
    """Convert 1/GPa to 1/kPa."""
    return (value * (1 / GPa)).to(1 / kPa)


def perGPa_to_perpsi(value):
    """Convert 1/GPa to 1/psi."""
    return (value * (1 / GPa)).to(1 / psi)


def perGPa_to_perbar(value):
    """Convert 1/GPa to 1/bar."""
    return (value * (1 / GPa)).to(1 / bar)


def perGPa_to_perusip(value):
    """Convert 1/GPa to 1/usip."""
    return (value * (1 / GPa)).to(1 / usip)


def perGPa_to_cm2perkgf(value):
    """Convert 1/GPa to cm²/kgf."""
    return (value * (1 / GPa)).to(cm**2 / kgf)


def cm2perkgf_to_perGPa(value):
    """Convert cm²/kgf to 1/GPa."""
    return (value * (cm**2 / kgf)).to(1 / GPa)


def cm2perkgf_to_perPa(value):
    """Convert cm²/kgf to 1/Pa."""
    return (value * (cm**2 / kgf)).to(1 / Pa)


def cm2perkgf_to_perMPa(value):
    """Convert cm²/kgf to 1/MPa."""
    return (value * (cm**2 / kgf)).to(1 / MPa)


def cm2perkgf_to_perkPa(value):
    """Convert cm²/kgf to 1/kPa."""
    return (value * (cm**2 / kgf)).to(1 / kPa)


def cm2perkgf_to_perpsi(value):
    """Convert cm²/kgf to 1/psi."""
    return (value * (cm**2 / kgf)).to(1 / psi)


#####################################################################################
# %           Time
#####################################################################################


def s_to_year(value):
    """Convert seconds to years."""
    return (value * s).to(year)


def s_to_d(value):
    """Convert seconds to days."""
    return (value * s).to(d)


def s_to_h(value):
    """Convert seconds to hours."""
    return (value * s).to(h)


def s_to_minute(value):
    """Convert seconds to minutes."""
    return (value * s).to(minute)


def s_to_ms(value):
    """Convert seconds to milliseconds."""
    return (value * s).to(ms)


def s_to_us(value):
    """Convert seconds to microseconds."""
    return (value * s).to(us)


def year_to_s(value):
    """Convert years to seconds."""
    return (value * year).to(s)


def d_to_s(value):
    """Convert days to seconds."""
    return (value * d).to(s)


def h_to_s(value):
    """Convert hours to seconds."""
    return (value * h).to(s)


def min_to_h(value):
    """Convert minutes to hours."""
    return (value * minute).to(h)
