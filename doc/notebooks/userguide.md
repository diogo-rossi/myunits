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
