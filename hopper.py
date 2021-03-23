#Quest hopper

#the slots will pull a random block after who's cool down is up.
	#randomly select from all quests
	#	check to see if it's off cd
	#		if it is add it to the hopper and exit this loop
	#		if it isn't select another random block
			
#the entirety of the selected block will  be presented
#the user will be asked if it would like to put the block on cd.

from pathandblocks import *
from datetime import datetime, timedelta
import dateutil.parser
import random
import time

thenow=datetime.now()

def slotfiller0():	
    thenow=datetime.now()
    grossblocks = []
    for disc in grossdisciplines:
        for path in disc.paths:
            for block in path.blocks:
                cooldownboolean = cooldownchecker(block)
                if cooldownboolean == True:
                    grossblocks.append(block)
        try:
            return random.choice(grossblocks)
        except(IndexError,):
            return systemicexit 
				



 

def slotfiller1():
    thenow=datetime.now()
    grossblocks = []
    for disc in grossdisciplines:
        for path in disc.paths:
            for block in path.blocks:
                cooldownboolean = cooldownchecker(block)
                if cooldownboolean == True:
                    grossblocks.append(block)
        try:
            return random.choice(grossblocks)
        except(IndexError,):
            return systemicexit


	
def hopperloader():
    slot0 = slotfiller0()
    slot1 = slotfiller1()
    return slot0, slot1
    
