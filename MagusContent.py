from TheListBackEnd import *



gnaw = Block("Gnaw",
"""Chew on a non-ficiton book. Try to stick to one at a time, reading linearly. No obligation to finish a book if it stops being interesting""",
"Orients the sybmolic frame and deepens the library",
2000,
3)




canopy = Path("Canopy",
"The surface upon which both the sun and moon shine",
(gnaw,), 2)


magus = Discipline("Magus", 
"""
The Magus labors under "Operation Metanarrative." It does so through adherance to the following values

Confidence through coherance

Mastery through recurrance

Constructed with intention

Manufactured history

Simulated future

"""
, 2, (canopy,), 10.0)
#The Magus holds on to Evocations and Enchantments
