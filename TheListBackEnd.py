# The armature is an adaptive methodology. It assures access to a 'past.' The value system that the methodology labors under is in theory unimportant to the methodology, none the less at the moment of writing the author is operating under an existentialist value system, as put forth by Simone De Beauvior in The Ethics of Ambiguity
import time
import pickle
import fileinput
from datetime import datetime, timedelta
import dateutil.parser
from clint.textui import colored

# Represents an identity
class Discipline:
    def __init__(self, name, flavor, priority, paths, cooldown):
        self.name = colored.yellow(name)
        self.flavor = colored.green(flavor)
        self.priority = priority
        self.paths = list(paths)
        self.cooldown = timedelta(minutes=cooldown)

# Represents a class of method serving an identity
class Path:
    def __init__(self, name, subtitle, blocks, order):
        self.name = colored.cyan(name)
        self.subtitle = subtitle
        self.blocks = list(blocks)
        self.order = order

# Represents a behavior, or a quest to further its parent values, or move the world towards a state similar to that presented in the imagery of the Path
class Block:
    def __init__(self, name, process, output, cooldown, chargecap):
        self.name = name
        self.title = colored.magenta(name)
        self.process = colored.cyan(process)
        self.output = colored.green(output)
        self.cooldown = timedelta(minutes=cooldown)
        self.chargecap = chargecap * 10

# Makes the files that we will be writing the pickles.
def picklejarfactory(grossdisciplines):
    # This makes the block file, which is used to store activation times
    for discipline in grossdisciplines:
        for path in discipline.paths:
            for block in path.blocks:
                block_file = f"Blocks/{block.name}.py"
                try:
                    pickle.load(open(block_file, "rb"))
                except (IndexError, IOError):
                    with open(block_file, "wb") as spawner:
                        thenow = datetime.now()
                        thethen = thenow + timedelta(days=-1500)
                        picklejar = [thethen]
                        pickle.dump(picklejar, spawner)

    # This makes the charge file, which tracks how many charges a given block is holding at this moment.
    for discipline in grossdisciplines:
        for path in discipline.paths:
            for block in path.blocks:
                charge_file = f"chargecounters/{block.name}chargecounter.py"
                try:
                    pickle.load(open(charge_file, "rb"))
                except (IOError, EOFError, IndexError):
                    with open(charge_file, "wb") as spawner:
                        picklejar = 1
                        pickle.dump(picklejar, spawner)

# This checks to see if a block is still burning through its remaining charges. Returning a boolean if it does.
def cooldownchecker(block):
    # This works by checking how long it's been since the block has been 'activated'. If it's been longer than the cooldown, then it returns True
    thenow = datetime.now()
    block_file = f"Blocks/{block.name}.py"
    blockmemory = pickle.load(open(block_file, "rb"))
    blockactivation = blockmemory[-1]
    timesinceblockactivation = thenow - blockactivation

    # If the following is true then the block is available.
    # If the test results if false then the block is active.
    return block.cooldown < timesinceblockactivation

# This just returns an int of the remaining number of charges
def chargechecker(block):
    charge_file = f"chargecounters/{block.name}chargecounter.py"
    blockchargememory = pickle.load(open(charge_file, "rb"))
    return int(blockchargememory)

# This runs chargechecker() on all paths
def path_level_charge_checker(path):
    return sum(chargechecker(block) for block in path.blocks)

# Runs the path_level_charge_checker() on all discs
def disc_level_charge_checker(disc):
    return sum(path_level_charge_checker(path) for path in disc.paths)

# Returns the total number of charges in a path, and the total number of 'active' blocks
def blockactivationcounter(path):
    counter_total = 0
    off_cd_counter = 0
    for block in path.blocks:
        counter_total += 1
        if not cooldownchecker(block):
            off_cd_counter += 1
    return counter_total, off_cd_counter

# Returns the total number of charges in a disc, and the total number of 'active' blocks
def disc_level_activation_counter(disc):
    total_blocks = 0
    blocks_off_cd = 0
    for path in disc.paths:
        temp_blocks, temp_blocks_off_cd = blockactivationcounter(path)
        total_blocks += temp_blocks
        blocks_off_cd += temp_blocks_off_cd
    return total_blocks, blocks_off_cd

def whitespace(size):
    print("\n" * (size - 1))