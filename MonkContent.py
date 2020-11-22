from TheListBackEnd import *


suryanamascara = Block("Sun Salutation",
"Offer yourself some combination of both Suryanamascara A and B. Take the time to remember why you're doing this, and to give yourself a moment of gratitude for coming to this nourishing practice.",
"Opens us up to recieve the days light.",

1000,
1,)


report = Block("Report",
"Notice and get curious about bodily sensations",
"Conscious attention to bodily sensations facilitates the integration of signals rooted in the activation of lower brain regions, specifically the parasympathetic nervous system. This is grounding and orienting",

1000,
1,)


tabularasa = Path("Tabula Rasa", """ Tabula Rasa is a grounding path. We clear the ground so that we may build outward
""", (suryanamascara, report), 0)


monkidol = Block("Monk Idol", 
"Focus on the green door",
"Concentrates and highlights the Monks light in our selves and in the world",
1000,
1)


magusidol = Block("Magus Idol",
"Focus on the blue door",
"Opens us to the intellect of the monk",
1000,
1)

cyberneticistidol = Block("Cyberneticist Idol",
"Focus on the yellow door",
"Opens us up to the joy of the Cyberneticist",
1000,
1)

industrialistidol = Block("Industrialist Idol",
"Focus on the Red door",
"Opens us up to the scaling of the industrialist.",
1000,
1)


meditations = Path("NeoSimulation Idol", """Bask in the auro of the NeoSimulation Idols and become bound to their twisting paths""",
(monkidol,), 0)





monk = Discipline("Monk", 
"""
The Monk values Tranquility(Stability) and Clarity(purpose)
""", 1, (tabularasa, meditations), 10)
#The monk holds on to Paths and Forms
