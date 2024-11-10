# Little Dungeons

This game is a flexible and creative game, designed to be both fast and simple to play, to make it accessible to a wide audience.

## LICENSE

"Little Dungeons" is released under the legal text found in the file [LICENSE](LICENSE).  
At the time of writing, this is the CC0 1.0 Universal license.  

## Needed Materials

+ A large piece of paper for drawing the map on.
+ Each player needs a piece of paper, a pencil, and an eraser, to track their current information on.
+ The narrator likely needs a small notebook to repeatedly track monster encounters and other things.

## Narrator

The narrator governs the game. 
They can choose to overrule or ignore any of the following statements, at any time.

The narrator's goal is to make the game fun and fair for everyone - which is not easy or always possible.

They try and tell a story, outside of the game mechanics outlined below.
The story will likely be a fairy tale style one, as that works best with some of the mechanics.
However, the narrator is free to choose anything that they feel like.

## Players

A player has a single class of:

| Class       | Action    | Category       |
| ----------- | --------- | -------------- |
| Musician    | Play Song | attack monster |
| Pirate      | Attack    | attack monster |
| Chef        | Cook      | heal teammate  |
| Nurse       | Medicine  | heal teammate  |

A player has:

| Stats           | Starts at   |
| --------------- | ----------- | ---------------------------------------- |
| Level           | 1           | Level-up in town (according to narrator) |
| Current Health  | Max Health  | set back to max entering a town          |
| Max Health      | d6 roll     | every level up: +d6 roll by player       |
| Current Stamina | Max Stamina | set back to max entering a town          |
| Max Stamina     | d6 roll     | every level up: +d6 roll by player       |
| Clothing        | 1           | -                                        |
| Item            | 1           | -                                        |
| Coins           | 0           | -                                        | 
| Badges          | 0           | numbers of last winning moves            |
| Relationship    | 0           | with every other player, max=6           |


| Stat            | Effect                                               |
| --------------- | ---------------------------------------------------- |
| Level           | Difficulty of monster encounters                     |
| Current Health  | They fall asleep on a negative value or 0            |
| Current Stamina | If negative or 0, can't do anything, in an encounter |

In Town
-------

Upon entering a town Current Health & Stamina set back to max for all players

Per visit, each player can do two of:

| 
| Outing     | Gives +1 to relationship of player and chosen friend |
| Restaurant | Gives +1 to Max Health                               |
| Sleep-In   | Gives +1 to Max Stamina                              |
| Shopping   | Cost 3*d6 coins from player to +1 clothing OR item   |

Out of Town
-----------

3 encounters occur, per travel outside of a town.

Map follows roads, and the same thing stays put, after the first encounter.
i.e. Always meet monster at the same location.

Narrator rolls for encounter:

+-------------------------+-----------------------------------------------+
| 1st  |                  |              2nd Dice roll                    |
| dice | Type of          +-----------------------------------------------+
| roll | Encounter        |        1-3      |          4-6                |
+-------------------------+-----------------+-----------------------------+
|    1 | Tell story       | no stats change | players get +1 relationship |
+------+------------------+-----------------+-----------------------------+
|    2 | Monster encount. | Reward for winning is 1x dice roll of coins   |
+------+------------------+-----------------------------------------------+
|    3 | Monster encount. | Reward for winning is 2x dice roll of coins   |
+------+------------------+-----------------------------------------------+
|    4 | Hidden Treasure  | Every player gets +1 coin                     |
+------+------------------+-----------------------------------------------+
|      |                  | Two players chosen by narrator                |
|    5 | Get in argument  +-----------------------------------------------+
|      |                  | no stats change | -1 to their relationship    |
+------+------------------+-----------------------------------------------+
|    6 | Nothing happened | Road forks                                    |
+------+------------------+-----------------------------------------------+


## Monster Encounter

The type of monster is rolled for at the start of the encounter:

1. Witch
2. Ghost
3. Big Bad Wolf
4. Goblin
5. Naughty Cat 
6. Snake

There are a number of monsters present.

+ The count is equal to the highest level of player.
+ The health of each is a number of dice rolls by the narrator, equal to the highest level of player.

To run away:

1. Players agree on either high (4-6) or low (1-3) roll.
2. Narrator rolls.
3. If roll matches, players escaped.

Every player and monster takes a turn:

+ Monsters do single roll damage, by narrator, every time.
	+ Clothing value is taken away from value, before doing health damage, up to 5.
	
+ Monsters target a single player, decided by narrator.

+ Player decides on "action" to heal or attack:
	+ Action is one dice roll
		+ Item value is added to action, after dice roll
		+ If the player has a pet, then +1 is added
		+ Any player with more than 3 relationship can add half a roll, rounding upwards, to the value.
			This takes 1 from their relationship.
	+ If action doesn't match class, half the final number, rounding upwards.
	+ If action final number greater than current stamina, nothing happens.
	+ If something happens, current stamina takes away the final number.

+ If all players fall asleep, then revert location to previous town. (Saved by a passerby, or similar story.)

+ A player can take a single defeated animal monster as a pet.

+ Every time 10 monsters defeated:
	- Gives +1 to max health for all players
	- Gives +1 to max stamina for all players
	- Narrator should consider leveling up.
