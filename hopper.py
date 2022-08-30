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
from TheListBackEnd import chargechecker
import dateutil.parser
import random
import time

thenow=datetime.now()
#d.get(max(d, key=d.get))

#2.0 to show you the block with the least charges

def  slotfiller0():
    thenow=datetime.now()
    grossblocks = {}
    for disc in grossdisciplines:
        for path in disc.paths:
            for block in path.blocks:
            #Need to test this to see if this works for 0 charge
                charge_count = chargechecker(block)
                if charge_count not in grossblocks.keys():
                    grossblocks[charge_count] = [block]
                else:
                    grossblocks[charge_count].append(block)
    largest_key = max(grossblocks.keys())
    return grossblocks[largest_key][0]
#Also looking to see how to get the second slot to present something different.	

#Might consider rolling this into the normal facade and taking out the hopper position entirely.
#Using these functions to present needed tasks within a given discipline


#Old version
# def slotfiller0():	
#     thenow=datetime.now()
#     grossblocks = []
#     for disc in grossdisciplines:
#         for path in disc.paths:
#             for block in path.blocks:
                
#                 cooldownboolean = cooldownchecker(block)
#                 if cooldownboolean == True:
#                     grossblocks.append(block)
#         try:
#             return random.choice(grossblocks)
#         except(IndexError,):
#             return systemicexit 
				



 

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
    
