from TheListBackEnd import *








#NAME = Block("NAME","PROCESS","OUTCOME","COOLDOWN","CHARGECAP"))

#NAME = Path(NAME, PROCESS, "BLOCKS, "ORDER"))

#earth blocks

empty_cup =Block("Empty Cup",
"Sit and watch your breath for 5 minutes or longer",
"Decant",
100,
3)

motion_lotion = Block("Motion Is Lotion",
"Get up and move for at least 15 minutes, set a timer",
"Humans are meant to move, not do what I want to do",
150,
2)





### Path ###

earth = Path("Earth",
"Yin, ground, darkness",
(empty_cup, motion_lotion),
0)


monk = Discipline("Monk", 
"""
The Monk values Tranquility(Stability) and Clarity(purpose)
""", 1, (earth,), 10)
#The monk holds on to Paths and Forms
