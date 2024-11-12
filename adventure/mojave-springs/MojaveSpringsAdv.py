# APPLICATION NAME: Mojave Springs Adventure
# AUTHOR: Ed S (https://github.com/mrshareware)
# LAST UPDATE: 10/04/2023
# ===========================================================================
# This was my first Python program. I started by searching for
# "simple python text adventure" and borrowed ideas and Python
# coding styles. Mixed in some of my own spice and heated until
# you could taste some old-fashioned text adventure goodness.
# Enjoy.

# Public Domain
# This is free and unencumbered software released into the public domain.
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any means.

from datetime import datetime

# Header
print('\n\nWelcome to...\n')
block_text = """
X   X  XXX   XXXX  XXX  X   X XXXXX     XXXX XXXX  XXXX  XXXXX X   X  XXXX  XXXX
XX XX X   X     X X   X X   X X        X     X   X X   X   X   XX  X X     X    
X X X X   X     X XXXXX  X X  XXXXX     XXX  XXXX  XXXX    X   X X X XXXXX  XXX  
X   X X   X X   X X   X  X X  X            X X     X X     X   X  XX X   X     X
X   X  XXX  XXXX  X   X   X   XXXXX    XXXX  X     X  XX XXXXX X   X  XXX  XXXX\n 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
print (block_text.replace('X','\u2588')) # Solid Block Character that should work in Terminal
print ("""
Welcome to the sunbaked expanse of the Mojave Desert, a rugged and unforgiving
terrain that hides secrets of years gone by. In this Python beginner's text
adventure you'll embark on an old-time journey, navigating the treacherous
Mojave Desert, gathering essential supplies to find water and conquer the
caverns, and ultimately making your way to the ghost town of Mojave Springs.

As you follow the dusty paths of previous explorers, you'll soon realize that
the true prize awaits you deep the heart of the forgotten town. Can you find
the key to entering the town's fortified bank and seize the legendary treasure
for your own?

With odds stacked against you, do you step into the shoes of a true desert
explorer and embark on this quest of fame and fortune?
""")

# Create Globals - Note these are set in function setup_game_objects()
start_room = 'desert08'
player_name = ''
game_objects = []
movement_counter = 0
water_counter = 0
found_water = False
start_time = datetime.now()
directions = ['north', 'south', 'east', 'west', 'up', 'down']

# Room tuple
# Every room must have at least one direction
# Directions can optionally have "way"s which change the word "path" to whatever is in "way" when creating the description
#    so instead of "There is a path leading" it becomes "There is a rocky trail leading"

rooms = {
    # Desert Rooms 
    # Game sarts in room 8
    'desert01': {
        'name': 'desert01',
        'desc': 'You find yourself lost in the Mojave, surrounded by prickly cacti in\n'
            + 'every direction!',
        'east': 'desert02',
        'eastway': 'rocky trail',
        'south': 'desert04',
        'west': 'desert03' # this loops to 3
    },    
    'desert02': {
        'name': 'desert02',
        'desc': 'You find yourself lost in the Mojave, surrounded by prickly cacti in\n'
            + 'every direction!',
        'west': 'desert01',
        'westway': 'rocky trail',
        'south': 'desert05',
        'east': 'desert03'
    },
    'desert03': {
        'name': 'desert03',
        'desc': 'Yippee! Signs of human presence amid this arid expanse. You stumble upon\n'
            + "the barely recognizable ruins of a miner's cabin, a relic of the past.\n"
            + 'Evidently, its former owner enjoyed simple pleasures and many, many\n'
            + 'budget-friendly brews.',
        'south': 'desertouthouse',
        'southway' : 'path to an outhouse',
        'west': 'desert02',
        'east': 'desert01' # this loops to 1
    },
    'desertouthouse': {
        'name': 'desertouthouse',
        'desc': "Welcome to the exclusive confines of Coyote Pete's private outhouse.\n"
            + 'Surprisingly, for an outhouse, it boasts a rather tasteful decor, good\n'
            + 'lightning and thankfully most of all, no coyotes inside.',
        'north': 'desert03'
    },    
    'desert04': {
        'name': 'desert04',
        'desc': 'The relentless sun beats down upon you, setting your skin ablaze as if it\n'
            + 'were made of kindling. Towering mountains loom in the distance, close to see\n'
            + 'but much too far to walk.',
        'north': 'desert01',
        'east': 'desert05'
    },
    'desert05': {
        'name': 'desert05',
        'desc': 'Roaming through the unforgiving expanse of the Mojave is typically\n'
            + 'ill-advised, [n]. It is a formidable and challenging environment.\n'
            + 'You see the silhouette of rugged mountains on the western horizon.',
        'north': 'desert02',
        'south': 'desert08',
        'east': 'desert06',
        'west': 'desert04'
    },
    'desert06': {
        'name': 'desert06',
        'desc': 'The density of cacti makes hiking a challenge. As far as your eye\n'
            + 'can see it is nothing but cacti, sand and rugged rocks. It seems\n'
            + "like heading south may be your opportunity to gain some elevation.",
        'west': 'desert05',
        'south': 'desert09',
        'southway': 'craggy, rocky trail'
    },
    'desert07': {
        'name': 'desert07',
        'desc': 'Beware [n]! Concealed within the shadows beneath a towering cactus, a\n'
            + 'menacing Crotalus scutulatus, AKA Mojave Rattlesnake, awaits.\n'
            + 'This one has a bad attitude and an abundance of lethal venom.',
        'east': 'desert08'
    }, 
    'desert08': { # Game starts in this room
        'name': 'desert08',
        'desc': 'You stand amidst the awe-inspiring Mojave Desert, surrounded by its\n'
            + 'breathtaking beauty and danger. Yucca, cactus, wild animals and harsh\n'
            + 'landscapes surround you. In the west, a mysterious buzzing sound can be\n'
            + 'heard. Is it a key to your survival or is it something else?\n'
            + 'Your thirst grows, driving you to seek water in this harsh land.',
        'north': 'desert05',
        'west': 'desert07'
    },
    'desert09': {
        'name': 'desert09',
        'desc': 'Perched upon on a rocky bluff, you see endless miles of unforgiving desert\n'
            + 'sprawled before you. The land is devoid of trees and accessible water.\n'
            + 'Brown, dry, mountains are barely visible on the western horizon.\n'
            + 'There is, however, something of great interest here.',
        'north': 'desert06',
        'northway': 'rocky trail',
        'down': 'desert10',
        'downway': 'cave entrance, dug into gray limestone,'
    },
    'desert10': {
        'name': 'desert10',
        'desc': 'You find yourself underground within a limestone cave, a geological relic of\n'
            + 'the Pleistocene epoch. Massive boulders lie strewn about, bearing testament to\n'
            + 'the eons of geological forces at play. A trace of recent human presence is\n'
            + 'marked by the remnants of a fire pit. The cave offers a break from the scorching\n'
            + 'surface. You can climb up to get out of the cave.',        
        'south': 'cave01',
        'southway': 'dark, foreboding path',
        'up': 'desert09'
    },    

    # Cavern Rooms
    # The cave entrances "desert10" and "town01" have to be outside of the "cave"
    # otherwise the player could not see the room descriptions without a lantern.
    # Check out the code in show_room that looks for 'cave'.

    'cave01': {
        'name': 'cave01',
        'desc': 'You find yourself within a limestone chamber, its ceiling bearing the marks of\n'
            + 'countless past explorers. Your eyes are immediately drawn to a deep chasm,\n'
            + 'stretching ominously to the south.',
        'north': 'desert10',
        'south': 'cave04',
        'southway': 'bottomless pit',
        'east': 'cave02',
    },
    'cave02': {
        'name': 'cave02',
        'desc': 'You find yourself in the Big Boulder Room, navigating a labyrinth of massive\n'
            + 'rocks above and below. In the shadows, unseen eyes observe your every move as\n'
            + 'the distant murmur of running water fills your ears.',
        'south': 'cave05',
        'east': 'cave03',
        'eastway': 'narrow crevice',
        'west': 'cave01'
    },
    'cave03': {
        'name': 'cave03',
        'desc': 'Oh, what a sight! The slender crevice widens into an expansive chamber, adorned\n'
            + 'with majestic stalactites and stalagmites. A crystal-clear stream meanders through,\n'
            + 'and etched onto the wall, the words declare your discovery:\n'
            + "*** Hooray! You've uncovered the Lost River ***",
        'west': 'cave02',
        'westway': 'narrow crevice'
    },     
     'cave04': {
        'name': 'cave04',
        'desc': 'Aaaaaaaahhhhhhhhh! Plunging into the bottomless pit, your fate is sealed.\n'
            + 'Regrettably [n], your journey ends here among the bones of past explorers.',
        'end': True
    },
     'cave05': {
        'name': 'cave05',
        'desc': "Welcome to a twisty, narrow room adorned with peculiar limestone creations.\n"
            + 'The walls are coated in knobby clusters of calcites, known as cave popcorn.\n'
            + 'Hold the butter, though!',
        'north': 'cave02',
        'south': 'cave06'
    },    
    'cave06': {
        'name': 'cave06',
        'desc': "Behold, you have entered the Queen's Chamber, a regal space adorned with\n"
            + 'stalactites and cave curtains, conjuring an image of a woman with long flowing\n'
            + "hair, immersed in a watery basin. Beware, pathways around the Queen are narrow.",
        'north': 'cave05',
        'south': 'town01',
        'southway': 'narrow passageway',        
        'west': 'cave07'
    },
    'cave07': {
        'name': 'cave07',
        'desc': 'You stand within the Cave Chapel, where heavenly music sounds from above. Is it\n'
            + 'real or a trick of your mind? Unfortunately, the towering ceiling conceals the\n'
            + "source, beyond the reach of your lantern's light.",
        'south': 'cave08',        
        'east': 'cave06'
    },
    'cave08': {
        'name': 'cave08',
        'desc': "Welcome to the King's Chamber, where millennia of water's artistry through\n"
            + 'limestone has crafted a throne-like formation. It waits, empty, for the return\n'
            + 'of the King under the Mountain.',
        'north': 'cave07'
    },

    # Mojave Springs Ghost Town Lower Rooms (starting at "town01") 

    'town01': {
        'name': 'town01',
        'desc': 'This cavernous chamber dwarfs you with its size! Sunlight streams through\n'
            + 'a natural cave entrance, painting the walls in a vivid tapestry of\n'
            + 'colors. A refreshing breeze dances through, a stark contrast to the\n'
            + 'scorching heat of the desert above.',
        'north': 'cave06',
        'northway': 'narrow passageway',
        'east': 'town02',
        'eastway': 'cave entrance'
    },
    'town02': {
        'name': 'town02',
        'desc': 'You are standing atop a parched hill crowned with sagebrush. An imposing,\n'
            + '50 foot tall rock outcropping towers overhead. Fingers crossed those\n'
            + "boulders don't drop!",
        'north': 'town05',
        'northway': 'rocky trail',
        'east': 'town03',
        'eastway': 'twisty trail',
        'west': 'town01',
        'westway': 'cave entrance'
    },
     'town03': {
        'name': 'town03',
        'desc': 'Merciless heat envelopes you. You stand on a cactus-strewn hillside of\n'
            + 'rocky terrain. Off to the distant east, the haunting silhouette of a\n'
            + 'cemetery emerges.',
        'north': 'town04',
        'west': 'town02',
        'westway': 'twisty trail',
        'east': 'town06',
        'eastway': 'steep twisty trail'
    },
    'town04': {
        'name': 'town04',
        'desc': 'You find yourself standing before an abandoned silver mine, its entrance\n'
            + 'narrow but you may be able to squeeze into it. The air is stagnant, carrying\n'
            + 'a musty odor from the darkness below. In the distance a cemetery can be seen.',
        'south': 'town03',
        'west': 'town05',
        'down': 'town09',
        'downway': 'mine shaft'
    },
    'town05': {
        'name': 'town05',
        'desc': 'You stand on a rugged rocky trail, strewn with remnants of broken old,\n'
            + 'unusable mining tools along its edges. The hillside is marred with mine\n'
            + 'tailing, a testament to the labor of hundreds of silver miners from days\n'
            + 'gone by.',
        'south': 'town02',
        'southway': 'rocky trail',
        'east': 'town04'
    },
    'town06': {
        'name': 'town06',
        'desc': 'You find yourself standing west of the Mojave Springs town cemetery. A wooden\n'
            + 'split-rail fence encircles this resting place, bordered by heaps of stone.\n'
            + 'The cemetery grounds appear to host a substantial number of former townsfolk.',
        'north': 'town10',
        'northway': 'dusty road',
        'east': 'town07',
        'eastway': 'open gate',
        'west': 'town03',
        'westway': 'steep twisty trail'
    },
    'town07': {
        'name': 'town07',
        'desc': 'You are in the town cemetery. A large sign proclaims:\n\n'
            + '*** 1881 - Mojave Springs Cemetery\n'
            + '*** Here many a valiant silver miner and modern day\n'
            + '*** adventurer has found their eternal repose.\n'
            + '*** Respect where they have been laid to rest or join them.\n\n'
            + 'There are several interesting tombstones to look at.', 
        'south': 'town08',
        'southway': 'large vault',
        'west': 'town06',
        'westway': 'open gate'
    },
    'town08': {
        'name': 'town08',
        'desc': "You've stumbled upon the tombstone of Mountain Man Murphy, a rootin' tootin'\n"
            + "and not so pootin' cowboy-turned-miner, who sadly met his end due to a\n"
            + "legendary showdown with a blocked colon. A Colt revolver clings awkwardly to\n"
            + "Murphy's marker. Maybe it's his way of saying, *Take it if you dare!*",
        'north': 'town07'
    },
    'town09': {
        'name': 'town09',
        'desc': 'As you step into the mine shaft, you are greeted by frail, dilapidated\n'
            + 'wooden beams that strain under the weight of the earth above. Descending\n' 
            + 'only 20 feet, your path is halted by the remains of a cave-in.',
        'up': 'town04',
        'upway': 'mine shaft'
    },
    'town10': {
        'name': 'town10',
        'desc': 'As you walk along a dusty, rutted road going north and south, your keen eye\n'
            + 'spots a delightful array of flora. Sage, Brittlebush, Prickly Pear, and\n'
            + 'Yucca grace the roadside. A line of Juniper trees can be seen to the north.',
        'north': 'town11',
        'northway': 'dusty road',
        'south': 'town06',
        'southway': 'dusty road'
    },     
        
    
    # Mojave Springs Ghost Town Upper Rooms (starting at "town11")
    'town11': {
        'name': 'town11',
        'desc': "Greetings, weary traveler! You've arrived at the ghostly realm of Mojave\n"
            + "Springs, an old west town where tranquility reigns supreme. In fact, it's\n"
            + "so quiet you might say it's ***DEAD*** quiet. To the north, a few old\n"
            + "wooden buildings comes into view.",
        'north': 'town12',
        'northway': 'road',
        'south': 'town10',
        'southway': 'dusty road'
    },     
    'town12': {
        'name': 'town12',
        'desc': "You find yourself on what's left of Main Street, a road now overrun by\n"
            + 'stubborn weeds. Your gaze catches a glimpse of a tiny shack to the east\n'
            + 'adorned with a sign proudly proclaiming it as the "Stage Coach Stop".\n',
        'north': 'town14',
        'northway': 'road',
        'south': 'town11',
        'southway': 'road',
        'east': 'town13',
        'eastway': 'Stage Coach Stop door'
    },     
    'town13': {
        'name': 'town13',
        'desc': 'You are inside the Stage Coach shack. Here a few dusty chairs line one wall,\n'
            + 'relics of an era when horse-drawn rides to the next town were the norm.\n'
            + 'Wanted posters adorn the other wall. Wait a minute... this seems familiar!\n\n'
            + '********** [n] **********\n'
            + 'WANTED MOSTLY ALIVE $100\n'
            + 'Also $50 for Bronco Billy and Wild Sarah Peacock.\n'
            + 'Any information leading to arrest will be rewarded.\n'
            + 'Sheriff Walker\n'
            + 'December 30, 1882',
        'west': 'town12',
        'westway': 'road'
    },
    'town14': {
        'name': 'town14',
        'desc': 'You are on Main Street and to the east, a worn-out building stands before\n'
            + 'you. Oddly, it lacks windows and features only a single door. Sign says\n'
            + '"C*wb*y B*th". It is a little hard to read with the bullet holes.',
        'north': 'town16',
        'northway': 'road',
        'south': 'town12',
        'southway': 'road',
        'east': 'town15',
        'eastway': 'business door'
    },    
    'town15': {
        'name': 'town15',
        'desc': "Welcome to the famous Cowboy Bath. It's a good thing too. You're getting a\n"
            + 'tad smelly after all this adventuring! A round, cast-iron tub beckons,\n'
            + 'promising a refreshing soak. A simple sign hangs on the wall:\n\n'
            + '"Back scrub 5 cents"\n'
            + '"Full body wash 10 cents"\n\n'
            + 'At those prices it is too bad there is no water and no one\n'
            + 'available to give you a bath.',
        'west': 'town14',
        'westway': 'road'
    },
    'town16': {
        'name': 'town16',
        'desc': 'You stand at the end of Main Street. To the north is the grand Mojave\n'
            + 'Springs Bank. It may be the nicest and largest building in town but the most\n'
            + 'enticing one is to your west. Signs say\n'
            + '"The Mojave Rose Saloon" and "Good Beer - Bad Music".',
        'north': 'town18',
        'northway': 'bank',
        'south': 'town14',
        'southway': 'road',
        'west': 'town17',
        'westway': 'saloon door'
    },
    'town17': {
        'name': 'town17',
        'desc': "You step inside The Mojave Rose Saloon, once the toast of its time. Now,\n"
            + 'dust blankets the wooden bar, broken bottles, and overturned tables and\n'
            + 'chairs. Yet, remarkably, a piano and a slot machine appear to be in\n'
            + 'PLAYable condition.',
        'east': 'town16',
        'eastway': 'road'
    },
    'town18': {
        'name': 'town18',
        'desc': "You've arrived at the Mojave Springs Bank, a fine structure indeed. History\n"
            + 'is etched in attempts at robbery, as evident in the barred windows, steel\n'
            + "door and pockets of bullet holes in the stone building. To enter, you'll\n"
            + 'need a very special key to OPEN its imposing door.',
        'south': 'town16',
        'southway': 'road'
    },
    'town19': {
        'name': 'town19',
        'desc': 'You are inside the bank. Here, portraits of former bank presidents adorn the\n'
            + 'walls, including one eerily resembling President Abraham Lincoln with fiery\n'
            + 'red long hair. On the eastern wall, a solitary teller window and door\n'
            + 'command your attention.',
        'south': 'town18',
        'southway': 'door',        
        'east': 'town20',
        'eastway': 'vault door'
    },
     'town20': {
        'name': 'town20',
        'desc': 'Well done [n]!!!\n\n'
            + 'Welcome to the bank vault. Inside, riches abound — stacks of paper money\n'
            + 'and glistening gold coins.\n'
            + 'But most importantly, a note boldly declares "THE END."\n\n'
            + 'CONGRATULATIONS, YOU WIN!',
        'end': True
    },    
    
    # End Game Rooms - this is where the player goes to die
    
    'quit': {
        'name': 'quit',
        'desc': "I guess a bit of adventuring isn't for you, [n].",
        'end': True
    },
    'diedofthirst': {
        'name': 'diedofthirst',
        'desc': "As darkness envelopes your vision, the realization dawns - you're succumbing\n"
            + 'to the cruel thirst. Regret fills your heart for not finding water sooner.\n'
            + 'Farewell, Courageous [n]!',
        'end': True
    },
    'diedofsnakebite': {
        'name': 'diedofsnakebite',
        'desc': "[n]. [n]. [n]. Snake wrangling isn't your forte. As you approach, the\n"
            + 'serpent strikes swiftly, sealing your fate in a grisly demise.\n'
            + "While you missed your opportunity, the rattlesnake certainly didn't.",
        'end': True       
     },
    'diedofrevolver': {
        'name': 'diedofrevolver',
        'desc': "As you remove the Colt revolver from Mountain Man Murphy's headstone you\n"
            + 'notice one of the wire bands holding it in place was wrapped around the trigger.\n'
            + 'Unfortunately, you notice 1/4 second too late.\n'
            + 'B-A-N-G!!!\n'
            + 'A new headstone in the Mojave Springs cemetery reads:\n'
            + 'Here lies [n], once on a journey. Now gut shot and dead on a gurney.',
        'end': True       
     },    
}

# Object list - things to be used - values get changed as game progresses

# Format is object name, location, actions, can move T(rue)/F(false), description
# If an object can be manipulated by multiple commands separate them with comma (such as "look,get")
# Player inventory is indicated by a location of "player"
# The key is not shown in a location until the player drops coin

def setup_game_objects():
    
    global game_objects
    game_objects = [
        ['sign', 'desert08', 'look', 'f',
            'The aged wooden sign, weathered by a century of time says:\n'
            + "*** In the heart of the arid Mojave Desert, appearances deceive.\n"
            + "*** Beneath the surface lies a hidden abundance of water.\n"
            + '*** A journey underground shall unveil its source.'],
        ['snake', 'desert07', 'look,kill', 'f', "Yup, a Mojave Rattler, a highly venomous pit viper native to the deserts of the Southwest."],
        ['lantern', 'desertouthouse', 'get,look', 't', "It appears to be a dust-covered lantern, but behold - it's in working order!"],
        ['cabin', 'desert03', 'look', 'f', "The cabin's remains offer little beyond weathered stone walls, remnants of timber,\nand rusted beer cans."],
        ['canteen', 'cave03', 'get,look', 't', "It's a nice big canteen full of water."],
        ['sign', 'desert10', 'look', 'f',
            'A small sign, written by hand long ago, reads:\n'
            + '*** You have made it to El Copa Cave.\n'
            + "*** The way to water and Mojave Springs lies just ahead.\n"
            + "*** You'll need a lantern to find them."],
        ['sign', 'town01', 'look', 'f',
            'Someone carved a sign into the rock. It reads:\n'
            + '*** You are in El Copa Cave.\n'
            + '*** The way through the caverns and desert lies north.\n'
            + '*** Watch out for the bottomless pit.'],
        ['coin', 'cave08', 'get,look', 't', "Looks like an 1885 Morgan Silver dollar!"],
        ['key', '*', 'get,look', 't', "It is an old key that might work on a door or something like that."],
        ['sign', 'town04', 'look', 'f',
            'A very official looking sign says:\n'
            + '*** Danger! Abandoned mine. Stay out!'],
        ['revolver', 'town08', 'get,look', 't', "Looks like an 1876 Colt Single Action Army. That's worth some money!"],
        ['amulet', 'town09', 'get,look', 't', "This talisman can be used to ward off evil spirits."],
        ['tombstone', 'town07', 'look', 'f',
            'It appears the townsfolk have a sense of humor.\n\n'
            + ' *************************     ***********************     ***********************\n'
            + '** Here lies Uncle Fred  **   ** Here lies Sam Moore **   ** Here lies Miss Sue. **\n'
            + '** A rock dropped on his **   ** Four slugs from a   **   ** Slipped on a banana **\n'
            + '** head. Now he is dead. **   ** .44 and no more.    **   ** and died, who knew? **\n'
            + '**---------1884----------**   **---------1877--------**   **---------1885--------**'
        ],
        ['piano', 'town17', 'play,look', 'f', "This is a fine 1867 Baldwin. Doesn't get any better. At least in 1867 it didn't get any better."],
        ['slot', 'town17', 'play,look', 'f', "It is a three reel Liberty Bell straight from San Franciso."],
        ['ghost', 'town19', 'look,kill', 'f', "Yup, it is a 7 foot tall spirit resembling Yosemite Samuel of the netherworld."]

]

# Game_Objects reference constants
go_name = 0
go_location = 1
go_actions = 2
go_canmove = 3
go_description = 4
    
# Action Word tuple - we search this and extract the key (north, south, etc)
action_words = {
    'north': { 'go north', 'n', 'move north' },
    'south': { 'go south', 's', 'move south' },
    'east': { 'go east', 'e', 'move east' },
    'west': { 'go west', 'w', 'move west' },
    'up': { 'go up', 'u', 'climb up' },
    'down': { 'go down', 'd', 'go cave', 'enter cave', 'climb down' },
    'desc': { 'description' },
    'look': { 'read', 'view' },
    'kill': { 'attack', 'fight' },
    'get': { 'take' },
    'drop': { 'put', 'give' },
    'inventory': { 'inv' },
    'xyzzy': { 'say xyzzy' },
    'slot': { 'slots', 'game', 'slotmachine' },
    'open': { 'unlock' }
}

# Get Player Name
# We substitute [n] with the player name in room descriptions
def get_player_name():
    
    import re
    import random
    import time
    import sys

    player_name = input("What is your first name? ").strip()

    if player_name > '':
        if player_name.count(' ') > 0:
            # Get the first word if there are multiple words in input
            player_name = player_name.split(' ', 1)[0].strip()
        # Strip everything but letters using RegEx
        player_name = re.sub(r'[^a-zA-Z]', '', player_name)
        # Capitalize the first letter
        player_name = player_name.capitalize()

    if len(player_name) < 2 or len(player_name) > 10:
        # Name was too short or too long so make one up
        print("I'm not sure about that.")
        print('How about I make up a name for you?')
        # Split string into pieces. Generate random result
        name_list = 'Billie|Bertie|Purdie|Riley|Calamity|Campbell|Dusty|Jimmie|Odell|Coda'.split("|")
        player_name = name_list [random.randint(1,len(name_list)-1)]
        print(f"I'll call you \"{player_name}\".\n")
        time.sleep(2) # Sleep 2 seconds
    
    # Delay printing between each letter for the "transporting effect" :)
    delayed_text = "Transporting " + player_name + " to ..."
    for char in delayed_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)     
    
    print("\n")
    return player_name

# Reset Game Function
def reset_game():
    
    # Reset globals
    global current_room
    global movement_counter
    global water_counter
    global found_water
    global start_time

    current_room = rooms[start_room] # reset the current room position to the starting room
    movement_counter = 0 # Number of movments the player made in total
    water_counter = 25 # Number of movements the player can make before finding water
    found_water = False
    start_time = datetime.now()
    
    # Reset Game Objects to put everything back in it's place
    setup_game_objects()

# Help Function - displays help text to the player
def show_help():
    
    print("Don't worry", player_name + ", we all need a little help at times.\n")
    print("""In the world of Mojave Springs Adventure, you'll use one or two word
commands to navigate in your journey.\n
For instance, you can use "North", "South", "East", "West", "Up" or "Down"
to explore. You can also say "Go North" or to simplify further by typing "N"
instead of "North". I understand all three variants!\n
But that's not all!
Give these action commands a try:\n
attack, climb, desc, description, drop, get, give,
help, hint, inv, inventory, kill, look, moves, open, play,
put, quit, read, restart, take, unlock, view, xyzzy\n
Remember your commands control your destiny in this game so issue
them with thought, otherwise the Mojave may claim another
brave adventurer.""")

# Displays "thirsty" message
def check_water_status():
    
    if (found_water == False) and (water_counter > 0) and (water_counter < 9):
        if water_counter > 7:
            msg = 'very thirsty'
        elif water_counter > 5:
            msg = 'totally parched, can barely swallow,'
        elif water_counter > 3:
            msg = 'starting to see things that are not there'
        else:
            msg = 'dying of thirst'
        print(f'{player_name} you are {msg} and must have water in {water_counter} moves!\n')   

# Show Room Function
# Displays room description, contents and path
def show_room(room):
    
    # Get the name of the current room
    name_of_current_room = room['name']

    # Check to see if we are in the cave
    if name_of_current_room[:4] == 'cave':
        # We are in the cave. The player needs a lantern to see the room and objects.
        if check_player_inventory('lantern') == False:
            print("It's dark in here and you cannot tell which way to go. You need a lantern.")
            # Check for water
            check_water_status()
            return

    # Print room description
    print(room['desc'].replace('[n]', player_name) + '\n')
    
    # Check for water
    check_water_status()

    # Display list of objects in the room that are not on the player
    for game_object in game_objects:
        if game_object[go_location] == name_of_current_room:
            if game_object[go_name] == 'slot':
                print('You see a slot machine here.')
            else:
                print(f'You see a {game_object[go_name]} here.')

    # Display all directions the player can go
    dlist = str('')
    walkway_mod = False
    path_count = 0
    
    # Check to see if we have any "walkway" modifiers in the room and get a count of the number of potential paths
    for walk_direction in directions: # directions = ['north', 'south', 'east', 'west', 'up', 'down']
        if walk_direction in room:
            path_count += 1
            if walk_direction + 'way' in room:
                walkway_mod = True
    
    # If we have walkway modifiers or a single way out of a room, show descriptions differently
    if (walkway_mod == True) or (path_count == 1):
        # Show with each direction on a different line
        for walk_direction in directions:
            if walk_direction in room:
                if walk_direction + 'way' in room: # This checks to see if "northway", "southway" is in the room
                    walkway = room[walk_direction + 'way'] # If so, it replaces the default "path" with text in "northway"
                else:
                    walkway = 'path' # Default walkway
                if walk_direction in ['up','down']:
                    dlist += 'There is a ' + walkway + ' leading ' + walk_direction + '\n'
                else: # Used for North, South, East, West
                    dlist += 'There is a ' + walkway + ' to your ' + walk_direction + '\n'
    else:
        # Show all directions on a single line using "path" as the walkway
        for walk_direction in directions:
            if walk_direction in room:
                dlist += walk_direction + ', '
        dlist = dlist[:-2] # Trim last 2 characters from string
        dlist = 'There are paths leading: ' + dlist + '\n'
    
    # Display paths out out room
    if dlist > '':
        print(dlist)
        
# Checks to see if player has object in their inventory
def check_player_inventory(object_name):
    
    for game_object in game_objects:
        # Find the object in the array
        if (object_name == game_object[go_name]) and (game_object[go_location] == 'player'):
            # We found it
            return True
    return False

# Move objects from their current location to a new location
def move_object_to(object_name, new_location):
    
    # loop through objects to find the object to move
    for game_object in game_objects:
        if (game_object[go_name] == object_name):
            game_object[go_location] = new_location    

# Check to see if we need to block access a room otherwise return next room to move to
def check_for_room_access_blocking (name_of_current_room, next_room):
    
    if next_room == 'town20':
        # Before we can move to this room we need to make sure the ghost is gone from town19
        for game_object in game_objects:
            if game_object[go_name] == 'ghost' and game_object[go_location] == 'town19':
                print('BOO!!! The ghost moves in front of the door, blocking you.')
                print('If there was only something you could DROP to scare it away.\n')
                move_to_room = name_of_current_room # Keep player current room
            else:
                move_to_room = next_room
    else:
        move_to_room = next_room
        
    return move_to_room

# Get Action Function
# Gets text input from the player, validates it and determine what to do next
def get_action(room):

    # Get the name of the current room
    name_of_current_room = room['name']
    
    # Tell Python to use Global variable since we are modifying it
    global found_water
    global movement_counter 

    while True: # keep looping until we get a valid input

        # Clear object name
        original_action = ''
        use_object_name = ''

        action = input('>> ').lower().strip()
        move_to_room = ''

        # Make sure they enter at least 1 character
        if action == '':
            print('Try entering one or two words such as "north" or "go north" or "n" or "help".')

        else:
            # Split off object, if any
            word_list = action.split()
            if len(word_list) > 1:
                action = word_list[0].strip()
                original_action = action
                use_object_name = word_list[1].strip()
            else:
                original_action = action
                
            # Change input text to words we use in app (e.g replaces "go north" with "north")
            for key, value in action_words.items():
                if (action in value) or (action + ' ' + use_object_name in value):
                    # Update action with preferred keyword 
                    action = key
                    # Make sure we don't duplicate the action and object
                    if action == use_object_name:
                        use_object_name = ''
                    break
            
            # Special transaction of object names to make things easier
            if use_object_name in ['rattlesnake','rattle','rattler']:
                use_object_name = 'snake'
            
            # Carry out action
            if action == 'help':
                show_help()
                movement_counter -= 1 # Do not increment move counter
            elif action == 'quit':
                move_to_room = 'quit'
            elif action == 'restart':
                reset_game()
                return start_room
            elif action == 'hint':
                name_4 = name_of_current_room[:4]
                # Write big, juicy descriptions of the location along with a hint
                if name_4 == 'dese':
                    print ("""You are in the desert section.\n
The Mojave Desert, pronounced "Moh HAW vee," is a land of arid extremes. As
a desert wanderer, caution is your closest companion. Keep a vigilant eye
for rattlesnakes, chart your course carefully, and always look for water!
Whispers speak of hidden underground springs and rivers. If you encounter
an item on your journey, be sure to "get" it.""") 
                elif name_4 == 'cave':
                    print ("""You are in the cavern section.\n
The caverns offer a much-needed respite from the scorching desert above.
A reliable source of light is needed when exploring the dark
underground labyrinth. Legends of silver miners speak of crystal-clear
rivers, a subterranean monarch, and his queen.\n
While most treasures have vanished with time, meticulous searching may
reveal something worth claiming with the "get" command.\n
Venture through the caverns to uncover the fabled town of Mojave Springs.""") 
                elif name_4 == 'town':
                    print ("""You are in the town section.\n
Greetings! You now stand within or near the legendary ghost town of Mojave
Springs. In days of old, it bustled with silver miners, shopkeepers, and
raucous barroom brawlers. Though they've faded into history, their spirits
may still linger. Seeking riches? The bank holds the key and a specific item
unlocks its door. Remember, claim only what's rightfully yours!""") 
                else:
                    print ("Try again later. I'm busy at the moment.")
            elif action == 'desc':
                show_room(room)
            elif action == 'xyzzy':
                print('You really think this is Colossal Cave? You transport... nowhere.')
            elif action == 'moves':
                print('So far you made', movement_counter, 'moves.')
                movement_counter -= 1
            elif action == 'inventory':
                # To show a player inventory loop through the item list
                inv_list = '' 
                for i in range(len(game_objects)):
                    if (game_objects[i][go_location] == 'player'):
                        inv_list = inv_list + game_objects[i][go_name] + ', '
                if inv_list == '':
                    print("You don't have any items in your inventory yet.")
                else:
                    # trim off the trailing ", " before printing
                    print("You have these items:", inv_list[:-2])
                    
            elif action == 'open':
                if name_of_current_room == 'town18':
                    if check_player_inventory('key') == True:
                        print("Nice work! You were able to unlock the door with the key.\n")
                        return 'town19'
                    else:
                        print('The key to breaking into banks is to have a key.')
                else:
                     print('Sorry, you cannot do that.')
                
            elif action == 'look':
                if (original_action == 'look') and (use_object_name == ''):
                    # First show the room description again
                    print("Let's take a look around:")
                    print('-------------------------')
                    show_room(room)                

                # See if we have an object in the room that we can look/read
                found_object = False 
                # Loop through all objects in the room
                for game_object in game_objects:
                    # Find the room in the array
                    if game_object[go_location] == name_of_current_room:
                        # Make sure we are checking the correct object in the room
                        if (action in game_object[go_actions]) and (use_object_name == '' or use_object_name == game_object[go_name]):
                            # We found something to look at
                            if use_object_name == '':
                                # If player did not provide a name to look at print name, repeated dash characters and description
                                dash = '-' * (len(game_object[go_name])) + '-'
                                print(f'{game_object[go_name].capitalize()}:\n{dash}\n{game_object[go_description]}')
                            else:
                                # If name provided just print description
                                print(game_object[go_description])
                            found_object = True

                # Since we didn't find the object in the room, try the player inventory
                if not found_object:
                    for game_object in game_objects:
                        # Find the object in the array
                        if (use_object_name == game_object[go_name]) and (game_object[go_location] == 'player'):                   
                            print(game_object[go_description])
                            found_object = True

                if not found_object and use_object_name != '':
                    print(f'I am confused. {use_object_name.capitalize()}?')
                    
            elif action == 'get':
                found_object = False
                # Check to see if the player already has the object (assuming object name is available)
                if use_object_name > '':
                    if check_player_inventory(use_object_name) == True:
                        print('You already have that item.\n')
                        return name_of_current_room
                # Loop through all objects in the room
                for game_object in game_objects:
                    # Find the room in the array
                    if game_object[go_location] == name_of_current_room:
                        # Make sure we are checking the correct object in the room
                        if (action in game_object[go_actions]) and (use_object_name == '' or use_object_name == game_object[go_name]):
                            # We found something to get
                            # Make sure we can get it
                            if game_object[go_canmove] == 't':
                                # If player tries to take revolver it fails
                                if game_object[go_name] == 'revolver':
                                    move_to_room = 'diedofrevolver'
                                    return move_to_room
                                # Assign object to player
                                game_object[go_location] = 'player'
                                print('You got the', game_object[go_name])
                                found_object = True
                                # Certain objects have special properties
                                if game_object[go_name] == 'canteen':
                                    print('That water tastes mighty good!')
                                    found_water = True                                    
                                break
                if not found_object:
                    print("Sorry, that is not possible.")
            
            elif action == 'drop':
                if use_object_name == '':
                    # Player did not specify what to drop
                    print("I have no idea. Say something like DROP LANTERN.")
                else:
                    found_object = False 
                    # Loop through all objects             
                    for i in range(len(game_objects)):
                        if (game_objects[i][go_location] == 'player'):
                            # Make to see if the player is referencing that object
                            if use_object_name == game_objects[i][go_name]:
                                # We got it so place the object in the room
                                game_objects[i][go_location] = name_of_current_room
                                print('You dropped the', game_objects[i][go_name])
                                if use_object_name == 'amulet' and name_of_current_room == 'town19':
                                    print("Well, I'll be ... it worked! The ghost promptly disappears.")
                                    # Hide to ghost to never reappear
                                    move_object_to('ghost', '*')
                                found_object = True
                    if not found_object:
                        print("Can't do. I don't think you have a", use_object_name + '.')
                
            elif action == 'kill':
                if use_object_name == '':
                    # Player did not specify what to kill
                    print("I have no idea. Give me a hint what you want to kill.")
                else:                
                    # Make sure we have something in the room that can be killed
                    found_object = False
                    # Loop through all objects in the room
                    for game_object in game_objects:
                        # Find the room in the array
                        if game_object[go_location] == name_of_current_room:
                            # Make sure we are checking the correct object in the room
                            if (action in game_object[go_actions]) and (use_object_name == game_object[go_name]):
                                # We found something that might be killed
                                if use_object_name == 'snake':
                                    return 'diedofsnakebite' # moves to this room
                                elif use_object_name == 'ghost':
                                    print('Duh! The ghost is already dead.\n')
                                    return name_of_current_room
                                # If it is not a snake then just flag we found an object
                                found_object = True
                                break
                    if found_object:
                        print("You can't kill it now.")
                    else:
                        print("Violent tendancies? I don't see anything that merits that response.")
            
            elif action == 'play':
                if use_object_name == '':
                    # Player did not specify what to play
                    print("Try PLAY (item) if you want to play something.")
                else:                
                    # Make sure we have something in the room that can be killed
                    found_object = False
                    # Loop through all objects in the room
                    for game_object in game_objects:
                        # Find the room in the array
                        if game_object[go_location] == name_of_current_room:
                            # Make sure we are checking the correct object in the room
                            if (action in game_object[go_actions]) and (use_object_name == game_object[go_name]):
                                # We found something that might be played
                                if use_object_name == 'piano':
                                    print('As you start to play "Red River Valley" and belt out some rough lyrics\n'
                                          + '"From this valley they say you are goin\'..."\n\n'
                                          + 'You quickly realize you could not carry a tune in a bucket.\n'
                                          + 'That is, if you had a bucket. Which you do not.'
                                          )
                                elif use_object_name == 'slot':
                                    if check_player_inventory('coin') == True:
                                        print('You pull out that Morgan Silver Dollar in your pocket and take a big gamble.\n'
                                            + 'Dropping it into the coin slot, reels are spinning! As they slow\n'
                                            + 'three KEY pictures show in the dusty slot machine window. YOU WIN!\n'
                                            + 'Out pops a key, landing on the floor.'
                                            )
                                        # Hide coin, Show key
                                        move_object_to('coin', '*')
                                        move_object_to('key', name_of_current_room)
                                    else:
                                        print("Nothin' is free in Mojave Springs. You'll need some coin to play.")
                                # Flag we found an object
                                found_object = True
                                break
                    if not found_object:
                        print("I don't see anything that you can play.")
                    
            else:
                # Process movement
                trying_to_move = False
                for move_direction in directions: # Directions is a list NSEWUD
                    if action == move_direction:
                        trying_to_move = True
                        # Check to see if we can move in the direction
                        if move_direction in room:
                            # The check_for_... function returns the room the player is to move to
                            # It also displays messages and blocks access to rooms based on object locations
                            move_to_room = check_for_room_access_blocking (name_of_current_room, room[action])
                            break
                        
                if len(move_to_room) == 0:
                    if trying_to_move == True:
                        print('You cannot go in that direction.')
                    else:
                        # This message appears if the player entered a command that does not exist, such as "eat snake"
                        print('Not sure what you want to do. Type "help" for help.')

        # Increment movement counter
        movement_counter += 1

        # If move_to_room is not empty
        if len(move_to_room) > 0:
            if found_water == False:
                global water_counter # Tell Python to use Global variable
                water_counter -= 1
                if water_counter < 1:
                    move_to_room = 'diedofthirst'

            return move_to_room 

        print('\n')

# Start Game
player_name = get_player_name()
reset_game()

# Stay in main loop until we hit an 'end'
while 'end' not in current_room:
    show_room(current_room)
    next_room = get_action(current_room)
    current_room = rooms[next_room]

# We are done with main loop - show final room description
print(current_room['desc'].replace('[n]', player_name))        

# Finish up
# Calculate the elapsed time in seconds
ts = int((datetime.now() - start_time).total_seconds())
# Convert seconds to minutes and seconds
t_min, t_sec = divmod(ts, 60)

if t_min > 0:
    game_time = f'{t_min} minutes and {t_sec} seconds.'
else:
    game_time = f'{t_sec} seconds.'

print(f'\nYou played for {movement_counter} moves in {game_time}')

we_are_done = input('\nBye [[[Press Enter key]]] ')


# The End
# ===========================================================================
# Mojave Springs Adventure is not intended to be a full-blown adventure game. 
# I wrote it in about 40 hours (design, code) to get an understanding of Python.
# Following review by the first players I used ChatGPT to augment text
# to make the room and object descriptions more verbose and added "Hints".
# Changes took another 10 hours or so.

# Certainly, the game script could be enhanced and the code improved.
# That's where you come in.
# Learn from it, tear it apart, fix my coding faux pas, do with it whatever.

# Here are some ideas while still keeping this a terminal app:

# 1) Move room and object descriptions to a file or database
# 2) Enhance the action word parser - add language processing ability
# 3) Add puzzles the player can solve vs simply wandering around
# 4) Add NPCs (Non Player Characters) the player can interact with
# 5) Add a combat system so you can fight the snake or NPCs
# 6) Add a scoring system
# 7) Translate to other languages, Spanish and German :)

# Most of all have fun
