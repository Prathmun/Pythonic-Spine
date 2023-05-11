from TheListBackEnd import *



mecha_mantra = Block ("Mecha Mantra",
"activate the mecha mantra",
"empowers us to remember what we set out to attend to",
2440,
5)

thecode = Block ("The Code",
"Work through a mastey task on Khan academy.",
"Math is the foundation of most of what we do, let's learn it from the ground up.",
2880,
5)

mycelium = Path("Mycelium",
"Fibrous and Rhyzomatic",

(thecode,), 0)

cyberneticist = Discipline("Cyberneticist",
"""
Machines for Communication.

""", 
1,
(mycelium,), 
60)
