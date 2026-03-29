# myunits

[![PyPI - Version](https://img.shields.io/pypi/v/myunits.svg)](https://pypi.org/project/myunits)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/myunits.svg)](https://pypi.org/project/myunits)

A simple module with a selection of units to simple conversions, using library
[`pint`](https://pypi.org/project/Pint/)

## Installation

```sh
pip install myunits
```

## Usage

Import all names from the module and make conversions:

```python
>>> from myunits import *
...
>>> press = 1 * psi
>>> stress = 1 * MPa
>>> compressibility = 100e-6 * cm ** 2 / kgf
...
>>> print(
...     f"Pressure:\n    {press} = {press.to(kPa)}\n"
...     f"Stress:\n    {stress} = {stress.to(kgf / cm **2)}\n"
...     f"Compressibility:\n    {compressibility} = {compressibility.to(1/GPa)}\n"
>>> )
Pressure:
    1 pound_force_per_square_inch = 6.894757293168363 kilopascal
Stress:
    1 megapascal = 10.197162129779283 force_kilogram / centimeter ** 2
Compressibility:
    0.0001 centimeter ** 2 / force_kilogram = 1.0197162129779282 / gigapascal
```

The defined units are:

- `kg` = kilogram
- `g` = gram
- `mg` = milligram
- `d` = day
- `s` = second
- `us` = microsecond
- `m` = meter
- `cm` = centimeter
- `mm` = millimeter
- `um` = micrometer
- `ft` = foot
- `bbl` = oil_barrel
- `Pa` = Pascal
- `kPa` = kiloPascal
- `MPa` = megaPascal
- `GPa` = gigaPascal
- `psi` = pound_force_per_square_inch
- `bar` = bar
- `sip` = 1.0 / pound_force_per_square_inch
- `rab` = 1.0 / bar
- `microsip` = 1e-06 / pound_force_per_square_inch
- `microrab` = 1e-06 / bar
- `usip` = 1e-06 / pound_force_per_square_inch
- `urab` = 1e-06 / bar
- `K` = Kelvin
- `R` = degree_Rankine
- `oC` = degree_Celsius
- `oF` = degree_Fahrenheit
- `kgf` = force_kilogram
- `N` = Newton
- `daN` = decaNewton
- `kN` = kiloNewton
- `MN` = megaNewton
- `GN` = gigaNewton
- `D` = Darcy
- `mD` = miliDarcy
- `P` = Poise
- `cP` = centiPoise
- `J` = Joule
- `kJ` = kiloJoule
- `MJ` = megaJoule
- `GJ` = gigaJoule
- `W` = Watt
- `kW` = kiloWatt
- `MW` = megaWatt
- `GW` = gigaWatt

## License

`myunits` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.
