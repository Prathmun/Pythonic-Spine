#backend for orbisaccumuli
from pathandblocks import *
from datetime import datetime, timedelta
import dateutil.parser
from clint.textui import colored

               

    






def orbisaccumuli(block, useractivated):
    offcd = cooldownchecker(block)
    if offcd == True:	

        if useractivated == "n":
            blockcharge=chargechecker(block)
            if blockcharge > 0:
                blockcharge = blockcharge - 1		
                blockmemory = pickle.load(open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name + ".py"), "rb"))
                blockmemory.append(datetime.now())
                pickle.dump(blockmemory, open(("C:/Users/Prathmun/Documents/Python Stuff/Blocks/" + block.name + ".py"), "wb"))
                pickle.dump(blockcharge, open(("C:/Users/Prathmun/Documents/Python Stuff/chargecounters/" + block.name + "chargecounter.py"), "wb"))
                        

            
            
    #A charge is added
    if useractivated == "y":
            blockcharge = chargechecker(block)
            if blockcharge >= block.chargecap:
                whitespace(10)
                print (colored.red("Block is at max charges"))
                whitespace(10)
                time.sleep(3)
            else:
                blockcharge = blockcharge + 1
                with open(("C:/Users/Prathmun/Documents/Python Stuff/chargecounters/" + block.name + "chargecounter.py"), "wb") as blockaddress:
                    pickle.dump(blockcharge, blockaddress)
                        

    
    
        
        
        
            
            
            
#the voice or visual display of the state of accumiliation.


def orbisvox(segment):
#stars to indicate charge counters
    starcounter = 0
    starline = " "
    blockcharge = chargechecker(segment)
    while starcounter < blockcharge:
        print (starcounter)
                ##color options
        #	'red', 'green', 'yellow', 'blue',
        #  'black', 'magenta', 'cyan', 'white',
        #   'clean', 'disable')
        starline = starline + colored.cyan("*")
        starcounter = starcounter + 1
        print (starline)
    
    
def disclevelorbisvox(disc):
    disclevelchargecounter = 0
    chargecounter = 0
    for path in disc.paths:
        for block in path.blocks:
            blockcharge = chargechecker(block)
            while chargecounter < blockcharge:
                chargecounter = chargecounter + 1
        disclevelchargecounter = disclevelchargecounter + chargecounter
        disclevelchargecounter = str(disclevelchargecounter)
    print ("  " + "Cumalitve Charge: " + colored.cyan(disclevelchargecounter))
    
def pathlevelorbisvox(path):
    pathlevelchargecounter = 0
    chargecounter = 0
    for block in path.blocks:
        blockcharge = chargechecker(block)
        while chargecounter < blockcharge:
            chargecounter = chargecounter + 1
        pathlevelchargecounter = pathlevelchargecounter + chargecounter
    pathlevelchargecounter = str(pathlevelchargecounter)
    print ("  " + "Cumalitve Charge: " + colored.cyan(pathlevelchargecounter))
    
