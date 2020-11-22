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
            #### Anchor for all visual output ####					
            ####                              ####



    #permits timeouts and refereshing the interface





def timeout():
    whitespace(20)
    print("Refreshing the interface")
    whitespace(10)
    time.sleep(5)
    interface()					


    
def raw_input_with_timeout(prompt,): 
    interfacereset = threading.Timer(180, timeout, [])
    interfacereset.start()
    userinput = None	
    userinput = input(prompt)
    interfacereset.cancel()
    return userinput	

    #actual interface
def interface():
    whitespace(35)
    counter = 0
    whitespace(2)
        
        
    
    #Displays the choie of disciplines, the number of blocks contained, and the number of blocks off cooldown

    for disc in grossdisciplines:
        total = 0
        offcdcounter = 0
        for path in disc.paths:
        
        #Counts the blocks and their cooldown status
        
            for block in path.blocks:
                orbisaccumuli(block, "n")
                total = total + 1
                offcd = cooldownchecker(block)
                if offcd == False:
                    offcdcounter = offcdcounter + 1
                    
        disccd = disc.cooldown
        disccd = str(disccd)
        totalblocks = total
        totalblocks = str(totalblocks)
        blocksoffcd = offcdcounter
        blocksoffcd = str(offcdcounter)
        
        whitespace(2)		
        print(str(counter) + " " + disc.name  + " " + blocksoffcd + "/" + totalblocks + " active" )
        disclevelorbisvox(disc)
        whitespace(2)
        
        counter = counter + 1
        #displays paths and the number of off cooldown blocks each has_key
        for path in disc.paths:
            total = 0
            offcdcounter = 0
        #Counts the blocks and their cooldown status
            for block in path.blocks:
                total = total + 1
                offcd = cooldownchecker(block)
                if offcd == False:
                    offcdcounter = offcdcounter + 1
            totalblocks = total
            totalblocks = str(totalblocks)
            cdstring = offcdcounter
            cdstring = str(cdstring)
            print ("    " + path.name + "    " + cdstring + "/" + totalblocks )
            print (" ")
            
    #adds gui for selecting the cycle view
    viewslot = 0
    for each in grossdisciplines:
        viewslot = viewslot + 1
    viewslot = str(viewslot)
    whitespace(2)
    print (viewslot + " Cycle View" )
    viewslot = int(viewslot)
    
#**************************************************************	
    
    #Adds the gui for selecting the hopper

    hopperslot = 0
    for each in grossdisciplines:
        hopperslot = hopperslot + 1
    hopperslot1 = hopperslot + 1
    hopperslot2 = hopperslot1 + 1
    slot0 = slotfiller0()
    slot1 = slotfiller1()
    hopperslotmarker1 = hopperslot1
    hopperslotmarker2 = hopperslot2
    hopperslotmarker1 = str(hopperslotmarker1)
    hopperslotmarker2 = str(hopperslotmarker2)
    
    if slot0 is None:
        print ("All Blocks are Currently active")
        time.sleep(10)
        cycleview()
        time.sleep(15)
        interface()
    else:
        whitespace(4)
        print ("Hopper: Inactive Blocks.")
        print (hopperslotmarker1  + " " + slot0.title)
        print (slot0.process)
    
    if slot1 is None:
        print (" ")
    else:
        print (hopperslotmarker2  + " " + slot1.title)
        print (slot1.process)


    hopperslot = int(hopperslot)
    
    
#**************************************************************	
    
    
    #Processes the choice of discipline
    whitespace(2)
    discchoice = raw_input_with_timeout("Choose the discipline to explore")
    discchoice = int(discchoice)
    
    
    
#**************************************************************
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
        if answer == "s":
            orbisaccumuli(slot0, "s")
        interface()
    if discchoice == hopperslot2:
        whitespace(10)
        print ("Name: " + slot1.title)
        print ("Process: " + slot1.process)
        print ("Output: " + slot1.output)
        cooldownmarker = str(slot1.cooldown)
        print ("Cooldown: " + cooldownmarker)
        answer = raw_input("Activate this block's cooldown?")
        if answer == "y":
            orbisaccumuli(slot1, "y")
        if answer == "s":
            orbisaccumuli(slot1, "s")
            
        interface()
    

#**************************************************************


########Process the choice if it would selct the viewslot#########




    if discchoice == viewslot:
        for i in range (5):
            cycleview()
            time.sleep(15)
            interface()
    discchoice = grossdisciplines[discchoice]
    whitespace(20)
    print (discchoice.name)
    whitespace(2)
    print (discchoice.flavor)
    whitespace(2)
    counter = 0
    
    
    #####displays the paths avaliable####
    
    
    
    
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
    if addcharge == "s":
        orbisaccumuli(blockchoice, "s")
        
    

picklejarfactory(grossdisciplines)


for i in range(10000):
    interface()
