from TheListBackEnd import *



active_feedback = Block("Active Feedback",
"Read the workflowy report",
"See what intentions you ratified, noted and modified yesterday",
1000,
6)

mycelium = Path("Mycelium",
"Fibrous and Rhyzomatic",
(active_feedback,), 0)

cyberneticist = Discipline("Cyberneticist",
"""
Machines for Communication.

""", 
1,
(mycelium,), 
60)
