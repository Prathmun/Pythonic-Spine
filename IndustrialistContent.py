from TheListBackEnd import *












the_search = Block("The Search",
"improve job search tools, actively hunt, or reach out to folks",
"Look we put in the work to get the skills, lets get paid for them!",
5040,
5)




grid = Path("Grid",
"Organizes the world",
(the_search,),
1)



industrialist = Discipline("Industrialist", 
"""
The Industrialist

	Monitization
		Mediocristan
		Extremistan
	
	Extraction
		Labor
		Goods
		Information
"""
, 3, (grid,), 10)
#The Industrialist holds on to Processes and Schedules




