import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import font
from tkinter import ttk
elment_info = [
    {"name": "hydrogen",
     "symbol": "H",
     "atomic_number": 1,
     "atomic_mass": 1.008,
     "electrons_per_shell": (1,),
     "state": "gas",
     "group": 1,
     "period": 1,
     "melting_point_k": 13.99,
     "boiling_point_k": 20.271,
     "density": 8.988e-05,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Henry Cavendish",
     "discovery_year": 1766},

    {"name": "helium",
     "symbol": "He",
     "atomic_number": 2,
     "atomic_mass": 4.0026,
     "electrons_per_shell": (2,),
     "state": "gas",
     "group": 18,
     "period": 1,
     "melting_point_k": 0.95,
     "boiling_point_k": 4.222,
     "density": 0.0001786,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Pierre Janssen, Norman Lockyer",
     "discovery_year": 1868},

    {"name": "lithium",
     "symbol": "Li",
     "atomic_number": 3,
     "atomic_mass": 6.94,
     "electrons_per_shell": (2, 1),
     "state": "solid",
     "group": 1,
     "period": 2,
     "melting_point_k": 453.65,
     "boiling_point_k": 1603,
     "density": 0.534,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Johan August Arfwedson",
     "discovery_year": 1817},

    {"name": "beryllium",
     "symbol": "Be",
     "atomic_number": 4,
     "atomic_mass": 9.0122,
     "electrons_per_shell": (2, 2),
     "state": "solid",
     "group": 2,
     "period": 2,
     "melting_point_k": 1560,
     "boiling_point_k": 2742,
     "density": 1.85,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Louis Nicolas Vauquelin",
     "discovery_year": 1798},

    {"name": "boron",
     "symbol": "B",
     "atomic_number": 5,
     "atomic_mass": 10.81,
     "electrons_per_shell": (2, 3),
     "state": "solid",
     "group": 13,
     "period": 2,
     "melting_point_k": 2349,
     "boiling_point_k": 4200,
     "density": 2.34,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Joseph Louis Gay-Lussac, Louis Jacques Thénard",
     "discovery_year": 1808},

    {"name": "carbon",
     "symbol": "C",
     "atomic_number": 6,
     "atomic_mass": 12.011,
     "electrons_per_shell": (2, 4),
     "state": "solid",
     "group": 14,
     "period": 2,
     "melting_point_k": 3823,
     "boiling_point_k": 5100,
     "density": 2.27,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Antoine Lavoisier",
     "discovery_year": 1789},

    {"name": "nitrogen",
     "symbol": "N",
     "atomic_number": 7,
     "atomic_mass": 14.007,
     "electrons_per_shell": (2, 5),
     "state": "gas",
     "group": 15,
     "period": 2,
     "melting_point_k": 63.23,
     "boiling_point_k": 77.355,
     "density": 0.00125,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Daniel Rutherford",
     "discovery_year": 1772},

    {"name": "oxygen",
     "symbol": "O",
     "atomic_number": 8,
     "atomic_mass": 15.999,
     "electrons_per_shell": (2, 6),
     "state": "gas",
     "group": 16,
     "period": 2,
     "melting_point_k": 54.36,
     "boiling_point_k": 90.188,
     "density": 0.001429,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Wilhelm Scheele",
     "discovery_year": 1771},

    {"name": "fluorine",
     "symbol": "F",
     "atomic_number": 9,
     "atomic_mass": 18.998,
     "electrons_per_shell": (2, 7),
     "state": "gas",
     "group": 17,
     "period": 2,
     "melting_point_k": 53.48,
     "boiling_point_k": 85.03,
     "density": 0.001696,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "André-Marie Ampère",
     "discovery_year": 1810},

    {"name": "neon",
     "symbol": "Ne",
     "atomic_number": 10,
     "atomic_mass": 20.18,
     "electrons_per_shell": (2, 8),
     "state": "gas",
     "group": 18,
     "period": 2,
     "melting_point_k": 24.56,
     "boiling_point_k": 27.104,
     "density": 0.0009002,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Ramsay, Morris Travers",
     "discovery_year": 1898},

    {"name": "sodium",
     "symbol": "Na",
     "atomic_number": 11,
     "atomic_mass": 22.99,
     "electrons_per_shell": (2, 8, 1),
     "state": "solid",
     "group": 1,
     "period": 3,
     "melting_point_k": 370.944,
     "boiling_point_k": 1156.09,
     "density": 0.968,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Humphry Davy",
     "discovery_year": 1807},

    {"name": "magnesium",
     "symbol": "Mg",
     "atomic_number": 12,
     "atomic_mass": 24.305,
     "electrons_per_shell": (2, 8, 2),
     "state": "solid",
     "group": 2,
     "period": 3,
     "melting_point_k": 923,
     "boiling_point_k": 1363,
     "density": 1.738,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Joseph Black",
     "discovery_year": 1755},

    {"name": "aluminium",
     "symbol": "Al",
     "atomic_number": 13,
     "atomic_mass": 26.982,
     "electrons_per_shell": (2, 8, 3),
     "state": "solid",
     "group": 13,
     "period": 3,
     "melting_point_k": 933.47,
     "boiling_point_k": 2743,
     "density": 2.7,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Hans Christian Ørsted",
     "discovery_year": 1824},

    {"name": "silicon",
     "symbol": "Si",
     "atomic_number": 14,
     "atomic_mass": 28.085,
     "electrons_per_shell": (2, 8, 4),
     "state": "solid",
     "group": 14,
     "period": 3,
     "melting_point_k": 1414,
     "boiling_point_k": 3538,
     "density": 2.329,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Jöns Jacob Berzelius",
     "discovery_year": 1823},

    {"name": "phosphorus",
     "symbol": "P",
     "atomic_number": 15,
     "atomic_mass": 30.974,
     "electrons_per_shell": (2, 8, 5),
     "state": "solid",
     "group": 15,
     "period": 3,
     "melting_point_k": 317.3,
     "boiling_point_k": 553.7,
     "density": 1.823,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Hennig Brand",
     "discovery_year": 1669},

    {"name": "sulfur",
     "symbol": "S",
     "atomic_number": 16,
     "atomic_mass": 32.06,
     "electrons_per_shell": (2, 8, 6),
     "state": "solid",
     "group": 16,
     "period": 3,
     "melting_point_k": 388.36,
     "boiling_point_k": 717.8,
     "density": 2.07,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Antoine Lavoisier",
     "discovery_year": 1777},

    {"name": "chlorine",
     "symbol": "Cl",
     "atomic_number": 17,
     "atomic_mass": 35.45,
     "electrons_per_shell": (2, 8, 7),
     "state": "gas",
     "group": 17,
     "period": 3,
     "melting_point_k": 171.6,
     "boiling_point_k": 239.11,
     "density": 0.0032,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Wilhelm Scheele",
     "discovery_year": 1774},

    {"name": "argon",
     "symbol": "Ar",
     "atomic_number": 18,
     "atomic_mass": 39.95,
     "electrons_per_shell": (2, 8, 8),
     "state": "gas",
     "group": 18,
     "period": 3,
     "melting_point_k": 83.81,
     "boiling_point_k": 87.302,
     "density": 0.001784,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Lord Rayleigh, William Ramsay",
     "discovery_year": 1894},

    {"name": "potassium",
     "symbol": "K",
     "atomic_number": 19,
     "atomic_mass": 39.098,
     "electrons_per_shell": (2, 8, 8, 1),
     "state": "solid",
     "group": 1,
     "period": 4,
     "melting_point_k": 336.7,
     "boiling_point_k": 1032,
     "density": 0.89,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Humphry Davy",
     "discovery_year": 1807},

    {"name": "calcium",
     "symbol": "Ca",
     "atomic_number": 20,
     "atomic_mass": 40.078,
     "electrons_per_shell": (2, 8, 8, 2),
     "state": "solid",
     "group": 2,
     "period": 4,
     "melting_point_k": 1115,
     "boiling_point_k": 1757,
     "density": 1.55,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Humphry Davy",
     "discovery_year": 1808},

    {"name": "scandium",
     "symbol": "Sc",
     "atomic_number": 21,
     "atomic_mass": 44.956,
     "electrons_per_shell": (2, 8, 9, 2),
     "state": "solid",
     "group": 3,
     "period": 4,
     "melting_point_k": 1814,
     "boiling_point_k": 3109,
     "density": 2.985,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Lars Fredrik Nilson",
     "discovery_year": 1879},

    {"name": "titanium",
     "symbol": "Ti",
     "atomic_number": 22,
     "atomic_mass": 47.867,
     "electrons_per_shell": (2, 8, 10, 2),
     "state": "solid",
     "group": 4,
     "period": 4,
     "melting_point_k": 1941,
     "boiling_point_k": 3560,
     "density": 4.506,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Gregor",
     "discovery_year": 1791},

    {"name": "vanadium",
     "symbol": "V",
     "atomic_number": 23,
     "atomic_mass": 50.942,
     "electrons_per_shell": (2, 8, 11, 2),
     "state": "solid",
     "group": 5,
     "period": 4,
     "melting_point_k": 2183,
     "boiling_point_k": 3680,
     "density": 6.11,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Nils Gabriel Sefström",
     "discovery_year": 1830},

    {"name": "chromium",
     "symbol": "Cr",
     "atomic_number": 24,
     "atomic_mass": 51.996,
     "electrons_per_shell": (2, 8, 13, 1),
     "state": "solid",
     "group": 6,
     "period": 4,
     "melting_point_k": 2180,
     "boiling_point_k": 2944,
     "density": 7.15,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Louis Nicolas Vauquelin",
     "discovery_year": 1794},

    {"name": "manganese",
     "symbol": "Mn",
     "atomic_number": 25,
     "atomic_mass": 54.938,
     "electrons_per_shell": (2, 8, 13, 2),
     "state": "solid",
     "group": 7,
     "period": 4,
     "melting_point_k": 1519,
     "boiling_point_k": 2334,
     "density": 7.21,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Wilhelm Scheele",
     "discovery_year": 1774},

    {"name": "iron",
     "symbol": "Fe",
     "atomic_number": 26,
     "atomic_mass": 55.845,
     "electrons_per_shell": (2, 8, 14, 2),
     "state": "solid",
     "group": 8,
     "period": 4,
     "melting_point_k": 1811,
     "boiling_point_k": 3134,
     "density": 7.874,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": None,
     "discovery_year": None},

    {"name": "cobalt",
     "symbol": "Co",
     "atomic_number": 27,
     "atomic_mass": 58.933,
     "electrons_per_shell": (2, 8, 15, 2),
     "state": "solid",
     "group": 9,
     "period": 4,
     "melting_point_k": 1768,
     "boiling_point_k": 3200,
     "density": 8.9,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Georg Brandt",
     "discovery_year": 1735},

    {"name": "nickel",
     "symbol": "Ni",
     "atomic_number": 28,
     "atomic_mass": 58.693,
     "electrons_per_shell": (2, 8, 16, 2),
     "state": "solid",
     "group": 10,
     "period": 4,
     "melting_point_k": 1728,
     "boiling_point_k": 3003,
     "density": 8.908,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Axel Fredrik Cronstedt",
     "discovery_year": 1751},

    {"name": "copper",
     "symbol": "Cu",
     "atomic_number": 29,
     "atomic_mass": 63.546,
     "electrons_per_shell": (2, 8, 18, 1),
     "state": "solid",
     "group": 11,
     "period": 4,
     "melting_point_k": 1357.77,
     "boiling_point_k": 2835,
     "density": 8.96,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Middle East",
     "discovery_year": -9000},

    {"name": "zinc",
     "symbol": "Zn",
     "atomic_number": 30,
     "atomic_mass": 65.38,
     "electrons_per_shell": (2, 8, 18, 2),
     "state": "solid",
     "group": 12,
     "period": 4,
     "melting_point_k": 692.68,
     "boiling_point_k": 1180,
     "density": 7.14,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Andreas Sigismund Marggraf",
     "discovery_year": 1746},

    {"name": "gallium",
     "symbol": "Ga",
     "atomic_number": 31,
     "atomic_mass": 69.723,
     "electrons_per_shell": (2, 8, 18, 3),
     "state": "solid",
     "group": 13,
     "period": 4,
     "melting_point_k": 302.9146,
     "boiling_point_k": 2673,
     "density": 5.91,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Lecoq de Boisbaudran",
     "discovery_year": 1875},

    {"name": "germanium",
     "symbol": "Ge",
     "atomic_number": 32,
     "atomic_mass": 72.63,
     "electrons_per_shell": (2, 8, 18, 4),
     "state": "solid",
     "group": 14,
     "period": 4,
     "melting_point_k": 1211.4,
     "boiling_point_k": 3106,
     "density": 5.323,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Clemens Winkler",
     "discovery_year": 1886},

    {"name": "arsenic",
     "symbol": "As",
     "atomic_number": 33,
     "atomic_mass": 74.922,
     "electrons_per_shell": (2, 8, 18, 5),
     "state": "solid",
     "group": 15,
     "period": 4,
     "melting_point_k": 1090,
     "boiling_point_k": 887,
     "density": 5.727,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Albertus Magnus",
     "discovery_year": 1250},

    {"name": "selenium",
     "symbol": "Se",
     "atomic_number": 34,
     "atomic_mass": 78.971,
     "electrons_per_shell": (2, 8, 18, 6),
     "state": "solid",
     "group": 16,
     "period": 4,
     "melting_point_k": 494,
     "boiling_point_k": 958,
     "density": 4.81,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Jöns Jakob Berzelius",
     "discovery_year": 1817},

    {"name": "bromine",
     "symbol": "Br",
     "atomic_number": 35,
     "atomic_mass": 79.904,
     "electrons_per_shell": (2, 8, 18, 7),
     "state": "liquid",
     "group": 17,
     "period": 4,
     "melting_point_k": 265.8,
     "boiling_point_k": 332,
     "density": 3.1028,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Antoine Jérôme Balard",
     "discovery_year": 1825},

    {"name": "krypton",
     "symbol": "Kr",
     "atomic_number": 36,
     "atomic_mass": 83.798,
     "electrons_per_shell": (2, 8, 18, 8),
     "state": "gas",
     "group": 18,
     "period": 4,
     "melting_point_k": 115.78,
     "boiling_point_k": 119.93,
     "density": 0.003749,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Ramsay, Morris Travers",
     "discovery_year": 1898},

    {"name": "rubidium",
     "symbol": "Rb",
     "atomic_number": 37,
     "atomic_mass": 85.468,
     "electrons_per_shell": (2, 8, 18, 8, 1),
     "state": "solid",
     "group": 1,
     "period": 5,
     "melting_point_k": 312.45,
     "boiling_point_k": 961,
     "density": 1.532,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Robert Bunsen, Gustav Kirchhoff",
     "discovery_year": 1861},

    {"name": "strontium",
     "symbol": "Sr",
     "atomic_number": 38,
     "atomic_mass": 87.62,
     "electrons_per_shell": (2, 8, 18, 8, 2),
     "state": "solid",
     "group": 2,
     "period": 5,
     "melting_point_k": 1050,
     "boiling_point_k": 1650,
     "density": 2.64,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Cruickshank",
     "discovery_year": 1787},

    {"name": "yttrium",
     "symbol": "Y",
     "atomic_number": 39,
     "atomic_mass": 88.906,
     "electrons_per_shell": (2, 8, 18, 9, 2),
     "state": "solid",
     "group": 3,
     "period": 5,
     "melting_point_k": 1799,
     "boiling_point_k": 3203,
     "density": 4.472,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Johan Gadolin",
     "discovery_year": 1794},

    {"name": "zirconium",
     "symbol": "Zr",
     "atomic_number": 40,
     "atomic_mass": 91.224,
     "electrons_per_shell": (2, 8, 18, 10, 2),
     "state": "solid",
     "group": 4,
     "period": 5,
     "melting_point_k": 2125,
     "boiling_point_k": 4650,
     "density": 6.52,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Martin Heinrich Klaproth",
     "discovery_year": 1789},

    {"name": "niobium",
     "symbol": "Nb",
     "atomic_number": 41,
     "atomic_mass": 92.906,
     "electrons_per_shell": (2, 8, 18, 12, 1),
     "state": "solid",
     "group": 5,
     "period": 5,
     "melting_point_k": 2750,
     "boiling_point_k": 5017,
     "density": 8.57,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Charles Hatchett",
     "discovery_year": 1801},

    {"name": "molybdenum",
     "symbol": "Mo",
     "atomic_number": 42,
     "atomic_mass": 95.95,
     "electrons_per_shell": (2, 8, 18, 13, 1),
     "state": "solid",
     "group": 6,
     "period": 5,
     "melting_point_k": 2896,
     "boiling_point_k": 4912,
     "density": 10.28,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Wilhelm Scheele",
     "discovery_year": 1778},

    {"name": "technetium",
     "symbol": "Tc",
     "atomic_number": 43,
     "atomic_mass": 98,
     "electrons_per_shell": (2, 8, 18, 13, 2),
     "state": "solid",
     "group": 7,
     "period": 5,
     "melting_point_k": 2430,
     "boiling_point_k": 4538,
     "density": 11,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Emilio Segrè, Carlo Perrier",
     "discovery_year": 1937},

    {"name": "ruthenium",
     "symbol": "Ru",
     "atomic_number": 44,
     "atomic_mass": 101.07,
     "electrons_per_shell": (2, 8, 18, 15, 1),
     "state": "solid",
     "group": 8,
     "period": 5,
     "melting_point_k": 2607,
     "boiling_point_k": 4423,
     "density": 12.45,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Karl Ernst Claus",
     "discovery_year": 1844},

    {"name": "rhodium",
     "symbol": "Rh",
     "atomic_number": 45,
     "atomic_mass": 102.91,
     "electrons_per_shell": (2, 8, 18, 16, 1),
     "state": "solid",
     "group": 9,
     "period": 5,
     "melting_point_k": 2237,
     "boiling_point_k": 3968,
     "density": 12.41,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Hyde Wollaston",
     "discovery_year": 1804},

    {"name": "palladium",
     "symbol": "Pd",
     "atomic_number": 46,
     "atomic_mass": 106.42,
     "electrons_per_shell": (2, 8, 18, 18),
     "state": "solid",
     "group": 10,
     "period": 5,
     "melting_point_k": 1828.05,
     "boiling_point_k": 3236,
     "density": 12.023,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Hyde Wollaston",
     "discovery_year": 1802},

    {"name": "silver",
     "symbol": "Ag",
     "atomic_number": 47,
     "atomic_mass": 107.87,
     "electrons_per_shell": (2, 8, 18, 18, 1),
     "state": "solid",
     "group": 11,
     "period": 5,
     "melting_point_k": 1234.93,
     "boiling_point_k": 2435,
     "density": 10.49,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": None,
     "discovery_year": None},

    {"name": "cadmium",
     "symbol": "Cd",
     "atomic_number": 48,
     "atomic_mass": 112.41,
     "electrons_per_shell": (2, 8, 18, 18, 2),
     "state": "solid",
     "group": 12,
     "period": 5,
     "melting_point_k": 594.22,
     "boiling_point_k": 1040,
     "density": 8.65,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Karl Samuel Leberecht Hermann, Friedrich Stromeyer",
     "discovery_year": 1817},

    {"name": "indium",
     "symbol": "In",
     "atomic_number": 49,
     "atomic_mass": 114.82,
     "electrons_per_shell": (2, 8, 18, 18, 3),
     "state": "solid",
     "group": 13,
     "period": 5,
     "melting_point_k": 429.7485,
     "boiling_point_k": 2345,
     "density": 7.31,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Ferdinand Reich, Hieronymous Theodor Richter",
     "discovery_year": 1863},

    {"name": "tin",
     "symbol": "Sn",
     "atomic_number": 50,
     "atomic_mass": 118.71,
     "electrons_per_shell": (2, 8, 18, 18, 4),
     "state": "solid",
     "group": 14,
     "period": 5,
     "melting_point_k": 505.08,
     "boiling_point_k": 2875,
     "density": 7.265,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": None,
     "discovery_year": None},

    {"name": "antimony",
     "symbol": "Sb",
     "atomic_number": 51,
     "atomic_mass": 121.76,
     "electrons_per_shell": (2, 8, 18, 18, 5),
     "state": "solid",
     "group": 15,
     "period": 5,
     "melting_point_k": 903.78,
     "boiling_point_k": 1908,
     "density": 6.697,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": None,
     "discovery_year": None},

    {"name": "tellurium",
     "symbol": "Te",
     "atomic_number": 52,
     "atomic_mass": 127.6,
     "electrons_per_shell": (2, 8, 18, 18, 6),
     "state": "solid",
     "group": 16,
     "period": 5,
     "melting_point_k": 722.66,
     "boiling_point_k": 1261,
     "density": 6.24,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Franz-Joseph Müller von Reichenstein",
     "discovery_year": 1782},

    {"name": "iodine",
     "symbol": "I",
     "atomic_number": 53,
     "atomic_mass": 126.9,
     "electrons_per_shell": (2, 8, 18, 18, 7),
     "state": "solid",
     "group": 17,
     "period": 5,
     "melting_point_k": 386.85,
     "boiling_point_k": 457.4,
     "density": 4.933,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Bernard Courtois",
     "discovery_year": 1811},

    {"name": "xenon",
     "symbol": "Xe",
     "atomic_number": 54,
     "atomic_mass": 131.29,
     "electrons_per_shell": (2, 8, 18, 18, 8),
     "state": "gas",
     "group": 18,
     "period": 5,
     "melting_point_k": 161.4,
     "boiling_point_k": 165.051,
     "density": 0.005894,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Ramsay, Morris Travers",
     "discovery_year": 1898},

    {"name": "caesium",
     "symbol": "Cs",
     "atomic_number": 55,
     "atomic_mass": 132.91,
     "electrons_per_shell": (2, 8, 18, 18, 8, 1),
     "state": "solid",
     "group": 1,
     "period": 6,
     "melting_point_k": 301.7,
     "boiling_point_k": 944,
     "density": 1.93,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Robert Bunsen, Gustav Kirchhoff",
     "discovery_year": 1860},

    {"name": "barium",
     "symbol": "Ba",
     "atomic_number": 56,
     "atomic_mass": 137.33,
     "electrons_per_shell": (2, 8, 18, 18, 8, 2),
     "state": "solid",
     "group": 2,
     "period": 6,
     "melting_point_k": 1000,
     "boiling_point_k": 2118,
     "density": 3.51,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Wilhelm Scheele",
     "discovery_year": 1772},

    {"name": "lanthanum",
     "symbol": "La",
     "atomic_number": 57,
     "atomic_mass": 138.91,
     "electrons_per_shell": (2, 8, 18, 18, 9, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1193,
     "boiling_point_k": 3737,
     "density": 6.162,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Gustaf Mosander",
     "discovery_year": 1838},

    {"name": "cerium",
     "symbol": "Ce",
     "atomic_number": 58,
     "atomic_mass": 140.12,
     "electrons_per_shell": (2, 8, 18, 19, 9, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1068,
     "boiling_point_k": 3716,
     "density": 6.77,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Martin Heinrich Klaproth, Jöns Jakob Berzelius, Wilhelm "
                  "Hisinger",
     "discovery_year": 1803},

    {"name": "praseodymium",
     "symbol": "Pr",
     "atomic_number": 59,
     "atomic_mass": 140.91,
     "electrons_per_shell": (2, 8, 18, 21, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1208,
     "boiling_point_k": 3403,
     "density": 6.77,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Auer von Welsbach",
     "discovery_year": 1885},

    {"name": "neodymium",
     "symbol": "Nd",
     "atomic_number": 60,
     "atomic_mass": 144.24,
     "electrons_per_shell": (2, 8, 18, 22, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1297,
     "boiling_point_k": 3347,
     "density": 7.01,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Auer von Welsbach",
     "discovery_year": 1885},

    {"name": "promethium",
     "symbol": "Pm",
     "atomic_number": 61,
     "atomic_mass": 145,
     "electrons_per_shell": (2, 8, 18, 23, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1315,
     "boiling_point_k": 3273,
     "density": 7.26,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Charles D. Coryell, Jacob A. Marinsky, Lawrence E. "
                  "Glendenin",
     "discovery_year": 1945},

    {"name": "samarium",
     "symbol": "Sm",
     "atomic_number": 62,
     "atomic_mass": 150.36,
     "electrons_per_shell": (2, 8, 18, 24, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1345,
     "boiling_point_k": 2173,
     "density": 7.52,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Lecoq de Boisbaudran",
     "discovery_year": 1879},

    {"name": "europium",
     "symbol": "Eu",
     "atomic_number": 63,
     "atomic_mass": 151.96,
     "electrons_per_shell": (2, 8, 18, 25, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1099,
     "boiling_point_k": 1802,
     "density": 5.244,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Eugène-Anatole Demarçay",
     "discovery_year": 1896},

    {"name": "gadolinium",
     "symbol": "Gd",
     "atomic_number": 64,
     "atomic_mass": 157.25,
     "electrons_per_shell": (2, 8, 18, 25, 9, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1585,
     "boiling_point_k": 3273,
     "density": 7.9,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Jean Charles Galissard de Marignac",
     "discovery_year": 1880},

    {"name": "terbium",
     "symbol": "Tb",
     "atomic_number": 65,
     "atomic_mass": 158.93,
     "electrons_per_shell": (2, 8, 18, 27, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1629,
     "boiling_point_k": 3396,
     "density": 8.23,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Gustaf Mosander",
     "discovery_year": 1843},

    {"name": "dysprosium",
     "symbol": "Dy",
     "atomic_number": 66,
     "atomic_mass": 162.5,
     "electrons_per_shell": (2, 8, 18, 28, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1680,
     "boiling_point_k": 2840,
     "density": 8.54,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Lecoq de Boisbaudran",
     "discovery_year": 1886},

    {"name": "holmium",
     "symbol": "Ho",
     "atomic_number": 67,
     "atomic_mass": 164.93,
     "electrons_per_shell": (2, 8, 18, 29, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1734,
     "boiling_point_k": 2873,
     "density": 8.79,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Jacques-Louis Soret, Marc Delafontaine, Per Teodor Cleve",
     "discovery_year": 1878},

    {"name": "erbium",
     "symbol": "Er",
     "atomic_number": 68,
     "atomic_mass": 167.26,
     "electrons_per_shell": (2, 8, 18, 30, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1802,
     "boiling_point_k": 3141,
     "density": 9.066,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Gustaf Mosander",
     "discovery_year": 1843},

    {"name": "thulium",
     "symbol": "Tm",
     "atomic_number": 69,
     "atomic_mass": 168.93,
     "electrons_per_shell": (2, 8, 18, 31, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1818,
     "boiling_point_k": 2223,
     "density": 9.32,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Per Teodor Cleve",
     "discovery_year": 1879},

    {"name": "ytterbium",
     "symbol": "Yb",
     "atomic_number": 70,
     "atomic_mass": 173.05,
     "electrons_per_shell": (2, 8, 18, 32, 8, 2),
     "state": "solid",
     "group": None,
     "period": 6,
     "melting_point_k": 1097,
     "boiling_point_k": 1469,
     "density": 6.9,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Jean Charles Galissard de Marignac",
     "discovery_year": 1878},

    {"name": "lutetium",
     "symbol": "Lu",
     "atomic_number": 71,
     "atomic_mass": 174.97,
     "electrons_per_shell": (2, 8, 18, 32, 9, 2),
     "state": "solid",
     "group": 3,
     "period": 6,
     "melting_point_k": 1925,
     "boiling_point_k": 3675,
     "density": 9.841,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Carl Auer von Welsbach, Georges Urbain",
     "discovery_year": 1906},

    {"name": "hafnium",
     "symbol": "Hf",
     "atomic_number": 72,
     "atomic_mass": 178.49,
     "electrons_per_shell": (2, 8, 18, 32, 10, 2),
     "state": "solid",
     "group": 4,
     "period": 6,
     "melting_point_k": 2506,
     "boiling_point_k": 4876,
     "density": 13.31,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Dirk Coster, George de Hevesy",
     "discovery_year": 1922},

    {"name": "tantalum",
     "symbol": "Ta",
     "atomic_number": 73,
     "atomic_mass": 180.95,
     "electrons_per_shell": (2, 8, 18, 32, 11, 2),
     "state": "solid",
     "group": 5,
     "period": 6,
     "melting_point_k": 3290,
     "boiling_point_k": 5731,
     "density": 16.69,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Anders Gustaf Ekeberg",
     "discovery_year": 1802},

    {"name": "tungsten",
     "symbol": "W",
     "atomic_number": 74,
     "atomic_mass": 183.84,
     "electrons_per_shell": (2, 8, 18, 32, 12, 2),
     "state": "solid",
     "group": 6,
     "period": 6,
     "melting_point_k": 3695,
     "boiling_point_k": 6203,
     "density": 19.25,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Juan José Elhuyar, Fausto Elhuyar",
     "discovery_year": 1783},

    {"name": "rhenium",
     "symbol": "Re",
     "atomic_number": 75,
     "atomic_mass": 186.21,
     "electrons_per_shell": (2, 8, 18, 32, 13, 2),
     "state": "solid",
     "group": 7,
     "period": 6,
     "melting_point_k": 3459,
     "boiling_point_k": 5903,
     "density": 21.02,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Walter Noddack, Ida Noddack, Otto Berg",
     "discovery_year": 1925},

    {"name": "osmium",
     "symbol": "Os",
     "atomic_number": 76,
     "atomic_mass": 190.23,
     "electrons_per_shell": (2, 8, 18, 32, 14, 2),
     "state": "solid",
     "group": 8,
     "period": 6,
     "melting_point_k": 3306,
     "boiling_point_k": 5285,
     "density": 22.59,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Smithson Tennant",
     "discovery_year": 1803},

    {"name": "iridium",
     "symbol": "Ir",
     "atomic_number": 77,
     "atomic_mass": 192.22,
     "electrons_per_shell": (2, 8, 18, 32, 15, 2),
     "state": "solid",
     "group": 9,
     "period": 6,
     "melting_point_k": 2719,
     "boiling_point_k": 4403,
     "density": 22.56,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Smithson Tennant",
     "discovery_year": 1803},

    {"name": "platinum",
     "symbol": "Pt",
     "atomic_number": 78,
     "atomic_mass": 195.08,
     "electrons_per_shell": (2, 8, 18, 32, 17, 1),
     "state": "solid",
     "group": 10,
     "period": 6,
     "melting_point_k": 2041.4,
     "boiling_point_k": 4098,
     "density": 21.45,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Antonio de Ulloa",
     "discovery_year": 1735},

    {"name": "gold",
     "symbol": "Au",
     "atomic_number": 79,
     "atomic_mass": 196.97,
     "electrons_per_shell": (2, 8, 18, 32, 18, 1),
     "state": "solid",
     "group": 11,
     "period": 6,
     "melting_point_k": 1337.33,
     "boiling_point_k": 3243,
     "density": 19.3,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Middle East",
     "discovery_year": None},

    {"name": "mercury",
     "symbol": "Hg",
     "atomic_number": 80,
     "atomic_mass": 200.59,
     "electrons_per_shell": (2, 8, 18, 32, 18, 2),
     "state": "liquid",
     "group": 12,
     "period": 6,
     "melting_point_k": 234.321,
     "boiling_point_k": 629.88,
     "density": 13.534,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": None,
     "discovery_year": None},

    {"name": "thallium",
     "symbol": "Tl",
     "atomic_number": 81,
     "atomic_mass": 204.38,
     "electrons_per_shell": (2, 8, 18, 32, 18, 3),
     "state": "solid",
     "group": 13,
     "period": 6,
     "melting_point_k": 577,
     "boiling_point_k": 1746,
     "density": 11.85,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "William Crookes",
     "discovery_year": 1861},

    {"name": "lead",
     "symbol": "Pb",
     "atomic_number": 82,
     "atomic_mass": 207.2,
     "electrons_per_shell": (2, 8, 18, 32, 18, 4),
     "state": "solid",
     "group": 14,
     "period": 6,
     "melting_point_k": 600.61,
     "boiling_point_k": 2022,
     "density": 11.34,
     "natural": True,
     "has_stable_isotope": True,
     "discovery": "Middle East",
     "discovery_year": None},

    {"name": "bismuth",
     "symbol": "Bi",
     "atomic_number": 83,
     "atomic_mass": 208.98,
     "electrons_per_shell": (2, 8, 18, 32, 18, 5),
     "state": "solid",
     "group": 15,
     "period": 6,
     "melting_point_k": 544.7,
     "boiling_point_k": 1837,
     "density": 9.78,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Claude François Geoffroy",
     "discovery_year": 1753},

    {"name": "polonium",
     "symbol": "Po",
     "atomic_number": 84,
     "atomic_mass": 209,
     "electrons_per_shell": (2, 8, 18, 32, 18, 6),
     "state": "solid",
     "group": 16,
     "period": 6,
     "melting_point_k": 527,
     "boiling_point_k": 1235,
     "density": 9.196,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Marie Curie, Pierre Curie",
     "discovery_year": 1898},

    {"name": "astatine",
     "symbol": "At",
     "atomic_number": 85,
     "atomic_mass": 210,
     "electrons_per_shell": (2, 8, 18, 32, 18, 7),
     "state": None,
     "group": 17,
     "period": 6,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Dale R. Corson, Kenneth R. Mackenzie, Emilio Segre",
     "discovery_year": 1940},

    {"name": "radon",
     "symbol": "Rn",
     "atomic_number": 86,
     "atomic_mass": 222,
     "electrons_per_shell": (2, 8, 18, 32, 18, 8),
     "state": "gas",
     "group": 18,
     "period": 6,
     "melting_point_k": 202,
     "boiling_point_k": 211.5,
     "density": 0.00973,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Ernest Rutherford, Robert B. Owens",
     "discovery_year": 1899},

    {"name": "francium",
     "symbol": "Fr",
     "atomic_number": 87,
     "atomic_mass": 223,
     "electrons_per_shell": (2, 8, 18, 32, 18, 8, 1),
     "state": "solid",
     "group": 1,
     "period": 7,
     "melting_point_k": 300,
     "boiling_point_k": 950,
     "density": None,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Marguerite Perey",
     "discovery_year": 1939},

    {"name": "radium",
     "symbol": "Ra",
     "atomic_number": 88,
     "atomic_mass": 226,
     "electrons_per_shell": (2, 8, 18, 32, 18, 8, 2),
     "state": "solid",
     "group": 2,
     "period": 7,
     "melting_point_k": 973,
     "boiling_point_k": 2010,
     "density": 5.5,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Marie Curie, Pierre Curie",
     "discovery_year": 1898},

    {"name": "actinium",
     "symbol": "Ac",
     "atomic_number": 89,
     "atomic_mass": 227,
     "electrons_per_shell": (2, 8, 18, 32, 18, 9, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1323,
     "boiling_point_k": 3473,
     "density": 10,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Friedrich Oskar Giesel",
     "discovery_year": 1902},

    {"name": "thorium",
     "symbol": "Th",
     "atomic_number": 90,
     "atomic_mass": 232.04,
     "electrons_per_shell": (2, 8, 18, 32, 18, 10, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 2023,
     "boiling_point_k": 5061,
     "density": 11.7,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Jöns Jakob Berzelius",
     "discovery_year": 1829},

    {"name": "protactinium",
     "symbol": "Pa",
     "atomic_number": 91,
     "atomic_mass": 231.04,
     "electrons_per_shell": (2, 8, 18, 32, 20, 9, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1841,
     "boiling_point_k": 4300,
     "density": 15.37,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Kasimir Fajans, Oswald Helmuth Göhring",
     "discovery_year": 1913},

    {"name": "uranium",
     "symbol": "U",
     "atomic_number": 92,
     "atomic_mass": 238.03,
     "electrons_per_shell": (2, 8, 18, 32, 21, 9, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1405.3,
     "boiling_point_k": 4404,
     "density": 19.1,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Martin Heinrich Klaproth",
     "discovery_year": 1789},

    {"name": "neptunium",
     "symbol": "Np",
     "atomic_number": 93,
     "atomic_mass": 237,
     "electrons_per_shell": (2, 8, 18, 32, 22, 9, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 912,
     "boiling_point_k": None,
     "density": 20.45,
     "natural": True,
     "has_stable_isotope": False,
     "discovery": "Edwin McMillan, Philip H. Abelson",
     "discovery_year": 1940},

    {"name": "plutonium",
     "symbol": "Pu",
     "atomic_number": 94,
     "atomic_mass": 244,
     "electrons_per_shell": (2, 8, 18, 32, 24, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 912.5,
     "boiling_point_k": 3505,
     "density": 19.85,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Glenn T. Seaborg, Arthur Wahl, Joseph W. Kennedy, Edwin "
                  "McMillan",
     "discovery_year": 1940},

    {"name": "americium",
     "symbol": "Am",
     "atomic_number": 95,
     "atomic_mass": 243,
     "electrons_per_shell": (2, 8, 18, 32, 25, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1449,
     "boiling_point_k": None,
     "density": 12,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Glenn T. Seaborg, Ralph A. James, Leon O. Morgan, Albert "
                  "Ghiorso",
     "discovery_year": 1944},

    {"name": "curium",
     "symbol": "Cm",
     "atomic_number": 96,
     "atomic_mass": 247,
     "electrons_per_shell": (2, 8, 18, 32, 25, 9, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1613,
     "boiling_point_k": 3383,
     "density": 13.51,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Glenn T. Seaborg, Ralph A. James, Albert Ghiorso",
     "discovery_year": 1944},

    {"name": "berkelium",
     "symbol": "Bk",
     "atomic_number": 97,
     "atomic_mass": 247,
     "electrons_per_shell": (2, 8, 18, 32, 27, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1259,
     "boiling_point_k": None,
     "density": 14.78,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory",
     "discovery_year": 1949},

    {"name": "californium",
     "symbol": "Cf",
     "atomic_number": 98,
     "atomic_mass": 251,
     "electrons_per_shell": (2, 8, 18, 32, 28, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1173,
     "boiling_point_k": None,
     "density": 15.1,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory",
     "discovery_year": 1950},

    {"name": "einsteinium",
     "symbol": "Es",
     "atomic_number": 99,
     "atomic_mass": 252,
     "electrons_per_shell": (2, 8, 18, 32, 29, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1133,
     "boiling_point_k": None,
     "density": 8.84,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory",
     "discovery_year": 1952},

    {"name": "fermium",
     "symbol": "Fm",
     "atomic_number": 100,
     "atomic_mass": 257,
     "electrons_per_shell": (2, 8, 18, 32, 30, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1800,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory",
     "discovery_year": 1952},

    {"name": "mendelevium",
     "symbol": "Md",
     "atomic_number": 101,
     "atomic_mass": 258,
     "electrons_per_shell": (2, 8, 18, 32, 31, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1100,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory",
     "discovery_year": 1955},

    {"name": "nobelium",
     "symbol": "No",
     "atomic_number": 102,
     "atomic_mass": 259,
     "electrons_per_shell": (2, 8, 18, 32, 32, 8, 2),
     "state": "solid",
     "group": None,
     "period": 7,
     "melting_point_k": 1100,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research",
     "discovery_year": 1966},

    {"name": "lawrencium",
     "symbol": "Lr",
     "atomic_number": 103,
     "atomic_mass": 266,
     "electrons_per_shell": (2, 8, 18, 32, 32, 8, 3),
     "state": "solid",
     "group": 3,
     "period": 7,
     "melting_point_k": 1900,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory, Joint Institute "
                  "for Nuclear Research",
     "discovery_year": 1961},

    {"name": "rutherfordium",
     "symbol": "Rf",
     "atomic_number": 104,
     "atomic_mass": 267,
     "electrons_per_shell": (2, 8, 18, 32, 32, 10, 2),
     "state": "solid",
     "group": 4,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research",
     "discovery_year": 1964},

    {"name": "dubnium",
     "symbol": "Db",
     "atomic_number": 105,
     "atomic_mass": 268,
     "electrons_per_shell": (2, 8, 18, 32, 32, 11, 2),
     "state": "solid",
     "group": 5,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory, Joint Institute "
                  "for Nuclear Research",
     "discovery_year": 1970},

    {"name": "seaborgium",
     "symbol": "Sg",
     "atomic_number": 106,
     "atomic_mass": 269,
     "electrons_per_shell": (2, 8, 18, 32, 32, 12, 2),
     "state": "solid",
     "group": 6,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Lawrence Berkeley National Laboratory",
     "discovery_year": 1974},

    {"name": "bohrium",
     "symbol": "Bh",
     "atomic_number": 107,
     "atomic_mass": 270,
     "electrons_per_shell": (2, 8, 18, 32, 32, 13, 2),
     "state": "solid",
     "group": 7,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Gesellschaft für Schwerionenforschung",
     "discovery_year": 1981},

    {"name": "hassium",
     "symbol": "Hs",
     "atomic_number": 108,
     "atomic_mass": 269,
     "electrons_per_shell": (2, 8, 18, 32, 32, 14, 2),
     "state": "solid",
     "group": 8,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Gesellschaft für Schwerionenforschung",
     "discovery_year": 1984},

    {"name": "meitnerium",
     "symbol": "Mt",
     "atomic_number": 109,
     "atomic_mass": 278,
     "electrons_per_shell": (2, 8, 18, 32, 32, 15, 2),
     "state": "solid",
     "group": 9,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Gesellschaft für Schwerionenforschung",
     "discovery_year": 1982},

    {"name": "darmstadtium",
     "symbol": "Ds",
     "atomic_number": 110,
     "atomic_mass": 281,
     "electrons_per_shell": (2, 8, 18, 32, 32, 16, 2),
     "state": "solid",
     "group": 10,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Gesellschaft für Schwerionenforschung",
     "discovery_year": 1994},

    {"name": "roentgenium",
     "symbol": "Rg",
     "atomic_number": 111,
     "atomic_mass": 282,
     "electrons_per_shell": (2, 8, 18, 32, 32, 17, 2),
     "state": "solid",
     "group": 11,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Gesellschaft für Schwerionenforschung",
     "discovery_year": 1994},

    {"name": "copernicium",
     "symbol": "Cn",
     "atomic_number": 112,
     "atomic_mass": 285,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 2),
     "state": None,
     "group": 12,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Gesellschaft für Schwerionenforschung",
     "discovery_year": 1996},

    {"name": "nihonium",
     "symbol": "Nh",
     "atomic_number": 113,
     "atomic_mass": 286,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 3),
     "state": "solid",
     "group": 13,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Riken",
     "discovery_year": 2004},

    {"name": "flerovium",
     "symbol": "Fl",
     "atomic_number": 114,
     "atomic_mass": 289,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 4),
     "state": None,
     "group": 14,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research, Lawrence Livermore "
                  "National Laboratory",
     "discovery_year": 1998},

    {"name": "moscovium",
     "symbol": "Mc",
     "atomic_number": 115,
     "atomic_mass": 290,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 5),
     "state": "solid",
     "group": 15,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research, Lawrence Livermore "
                  "National Laboratory",
     "discovery_year": 2003},

    {"name": "livermorium",
     "symbol": "Lv",
     "atomic_number": 116,
     "atomic_mass": 293,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 6),
     "state": "solid",
     "group": 16,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research, Lawrence Livermore "
                  "National Laboratory",
     "discovery_year": 2000},

    {"name": "tennessine",
     "symbol": "Ts",
     "atomic_number": 117,
     "atomic_mass": 294,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 7),
     "state": "solid",
     "group": 17,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research, Lawrence Livermore "
                  "National Laboratory, Vanderbilt University, Oak Ridge "
                  "National Laboratory",
     "discovery_year": 2009},

    {"name": "oganesson",
     "symbol": "Og",
     "atomic_number": 118,
     "atomic_mass": 294,
     "electrons_per_shell": (2, 8, 18, 32, 32, 18, 8),
     "state": "solid",
     "group": 18,
     "period": 7,
     "melting_point_k": None,
     "boiling_point_k": None,
     "density": None,
     "natural": False,
     "has_stable_isotope": False,
     "discovery": "Joint Institute for Nuclear Research, Lawrence Livermore "
                  "National Laboratory",
     "discovery_year": 2002}]
window = Tk()

window_width = window .winfo_screenwidth()
window_height =window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (window_width,window_height))
# window.geometry('1200x600')
# window.resizable(width=False, height= False)
icon = PhotoImage(file = 'img_1.png')
bg_image = tkinter.Label(window, image=icon)
window.iconphoto(False, icon)
bg_image.place(relheight=1, relwidth =1)
from time import strftime
def time():
     string = strftime('%H:%M:%S %p')
     lbl1 = Label(window, font=('arial', 20, 'bold'),
            background='purple',
            foreground='white')
     lbl1.config(text=string)
     lbl1.after(1000, time)
     lbl1.place(x = 1685, y = 20)

time()
window.config(background='#F1B3E3')
window.title('Periodic Table of Element')
def command1():
 label1['text'] = elment_get1(0)
 label2['text'] = elment_get2(0)

def command2():
 label1['text'] = elment_get1(1)
 label2['text'] = elment_get2(1)

def command3():
 label1['text'] = elment_get1(2)
 label2['text'] = elment_get2(2)

def command4():
  label1['text'] = elment_get1(3)
  label2['text'] = elment_get2(3)

def command5():
  label1['text'] = elment_get1(4)
  label2['text'] = elment_get2(4)

def command6():
  label1['text'] = elment_get1(5)
  label2['text'] = elment_get2(5)
def command7():
 label1['text'] = elment_get1(6)
 label2['text'] = elment_get2(6)

def command8():
  label1['text'] = elment_get1(7)
  label2['text'] = elment_get2(7)

def command9():
  label1['text'] = elment_get1(8)
  label2['text'] = elment_get2(8)

def command10():
  label1['text'] = elment_get1(9)
  label2['text'] = elment_get2(9)

def command11():
   label1['text'] = elment_get1(10)
   label2['text'] = elment_get2(10)

def command12():
   label1['text'] = elment_get1(11)
   label2['text'] = elment_get2(11)

def command13():
   label1['text'] = elment_get1(12)
   label2['text'] = elment_get2(12)

def command14():
  label1['text'] = elment_get1(13)
  label2['text'] = elment_get2(13)


def command15():
  label1['text'] = elment_get1(14)
  label2['text'] = elment_get2(14)


def command16():
 label1['text'] = elment_get1(15)
 label2['text'] = elment_get2(15)


def command17():
 label1['text'] = elment_get1(16)
 label2['text'] = elment_get2(16)


def command18():
 label1['text'] = elment_get1(17)
 label2['text'] = elment_get2(17)

def command19():
  label1['text'] = elment_get1(18)
  label2['text'] = elment_get2(18)


def command20():
 label1['text'] = elment_get1(19)
 label2['text'] = elment_get2(19)


def command21():
 label1['text'] = elment_get1(20)
 label2['text'] = elment_get2(20)


def command22():
 label1['text'] = elment_get1(21)
 label2['text'] = elment_get2(21)


def command23():
 label1['text'] = elment_get1(22)
 label2['text'] = elment_get2(22)


def command24():
 label1['text'] = elment_get1(23)
 label2['text'] = elment_get2(23)


def command25():
 label1['text'] = elment_get1(24)
 label2['text'] = elment_get2(24)


def command26():
 label1['text'] = elment_get1(25)
 label2['text'] = elment_get2(25)


def command27():
 label1['text'] = elment_get1(26)
 label2['text'] = elment_get2(26)


def command28():
 label1['text'] = elment_get1(27)
 label2['text'] = elment_get2(27)


def command29():
 label1['text'] = elment_get1(28)
 label2['text'] = elment_get2(28)


def command30():
 label1['text'] = elment_get1(29)
 label2['text'] = elment_get2(29)

def command31():
  label1['text'] = elment_get1(30)
  label2['text'] = elment_get2(30)


def command32():
 label1['text'] = elment_get1(31)
 label2['text'] = elment_get2(31)


def command33():
 label1['text'] = elment_get1(32)
 label2['text'] = elment_get2(32)


def command34():
 label1['text'] = elment_get1(33)
 label2['text'] = elment_get2(33)


def command35():
 label1['text'] = elment_get1(34)
 label2['text'] = elment_get2(34)


def command36():
 label1['text'] = elment_get1(35)
 label2['text'] = elment_get2(35)

def command37():
 label1['text'] = elment_get1(36)
 label2['text'] = elment_get2(36)

def command38():
 label1['text'] = elment_get1(37)
 label2['text'] = elment_get2(37)

def command39():
 label1['text'] = elment_get1(38)
 label2['text'] = elment_get2(38)


def command40():
  label1['text'] = elment_get1(39)
  label2['text'] = elment_get2(39)


def command41():
 label1['text'] = elment_get1(40)
 label2['text'] = elment_get2(40)


def command42():
 label1['text'] = elment_get1(41)
 label2['text'] = elment_get2(41)


def command43():
 label1['text'] = elment_get1(42)
 label2['text'] = elment_get2(42)


def command44():
 label1['text'] = elment_get1(43)
 label2['text'] = elment_get2(43)


def command45():
 label1['text'] = elment_get1(44)
 label2['text'] = elment_get2(44)


def command46():
 label1['text'] = elment_get1(45)
 label2['text'] = elment_get2(45)


def command47():
 label1['text'] = elment_get1(46)
 label2['text'] = elment_get2(46)


def command48():
 label1['text'] = elment_get1(47)
 label2['text'] = elment_get2(47)


def command49():
 label1['text'] = elment_get1(48)
 label2['text'] = elment_get2(48)


def command50():
 label1['text'] = elment_get1(49)
 label2['text'] = elment_get2(49)

def command51():
  label1['text'] = elment_get1(50)
  label2['text'] = elment_get2(50)


def command52():
 label1['text'] = elment_get1(51)
 label2['text'] = elment_get2(51)


def command53():
  label1['text'] = elment_get1(52)
  label2['text'] = elment_get2(52)


def command54():
 label1['text'] = elment_get1(53)
 label2['text'] = elment_get2(53)


def command55():
 label1['text'] = elment_get1(54)
 label2['text'] = elment_get2(54)


def command56():
 label1['text'] = elment_get1(55)
 label2['text'] = elment_get2(55)

def command57():
 label1['text'] = elment_get1(56)
 label2['text'] = elment_get2(56)

def command57_71():
  label1['text'] = ''
  label2['text'] = ''


def command58():
 label1['text'] = elment_get1(57)
 label2['text'] = elment_get2(57)


def command59():
 label1['text'] = elment_get1(58)
 label2['text'] = elment_get2(58)


def command60():
  label1['text'] = elment_get1(59)
  label2['text'] = elment_get2(59)


def command61():
 label1['text'] = elment_get1(60)
 label2['text'] = elment_get2(60)


def command62():
 label1['text'] = elment_get1(61)
 label2['text'] = elment_get2(61)


def command63():
  label1['text'] = elment_get1(62)
  label2['text'] = elment_get2(62)


def command64():
 label1['text'] = elment_get1(63)
 label2['text'] = elment_get2(63)


def command65():
 label1['text'] = elment_get1(64)
 label2['text'] = elment_get2(64)


def command66():
 label1['text'] = elment_get1(65)
 label2['text'] = elment_get2(65)


def command67():
 label1['text'] = elment_get1(66)
 label2['text'] = elment_get2(66)


def command68():
 label1['text'] = elment_get1(67)
 label2['text'] = elment_get2(67)


def command69():
  label1['text'] = elment_get1(68)
  label2['text'] = elment_get2(68)


def command70():
 label1['text'] = elment_get1(69)
 label2['text'] = elment_get2(69)


def command71():
 label1['text'] = elment_get1(70)
 label2['text'] = elment_get2(70)

def command72():
  label1['text'] = elment_get1(71)
  label2['text'] = elment_get2(71)


def command73():
 label1['text'] = elment_get1(72)
 label2['text'] = elment_get2(72)


def command74():
 label1['text'] = elment_get1(73)
 label2['text'] = elment_get2(73)


def command75():
  label1['text'] = elment_get1(74)
  label2['text'] = elment_get2(74)


def command76():
 label1['text'] = elment_get1(75)
 label2['text'] = elment_get2(75)


def command77():
 label1['text'] = elment_get1(76)
 label2['text'] = elment_get2(76)


def command78():
 label1['text'] = elment_get1(77)
 label2['text'] = elment_get2(77)


def command79():
 label1['text'] = elment_get1(78)
 label2['text'] = elment_get2(78)


def command80():
 label1['text'] = elment_get1(79)
 label2['text'] = elment_get2(79)


def command81():
 label1['text'] = elment_get1(80)
 label2['text'] = elment_get2(80)


def command82():
 label1['text'] = elment_get1(81)
 label2['text'] = elment_get2(81)


def command83():
 label1['text'] = elment_get1(82)
 label2['text'] = elment_get2(82)


def command84():
 label1['text'] = elment_get1(83)
 label2['text'] = elment_get2(83)


def command85():
 label1['text'] = elment_get1(84)
 label2['text'] = elment_get2(84)


def command86():
 label1['text'] = elment_get1(85)
 label2['text'] = elment_get2(85)


def command87():
 label1['text'] = elment_get1(86)
 label2['text'] = elment_get2(86)


def command88():
 label1['text'] = elment_get1(87)
 label2['text'] = elment_get2(87)

def command89():
 label1['text'] = elment_get1(88)
 label2['text'] = elment_get2(88)


def command89_103():
 label1['text'] = ''
 label2['text'] = ''


def command90():
 label1['text'] = elment_get1(89)
 label2['text'] = elment_get2(89)


def command91():
 label1['text'] = elment_get1(90)
 label2['text'] = elment_get2(90)


def command92():
 label1['text'] = elment_get1(91)
 label2['text'] = elment_get2(91)


def command93():
 label1['text'] = elment_get1(92)
 label2['text'] = elment_get2(92)


def command94():
 label1['text'] = elment_get1(93)
 label2['text'] = elment_get2(93)


def command95():
 label1['text'] = elment_get1(94)
 label2['text'] = elment_get2(94)


def command96():
 label1['text'] = elment_get1(95)
 label2['text'] = elment_get2(95)


def command97():
 label1['text'] = elment_get1(96)
 label2['text'] = elment_get2(96)


def command98():
 label1['text'] = elment_get1(97)
 label2['text'] = elment_get2(97)


def command99():
 label1['text'] = elment_get1(98)
 label2['text'] = elment_get2(98)


def command100():
 label1['text'] = elment_get1(99)
 label2['text'] = elment_get2(99)


def command101():
 label1['text'] = elment_get1(100)
 label2['text'] = elment_get2(100)


def command102():
 label1['text'] = elment_get1(101)
 label2['text'] = elment_get2(101)


def command103():
 label1['text'] = elment_get1(102)
 label2['text'] = elment_get2(102)


def command104():
 label1['text'] = elment_get1(103)
 label2['text'] = elment_get2(103)


def command105():
 label1['text'] = elment_get1(104)
 label2['text'] = elment_get2(104)


def command106():
 label1['text'] = elment_get1(105)
 label2['text'] = elment_get2(105)


def command107():
 label1['text'] = elment_get1(106)
 label2['text'] = elment_get2(106)


def command108():
 label1['text'] = elment_get1(107)
 label2['text'] = elment_get2(107)


def command109():
 label1['text'] = elment_get1(108)
 label2['text'] = elment_get2(108)


def command110():
 label1['text'] = elment_get1(109)
 label2['text'] = elment_get2(109)


def command111():
 label1['text'] = elment_get1(110)
 label2['text'] = elment_get2(110)

def command112():
  label1['text'] = elment_get1(111)
  label2['text'] = elment_get2(111)

def command113():
  label1['text'] = elment_get1(112)
  label2['text'] = elment_get2(112)

def command114():
  label1['text'] = elment_get1(113)
  label2['text'] = elment_get2(113)

def command115():
  label1['text'] = elment_get1(114)
  label2['text'] = elment_get2(114)

def command116():
  label1['text'] = elment_get1(115)
  label2['text'] = elment_get2(115)

def command117():
  label1['text'] = elment_get1(116)
  label2['text'] = elment_get2(116)

def command118():
  label1['text'] = elment_get1(117)
  label2['text'] = elment_get2(117)


frame= LabelFrame(window,borderwidth='7', relief=RAISED )
frame.place(relx = 0.042, rely = 0.052, relheight = 0.870, relwidth = 0.922)

label1 = Label(frame, font= ('Arial', 16, 'bold'), wraplength= 340,
                      relief=RAISED ,anchor='nw',padx=4, pady=5,
                       justify=LEFT, bd = 5, bg="lightblue" )
label1.place(relx=0.164, rely=0.05, height=190, width=380)
label2 = Label(frame,font= ('Arial', 16, 'bold'), wraplength= 340,
                      relief=RAISED ,anchor='nw',padx=4, pady=5,
                       justify=LEFT, bd = 5, bg="lightblue")
label2.place(relx=0.381, rely=0.05, height=190, width=380)
def elment_get1(x1):
         return (f'Name: {elment_info[x1].get("name")}\n'                               
         f'Atomic number: {elment_info[x1].get("atomic_number")}\n'                                
         f'Melting point(k): {elment_info[x1].get("melting_point_k")} k\n'
         f'Density: {elment_info[x1].get("density")} kg/m³\n'
         f'Discovery: {elment_info[x1].get("discovery")}')


def elment_get2(x2):
 return (f'Symbol: {elment_info[x2].get("symbol")}\n'
              f'Group: {elment_info[x2].get("group")}\n'
              f'Boiling Point (k): {elment_info[x2].get("boiling_point_k")} k\n'
              f'Has a stable isotope: {elment_info[x2].get("has_stable_isotope")}\n'
         f'Electron per shell: {elment_info[x2].get("electrons_per_shell")}')

button1 = Button(frame,
                 text=f"1\n  {elment_info[0]['symbol']}",
                 height=1,
                 anchor=W,
                 relief=RAISED, command = command1,
                 bd=5, bg='#FFFFFF', font=('Arial', 18, 'bold'))
button1.place(relx=0.018, rely=0.1, height=63, width=90)
button2 = Button(frame,
                 text=f"2\n {elment_info[1]['symbol']}",
                 height=1,
                 anchor=W,
                 relief=RAISED,command=command2,
                 bd=5, bg='#D9FFFF', font=('Arial', 18, 'bold'))
button2.place(relx=0.902, rely=0.1, height=63, width=90)
button3 = Button(frame,
                      text=f"3\n {elment_info[2]['symbol']}",
                      height=1,
                      anchor=W,
                     relief=RAISED,command=command3,
                 bd=5, bg='#CC80FF', font=('Arial', 18, 'bold'))
button3.place(relx=0.018, rely=0.17 , height=63, width=90)
button4 = Button(frame,
                  text=f"4\n {elment_info[3]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command=command4,
                  bd=5, bg='#C2FF00', font=('Arial', 18, 'bold'))
button4.place(relx=0.07, rely=0.17 , height=63, width=90)
button5 = Button(frame,
                  text=f"5\n {elment_info[4]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED,command= command5,
                  bd=5, bg='#FFB5B5', font=('Arial', 18, 'bold'))
button5.place(relx=0.642, rely=0.17 , height=63, width=90)
button6 = Button(frame,
                  text=f"6\n {elment_info[5]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED,command=command6,
                  bd=5, bg='#909090', font=('Arial', 18, 'bold'))
button6.place(relx=0.694, rely=0.17 , height=63, width=90)
button7 = Button(frame,
                  text=f"7\n {elment_info[6]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED,command=command7,
                  bd=5, bg='#3050F8', font=('Arial', 18, 'bold'))
button7.place(relx=0.746, rely=0.17 , height=63, width=90)
button8 = Button(frame,
                  text=f"8\n {elment_info[7]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED,command = command8,
                  bd=5, bg='#FF0D0D', font=('Arial', 18, 'bold'))
button8.place(relx=0.798, rely=0.17 , height=63, width=90)
button9 = Button(frame,
                  text=f"9\n {elment_info[8]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command = command9,
                  bd=5, bg='#90E050', font=('Arial', 18, 'bold'))
button9.place(relx=0.85, rely=0.17 , height=63, width=90)
button10 = Button(frame,
                   text=f"10\n {elment_info[9]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED,command=command10,
                  bd=5, bg='#90E050', font=('Arial', 18, 'bold'))
button10.place(relx=0.902, rely=0.17 , height=63, width=90)
button11 = Button(frame,
                   text=f"11\n {elment_info[10]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED, command= command11,
                  bd=5, bg='#B3E3F5', font=('Arial', 18, 'bold'))
button11.place(relx=0.018, rely=0.24,  height=63, width=90)
button12 = Button(frame,
                   text=f"12\n {elment_info[11]['symbol']}",
                   height=2, pady=4,
                   anchor=W,
                  relief=RAISED, command = command12,
                  bd=5, bg='#8AFF00', font=('Arial', 18, 'bold'))
button12.place(relx=0.070, rely=0.24, height=63, width=90)
button13 = Button(frame,
                  text=f"13\n {elment_info[12]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command= command13,
                  bd=5, bg='#BFA6A6', font=('Arial', 18, 'bold'))
button13.place(relx=0.642, rely=0.24, height=63, width=90)
button14 = Button(frame,
                  text=f"14\n {elment_info[13]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command= command14,
                  bd=5, bg='#F0C8A0', font=('Arial', 18, 'bold'))
button14.place(relx=0.694, rely=0.24, height=63, width=90)
button15 = Button(frame,
                  text=f"15\n {elment_info[14]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command = command15,
                  bd=5, bg='#FF8000', font=('Arial', 18, 'bold'))
button15.place(relx=0.746, rely=0.24, height=63, width=90)
button16 = Button(frame,
                  text=f"16\n {elment_info[15]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command = command16,
                  bd=5, bg='#FFFF30', font=('Arial', 18, 'bold'))
button16.place(relx=0.798, rely=0.24, height=63, width=90)
button17 = Button(frame,
                  text=f"17\n {elment_info[16]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command= command17,
                  bd=5, bg='#1FF01F', font=('Arial', 18, 'bold'))
button17.place(relx=0.85, rely=0.24, height=63, width=90)
button18 = Button(frame,
                  text=f"18\n {elment_info[17]['symbol']}",
                  height=1,
                  anchor=W,
                  relief=RAISED, command= command18,
                  bd=5, bg='#80D1E3', font=('Arial', 18, 'bold'))
button18.place(relx=0.902, rely=0.24, height=63, width=90)
button19 = Button(frame,
                   text=f"19\n {elment_info[18]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED, command= command19,
                  bd=5, bg='#8F40D4', font=('Arial', 18, 'bold'))
button19.place(relx=0.018, rely=0.31 , height=63, width=90)
button20 = Button(frame,
                   text=f"20\n {elment_info[19]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED, command = command20,
                  bd=5, bg='#3DFF00', font=('Arial', 18, 'bold'))
button20.place(relx=0.07, rely=0.31, height=63, width=90)
button21 = Button(frame,
                   text=f"21\n {elment_info[20]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command21,
                   bd=5, bg='#E6E6E6', font=('Arial', 18, 'bold'))
button21.place(relx=0.122, rely=0.31, height=63, width=90)
button22 = Button(frame,
                   text=f"22\n {elment_info[21]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command22,
                   bd=5, bg='#BFC2C7', font=('Arial', 18, 'bold'))
button22.place(relx=0.174, rely=0.31, height=63, width=90)
button23 = Button(frame,
                   text=f"23\n {elment_info[22]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command23,
                   bd=5, bg='#A6A6AB', font=('Arial', 18, 'bold'))
button23.place(relx=0.226, rely=0.31, height=63, width=90)
button24 = Button(frame,
                   text=f"24\n {elment_info[23]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command24,
                   bd=5, bg='#8A99C7', font=('Arial', 18, 'bold'))
button24.place(relx=0.278, rely=0.31, height=63, width=90)
button25 = Button(frame,
                   text=f"25\n {elment_info[24]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command25,
                   bd=5, bg='#9C7AC7', font=('Arial', 18, 'bold'))
button25.place(relx=0.33, rely=0.31, height=63, width=90)
button26 = Button(frame,
                   text=f"26\n {elment_info[25]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command26,
                   bd=5, bg='#E06633', font=('Arial', 18, 'bold'))
button26.place(relx=0.382, rely=0.31, height=63, width=90)
button27 = Button(frame,
                   text=f"27\n {elment_info[26]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command27,
                   bd=5, bg='#F090A0', font=('Arial', 18, 'bold'))
button27.place(relx=0.434, rely=0.31, height=63, width=90)
button28 = Button(frame,
                   text=f"28\n {elment_info[27]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command28,
                   bd=5, bg='#50D050', font=('Arial', 18, 'bold'))
button28.place(relx=0.486, rely=0.31, height=63, width=90)
button29 = Button(frame,
                   text=f"29\n {elment_info[28]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command29,
                   bd=5, bg='#C88033', font=('Arial', 18, 'bold'))
button29.place(relx=0.538, rely=0.31, height=63, width=90)
button30 = Button(frame,
                   text=f"30\n {elment_info[29]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command30,
                   bd=5, bg='#7D80B0', font=('Arial', 18, 'bold'))
button30.place(relx=0.59, rely=0.31, height=63, width=90)
button31 = Button(frame,
                   text=f"31\n {elment_info[30]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command31,
                   bd=5, bg='#C28F8F', font=('Arial', 18, 'bold'))
button31.place(relx=0.642, rely=0.31, height=63, width=90)

def command32():
 label1['text'] = elment_get1(31)
 label2['text'] = elment_get2(31)

button32 = Button(frame,
                   text=f"32\n {elment_info[31]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command32,
                   bd=5, bg='#668F8F', font=('Arial', 18, 'bold'))
button32.place(relx=0.694, rely=0.31, height=63, width=90)
button33 = Button(frame,
                   text=f"33\n {elment_info[32]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command33,
                   bd=5, bg='#BD80E3', font=('Arial', 18, 'bold'))
button33.place(relx=0.746, rely=0.31, height=63, width=90)
button34 = Button(frame,
                   text=f"34\n {elment_info[33]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command34,
                   bd=5, bg='#FFA100', font=('Arial', 18, 'bold'))
button34.place(relx=0.798, rely=0.31, height=63, width=90)
button35 = Button(frame,
                   text=f"35\n {elment_info[34]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command35,
                   bd=5, bg='#A62929', font=('Arial', 18, 'bold'))
button35.place(relx=0.85, rely=0.31, height=63, width=90)
button36 = Button(frame,
                   text=f"36\n {elment_info[35]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command=command36,
                   bd=5, bg='#5CB8D1', font=('Arial', 18, 'bold'))
button36.place(relx=0.902, rely=0.31 , height=63, width=90)
button37 = Button(frame,
                   text=f"37\n {elment_info[36]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED, command= command37,
                  bd=5, bg='#702EB0', font=('Arial', 18, 'bold'))
button37.place(relx=0.018, rely=0.38, height=63, width=90)
button38 = Button(frame,
                   text=f"38\n {elment_info[37]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED,command=command38,
                  bd=5, bg='#00FF00', font=('Arial', 18, 'bold'))
button38.place(relx=0.07, rely=0.38, height=63, width=90)
button39 = Button(frame,
                   text=f"39\n {elment_info[38]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command39,
                   bd=5, bg='#94FFFF', font=('Arial', 18, 'bold'))
button39.place(relx=0.122, rely=0.38, height=63, width=90)
button40 = Button(frame,
                   text=f"40\n {elment_info[39]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command40,
                   bd=5, bg='#94E0E0', font=('Arial', 18, 'bold'))
button40.place(relx=0.174, rely=0.38, height=63, width=90)
button41 = Button(frame,
                   text=f"41\n {elment_info[40]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command41,
                   bd=5, bg='#73C2C9', font=('Arial', 18, 'bold'))
button41.place(relx=0.226, rely=0.38, height=63, width=90)
button42 = Button(frame,
                   text=f"42\n {elment_info[41]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command42,
                   bd=5, bg='#54B5B5', font=('Arial', 18, 'bold'))
button42.place(relx=0.278, rely=0.38, height=63, width=90)
button43 = Button(frame,
                   text=f"43\n {elment_info[42]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command43,
                   bd=5, bg='#3B9E9E', font=('Arial', 18, 'bold'))
button43.place(relx=0.33, rely=0.38, height=63, width=90)
button44 = Button(frame,
                   text=f"44\n {elment_info[43]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command44,
                   bd=5, bg='#248F8F', font=('Arial', 18, 'bold'))
button44.place(relx=0.382, rely=0.38, height=63, width=90)
button45 = Button(frame,
                   text=f"45\n {elment_info[44]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command45,
                   bd=5, bg='#0A7D8C', font=('Arial', 18, 'bold'))
button45.place(relx=0.434, rely=0.38, height=63, width=90)
button46 = Button(frame,
                   text=f"46\n {elment_info[45]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command46,
                   bd=5, bg='#006985', font=('Arial', 18, 'bold'))
button46.place(relx=0.486, rely=0.38, height=63, width=90)
button47 = Button(frame,
                   text=f"47\n {elment_info[46]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command47,
                   bd=5, bg='#C0C0C0', font=('Arial', 18, 'bold'))
button47.place(relx=0.538, rely=0.38, height=63, width=90)
button48 = Button(frame,
                   text=f"48\n {elment_info[47]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command48,
                   bd=5, bg='#FFD98F', font=('Arial', 18, 'bold'))
button48.place(relx=0.59, rely=0.38, height=63, width=90)
button49 = Button(frame,
                   text=f"49\n {elment_info[48]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command = command49,
                   bd=5, bg='#A67573', font=('Arial', 18, 'bold'))
button49.place(relx=0.642, rely=0.38, height=63, width=90)
button50 = Button(frame,
                   text=f"50\n {elment_info[49]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command50,
                   bd=5, bg='#668080', font=('Arial', 18, 'bold'))
button50.place(relx=0.694, rely=0.38, height=63, width=90)
button51 = Button(frame,
                   text=f"51\n {elment_info[50]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command51,
                   bd=5, bg='#9E63B5', font=('Arial', 18, 'bold'))
button51.place(relx=0.746, rely=0.38, height=63, width=90)
button52 = Button(frame,
                   text=f"52\n {elment_info[51]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command52,
                   bd=5, bg='#D47A00', font=('Arial', 18, 'bold'))
button52.place(relx=0.798, rely=0.38, height=63, width=90)
button53 = Button(frame,
                   text=f"53\n {elment_info[52]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command53,
                   bd=5, bg='#940094', font=('Arial', 18, 'bold'))
button53.place(relx=0.85, rely=0.38, height=63, width=90)

button54 = Button(frame,
                   text=f"54\n {elment_info[53]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command54,
                   bd=5, bg='#429EB0', font=('Arial', 18, 'bold'))
button54.place(relx=0.902,rely=0.38, height=63, width=90)
button55 = Button(frame,
                   text=f"55\n {elment_info[54]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED,command= command55,
                  bd=5, bg='#57178F', font=('Arial', 18, 'bold'))
button55.place(relx=0.018, rely=0.449, height=63, width=90)
button56 = Button(frame,
                   text=f"56\n {elment_info[55]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED,command= command56,
                  bd=5, bg='#00C900', font=('Arial', 18, 'bold'))
button56.place(relx=0.07, rely=0.449, height=63, width=90)
button57 = Button(frame,
                   text=f"57-71",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command57_71,
                   bd=5, font=('Arial', 18, 'bold'))
button57.place(relx=0.122, rely=0.449, height=63, width=90)
button72 = Button(frame,
                   text=f"72\n {elment_info[71]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command72,
                   bd=5, bg='#4DC2FF', font=('Arial', 18, 'bold'))
button72.place(relx=0.174, rely=0.449, height=63, width=90)
button73 = Button(frame,
                   text=f"73\n {elment_info[72]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command73,
                   bd=5, bg='#4DA6FF', font=('Arial', 18, 'bold'))
button73.place(relx=0.226, rely=0.449, height=63, width=90)
button74 = Button(frame,
                   text=f"74\n {elment_info[73]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command74,
                   bd=5, bg='#2194D6', font=('Arial', 18, 'bold'))
button74.place(relx=0.278, rely=0.449, height=63, width=90)
button75 = Button(frame,
                   text=f"75\n {elment_info[74]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command75,
                   bd=5, bg='#267DAB', font=('Arial', 18, 'bold'))
button75.place(relx=0.33, rely=0.449, height=63, width=90)
button76 = Button(frame,
                   text=f"76\n {elment_info[75]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command76,
                   bd=5, bg='#266696', font=('Arial', 18, 'bold'))
button76.place(relx=0.382, rely=0.449, height=63, width=90)
button77 = Button(frame,
                   text=f"77\n {elment_info[76]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command77,
                   bd=5, bg='#175487', font=('Arial', 18, 'bold'))
button77.place(relx=0.434, rely=0.449, height=63, width=90)
button78 = Button(frame,
                   text=f"78\n {elment_info[77]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command78,
                   bd=5, bg='#D0D0E0', font=('Arial', 18, 'bold'))
button78.place(relx=0.486, rely=0.449, height=63, width=90)
button79 = Button(frame,
                   text=f"79\n {elment_info[78]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command79,
                   bd=5, bg='#FFD123', font=('Arial', 18, 'bold'))
button79.place(relx=0.538, rely=0.449, height=63, width=90)
button80 = Button(frame,
                   text=f"80\n {elment_info[79]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command80,
                   bd=5, bg='#B8B8D0', font=('Arial', 18, 'bold'))
button80.place(relx=0.59, rely=0.449, height=63, width=90)
button81 = Button(frame,
                   text=f"81\n {elment_info[80]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command81,
                   bd=5, bg='#A6544D', font=('Arial', 18, 'bold'))
button81.place(relx=0.642, rely=0.449, height=63, width=90)
button82 = Button(frame,
                   text=f"82\n {elment_info[81]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command82,
                   bd=5, bg='#575961', font=('Arial', 18, 'bold'))
button82.place(relx=0.694, rely=0.449, height=63, width=90)
button83 = Button(frame,
                   text=f"83\n {elment_info[82]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command83,
                   bd=5, bg='#9E4FB5', font=('Arial', 18, 'bold'))
button83.place(relx=0.746, rely=0.449, height=63, width=90)
button84 = Button(frame,
                   text=f"84\n {elment_info[83]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command84,
                   bd=5, bg='#AB5C00', font=('Arial', 18, 'bold'))
button84.place(relx=0.798, rely=0.449, height=63, width=90)
button85 = Button(frame,
                   text=f"85\n {elment_info[84]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command85,
                   bd=5, bg='#754F45', font=('Arial', 18, 'bold'))
button85.place(relx=0.85, rely=0.449, height=63, width=90)

button86 = Button(frame,
                   text=f"86\n {elment_info[86]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command86,
                   bd=5, bg='#428296', font=('Arial', 18, 'bold'))
button86.place(relx=0.902, rely=0.449, height=63, width=90)
button87 = Button(frame,
                   text=f"87\n {elment_info[86]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED,command= command87,
                  bd=5, bg='#420066', font=('Arial', 18, 'bold'))
button87.place(relx=0.018, rely=0.518 ,height=63, width=90)
button88 = Button(frame,
                   text=f"88\n {elment_info[87]['symbol']}",
                   height=1,
                   anchor=W,
                  relief=RAISED,command= command88,
                  bd=5, bg='#007D00', font=('Arial', 18, 'bold'))
button88.place(relx=0.07, rely=0.518 ,height=63, width=90)
button89 = Button(frame,
                   text=f"89-103",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command89_103,
                   bd=5, font=('Arial', 18, 'bold'))
button89.place(relx=0.122, rely=0.518 ,height=63, width=90)
button104 = Button(frame,
                   text=f"104\n {elment_info[103]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command104,
                   bd=5, bg='#CC0059', font=('Arial', 18, 'bold'))
button104.place(relx=0.174, rely=0.518 ,height=63, width=90)
button105 = Button(frame,
                   text=f"105\n {elment_info[104]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command105,
                   bd=5, bg='#D1004F', font=('Arial', 18, 'bold'))
button105.place(relx=0.226, rely=0.518 ,height=63, width=90)
button106 = Button(frame,
                   text=f"106\n {elment_info[105]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command106,
                   bd=5, bg='#D90045', font=('Arial', 18, 'bold'))
button106.place(relx=0.278, rely=0.518 ,height=63, width=90)
button107 = Button(frame,
                   text=f"107\n {elment_info[106]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command107,
                   bd=5, bg='#E00038', font=('Arial', 18, 'bold'))
button107.place(relx=0.33, rely=0.518 ,height=63, width=90)
button108 = Button(frame,
                    text=f"108\n {elment_info[107]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command108,
                   bd=5, bg='#E6002E', font=('Arial', 18, 'bold'))
button108.place(relx=0.382, rely=0.518 ,height=63, width=90)
button109 = Button(frame,
                   text=f"109\n {elment_info[108]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command109,
                   bd=5, bg='#EB0026', font=('Arial', 18, 'bold'))
button109.place(relx=0.434, rely=0.518 ,height=63, width=90)
button110 = Button(frame,
                   text=f"110\n {elment_info[109]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command110,
                   bd=5,  font=('Arial', 18, 'bold'))
button110.place(relx=0.486, rely=0.518 ,height=63, width=90)
button111 = Button(frame,
                   text=f"111\n {elment_info[110]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command111,
                   bd=5,  font=('Arial', 18, 'bold'))
button111.place(relx=0.538, rely=0.518 ,height=63, width=90)
button112 = Button(frame,
                   text=f"112\n {elment_info[111]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command112,
                   bd=5,  font=('Arial', 18, 'bold'))
button112.place(relx=0.59, rely=0.518 ,height=63, width=90)
button113= Button(frame,
                   text=f"113\n {elment_info[112]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command113,
                   bd=5,font=('Arial', 18, 'bold'))
button113.place(relx=0.642, rely=0.518 ,height=63, width=90)
button114 = Button(frame,
                   text=f"114\n {elment_info[113]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command114,
                   bd=5,font=('Arial', 18, 'bold'))
button114.place(relx=0.694, rely=0.518 ,height=63, width=90)
button115 = Button(frame,
                   text=f"115\n {elment_info[114]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command115,
                   bd=5, font=('Arial', 18, 'bold'))
button115.place(relx=0.746, rely=0.518 ,height=63, width=90)
button116 = Button(frame,
                   text=f"116\n {elment_info[115]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command116,
                   bd=5, font=('Arial', 18, 'bold'))
button116.place(relx=0.798, rely=0.518 ,height=63, width=90)
button117 = Button(frame,
                   text=f"117\n {elment_info[116]['symbol']}",
                   height=1,
                   anchor=W,command= command117,
                   relief=RAISED,
                   bd=5,font=('Arial', 18, 'bold'))
button117.place(relx=0.85, rely=0.518 ,height=63, width=90)

button118 = Button(frame,
                   text=f"118\n {elment_info[117]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command118,
                   bd=5, font=('Arial', 18, 'bold'))
button118.place(relx=0.902, rely=0.518 ,height=63, width=90)
button57 = Button(frame,
                   text=f"57\n {elment_info[56]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command57,
                   bd=5, bg='#70D4FF', font=('Arial', 18, 'bold'))
button57.place(relx=0.122, rely=0.7, height=63, width=90)
button58 = Button(frame,
                   text=f"58\n {elment_info[57]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command58,
                   bd=5, bg='#FFFFC7', font=('Arial', 18, 'bold'))
button58.place(relx=0.174, rely=0.7, height=63, width=90)
button59 = Button(frame,
                   text=f"59\n {elment_info[58]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command59,
                   bd=5, bg='#D9FFC7', font=('Arial', 18, 'bold'))
button59.place(relx=0.226, rely=0.7, height=63, width=90)
button60 = Button(frame,
                   text=f"60\n {elment_info[59]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command60,
                   bd=5, bg='#C7FFC7', font=('Arial', 18, 'bold'))
button60.place(relx=0.278, rely=0.7, height=63, width=90)
button61 = Button(frame,
                   text=f"61\n {elment_info[60]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command61,
                   bd=5, bg='#A3FFC7', font=('Arial', 18, 'bold'))
button61.place(relx=0.33, rely=0.7, height=63, width=90)
button62 = Button(frame,
                    text=f"62\n {elment_info[61]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command62,
                   bd=5, bg='#8FFFC7', font=('Arial', 18, 'bold'))
button62.place(relx=0.382, rely=0.7, height=63, width=90)
button63 = Button(frame,
                   text=f"63\n {elment_info[62]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command63,
                   bd=5, bg='#61FFC7', font=('Arial', 18, 'bold'))
button63.place(relx=0.434, rely=0.7, height=63, width=90)
button64 = Button(frame,
                   text=f"64\n {elment_info[63]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command64,
                   bd=5, bg='#45FFC7', font=('Arial', 18, 'bold'))
button64.place(relx=0.486, rely=0.7, height=63, width=90)
button65 = Button(frame,
                   text=f"65\n {elment_info[64]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command65,
                   bd=5, bg='#30FFC7', font=('Arial', 18, 'bold'))
button65.place(relx=0.538, rely=0.7, height=63, width=90)
button66 = Button(frame,
                   text=f"66\n {elment_info[65]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command66,
                   bd=5, bg='#1FFFC7', font=('Arial', 18, 'bold'))
button66.place(relx=0.59, rely=0.7, height=63, width=90)
button67= Button(frame,
                   text=f"67\n {elment_info[66]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command67,
                   bd=5,bg='#00FF9C', font=('Arial', 18, 'bold'))
button67.place(relx=0.642, rely=0.7, height=63, width=90)
button68 = Button(frame,
                   text=f"68\n {elment_info[67]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command68,
                   bd=5, bg='#00E675',font=('Arial', 18, 'bold'))
button68.place(relx=0.694, rely=0.7, height=63, width=90)
button69 = Button(frame,
                   text=f"69\n {elment_info[68]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command69,
                   bd=5, bg='#00D452', font=('Arial', 18, 'bold'))
button69.place(relx=0.746, rely=0.7, height=63, width=90)
button70 = Button(frame,
                   text=f"70\n {elment_info[69]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command70,
                   bd=5,  bg='#00BF38', font=('Arial', 18, 'bold'))
button70.place(relx=0.798, rely=0.7, height=63, width=90)
button71 = Button(frame,
                   text=f"71\n {elment_info[70]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command71,
                   bd=5, bg='#00AB24',font=('Arial', 18, 'bold'))
button71.place(relx=0.85, rely=0.7, height=63, width=90)
button89 = Button(frame,
                   text=f"89\n {elment_info[88]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command89,
                   bd=5, bg='#70ABFA', font=('Arial', 18, 'bold'))
button89.place(relx=0.122, rely=0.77, height=63, width=90)
button90 = Button(frame,
                   text=f"90\n {elment_info[89]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command90,
                   bd=5, bg='#00BAFF', font=('Arial', 18, 'bold'))
button90.place(relx=0.174, rely=0.77, height=63, width=90)
button91 = Button(frame,
                   text=f"91\n {elment_info[90]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED,command= command91,
                   bd=5, bg='#00A1FF', font=('Arial', 18, 'bold'))
button91.place(relx=0.226, rely=0.77, height=63, width=90)
button92 = Button(frame,
                   text=f"92\n {elment_info[91]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command92,
                   bd=5, bg='#008FFF', font=('Arial', 18, 'bold'))
button92.place(relx=0.278, rely=0.77, height=63, width=90)
button93 = Button(frame,
                   text=f"93\n {elment_info[92]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command93,
                   bd=5, bg='#0080FF', font=('Arial', 18, 'bold'))
button93.place(relx=0.33, rely=0.77, height=63, width=90)
button94 = Button(frame,
                    text=f"94\n {elment_info[93]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command94,
                   bd=5, bg='#006BFF', font=('Arial', 18, 'bold'))
button94.place(relx=0.382, rely=0.77, height=63, width=90)
button95 = Button(frame,
                   text=f"95\n {elment_info[94]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command95,
                   bd=5, bg='#545CF2', font=('Arial', 18, 'bold'))
button95.place(relx=0.434, rely=0.77, height=63, width=90)
button96 = Button(frame,
                   text=f"96\n {elment_info[95]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command96,
                   bd=5, bg='#785CE3', font=('Arial', 18, 'bold'))
button96.place(relx=0.486, rely=0.77, height=63, width=90)
button97 = Button(frame,
                   text=f"97\n {elment_info[96]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command97,
                   bd=5, bg='#8A4FE3', font=('Arial', 18, 'bold'))
button97.place(relx=0.538, rely=0.77, height=63, width=90)
button98 = Button(frame,
                   text=f"98\n {elment_info[97]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command98,
                   bd=5, bg='#A136D4', font=('Arial', 18, 'bold'))
button98.place(relx=0.59, rely=0.77, height=63, width=90)
button99= Button(frame,
                   text=f"99\n {elment_info[98]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command99,
                   bd=5,bg='#B31FD4', font=('Arial', 18, 'bold'))
button99.place(relx=0.642, rely=0.77, height=63, width=90)
button100 = Button(frame,
                   text=f"100\n {elment_info[99]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command100,
                   bd=5, bg='#B31FBA',font=('Arial', 18, 'bold'))
button100.place(relx=0.694, rely=0.77, height=63, width=90)
button101 = Button(frame,
                   text=f"101\n {elment_info[100]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command101,
                   bd=5, bg='#B30DA6', font=('Arial', 18, 'bold'))
button101.place(relx=0.746, rely=0.77, height=63, width=90)
button102 = Button(frame,
                   text=f"102\n {elment_info[101]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command102,
                   bd=5,  bg='#BD0D87', font=('Arial', 18, 'bold'))
button102.place(relx=0.798, rely=0.77, height=63, width=90)
button103 = Button(frame,
                   text=f"103\n {elment_info[102]['symbol']}",
                   height=1,
                   anchor=W,
                   relief=RAISED, command= command103,
                   bd=5, bg='#C70066',font=('Arial', 18, 'bold'))
button103.place(relx=0.85, rely=0.77, height=63, width=90)



window.mainloop()
