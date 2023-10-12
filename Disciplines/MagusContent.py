from TheListBackEnd import *



gnaw = Block("Gnaw",
"""Chew on a non-ficiton book. Try to stick to one at a time, reading linearly. No obligation to finish a book if it stops being interesting""",
"Orients the sybmolic frame and deepens the library",
2000,
15)


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

journaling = Block("Journaling - Narrative Cultivation",
                   "Update the journal on the status of the disciplines.",
                   "Makes specific the current narratives.",
                   1800,  # 30 hours in minutes
                   5)

lymeric_writing = Block("Lymeric Writing - Prose shaping",
                        "Write a limerick AABBA.",
                        "Gets us more comfortable rhyming and being intentional with our words.",
                        3600,  # 60 hours in minutes
                        5)

personal_narrative = Path("Personal Narrative",
                          "Tools and Practices Shaping narrative being",
                          (journaling, lymeric_writing), 1)

magus.paths.append(personal_narrative)