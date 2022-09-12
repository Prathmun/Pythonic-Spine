from TheListBackEnd import *


slurm = Block ("Slurm",
"Heroes of the Slurm",
"It's dangerously addictive!",
(24*60),
10)

homecoming = Block ("Homecoming",
"Hang out in one of the old MMOs, preferably with pals",
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

funny_little_games =Block ("Funny Little Games",
"Play a game with JD",
"JD is a good ally and a prosocial agent. Fun to game with",
((7/3)*24*60),10)

explorer_pals =Block("Explorer Pals",
"Play a game with Alpal",
"Together we are strong. Together we are leaders",
((7/3)*24*60),10)

skinny_box = Block("Skinny Box", 
"play a game with Andrew",
"he fun pal, he game good",
((7/3)*24*60),10)


coop= Path("Cooporitve",
"Multiplayer is about friendship, and friendship is magic",
(explorer_pals, funny_little_games,  skinny_box),2)
gamer = Discipline("gamer",
"""
play in systems

""", 
1,
(comfort_systems,coop,), 
60)
