from TheListBackEnd import *
from Cyberneticist import cyberneticist
from IndustrialistContent import *
from MagusContent import *
from MonkContent import *
from Gamer_content import *
grossdisciplines =[monk, magus, cyberneticist, industrialist]
picklejarfactory(grossdisciplines)
ordered_disciplines = []
discipline_dict = {}
for disc in grossdisciplines:
    key = disc_level_charge_checker(disc)
    if key not in discipline_dict.keys():
        discipline_dict[key] = [disc]
    else:
        discipline_dict[key].append(disc)
for key in sorted(discipline_dict.keys()):
    for disc in discipline_dict[key]:
        ordered_disciplines.append(disc)


