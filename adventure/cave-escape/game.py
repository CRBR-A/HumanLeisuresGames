# file: text_game.py
# description: text game
# authors: Jacob Bickle, Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
    12/03/2017

    * Fixed bug in equip function, if player pressed enter without any arguments the
    game would crash

    * Fixed reprinting of action list in combat function. the for loop needed an elif
    statement

    *Map is now fully dynamic! The map will update the current room title to 'player'
    as well as 'XXXXX' any undiscovered rooms. Rooms that are adjoining the players
    room are added to the discovered_rooms attribute.

    *moved map to a separate map.txt file, this made parsing the map a whole lot easier.

    * Reduced bear health by 50.

    * Increased the accuracy of all player weapons by 5

"""
import csv
import textwrap
import time

from random import randint


class Players:
    """Initializes player class with attributes"""

    player_objects = []

    def __init__(self, name='', health=100, dignity=1):
        self.name = name
        self.health = health
        self.equipped_weapon = None
        self.inventory = Players.initialize_inventory(name)
        self.equipped_weapon = self.inventory[0]
        self.dignity = dignity
        self.current_room = None
        self.player_objects.append(self)
        self.discovered_rooms = []

    def read_inventory(self):
        print("\nInventory:\n====================")
        for item in self.inventory:
            print(item.name.capitalize(), 'x', item.uses)
        print("====================\n")

    def add_item(self, item):
        if item.name in [i.name for i in self.inventory]:
            player_item = [i for i in self.inventory if item.name == i.name]
            player_item[0].uses += 1
        else:
            self.inventory.append(item)
            if item in Weapons.weapon_objects:
                self.equip_weapon(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def equip_weapon(self, item):
        print("\nEquip {}? (yes or no)".format(item.name))
        opt = input(">  ")
        if opt.lower() in ('y', 'yes'):
            self.equipped_weapon = item
            print("You equipped {}!\n".format(item.name))
        else:
            print("\n{} remains unequipped.".format(item.name))

    def combat(self, enemy):
        action_list = ['fight', 'use', 'equip', 'run', 'inventory', 'cry']
        player = Players.get_player('player')

        print("\nYou entered combat with {}.".format(enemy.name))
        # get_graphics('art.txt', enemy.name)
        time.sleep(1)

        while self.health > 0 and enemy.health > 0:
            print("\nActions:")
            for action in action_list:
                if action == 'use' or action == 'equip':
                    print('\t' + action.capitalize(), '(item)')
                elif action == "fight":
                    print('\t' + action.capitalize(),
                          "(Current Weapon: "
                          + (player.equipped_weapon).name.capitalize() + ')')
                else:
                    print('\t' + action.capitalize())
            opt = get_input("\n>  ", self.current_room, action_list)
            if opt[0] == 'run':
                if self.run_away(enemy) == True:
                    self.current_room.next_room(self.current_room.branches[0])
                    break
            elif opt[0] == "cry":
                print(
                    "Your fear overwhelms you. You sit down and cry. Crying gets you nowhere.")
                player.dignity = 0
            elif opt[0] == 'inventory':
                action = Actions(opt[0], opt[1:])
                action.run_action()
            else:
                action = Actions(opt[0], opt[1:])
                action.run_action()
                enemy.enemy_turn()

        if self.health > 0 and enemy.health <= 0:
            print("\nCongratulations! You defeated {}".format(enemy.name))
            loot = enemy.inventory[randint(1, len(enemy.inventory) - 1)]
            time.sleep(1)
            print("{} dropped a {}. You picked it up.".format(
                enemy.name, loot.name))
            self.add_item(loot)
            self.current_room.enemies = None
            self.current_room.events = 'None'
            Players.player_objects.remove(enemy)
            del enemy
            self.current_room.enter_room()
        if self.health <= 0:
            print("\nYou were deafeated by {}".format(enemy.name))
            death("GAME OVER")

    @staticmethod
    def run_away(enemy):
        # Must roll above an 85 to run away
        print("Running away!. . . .")
        time.sleep(1)
        if randint(1, 100) > 85:
            print("\nYou ran away!")
            time.sleep(1)
            return True
        else:
            print("\nYou failed to run away!")
            time.sleep(1)
            enemy.enemy_turn()
            return False

    @classmethod
    def get_player(cls, name):
        for p in cls.player_objects:
            if name == p.name:
                return p

    @classmethod
    def initialize_inventory(cls, name):
        item_list = parse_file('data.txt', name, '*player_inventory')
        inventory = []
        for i in item_list:
            i = eval_item(i)
            inventory.append(i)
        return inventory


class Enemy(Players):
    """Creates enemy object for use in story"""

    def __init__(self, name='', health=100, dignity=1):
        super().__init__(name, health)

    def enemy_turn(self):
        if self.health <= 0:  # Prevents enemy from taking another turn after killed
            print("\nThe {} was defeated!".format(self.name))
        else:
            player = Players.get_player('player')
            weapon = self.equipped_weapon
            accuracy_roll = weapon.acc + randint(1, 100)
            print("\n{}'s turn!. . . . ".format(self.name), end='')
            time.sleep(2)
            # Add a roll to for enemy to run away
            print("\nThe {} attacks!".format(self.name))
            time.sleep(1)
            if accuracy_roll > 100:
                if accuracy_roll > 85 + weapon.acc:
                    print("\nCritical hit!!! The {} hit you for {} damage".format(
                        self.name, int(weapon.dmg * 1.5)))
                    player.health -= int(weapon.dmg * 1.5)
                else:
                    damage_roll = weapon.dmg + randint(-5, 5)
                    print("\nOuch! The {} hit you for {} damage".format(
                        self.name, damage_roll))
                    player.health -= damage_roll
            else:
                print("\nYou nimbly dodge out of the way!")
            time.sleep(1)
            print("You have {}/100 health remaining".format(player.health))


class Room:
    """Initializes room object, attributes are pulled from text file"""

    room_objects = []

    def __init__(self, room_title=''):
        keywords = ['*room_descriptions', '*room_branches', '*room_count',
                    '*room_events', '*room_items', '*room_actions',
                    '*room_lock_description', '*room_enemies', "*room_examinations"]
        attributes = [parse_file('data.txt', room_title, target)
                      for target in keywords]
        self.name = room_title
        self.description = attributes[0]  # list of descriptions
        self.branches = attributes[1]   # list of branches
        self.counter = int(attributes[2][0])  # int
        self.events = attributes[3][0]  # string
        self.items = [eval_item(name) for name in attributes[4]]  # list comp
        self.actions = attributes[5]  # list
        self.lock_description = attributes[6]  # list
        if attributes[7][0] == 'None':  # Prevents game from using Nonetype to make
            self.enemies = None         # enemies
        else:
            self.enemies = Enemy(
                name=attributes[7][0], health=int(attributes[7][1]))
        self.room_examination = attributes[8]  # list
        self.room_objects.append(self)

    def enter_room(self):
        player = Players.get_player('player')
        player.current_room = self
        player.discovered_rooms.append(self.name)
        player.discovered_rooms += player.current_room.branches

        if self.lock_description[0] == 'True':
            load_map('map.txt')
            print('\n\n' + textwrap.fill(
                self.description[int(self.lock_description[1])]))
        else:
            if self.events == 'None':
                load_map('map.txt')
            try:
                print('\n\n' + textwrap.fill(self.description[self.counter]))
            except IndexError:
                print('\n\n' + textwrap.fill(self.description[-1]))
            self.increment_counter()
            eval(self.events)

    def encounter(self):
        player = Players.get_player('player')
        player.combat(self.enemies)

    def next_room(self, room_title=''):
        room = Room.get_room(room_title)
        room.enter_room()

    def increment_counter(self):
        self.counter += 1

    def keypad(self):
        player = Players.get_player("player")
        code = "6824"
        while player.health > 0:
            player_attempt = input(
                "Enter code (type \"back\" to back out): ")
            if player_attempt == code:
                self.next_room('secret')
                break
            elif player_attempt.lower() == "back":
                self.next_room(self.branches[0])
                break
            elif player_attempt.isnumeric():
                print(
                    "\nYouch! That felt just about as good as an electrical"
                    " shock shooting throughout your body could.")
                player.health -= 25
            else:
                print("\nThe keypad lets out a quizical beep. (Invalid input)")
        if player.health <= 0:
            print("\nThat was stupid, death by keypad")
            death("GAME OVER")

    def aztec_statue(self):  # Special endgame scenario
        # get_graphics('art.txt', 'statue')
        while True:
            choice = input("\nDo you take the statue? (yes or no)\n>  ")
            if choice in ('y', 'yes'):
                print("You slowly, and carefully swap the statue with your phone.")
                time.sleep(2)
                print(
                    "You're holding the most prized posestion. But you still need the phone!")
                time.sleep(2)
                print("You hear a click. The walls shoot poison darts at you."
                      "\nYour greed was the death of you.")
                death("GAME OVER")
            elif choice in ('n', 'no'):
                print("\nYour instinct yells at you to back away from the statue."
                      "\nYou back away slowly and return to the LAB.")
                self.next_room('lab')
                break
            else:
                print("Sorry, I don't understand. Type 'Yes' or 'No'")

    @classmethod
    def get_room(cls, name):
        for r in cls.room_objects:
            if name == r.name:
                return r


class Actions:
    """creates object with users string to run a function"""

    def __init__(self, verb="", *args):
        self.verb = verb
        self.args = [arg for a in args for arg in a]

    def run_action(self):
        eval('self.' + self.verb + '()')

    def help(self):
        player = Players.get_player('player')
        special_actions = player.current_room.actions[0]
        print(textwrap.dedent(
            """
            Here is a list of commands:
            ==================================================

            goto <location>: Moves you to the next room.
            examine <item or room>: Inspect an item.
            use <item>: Use an item.
            pickup <item>: Pick up an item in the current room.
            inventory: Display all items in your inventory.
            equip <weapon>: Equip a weapon.
            status: Provides general information about you and the current room.
            map: Displays map
            quit: Quit the game.

            ==================================================

            Special commands for this room: {}
            """.format(special_actions)))

    def status(self):
        player = Players.get_player('player')
        weapon = player.equipped_weapon
        room = player.current_room
        try:
            items = [i.name for i in room.items]
        except AttributeError:
            items = ['None']
        print(textwrap.dedent(
            """
            STATUS:
            ==============================
            HEALTH:          {}/100
            EQUIPPED WEAPON: {} DMG:{}  ACC:{}
            CURRENT ROOM:    {}
            ROOM ACTIONS:    {}
            ROOM BRANCHES:   {}
            ROOM ITEMS:      {}
            """.format(player.health, weapon.name.capitalize(), weapon.dmg,
                       weapon.acc, room.name.capitalize(), room.actions,
                       room.branches, items)))

    def goto(self):
        player = Players.get_player('player')
        current_room = player.current_room
        if len(self.args) == 0:
            print("Go where?")
        else:
            if self.args[0] in current_room.branches:
                current_room.next_room(self.args[0])
            else:
                print("\n{} isn't an option".format(self.args[0]))

    def drink(self):
        try:
            if self.args[0] == 'water':
                print("\nYou drink the water, and immediately feel nauseous.")
                time.sleep(2)
                print("\nYou pass out and die.")
                death("GAME OVER")
            else:
                print("\nI don't understand drink '{}'".format(self.args[0]))
        except IndexError:
            print("\n Drink what?")

    @staticmethod
    def inventory():
        player = Players.get_player('player')
        player.read_inventory()

    def equip(self):
        player = Players.get_player('player')
        try:
            if self.args[0] not in [i.name for i in player.inventory]:
                print("\nThere is no {} to equip".format(self.args[0]))
            else:
                item = Items.get_item(self.args[0])
                if item == player.equipped_weapon:
                    print("\n{} is already equipped.".format(item.name))
                elif item not in Weapons.weapon_objects:
                    print("\nYou can't equip {}".format(item.name))
                else:
                    player.equip_weapon(item)
        except IndexError:
            print("\nEquip what?")

    def pet(self):
        player = Players.get_player('player')
        enemy = player.current_room.enemies
        try:
            print(textwrap.dedent("""
                The {0} is taken aback by your friendly gesture.
                You scratch him behind the ears, he loves it and decides to be your friend.
                The {0} leaves you in peace.
                """.format(enemy.name)))
            enemy.health = 0
            time.sleep(2)
        except AttributeError:
            print("There is nothing to pet.")

    def pickup(self):
        try:
            item_name = self.args[0]
        except IndexError:
            print("\nYou didn't specify what to pickup!")
            return None
        player = Players.get_player('player')
        current_room = player.current_room
        try:
            if item_name not in [i.name for i in current_room.items]:
                print("\nSorry, there is no {} here".format(item_name))
            else:
                room_item = [
                    i for i in current_room.items if item_name == i.name]
                if item_name in [i.name for i in player.inventory]:
                    print("\nYou picked up {}!".format(item_name))
                    item = [i for i in player.inventory if item_name == i.name]
                    item[0].uses += 1
                    current_room.items.remove(room_item[0])
                elif room_item[0].pickup == 'False':
                    print("\n{} cannot be picked up.".format(item_name))
                else:
                    print("\nYou picked up {}!".format(item_name))
                    player.add_item(room_item[0])
                    current_room.items.remove(room_item[0])
        except AttributeError:
            print("\nSorry, there is no {} here".format(item_name))

    def examine(self):
        if len(self.args) == 0:
            print("Examine what?")
        else:
            item_name = self.args[0]
            player = Players.get_player('player')
            current_room = player.current_room
            examination = current_room.room_examination[0]
            try:
                room_items = [i.name for i in current_room.items]
            except AttributeError:
                room_items = []
            if item_name in [i.name for i in player.inventory]:
                item = Items.get_item(item_name)
                item.examine_item()
            elif item_name == 'room':
                if current_room.lock_description[0] == 'True':
                    print('\n' + textwrap.fill(
                        current_room.description[int(current_room.lock_description[1])]))
                else:
                    print("\n" + textwrap.fill(examination))
            elif item_name in room_items:
                item = Items.get_item(item_name)
                item.examine_item()

            else:
                print("\nYou can't examine {}".format(item_name))

    def use(self):
        try:
            item_name = self.args[0]
            player = Players.get_player('player')
            if item_name in [i.name for i in player.inventory]:
                item = [i for i in player.inventory if item_name == i.name]
                item[0].use_item()
            else:
                print("\nThere is no {} to use".format(item_name))
        except IndexError:
            print("\nUse what?")

    def map(self):
        load_map('map.txt')

    def fight(self):
        # Grab needed objects
        player = Players.get_player('player')
        enemy = player.current_room.enemies
        weapon = player.equipped_weapon
        # Execute combat actions
        # Takes weapon accuracy from .txt file and adds a number 1-100 to it.
        accuracy_roll = weapon.acc + randint(1, 100)
        print("You attack!. . . .")
        time.sleep(1.5)
        if accuracy_roll > 100:
            if accuracy_roll > 85 + weapon.acc:
                print("\nCritical hit!!! You hit {} for {} damage"
                      .format(enemy.name, int(weapon.dmg * 1.5)))
                enemy.health -= int(weapon.dmg * 1.5)
            else:
                damage_roll = weapon.dmg + randint(-5, 5)
                print("\nYou hit {} for {} damage".format(
                    enemy.name, damage_roll))
                enemy.health -= damage_roll
        else:
            print("\nYour attack misses!")
        print("{} has {} health remaining".format(enemy.name, enemy.health))
        time.sleep(1)

    def quit(self):
        print("\nAre you sure you want to quit? Nothing will be saved. (yes or no)")
        opt = input(">  ").lower()
        if opt in ('y', 'yes'):  # This prevents use from typing 'you' or any word
            quit()               # with 'y' and quitting the game.
        else:
            print("Returning to game.")


class Items:
    """Creates item object for use"""

    item_objects = []

    def __init__(self, item_name="", attributes=[]):
        self.name = item_name
        self.uses = int(attributes[0])
        self.func = attributes[1]
        self.pickup = attributes[2]
        self.description = attributes[-1]
        self.item_objects.append(self)

    def examine_item(self):
        print('\n' + self.description)

    def use_item(self):
        if self.uses > 0 and self.func != 'None':
            eval('self.' + self.func)
        else:
            print("\nYou can't use {} here".format(self.name))

    def decrement_uses(self):
        player = Players.get_player('player')
        self.uses -= 1
        if self.uses == 0:
            player.remove_item(self)
            self.item_objects.remove(self)
            del self

    def heal(self):
        player = Players.get_player('player')
        if player.health == 100:
            print("\nYou're not injured.")
        else:
            player.health += 40
            if player.health > 100:
                player.health = 100
            self.decrement_uses()
            print("\nYou healed yourself. You have {}/100 health".format(
                player.health))

    def light(self):
        player = Players.get_player('player')
        current_room = player.current_room
        if current_room.lock_description[0] == 'True':
            current_room.lock_description[0] = 'False'
            print("\nYou lit your {}".format(self.name))
            time.sleep(1)
            self.decrement_uses()
            current_room.counter = 1
            current_room.enter_room()
        else:
            print("\nYou can't use that here")

    def beartrap(self):
        player = Players.get_player("player")
        current_room = player.current_room
        enemy = current_room.enemies
        if enemy == None:
            print("\nYou can't use that here. Try to use this in combat")
        else:
            print("\nYou quickly set the trap in front of you.")
            print("You yell at the {}, baiting it to attack you.".format(enemy.name))
            time.sleep(2)
            print("\nThe {0} takes the bait! it jumps for your throat!"
                  "\nYou dodge at the last moment forcing the {0} to land on the trap"
                  "\n\n{0} takes 100 damage!!".format(enemy.name))
            time.sleep(2)
            enemy.health -= 100
            self.decrement_uses()

    def speargun(self):
        player = Players.get_player("player")
        current_room = player.current_room
        enemy = current_room.enemies
        if enemy == None:
            print("\nYou can't use that here. Try to use this in combat")
        else:
            print("\nYou pull out your speargun and take aim!")
            time.sleep(2)
            if randint(1, 100) > 65:
                print("\nYour aim is true! The spear is fired and lodged directly in"
                      "\nthe {}'s chest.".format(enemy.name))
                time.sleep(2)
                enemy.health -= 100
                self.decrement_uses()
            else:
                print("Your nerves get the better of you and you shoot far left."
                      "\nThe spear flies past the {} and crashes into the wall.".format(enemy.name))
                self.decrement_uses()
    # Should be outside of Items class.

    @staticmethod
    def victory():
        player = Players.get_player('player')
        if player.dignity == 0:
            victory = parse_file(
                "data.txt", "no_dignity", "*victory_sequence")
            for v in victory:
                print('\n' + textwrap.fill(v))
                time.sleep(4)
            # get_graphics('art.txt', 'no_dignity')
        else:
            victory = parse_file(
                "data.txt", 'cellphone', '*victory_sequence')
            for v in victory:
                print('\n' + textwrap.fill(v))
                time.sleep(4)
            # get_graphics('art.txt', 'victory')
        quit()

    @classmethod
    def get_item(cls, name):
        for i in cls.item_objects:
            if name == i.name:
                return i


class Weapons(Items):
    """Creates weapons class, inherits from Items"""

    weapon_objects = []

    def __init__(self, item_name="", attributes=[]):
        super().__init__(item_name, attributes)
        self.dmg = int(attributes[3])
        self.acc = int(attributes[4])
        self.weapon_objects.append(self)


def get_input(prompt, current_room, option_list):
    try:
        action_list = option_list + current_room.actions
    except AttributeError:
        action_list = option_list
    while True:
        choice = input(prompt).split()
        try:
            if choice[0].lower() in action_list:
                choice = [s.lower() for s in choice]
                return choice
            else:
                print("\nSorry, I didn't understand. Type 'help' for help")
        except IndexError:
            print("\nSorry, I didn't understand. Type 'help' for help")


def create_game_world(filename):
    rooms = parse_file(filename, 'survival_game', '*rooms')
    for r in rooms:
        Room(r)


def eval_item(name):
    if name == 'None':
        return None
    else:
        attributes = parse_file('data.txt', name, '*items')
        if attributes == None:
            attributes = parse_file(
                'data.txt', name, '*weapons')
            return Weapons(name, attributes)
        else:
            return Items(name, attributes)


def parse_file(filename, key, target):
    descriptions = {}
    with open(filename, 'r') as f:
        file = csv.reader(f, delimiter='|')
        for i, row in enumerate(file):
            if target in row:
                start = i + 2
        f.seek(0, 0)
        for i, row in enumerate(file):
            if i >= start:
                try:
                    descriptions[row[0]] = [s.strip() for s in row[1:]]
                except IndexError:
                    break
        try:
            return descriptions[key]
        except KeyError:
            return None


def load_map(filename):
    player = Players.get_player('player')
    rooms = set(player.discovered_rooms)
    with open(filename, 'r') as f:
        file = [line.split('|') for line in f.readlines()]
        for line in file:
            for element in line:
                if element.strip().lower() not in rooms:
                    line[line.index(element)] = ''.join(
                        [c if not c.isalnum() else ' ' for c in element])
                elif element.strip().lower() == player.current_room.name:
                    line[line.index(element)] = 'PLAYER' + \
                        ' ' * (len(element) - 6)
        print()
        for line in file:
            print('|'.join(line), end='')
            time.sleep(.04)


def readme(filename):
    with open(filename, 'r') as f:
        file = f.read()
        print(file)
    input("Press enter to continue\n>  ")


def get_graphics(filename, target):
    with open(filename, 'r') as f:
        file = f.readlines()
        print_line = False
        for line in file:
            if target in line:
                print_line = not print_line
            elif print_line == True:
                print(line, end='')


def death(message):
    print(message)
    # get_graphics('art.txt', 'death')
    quit()


def main():
    # Initializes game world
    readme('readme.txt')
    create_game_world('data.txt')
    player = Players('player')
    player.current_room = Room.get_room('hole')
    player.current_room.enter_room()
    action_list = ['goto', 'pickup', 'examine',
                   'use', 'help', 'inventory', 'equip', 'status', 'quit', "map"]

    # Actual game loop
    while player.health > 0:
        opt = get_input(">  ", player.current_room, action_list)
        player_input = Actions(opt[0], opt[1:])
        player_input.run_action()


main()
