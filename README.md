# BoyoRPG: Hawk-Eye RPG Written in Python
# Grade Recieved: A+ from UCSC CS115: Software Engineering with Prof. Richard Jullig

BoyoRPG is an Open-World, Live-Action Combat Game with Multi-Phase Bosses, Questing, Friendly/Enemy NPCs, Modifiable Inventory, Modifiable Player Stats and more! 

Unit Test Script Also Included!


# Most up-to-date version: 042

And Yes, this hub uses non-standard git hierarchical practices. 
The reason behind this is simple: we wanted to pull the entire repo and see the changes from version to version. 

These files CURRENTLY require PYGAME module installed and recommend PYTHON 3.x and are not tested with any other versions. 

To Install PYGAME: 

python3 -m pip install -U pygame --user

Final edition will NOT require pygame NOR python. 

To play, open a version (i.e 042 folder) and run BoyoRPG.py

ART CREDITS LISTED IN "Credits.txt"

Patches are in ascending order. Look for the most up to date patch/version. 

===============CHANGE LOG=================

===SPRINT 1===

PATCH-00
Basic Map/player generation. Basic movement/controls. Basic entry/exit functionality.

PATCH-001
Added menus, buttons, theme music, better movement. 
Better Code Structure.

PATCH-01 (Animation Testing) 
Added, Attacks: Left Mouse, House Entry: Left Mouse, all Paths and Houses are linked (except for homeTown castle), Generic attack sounds

===SPRINT 2===

PATCH-02
Restructured Code 
Added HP bars, Inventory shell, rough boundary checking (broken),  and loading screen

PATCH-03
Optimized code in BoyoRPG.py and PlayerTest.py. Also Added MapLink.py for better structure.  
Added basic boundaries, deathscreen/restart, menu "flare", fixed infinite attack bug, and fixed some inventory bugs. 
Added player movement animations
Also restructured code to run from main(). 

PATCH-035
Added Mobs (EnemyTest.py)
Fixed Inventory Bugs

===SPRINT 3===

PATCH-036
Added BossTest for the (current) final boss, different music for different maps, and modified existing maps. 
*Quests/NPC interactions were backlogged to sprint 4 due to not meeting full done criteria (Framework is in place however)*


===SPRINT 4=== (RELEASE 1)

PATCH-042
Finalized quest mechanics: killQuests, findQuests, and destinationQuests added. Quests give items on completion. 
NPC's are also finalized and spawn/despawn correctly. They also display their dialogue on screen and give quests. 
Added quest log to player paused menu. 
Added modifiable player stats based off equipped items. These stats are implemented on enemy mob/boss interactions. 
Added 3 boss phase arena mode in sunkenChapel. 
