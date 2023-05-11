from TheListBackEnd import *












code_face = Block("Code Face",
"Work on web design class",
"Whether we freelance, make art or sell code we're going to need a website. The face of our Digital Oikos.",
3000,
5)




independance = Path("Independance",
"Work to free ourself from dependance upon employment",
                    (code_face,),
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
                           , 3, (independance,), 10)
#The Industrialist holds on to Processes and Schedules




