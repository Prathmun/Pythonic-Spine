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

(mecha_mantra,thecode,), 0)


set_up_pythonic_spine = Block("Set up Pythonic Spine",
                              "Run the corresponding python script.",
                              "Provides framework for long term beingshaping.",
                              1440,  # 24 hours in minutes
                              3)

set_up_consumption_tracker = Block("Set up Consumption Tracker",
                                   "Run the corresponding python script.",
                                   "Provides framework for tracking short term state impacting consumption.",
                                   1440,  # 24 hours in minutes
                                   3)

set_up_sad_circle = Block("Set up Sad Circle",
                          "Run the corresponding python script.",
                          "Sets up an eye-catching idle toy on our codebox. Enticing interaction with other systems and the idle toy's own code.",
                          1440,  # 24 hours in minutes
                          3)

set_up_tools = Path("Set Up Tools",
                    "Coming Online!",
                    (set_up_pythonic_spine, set_up_consumption_tracker, set_up_sad_circle),
                    1)


cyberneticist = Discipline("Cyberneticist",
"""
Responsive Machines

""", 
1,
(mycelium,set_up_tools), 
60)
