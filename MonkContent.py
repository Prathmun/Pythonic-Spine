from TheListBackEnd import *








#NAME = Block("NAME","PROCESS","OUTCOME","COOLDOWN","CHARGECAP"))

#NAME = Path(NAME, PROCESS, "BLOCKS, "ORDER"))

#earth blocks

empty_cup =Block("Empty Cup",
"Sit and watch your breath for 5 minutes or longer",
"Decant",
100,
3)

motion_lotion = Block("Motion Is Lotion",
"Get up and move for at least 15 minutes, set a timer",
"Humans are meant to move, not do what I want to do",
150,
2)





### Path ###

earth = Path("Earth",
"Yin, ground, darkness",
(empty_cup, motion_lotion),
0)



thoracic_wavies =Block("Thoracic Wavies",
"""open books 3 sets 10 reps
arm scissors 3 sets 10 reps
snow angels 3 sets 10 reps
""",
"Maintain shoulder mobility, recover from computer use"
,(1.6*24*60),
5
)

thoracic_rotations =Block("Thoracic Rotations",
"""On all fours, with hand on neck rotate thoracic spine, focus on elbow movement
3sets ten reps""","Maintain thoracic mobility, build strength, recover from computer use",(1.6*24*60),
5)

ham_slider = Block("Ham Sliders",
" sets 3x6 reps per leg Lay on back, left one leg up in the air, place other on slider",
"Strengthens/Extends hamstrings, recover from sitting",
(2*24*60),
5)


side_planks = Block("Side Planks",
"two sets of 40 seconds of sideplank with pulsations on each side",
"Build core and oblique strength, recover from computer use",
(2*24*60),5)

steppers = Block("Stepper",
"""Bending at the hips,  lean your upper body forward slightly
step up using only the leg on the step. Avoid using your back leg to help push off. Keep your back leg straight with your foot flexed
Keeping the same body position, step down using only the leg on the step""",
"""Big strong: Core, butt, leggs""",
(2*24*60),5)

half_deadlift = Block("Half Deadlift",
"""3sets 10 reps
Bend at your to reach down and grasp the kettlebell. Lift the ewight off the ground, engaging your back and thigh muscles.
 Then lower it back down just below your knees and repeat.""",
 """Safely load lower back, recover from sitting all the time.""", (2*24*60),5)

goblin_squat = Block("Goblin Squat", 
"""
3sets 10 reps
Feet slightly wider than hips, squat with a 30lb weight """,
"""Load bootay safely, recover from computer use""",(2*24*60),5)

### Path ###

Physical_T = Path("PT",
"Physical Therapy ~~ Physical Training",
(thoracic_wavies, thoracic_rotations,ham_slider, side_planks, steppers, half_deadlift, goblin_squat),
1)



monk = Discipline("Monk", 
"""
The Monk values Tranquility(Stability) and Clarity(purpose)
""", 1, (earth,Physical_T), 10)
#The monk holds on to Paths and Forms
