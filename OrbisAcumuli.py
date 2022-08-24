#backend for orbisaccumuli
from TheListBackEnd import *
from pathandblocks import *
from datetime import datetime, timedelta
import dateutil.parser
from pathandblocks import *
from clint.textui import colored

               

def orbisaccumuli(block, useractivated):
    offcd = cooldownchecker(block)
    if offcd == True:	

        if useractivated != "y":
            blockcharge=chargechecker(block)
            if blockcharge > 0:
                blockcharge = blockcharge - 1		
                blockmemory = pickle.load(open(("Blocks/" + block.name + ".py"), "rb"))
                blockmemory.append(datetime.now())
                pickle.dump(blockmemory, open(("Blocks/" + block.name + ".py"), "wb"))
                pickle.dump(blockcharge, open(("chargecounters/" + block.name + "chargecounter.py"), "wb"))   
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
                with open(("chargecounters/" + block.name + "chargecounter.py"), "wb") as blockaddress:
                    pickle.dump(blockcharge, blockaddress)                            
    #Run orbis accumuli on all the blocks
def orbis_rotatus():
    for disc in grossdisciplines:
        for path in disc.paths:
            for block in path.blocks:
                orbisaccumuli(block, "n")            

#stars to indicate charge counters
def orbisvox(segment):
    starcounter = 0
    starline = " "
    blockcharge = chargechecker(segment)
    while starcounter < blockcharge:
        print (starcounter)
                ##color options
        #	'red', 'green', 'yellow', 'blue',
        #  'black', 'magenta', 'cyan', 'white',
        #   'clean', 'disable')
        starline = starline + colored.red("*")
        starcounter = starcounter + 1
        print (starline)
def disclevelorbisvox(disc, counter):
    total_blocks, total_blocks_off_cd =disc_level_activation_counter(disc)
    disclevelchargecounter = disc_level_charge_checker(disc)
    
    ### #Disc bark

    print(str(counter) + " " + disc.name  + " " + str(total_blocks_off_cd) + "/" + str(total_blocks) + " active" )
    print ("  " + "Cumalitve Charge: " + colored.red(str(disclevelchargecounter)))
    
    ### #Path bark
    for path in disc.paths:
        total_path_blocks, offcdcounter = blockactivationcounter(path)
 
        print ("    " + path.name + "    " + str(offcdcounter) + "/" + str(total_path_blocks) )
        print (" ")   
        for block in path.blocks:
            print("      " + block.name)
            print(colored.red("        " + "*" * (chargechecker(block))))
def pathlevelorbisvox(path):
    pathlevelchargecounter = path_level_charge_checker(path)
    pathlevelchargecounter = str(pathlevelchargecounter)
    print ("  " + "Cumalitve Charge: " + colored.cyan(pathlevelchargecounter))
    
