import os
from pathlib import Path

import pyprj.markdown_utils as md_utils
import pyprj.nbmd as nbmd
from pint import UnitRegistry

from myunits import *

THIS_DIR = Path(__file__).parent
ROOT_DIR = THIS_DIR.parent
os.chdir(THIS_DIR)
NAMES = ["newton", "kelvin", "pascal", "darcy", "poise", "joule", "watt"]


def getprefix(value: float) -> str:
    prefixes = {
        1e-24: "y",
        1e-21: "z",
        1e-18: "a",
        1e-15: "f",
        1e-12: "p",
        1e-9: "n",
        1e-6: "u",
        1e-3: "mili",
        1e3: "k",
        1e6: "M",
        1e9: "G",
        1e12: "T",
        1e15: "P",
        1e18: "E",
        1e21: "Z",
        1e24: "Y",
    }
    return prefixes.get(value, "")


with open(ROOT_DIR / "README.md", "r", encoding="utf-8") as file:
    content = file.read()

with open(ROOT_DIR / "src/myunits/__init__.py", "r", encoding="utf-8") as file:
    module_content = file.readlines()

ureg = UnitRegistry()
definitions: list[str] = []
for line in module_content:
    if " = " in line.strip():
        cte, expr = line.strip().split(" = ")
        if "." not in cte and "(" not in expr:
            if "*" in expr:
                multiplier, unit = expr.split("*")
                prefix = getprefix(float(multiplier.strip()))
                description = prefix + eval(unit.strip()).__str__()
            else:
                description = eval(expr.strip()).__str__()
            for name in NAMES:
                if name in description:
                    description = description.replace(name, name.capitalize())
            definitions.append(f"- `{cte}` = {description}")

sections: list[str] = md_utils.get_markdown_sections(ROOT_DIR / "README.md")

nbmd.nbmd(Path("notebooks/userguide.ipynb"))

with open(THIS_DIR / "notebooks/userguide.md", "r", encoding="utf-8") as file:
    content = file.read()

index = [i for i, section in enumerate(sections) if section.startswith("## Usage")][0]


sections[index] = content + "\n" + "\n".join(definitions) + "\n\n"

with open(ROOT_DIR / "README.md", "w", encoding="utf-8") as file:
    file.write("".join(sections))
