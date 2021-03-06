from datetime import datetime, timedelta

import dateutil.parser
import random
import time
import threading 
from pathandblocks import *
from hopper import *
from OrbisAcumuli import *
from Flowview import *
import os    


        
            ####                              ####
            #### Anchor for visual output     ####					
            ####                              ####


def interface():
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
        
        
                                             
            ###
    #adds gui for selecting the cycle view
            ###
    viewslot = 0
    for each in grossdisciplines:
        viewslot = viewslot + 1
    viewslot = str(viewslot)
    whitespace(2)
    print (viewslot + " Cycle View" )
    viewslot = int(viewslot)
    
#**************************************************************	
    
    #Adds the gui for selecting the hopper

    hopperslot1 = 1    
    for each in grossdisciplines:
        hopperslot1 = hopperslot1 + 1
    hopperslot2 = hopperslot1 + 1
    
    slot0, slot1 = hopperloader()
    
    whitespace(4)
    
    print ("Hopper: Avaliable Blocks.")    
    print (str(hopperslot1)  + " " + slot0.title)
    print (slot0.process)
    print (str(hopperslot2)  + " " + slot1.title)
    print (slot1.process)











    ###
#**************************************************************	
    ###
    
    #Processes the choice of discipline
    whitespace(2)
    discchoice = input("Choose the discipline to explore")
    discchoice = int(discchoice)
    
    
    ###
#**************************************************************
    ###
    
    
    
    
    
    
    
    
    #Procceses the input if the input would select the hopper
    if discchoice == hopperslot1:
        whitespace(10)
        print ("Name: " + slot0.title)
        print ("Process: " + slot0.process)
        print ("Output: " + slot0.output)
        cooldownmarker = str(slot0.cooldown)
        print ("Cooldown: " + cooldownmarker)
        answer = input("Activate this block's cooldown?")
        if answer == "y":
            orbisaccumuli(slot0, "y")
        interface()
    if discchoice == hopperslot2:
        whitespace(10)
        print ("Name: " + slot1.title)
        print ("Process: " + slot1.process)
        print ("Output: " + slot1.output)
        cooldownmarker = str(slot1.cooldown)
        print ("Cooldown: " + cooldownmarker)
        answer = input("Activate this block's cooldown?")
        if answer == "y":
            orbisaccumuli(slot1, "y")
            
        interface()
    

#**************************************************************


########Process the choice if it would selct the viewslot#########




    if discchoice == viewslot:
        for i in range (5):
            cycleview()
            time.sleep(15)
            interface()
    
    
    
    
    ###
    
    #####displays the paths avaliable####
    
    ###
    
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
            
        
        
    #Processes the path request
    pathchoice = input("Choose a path to explore")		
    
    
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
    
    
    #processes the block request
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
        
    

picklejarfactory(grossdisciplines)


for i in range(1000000):
    interface()
