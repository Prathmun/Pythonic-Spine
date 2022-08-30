
from pathandblocks import *
from datetime import datetime, timedelta
from TheListBackEnd import chargechecker
import dateutil.parser
import random
import time

def hopper(disc):
    thenow=datetime.now()
    grossblocks = {}
    for path in disc.paths:
        for block in path.blocks:
            charge_count = chargechecker(block)
            if charge_count not in grossblocks.keys():
                grossblocks[charge_count] = [block]
            else:
                grossblocks[charge_count].append(block)
    smallest_key = min(grossblocks.keys())
    return grossblocks[smallest_key][0]



    
