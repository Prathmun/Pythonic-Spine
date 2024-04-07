from datetime import datetime, timedelta

from TheListBackEnd import whitespace, cooldownchecker, colored
from pathandblocks import ordered_disciplines
from OrbisAcumuli import orbisaccumuli, orbis_rotatus, orbisvox, disclevelorbisvox, pathlevelorbisvox
from Carrot_Machine import celebration
import pickle



        
            ####                              ####
            #### Anchor for visual output     ####					
            ####                              ####
def refreshbarker(block):
    thenow = datetime.now()
    blockmemory = pickle.load(open(("Blocks/" + block.name + ".py"), "rb"))
    blockactivation = blockmemory[-1]
    print (thenow + (block.cooldown - (thenow - blockactivation)))
    
    #Initial display


def display_disciplines():
    for counter, disc in enumerate(ordered_disciplines):
        print(f"\n\n{disc.name}")
        disclevelorbisvox(disc, counter)
        print("\n")

def facade():
    whitespace(35)
    orbis_rotatus()     
    display_disciplines()
    print("Select the hopper:")

def discprocessor(discchoice):
    discchoice = ordered_disciplines[discchoice]
    whitespace(20)
    print (discchoice.name)
    whitespace(2)
    print (discchoice.flavor)
    whitespace(2)
    counter = 0        
        
    for counter, path in enumerate(discchoice.paths):
        total_blocks = len(path.blocks)
        blocks_off_cooldown = sum(1 for block in path.blocks if not cooldownchecker(block))

        print(f"{counter} {path.name} {blocks_off_cooldown}/{total_blocks} Processes are active in this path")
        pathlevelorbisvox(path)
        whitespace(2)

        for block in path.blocks:
            offcd = cooldownchecker(block)
            attrition_status = "Available." if offcd else "Active"
            print(f"    {block.title}  {attrition_status}")
            orbisvox(block)


def pathprocessor(disc_choice):
    disc = ordered_disciplines[disc_choice]
    path_choice = int(input("Choose a path to explore: "))
    path = disc.paths[path_choice]

    whitespace(20)
    print(path.name)
    print(path.subtitle)
    whitespace(2)

    for counter, block in enumerate(path.blocks):
        offcd = cooldownchecker(block)
        attrition_status = "Available." if offcd else "Active"

        print(f"{counter} {block.title}  {attrition_status}")
        print(block.process)

        if not offcd:
            print(block.output)

        print(block.cooldown)
        orbisvox(block)
        whitespace(2)

    whitespace(2)
    return path

def blockprocessor(pathchoice):
    blockchoice = input("Choose a block to expand")
    blockchoice = int(blockchoice)
    intermediary = pathchoice.blocks
    blockchoice = intermediary[blockchoice]
    whitespace(43)
    
    print (blockchoice.title)
    whitespace(2)
    print (blockchoice.process)
    whitespace(2)
    print (blockchoice.output)
    print (blockchoice.cooldown)
    print (colored.red("Date and time of cooldown refresh"))
    refreshbarker(blockchoice)
    
    print (whitespace(8))
    
    addcharge =  input("Add a charge?")
    if addcharge == "y":
        orbisaccumuli(blockchoice, "y")
        celebration()
        facade()



def interface():
    facade()


    #Processes the choice of discipline
    whitespace(2)
    discchoice = input("Choose the discipline to explore")
    discchoice = int(discchoice)
    ###
    #####displays the paths avaliable####
    ###
    discprocessor(discchoice)     
    ###       
    #Processes the path request
    ###
    pathchoice = pathprocessor(discchoice)
    ###
    #processes the block request
    ###
    blockprocessor(pathchoice)
        



interface()