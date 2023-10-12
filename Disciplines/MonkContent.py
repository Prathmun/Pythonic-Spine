from TheListBackEnd import *








#NAME = Block("NAME","PROCESS","OUTCOME","COOLDOWN","CHARGECAP"))

#NAME = Path(NAME, PROCESS, "BLOCKS, "ORDER"))

#earth blocks

level_set = Block ("Level Set",
                   "Medidate for a while, with a timer usually. Keeping breath and attention steady",
                   "Neutral log stimuli, organizing around regulation, observer cultivation.",
                   30*60,
                   4)

#fire

defying_gravity =Block("Defying Gravity",
"Do a minute hold on a handstand, or five hops on each side.",
"Decant",
2160,
3)





### Path ###


earth = Path("Earth",
"Yin, ground, cultivation, routine",
(level_set,),
0)

fire = Path("Fire",
"Awareness, Passion, Power, Novelty",
(defying_gravity,),
0)

monk = Discipline("Monk", 
"""
The Monk values Tranquility(Stability) and Clarity(purpose)
""", 1, (fire,earth,), 10)
#The monk holds on to Paths and Forms
