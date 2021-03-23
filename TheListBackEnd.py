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
                    pickletext = pickle.load(open(("Blocks/" + block.name +  ".py"), "rb"))
                except (IndexError, IOError,):
                    spawner = open(("Blocks/" + block.name +  ".py"), "a")
                    spawner.close
                    thenow = datetime.now()
                    thethen = (thenow + timedelta(days=-1500))
                    picklejar = [thethen,]
                    pickle.dump(picklejar, open(("Blocks/" + block.name +  ".py"), "wb"))


    for discipline in grossdisciplines:
        for path in discipline.paths:
            for block in path.blocks:
                try:
                    pickletext = pickle.load(open(("chargecounters/" + block.name +   "chargecounter.py"), "rb"))
                except (IOError, EOFError, IndexError,):
                    spawner = open(("chargecounters/" + block.name +  "chargecounter.py"), "a")
                    spawner.close 
                    picklejar = 1 
                    pickle.dump(picklejar, open(("chargecounters/" + block.name +  "chargecounter.py"), "wb"))




def cooldownchecker(block):
    thenow = datetime.now()
    blockmemory = pickle.load(open(("Blocks/" + block.name + ".py"), "rb"))
    blockactivation = blockmemory[-1]
    timesinceblockactivation = (thenow - blockactivation)
		#If the following is true then the block is avaliable.
		#if the test results if false then the block is active.
    if block.cooldown < timesinceblockactivation:
        return True
    if block.cooldown > timesinceblockactivation:
        return False
        

def chargechecker(block):
    blockchargememory = pickle.load(open(("chargecounters/" + block.name +  "chargecounter" + ".py"), "rb"))
    return int(blockchargememory)

def path_level_charge_checker(path):
    total_charge_counter = 0
    for each in path.blocks:
        total_charge_counter = total_charge_counter + chargechecker(each)
    return total_charge_counter

def disc_level_charge_checker(disc):
    sum_charge_counter = 0
    for each in disc.paths:
        sum_charge_counter = sum_charge_counter + path_level_charge_checker(each)
        return sum_charge_counter


def refreshbarker(block):
    thenow = datetime.now()
    blockmemory = pickle.load(open(("Blocks/" + block.name + ".py"), "rb"))
    blockactivation = blockmemory[-1]
    print (thenow + (block.cooldown - (thenow - blockactivation)))
   









def blockactivationcounter(path):
    counter_total = 0
    off_cd_counter = 0
    for block in path.blocks:
            counter_total = counter_total + 1
            offcd = cooldownchecker(block)
            if offcd == False:
                off_cd_counter = off_cd_counter + 1
    return counter_total, off_cd_counter

def disc_level_activation_counter(disc):
    total_blocks = 0
    blocks_off_cd = 0
    for path in disc.paths:
        temp_blocks, temp_blocks_off_cd = blockactivationcounter(path)
        total_blocks = total_blocks + temp_blocks
        blocks_off_cd = blocks_off_cd + temp_blocks_off_cd
    return total_blocks, blocks_off_cd





		
def whitespace(size): 
		for i in range (1,size):
			print(" ")
