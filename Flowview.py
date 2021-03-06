from datetime import datetime, timedelta
import dateutil.parser
import random
import time
from pathandblocks import *
from OrbisAcumuli import *

        
def cycleview():
    
    sampledisc = random.sample(grossdisciplines, 2)
    for disc in (sampledisc):
        for path in disc.paths:
        
        
            whitespace(3)
            whitespace(3)
            
            print (disc.name + ": ")
            print ((disc.flavor))
            
            time.sleep(3)
            whitespace(3)
            
            print  (path.name)
            
            time.sleep(1)
            
            print (colored.green(path.subtitle))
            
            time.sleep(2)
            whitespace(4)
            
            
            for block in path.blocks:
                print ("Name: " + colored.magenta(block.name))
                orbisvox(block)
                time.sleep(2)
                print ("Process: " + block.process)
                time.sleep(2)
                print ("Output: " + block.output)
                time.sleep(1)
                print ("Cooldown: " + str(block.cooldown))
                print (colored.red("Date and time of cooldown refresh"))
                waittime = random.randint(5,20)
                refreshbarker(block)
                time.sleep(waittime)
                whitespace(50)
