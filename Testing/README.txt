To run the tests, simply start BoyoRPG.py in Testing/BoyoRPG Tests/
An automated script will go through each test as a normal player would. 

The script is known to crash if you alt-tab or switch to another window midrun.

The other files in this directory (/testing) are extra EXCEPT "testing" file has an outline of the testing process


There are 8 tests included in BoyoTest.txt. Since this is a live game, the unit testing is slightly different than other types of programs as game makers generally rely on player driven testing. We created a script that runs through some basic functions of the game as a player would. Although it works, it’s also very time consuming to create these types of tests and they reach diminishing returns quickly based on testing complexity. 

Equivalence Classes: 
All map changes are equivalent 
All EnemyTest.Mob (de)spawns, collisions with player, and damages are equivalent
All boundary generation, preservation, maintenance, and detections are equivalent 

Test Module: BoyoTest.txt
Tests 1 through 8 all test the following cases: 
Player Spawn
Map Changes
Player X,Y movement
Player X,Y animation (although outdated animation it still sufficiently demonstrates it)
Boundary Generation, Preservation, and Maintenance 

Tests 2 and 4 extend the prior equivalence classes and test: 
Boundary Detection 

Tests 5 through 8 all test: 
EnemyTest.Mob Spawns
EnemyTest.Mob Despawns
EnemyTest.Mob player seeking
EnemyTest.Mob animations
EnemyTest.Mob collision/damage to player 
BoyoRPG game over and restart 
