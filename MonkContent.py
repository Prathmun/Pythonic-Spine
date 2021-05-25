from TheListBackEnd import *








#NAME = Block("NAME","PROCESS","OUTCOME","COOLDOWN","CHARGECAP"))

#NAME = Path(NAME, PROCESS, "BLOCKS, "ORDER"))

#earth blocks

shaping_the_cup = Block("Shaping The Cup", 
"""Flow""",
"""Stand on the Earth, Stoke the flame, move the water, free the air""",

5040,
3)

running = Block("Running",
"Run!",
'Flushes the system, builds endorphins and makes your heart happy',
2520,
4)

handstand_conditioning = Block('Handstand Conditioning',
"Work through the handstand conditioning Brianna put together for you",
"Inches towards that most visible of inversions",
1080,
2)


#Wind up
    #Sidebend squat cycle
    #Goddess Squat Thoracic Cat Cow
    #Sidebody extensions
#Sustain
    #neck, and extension
    #Twists
    #figure 4
#Wind down/after care
    #Quad Stretch
    #Palattis Lunge
    #Supportted Downward dog








### Paths ###

earth = Path("Earth",
"Yin, ground, darkness",
(shaping_the_cup, running, handstand_conditioning),
0)





monk = Discipline("Monk", 
"""
The Monk values Tranquility(Stability) and Clarity(purpose)
""", 1, (earth,), 10)
#The monk holds on to Paths and Forms
