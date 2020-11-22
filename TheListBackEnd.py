#The armature is an adaptive methodology. It assures access to a 'past.' The value system that the methodology labors under is in theory unimportant to the methodology, none the less at the moment of writing the author is operating under an existentialist value system, as put forth by Simone De Beauvior in The Ethics of Ambiguity
import time
import pickle
import fileinput
from datetime import datetime, timedelta
import dateutil.parser
from clint.textui import colored

class Discipline:
    def __init__(self, name, flavor, priority, paths, cooldown,):
        self.name = colored.yellow(name)
        self.flavor = colored.green(flavor)
        self.priority = priority
        self.paths = list(paths)
        self.cooldown = timedelta(minutes=cooldown)
		#Represents a methodology
	
		
        
class Path:
	def __init__(self, name, subtitle, blocks, order,):
		self.name = colored.red(name)
		self.subtitle = subtitle
		self.blocks = list(blocks)
		self.order = order
		#Represents a desired tabula or individual value/value cluster under the umbrella of it's discipline


class Block:
    def __init__(self, name, process, output, cooldown, chargecap,):
        self.name = name
        self.title = colored.magenta(name)
        self.process = colored.cyan(process)
        self.output = colored.green(output)
        self.cooldown = timedelta(minutes=(cooldown))
        self.chargecap = chargecap
		#Represents a behavior, or a quest to further it's parent values, or move the world towards a state similar to that presented in the imagery of the Path
		



def picklejarfactory(grossdisciplines):

    for discipline in grossdisciplines:
        for path in discipline.paths:
            for block in path.blocks:
                try:
                    pickletext = pickle.load(open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name +  ".py"), "rb"))
                except (IndexError, IOError,):
                    spawner = open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name +  ".py"), "a")
                    spawner.close
                    #unsure if this is the correct way to initialize the datetime object.Just marking this line so that we can test it when the archecture is runnable.
                    thenow = datetime.now()
                    thethen = (thenow + timedelta(days=-1500))
                    picklejar = [thethen,]
                    pickle.dump(picklejar, open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name +  ".py"), "wb"))


    for discipline in grossdisciplines:
        for path in discipline.paths:
            for block in path.blocks:
                try:
                    pickletext = pickle.load(open(("C:/Users/Prathmun/Documents/Python Stuff/chargecounters/" + block.name +   "chargecounter.py"), "rb"))
                except (IOError, EOFError, IndexError,):
                    spawner = open(("C:/Users/Prathmun/Documents/Python Stuff/chargecounters/" + block.name +  "chargecounter.py"), "a")
                    spawner.close 
                    picklejar = 1 
                    pickle.dump(picklejar, open(("C:/Users/Prathmun/Documents/Python Stuff/chargecounters/" + block.name +  "chargecounter.py"), "wb"))











def cooldownchecker(block):
    thenow = datetime.now()
    blockmemory = pickle.load(open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name + ".py"), "rb"))
    blockactivation = blockmemory[-1]
    timesinceblockactivation = (thenow - blockactivation)
		#If the following is true then the block is avaliable.
		#if the test results if false then the block is active.
    if block.cooldown < timesinceblockactivation:
        return True
    if block.cooldown > timesinceblockactivation:
        return False
        







def chargechecker(block):
    blockchargememory = pickle.load(open(("C:/Users/Prathmun/Documents/Python Stuff/chargecounters/" + block.name +  "chargecounter" + ".py"), "rb"))
    #unclear if the unpickled object will need to be converted into an int like in the legacy code. I don't think so, but I made this marker to suggest this possibility in case an error appears when we get the architecture running. Delete later if no error!
    return blockchargememory



def refreshbarker(block):
    thenow = datetime.now()
    blockmemory = pickle.load(open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name + ".py"), "rb"))
    blockactivation = blockmemory[-1]
    print (thenow + (block.cooldown - (thenow - blockactivation)))
   









def blockactivationcounter(path):
	for block in path.blocks:
			total = total + 1
			offcd = cooldownchecker(block)
			if offcd == False:
				offcdcounter = offcdcounter + 1
		
		





		
def whitespace(size): 
		for i in range (1,size):
			print(" ")
