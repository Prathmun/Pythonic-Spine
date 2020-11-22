from TheListBackEnd import *


storyform = Block("Story Form",
"Pull three tarot cards, and use them as a prompt for a short story. Three sentance min, no cap.",
"Primes and practices the basic object of communication. Makes artifacts that could be reused by other processes",
10080,
1)  

grindstone = Block("Grindstone",
"Write a limerick AABBA",
"Creates and maintains the groove in which an awareness of the structure of our language may sit. This will prove to be a boon in social situations, in music and other expressive forms that take place over time",
2000,1)

objectorientedprose = Block("Object Oriented Prose",
"Write a haiku. Five syllables seven syllables, five syllables",
"Creates and maintains a relationship to the syllabic structure of language",
4000,1)


mycelium = Path("Mycelium",
"Fibrous and Rhyzomatic",
(storyform, grindstone, objectorientedprose,), 0)

cyberneticist = Discipline("Cyberneticist",
"""
Machines for Communication.

""", 
1,
(mycelium,), 
60)
