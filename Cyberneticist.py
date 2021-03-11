from TheListBackEnd import *



active_feedback = Block("Active Feedback",
"Read the workflowy report",
"See what intentions you ratified, noted and modified yesterday",
1000,
6)
#If we could make this reset daily rather then on a charge that would be preferable.

mooc = Block("Mooc",
"datascience course, syllabus item",
"digital literacy yo.",
2000,
5)

mycelium = Path("Mycelium",
"Fibrous and Rhyzomatic",
(active_feedback, mooc), 0)

cyberneticist = Discipline("Cyberneticist",
"""
Machines for Communication.

""", 
1,
(mycelium,), 
60)
