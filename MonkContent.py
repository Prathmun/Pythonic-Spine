from TheListBackEnd import *








#NAME = Block("NAME","PROCESS","OUTCOME","COOLDOWN","CHARGECAP"))

#NAME = Path(NAME, PROCESS, "BLOCKS, "ORDER"))

#earth blocks

shaping_the_cup = Block("Shaping The Cup", 
"""Flow""",
"""Stand on the Earth, Stoke the flame, move the water, free the air""",

2000,
5)






### Paths ###

earth = Path("Earth",
"Yin, ground, darkness",
(shaping_the_cup,),
0)





monk = Discipline("Monk", 
"""
The Monk values Tranquility(Stability) and Clarity(purpose)
""", 1, (earth,), 10)
#The monk holds on to Paths and Forms
