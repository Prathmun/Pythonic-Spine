from datetime import datetime, timedelta

import dateutil.parser
import random
import time
import threading 
from TheListBackEnd import whitespace, cooldownchecker, colored, picklejarfactory
from pathandblocks import grossdisciplines
from hopper import hopperloader
from OrbisAcumuli import orbisaccumuli, orbis_rotatus, orbisvox, disclevelorbisvox, pathlevelorbisvox
import os    
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


def facade():
    #clears the stage
    whitespace(35)
    #Checks cooldowns, and turns over the cycle
    orbis_rotatus()     
    #Displays the choie of disciplines, the number of blocks contained, and the number of blocks off cooldown
    counter = 0
    for disc in grossdisciplines:
        whitespace(2)		
        disclevelorbisvox(disc, counter)
        counter = counter + 1
        whitespace(2)                          
    #Adds the gui for selecting the hopper

def discprocessor(discchoice):
    discchoice = grossdisciplines[discchoice]
    whitespace(20)
    print (discchoice.name)
    whitespace(2)
    print (discchoice.flavor)
    whitespace(2)
    counter = 0        
    
    for path in discchoice.paths :
        total = 0
        offcdcounter = 0
        for block in path.blocks:
            total = total + 1
            offcd = cooldownchecker(block)
            if offcd == False:
                offcdcounter = offcdcounter + 1
        totalblocks = total
        totalblocks = str(totalblocks)
        blocksoffcd = offcdcounter
        blocksoffcd = str(offcdcounter)
        
        print (str(counter) + " " + path.name + " " + blocksoffcd + "/" + totalblocks + " Processes are active in this path")
        pathlevelorbisvox(path)
        whitespace(2)
        counter = counter + 1 
        for block in path.blocks:
            offcd = cooldownchecker(block)
            attritionstatus = "Active"
            if offcd == True:
                attritionstatus = "Avaliable."
            print ("    " + block.title + "  " + attritionstatus)
            orbisvox(block)
def pathprocessor(discchoice):
    pathchoice = input("Choose a path to explore")		
    
    discchoice=grossdisciplines[discchoice]
    pathchoice = int(pathchoice)
    intermediary = discchoice.paths
    pathchoice = intermediary[pathchoice]
    
    whitespace(20)
    print (pathchoice.name)
    print (pathchoice.subtitle)
    whitespace(2)
    
    counter = 0

    for block in pathchoice.blocks:
        offcd = cooldownchecker(block)
        attritionstatus = "Avaliable."
        if offcd == True:
            print (str(counter) + " " + block.title + "                     " + attritionstatus)
        if offcd == True:
            print (block.process )
        if offcd == False:
            attritionstatus = "Active"
            print (str(counter) + " " + block.title) 
            print (block.process) 
            print (block.output)
        print (block.cooldown)
        counter = counter + 1
        orbisvox(block)
        whitespace(2)
    whitespace(2)
    return(pathchoice)
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


def interface():
    facade()


    #Processes the choice of discipline
    whitespace(2)
    discchoice = input("Choose the discipline to explore")
    discchoice = int(discchoice)
    hopperchoice(discchoice)
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
        
picklejarfactory(grossdisciplines)


interface()