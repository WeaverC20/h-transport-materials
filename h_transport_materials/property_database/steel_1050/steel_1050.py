import h_transport_materials as htm
from h_transport_materials import Permeability, Solubility
import numpy as np

u = htm.ureg

bibsource = """@techreport{san_marchi_technical_2012,
    title = {Technical Reference for Hydrogen Compatibility of Materials},
    author = {San Marchi, Christopher W. and Somerday, Brian P.},
    number = {SAND2012-7321},
    doi = {10.2172/1055634},
    institution = {Sandia National Laboratories},
    year = {2012},
    month = {sep},
    pages = {1100--23},
}"""

perm_data = np.genfromtxt(
    htm.absolute_path("san_marchi_2012_permeability.csv"),
    delimiter=",",
)

steel_1050_permeability_h = Permeability(
    data_T=1000 / (perm_data[:, 0] * u.K**-1),
    data_y=perm_data[:, 1] * u.mol * u.m**-1 * u.s**-1 * u.MPa**-0.5,
    source="san_marchi_technical_2012",
    isotope="H",
    note="Figure p.1100-23",
)

sol_data = np.genfromtxt(
    htm.absolute_path("san_marchi_2012_solubility.csv"),
    delimiter=",",
)

steel_1050_solubility_h = Solubility(
    data_T=1000 / (sol_data[:, 0] * u.K**-1),
    data_y=sol_data[:, 1] * u.mol * u.m**-3 * u.MPa**-0.5,
    source="san_marchi_technical_2012",
    isotope="H",
    note="Figure p.1100-23",
)

properties = [steel_1050_permeability_h, steel_1050_solubility_h]

for prop in properties:
    prop.material = htm.STEEL_1050

htm.database += properties
