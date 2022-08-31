from TheListBackEnd import *


slurm = Block ("Slurm",
"Heroes of the Slurm",
"It's dangerously addictive!",
(24*60),
10)

homecoming = Block ("Homecoming",
"City of Heroes",
"It's dangerously addictive!",
(24*60),
10)

lets_play = Block ("Lets_Play",
"Record an episode of gameplay. Current series: Starcraf2 Campaigns",
"We like to watch ourselves, and crucially... listen!",
(24*60*7),
5)

comfort_systems = Path("Comfort_Systems",
"As pointless as desire",

(slurm, homecoming, lets_play), 0)

gamer = Discipline("gamer",
"""
play in systems

""", 
1,
(comfort_systems,), 
60)
