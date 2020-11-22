from TheListBackEnd import *




operationalframe = Block("Operational Frame",
"Read the operation document for each Discipline from start to finish",
"Establishes the operational frame enabling organization to be undertaken",
5000,
1)

hud= Path("HUD", 
"Object in hand",
(operationalframe,), 2)







canopy = Path("Canopy",
"The surface upon which both the sun and moon shine",
(), 2)


magus = Discipline("Magus", 
"""
The Magus labors under "Operation Metanarrative." It does so through adherance to the following values

Confidence through coherance

Mastery through recurrance

Constructed with intention

Manufactured history

Simulated future

"""
, 2, (hud,), 10.0)
#The Magus holds on to Evocations and Enchantments
