import random
import os
import platform

# Dictionary of racial ability score increases
racabinc = dict()
# {"Strength": , "Dexterity": , "Constitution": ,
# "Intelligence": , "Wisdom": , "Charisma": }
racabinc["Human"] = {"Strength": 1, "Dexterity": 1, "Constitution": 1,
 "Intelligence": 1, "Wisdom": 1, "Charisma": 1}
racabinc["Hill Dwarf"] = {"Strength": 0, "Dexterity": 0, "Constitution": 2,
 "Intelligence": 0, "Wisdom": 1, "Charisma": 0}
racabinc["Mountain Dwarf"] = {"Strength": 2, "Dexterity": 0, "Constitution": 2,
 "Intelligence": 0, "Wisdom": 0, "Charisma": 0}
racabinc["High Elf"] = {"Strength": 0, "Dexterity": 2, "Constitution": 0,
 "Intelligence": 1, "Wisdom": 0, "Charisma": 0}
racabinc["Wood Elf"] = {"Strength": 0, "Dexterity": 2, "Constitution": 0,
 "Intelligence": 0, "Wisdom": 1, "Charisma": 0}
racabinc["Drow"] = {"Strength": 0, "Dexterity": 2, "Constitution": 0,
 "Intelligence": 0, "Wisdom": 0, "Charisma": 1}
racabinc["Lightfoot Halfling"] = {"Strength": 0, "Dexterity": 2,                               
 "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 1}
racabinc["Stout Halfling"] = {"Strength": 0, "Dexterity": 2,                               
 "Constitution": 1, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}
racabinc["Dragonborn"] = {"Strength": 2, "Dexterity": 0, "Constitution": 0,
 "Intelligence": 0, "Wisdom": 0, "Charisma": 1}
racabinc["Forest Gnome"] = {"Strength": 0, "Dexterity": 1, "Constitution": 0,
 "Intelligence": 2, "Wisdom": 0, "Charisma": 0}
racabinc["Rock Gnome"] = {"Strength": 0, "Dexterity": 0, "Constitution": 1,
 "Intelligence": 2, "Wisdom": 0, "Charisma": 0}
racabinc["Half-Elf"] = {"Strength": 0, "Dexterity": 0, "Constitution": 0,
 "Intelligence": 0, "Wisdom": 0, "Charisma": 2}
racabinc["Half-Orc"] = {"Strength": 2, "Dexterity": 0, "Constitution": 1,
 "Intelligence": 0, "Wisdom": 0, "Charisma": 0}
racabinc["Tiefling"] = {"Strength": 0, "Dexterity": 0, "Constitution": 0,
 "Intelligence": 1, "Wisdom": 0, "Charisma": 2}
# Races with one extra hit point per level
race_with_extra_hp_per_level = {"Hill Dwarf"}
# Proficiencies by race
raceprof = dict()
raceprof["Hill Dwarf"] = {'battleaxe', 'handaxe', 'throwing hammer',
                          'warhammer'}
raceprof["Mountain Dwarf"] = {'battleaxe', 'handaxe', 'throwing hammer',
                          'warhammer', 'light armor', 'medium armor'}
raceprof["High Elf"] = {'longsword', 'shortsword', 'shortbow', 'longbow',
                        'Perception'}
raceprof["Wood Elf"] = {'longsword', 'shortsword', 'shortbow', 'longbow',
                        'Perception'}
raceprof["Drow"] = {'rapier', 'shortsword', 'hand crossbow', 'Perception'}
raceprof["Half-Orc"] = {'Intimidation'}
raceprof["Rock Gnome"] = {"Tinker's tools"}

# Sets of tools and weapons
artisantools = {"Alchemist's supplies", "Brewer's supplies",
                "Calligrapher's supplies", "Carpenter's tools",
                "Cartographer's tools", "Cobbler's tools", "Cook's utensils",
                "Glassblower's tools", "Jeweler's tools",
                "Leatherworker's tools", "Mason's tools", "Painter's supplies",
                "Potter's tools", "Smith's tools", "Tinker's tools",
                "Weaver's tools", "Woodcarver's tools"}
gamingsets = {"Dice set", "Dragonchess set", "Playing card set",
              "Three-Dragon Ante set"}
musicalinstruments = {"Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre",
                      "Horn", "Pan flute", "Shawm", "Viol"}
othertools = {"Disguise kit", "Forgery kit", "Herbalism kit",
              "Navigator's tools", "Poisoner's kit", "Thieves' tools",
              "Vehicles (land)", "Vehicles (water)"}
simpleweapons = {'club', 'dagger', 'greatclub', 'handaxe', 'javelin',
                 'light hammer', 'mace', 'quarterstaff', 'sickle', 'spear',
                 'unarmed strike', 'light crossbow', 'dart', 'shortbow', 'sling'}
martialweapons = {'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword',
                  'halberd', 'lance', 'longsword', 'maul', 'morningstar',
                  'pike', 'rapier', 'scimitar', 'shortsword', 'trident',
                  'war pick', 'warhammer', 'whip', 'blowgun', 'hand crossbow',
                  'heavy crossbow', 'longbow', 'net'}
# Armor, required proficiency, and armor class
armortypes = {'Padded': ('light armor', 11), 'Leather': ('light armor', 11),
              'Studded leather': ('light armor', 12), 'Hide': ('medium armor', 12),
              'Chain shirt': ('medium armor', 13),
              'Scale mail': ('medium armor', 14),
              'Breastplate': ('medium armor', 14),
              'Half plate': ('medium armor', 15), 'Ring mail': ('heavy armor', 14),
              'Chain mail': ('heavy armor', 16), 'Splint': ('heavy armor', 17),
              'Plate': ('heavy armor', 18)}

# Dictionary of hit dice
hitdice = {"Barbarian": 12, "Bard": 8, "Cleric": 8, "Druid": 8, "Fighter": 10,
           "Monk": 8, "Paladin": 10, "Ranger": 10, "Rogue": 8,
           "Sorcerer": 6, "Warlock": 8, "Wizard": 6}
# Dictionary of hit points to add per level, if not rolling die
hitperlevel = {"Barbarian": 7, "Bard": 5, "Cleric": 5, "Druid": 5, "Fighter": 6,
           "Monk": 5, "Paladin": 6, "Ranger": 6, "Rogue": 5,
           "Sorcerer": 4, "Warlock": 5, "Wizard": 4}
# Dictionary of levels at which there is an ability score improvement (or feat)
abimprovelevel = {"Barbarian": {4, 8, 12, 16, 19},
                  "Bard": {4, 8, 12, 16, 19},
                  "Cleric": {4, 8, 12, 16, 19},
                  "Druid": {4, 8, 12, 16, 19},
                  "Fighter": {4, 6, 8, 12, 14, 16, 19},
                  "Monk": {4, 8, 12, 16, 19},
                  "Paladin": {4, 8, 12, 16, 19},
                  "Ranger": {4, 8, 12, 16, 19},
                  "Rogue": {4, 8, 10, 12, 16, 19},
                  "Sorcerer": {4, 8, 12, 16, 19},
                  "Warlock": {4, 8, 12, 16, 19},
                  "Wizard": {4, 8, 12, 16, 19}}
# For dictionary of multiclassing prerequisites, see multiclass_check function.
# Dictionary of automatic proficiencies by class.
classprofauto = {"Barbarian": {'light armor', 'medium armor', 'shield',
                               'saving: Strength', 'saving: Constitution'} | \
                 simpleweapons | martialweapons,
                 "Bard": {'light armor', 'simple weapons', 'hand crossbow',
                          'longsword', 'rapier', 'shortsword',
                          'saving: Dexterity', 'saving: Charisma'},
                 "Cleric": {'light armor', 'medium armor', 'shield',
                            'saving: Wisdom',
                            'saving: Charisma'} | simpleweapons,
                 "Druid": {'light armor', 'medium armor', 'shield',
                           'club', 'dagger', 'dart', 'javelin', 'mace',
                           'quarterstaff', 'scimitar', 'sickle', 'sling',
                           'spear', 'saving: Intelligence', 'saving: Wisdom',
                           'Herbalism kit'},
                 "Fighter": {'light armor', 'medium armor', 'heavy armor',
                             'shield', 
                             'saving: Strength', 'saving: Constitution'} | \
                 simpleweapons | martialweapons,
                 "Monk": simpleweapons | {'shortsword',
                          'saving: Strength', 'saving: Dexterity'},
                 "Paladin": {'light armor', 'medium armor', 'heavy armor',
                             'shield', 
                             'saving: Wisdom', 'saving: Charisma'} | \
                 simpleweapons | martialweapons,
                 "Ranger": {'light armor', 'medium armor', 'shield',
                            'saving: Strength', 'saving: Dexterity'} | \
                 simpleweapons | martialweapons,
                 "Rogue": {'light armor', 'hand crossbow',
                           'longsword', 'rapier', 'shortsword',
                           'saving: Dexterity', 'saving: Intelligence',
                           "Thieves' tools"} | simpleweapons,
                 "Sorcerer": {'dagger', 'dart', 'sling', 'quarterstaff',
                              'light crossbow', 'saving: Constitution',
                              'saving: Charisma'},
                 "Warlock": simpleweapons | {'light armor', 
                             'saving: Wisdom', 'saving: Charisma'},
                 "Wizard": {'dagger', 'dart', 'sling', 'quarterstaff',
                            'light crossbow', 'saving: Intelligence',
                            'saving: Wisdom'}}
# Dictionary of abilities used in spell save DC and spell attack rolls
spellabs = {"Bard": "Charisma", "Cleric": "Wisdom", "Druid": "Wisdom",
            "Eldritch Knight": "Intelligence", #"Monk": "Wisdom",
            "Paladin": "Charisma", "Ranger": "Wisdom",
            "Arcane Trickster": "Intelligence",
            "Sorcerer": "Charisma", "Warlock": "Charisma",
            "Wizard": "Intelligence"}
# Automatic proficiencies by class when multiclassing.
multiclassprof = {"Barbarian": {'shield'} | simpleweapons | martialweapons,
                 "Bard": {'light armor'},
                 "Cleric": {'light armor', 'medium armor', 'shield'},
                 "Druid": {'light armor', 'medium armor', 'shield'},
                 "Fighter": {'light armor', 'medium armor', 'shield'} | \
                             simpleweapons | martialweapons,
                 "Monk": {'simple weapons', 'shortsword'},
                 "Paladin": {'light armor', 'medium armor', 'shield'} | \
                             simpleweapons | martialweapons,
                 "Ranger": {'light armor', 'medium armor', 'shield'} | \
                            simpleweapons | martialweapons,
                 "Rogue": {'light armor', "Thieves' tools"},
                 "Sorcerer": set(),
                 "Warlock": {'light armor', 'simple weapons'},
                 "Wizard": set()}
# Listing of all skills, and corresponding abilities.
allskills = {'Acrobatics': 'Dexterity', 'Animal Handling': 'Wisdom',
             'Arcana': 'Intelligence', 'Athletics': 'Strength',
             'Deception': 'Charisma', 'History': 'Intelligence',
             'Insight': 'Wisdom', 'Intimidation': 'Charisma',
             'Investigation': 'Intelligence', 'Medicine': 'Wisdom',
             'Nature': 'Intelligence', 'Perception': 'Wisdom',
             'Performance': 'Charisma', 'Persuasion': 'Charisma',
             'Religion': 'Intelligence', 'Sleight of Hand': 'Dexterity',
             'Stealth': 'Dexterity', 'Survival': 'Wisdom'}
# Dictionary of skill proficiencies by class, and how many can be taken.
classprofopt = {"Barbarian": ({'Animal Handling', 'Athletics', 'Intimidation',
                              'Nature', 'Perception', 'Survival'}, 2),
                  "Bard": (set(allskills.keys()), 3),
                  "Cleric": ({'History', 'Insight', 'Medicine', 'Persuasion',
                              'Religion'}, 2),
                  "Druid": ({'Arcana', 'Animal Handling', 'Insight',
                             'Medicine', 'Nature', 'Perception', 'Religion',
                             'Survival'}, 2),
                  "Fighter": ({'Acrobatics', 'Animal Handling', 'Athletics',
                               'History', 'Insight', 'Intimidation',
                               'Perception', 'Survival'}, 2),
                  "Monk": ({'Acrobatics', 'Athletics', 'History', 'Insight',
                            'Religion', 'Stealth'}, 2),
                  "Paladin": ({'Athletics', 'Insight', 'Intimidation',
                               'Medicine', 'Persuasion', 'Religion'}, 2),
                  "Ranger": ({'Animal Handling', 'Athletics', 'Insight',
                              'Investigation', 'Nature', 'Perception',
                              'Stealth', 'Survival'}, 3),
                  "Rogue": ({'Acrobatics', 'Athletics', 'Deception',
                             'Insight', 'Intimidation', 'Investigation',
                             'Perception', 'Performance', 'Persuasion',
                             'Sleight of Hand', 'Stealth'}, 4),
                  "Sorcerer": ({'Arcana', 'Deception', 'Insight',
                                'Intimidation', 'Persuasion', 'Religion'}, 2),
                  "Warlock": ({'Arcana', 'Deception', 'History',
                               'Intimidation', 'Investigation', 'Nature',
                               'Religion'}, 2),
                  "Wizard": ({'Arcana', 'History', 'Insight', 'Investigation',
                              'Medicine', 'Religion'}, 2)}
# Dictionary of additional skills that can be taken when multiclassing
multiclassskill = {"Bard": 1, "Ranger": 1, "Rogue": 1}
# Dictionary of automatic proficiencies by background
background_prof = {'Acolyte': {'Insight', 'Religion'},
                   'Charlatan': {'Deception', 'Sleight of Hand',
                                 'Disguise kit', 'Forgery kit'},
                   'Criminal': {'Deception', 'Stealth', "Thieves' tools"},
                   'Entertainer': {'Acrobatics', 'Performance', 'Disguise kit'},
                   'Folk Hero': {'Animal Handling', 'Survival',
                                 'Vehicles (land)'},
                   'Guild Artisan': {'Insight', 'Persuasion', "artisan's tools"},
                   'Hermit': {'Medicine', 'Religion', 'Herbalism kit'},
                   'Noble': {'History', 'Persuasion'},
                   'Outlander': {'Athletics', 'Survival'},
                   'Sage': {'Arcana', 'History'},
                   'Sailor': {'Athletics', 'Perception', "Navigator's tools",
                              'Vehicles (water)'},
                   'Soldier': {'Athletics', 'Intimidation', 'gaming set',
                               'Vehicles (land)'},
                   'Urchin': {'Sleight of Hand', 'Stealth', 'Disguise kit',
                              "Thieves' tools"}}
# Dictionary of who gets optional tool proficiencies and how many they can choose.
toolprofs = {"Hill Dwarf": ({"Smith's tools", "Brewer's supplies",
                             "Mason's tools"}, 1),
             "Mountain Dwarf": ({"Smith's tools", "Brewer's supplies",
                                 "Mason's tools"}, 1),
             "Bard": (musicalinstruments, 3),
             "Monk": (musicalinstruments | artisantools, 1),
             "Criminal": (gamingsets, 1),
             "Entertainer": (musicalinstruments, 1),
             "Folk Hero": (artisantools, 1),
             "Guild Artisan": (artisantools, 1),
             "Noble": (gamingsets, 1),
             "Outlander": (musicalinstruments, 1)}

# Dictionary of paths each class can take, and at what level they are chosen
classpaths = {"Barbarian": ({"Path of the Berserker",
                             "Path of the Totem Warrior"}, 3),
              "Bard": ({"College of Lore", "College of Valor"}, 3),
              "Cleric": ({"Knowledge Domain", "Life Domain", "Light Domain",
                          "Nature Domain", "Tempest Domain", "Trickery Domain",
                          "War Domain"}, 1),
              "Druid": ({"Circle of the Land", "Circle of the Moon"}, 2),
              "Fighter": ({"Champion", "Battle Master", "Eldritch Knight"}, 3),
              "Monk": ({"Way of the Open Hand", "Way of Shadow",
                        "Way of the Four Elements"}, 3),
              "Paladin": ({"Oath of Devotion", "Oath of the Ancients",
                           "Oath of Vengeance"}, 3),
              "Ranger": ({"Hunter", "Beast Master"}, 3),
              "Rogue": ({"Thief", "Assassin", "Arcane Trickster"}, 3),
              "Sorcerer": ({"Draconic Bloodline", "Wild Magic"}, 1),
              "Warlock": ({"The Archfey", "The Fiend", "The Great Old One"}, 1),
              "Wizard": ({"School of Abjuration", "School of Conjuration",
                          "School of Divination", "School of Enchantment",
                          "School of Evocation", "School of Illusion",
                          "School of Necromancy", "School of Transmutation"}, 2)}
# Damage bonus for Barbarian rage (index by level, incl level 0)
barbrage = [0, 2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3, 4,4,4,4,4]

# Feats and related info
feats = {'Alert', 'Athelete', 'Actor', 'Charger', 'Crossbow Expert',
         'Defensive Duelist', 'Dual Wielder', 'Dungeon Delver', 'Durable',
         'Elemental Adept', 'Grappler', 'Great Weapon Master', 'Healer',
         'Heavily Armored', 'Heavy Armor Master', 'Inspiring Leader',
         'Keen Mind', 'Lightly Armored', 'Linguist', 'Lucky', 'Mage Slayer',
         'Magic Initiate', 'Martial Adept', 'Medium Armor Master', 'Mobile',
         'Moderately Armored', 'Mounted Combatant', 'Observant',
         'Polearm Master', 'Resilient', 'Ritual Caster', 'Savage Attacker',
         'Sentinel', 'Sharpshooter', 'Shield Master', 'Skilled', 'Skulker',
         'Spell Sniper', 'Tavern Brawler', 'Tough', 'War Caster',
         'Weapon Master'}
# Feats that increase abilities
featabinc = {'Athelete': ['Strength', 'Dexterity'],
             'Actor': ['Charisma'], 'Durable': ['Constitution'],
             'Heavily Armored': ['Strength'],
             'Heavy Armor Master': ['Strength'], 'Keen Mind': ['Intelligence'],
             'Lightly Armored': ['Strength', 'Dexterity'],
             'Linguist': ['Intelligence'],
             'Moderately Armored': ['Strength', 'Dexterity'],
             'Observant': ['Wisdom', 'Intelligence'],
             'Resilient': ['Strength', 'Dexterity', 'Constitution',
                          'Intelligence', 'Wisdom', 'Charisma'],
             'Tavern Brawler': ['Strength', 'Constitution'],
             'Weapon Master': ['Strength', 'Dexterity']}
# Feats that have ability prerequisites
featprereq = {'Defensive Duelist': ['Dexterity'], 'Grappler': ['Strength'],
              'Inspiring Leader': ['Charisma'],
              'Ritual Caster': ['Wisdom', 'Intelligence'],
              'Skulker': ['Dexterity']}
# Feats with proficiency prerequisites
featprofpr = {'Heavily Armored': 'medium armor',
              'Heavy Armor Master': 'heavy armor',
              'Medium Armor Master': 'medium armor',
              'Moderately Armored': 'light armor'}

# Tuple of ability modifiers, indexed by ability scores.
# Ability scores can range from 1 to 30.  Zero is included here for ease
# of indexing.
abmod = (-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3,
         4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10)

# Tuple of proficiency bonuses, indexed by level.  Level zero is included
# for ease of indexing.
profbon = (0, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6)

## Global variables pertaining to the specific character: ##
# race: string indicating the character's race
# playerbackground: string indicating the character's background
# hitpoints: integer indicating the character's total hit points
# tough: boolean indicating whether character has Tough feat
# playerabs: dictionary of character's ability scores
# classes: dictionary, where keys are classes and values are levels
# comblevels: integer, combined levels across all classes
# playerprofs: set containing all proficiencies (skills, weapons, saving throws,
#     tools, armor) for the character
# playerprofsdouble: set containing all proficiencies for the character that get
#     double proficiency bonus (for Rogues and Domain of Knowledge Clerics)
# playerfeats: set containing all feats for the character
# playerfs: set containing all fighting styles for the character
# playerpaths: dictionary with classes as keys and chosen path within class as
#     values
# playerarmor: string indicating what type of armor the character is wearing
# playershield: boolean indicating whether character is carrying a shield
# firstclass: the original class of the level 1 character

## Function definitions:
def choose_race(racenames, race_or_class):
    '''Take user input to choose a race or class, allowing for variant
capitalization and hyphenation.'''
    notdone = True
    if race_or_class[0] in 'aeiou':
        promptstring = "\nChoose an {0}: "
    else:
        promptstring = "\nChoose a {0}: "
    while notdone: 
        result=[]
        raceinpt = input(promptstring.format(race_or_class))
        for r in racenames:
            if raceinpt.lower().replace('-', ' ') == r.lower().replace('-', ' '):
                result = [r]
                break
            if raceinpt.lower().replace('-', ' ') in r.lower().replace('-', ' '):
                result.append(r)
        if len(result) > 1:
            print("\nSpecify among:")
            print(result)
        if len(result) == 0:
            print("\nPossible choices are:")
            print(racenames)
        if len(result) == 1:
            notdone = False
    return result[0]


def make_ability_scores(racialmods):
    '''Generate a set of ability scores by any of the three methods
    listed in the PHB, then assign scores to abilities and add racial
    increases.'''
    i = 0
    while i not in {1, 2, 3}:
        i = int(input('''
Press 1 to generate a random set of level 1 ability scores, 2 to use
the standard set, or 3 to buy ability scores with points.
'''))
    if i == 1:
        abscores = []
        for j in range(6):
            thesedice = []
            # Roll 4 d6 and keep the best three
            for k in range(4):
                thesedice[k:k] = [random.randint(1,6)]
            abscores[j:j] = [sum(sorted(thesedice)[1:])]
        abscores.sort()
        if sum(abscores) <= 60:
            print("I'm so sorry.")
        if sum(abscores) >= 90:
            print("Hot damn.")
    if i == 2:
        abscores = [15, 14, 13, 12, 10, 8]
    if i == 3:
        abpoints = 27
        abscores = []
        scorecosts = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
        print('''
Choose your scores.  We will assign them to abilities in a moment.
Do not include racial increases.

Score Cost   Score Cost
  8    0      12    4
  9    1      13    5
 10    2      14    7
 11    3      15    9''')
        for j in range(6):
            thiscost = abpoints + 1
            while(abpoints - thiscost < 0):
                print("\n{0} points remain to choose {1} scores.".format(abpoints,
                                                                   6 - j))
                thisscore = int(input("Choose next score: "))
                if thisscore in scorecosts.keys():
                    thiscost = scorecosts[thisscore]
            abpoints = abpoints - thiscost
            abscores[j:j] = [thisscore]
    # end methods for generating scores to choose from.

    abnames = ["Strength", "Dexterity", "Constitution",
               "Intelligence", "Wisdom", "Charisma"]
    playerabs = dict() # contains ability name and ability score
    for j in range(6): # loop through the six specific abilities
        print("\nRemaining scores to choose from are:")
        print(abscores)
        thismod = racialmods[abnames[j]]
        if thismod != 0:
            if thismod > 0:
                thismodtxt = "+" + str(thismod)
            else:
                thismodtxt = str(thismod)
            print('''A {0} racial increase will be added for {1}.  Do not
include increase when choosing score.'''.format(thismodtxt, abnames[j]))
        thisscore = -99
        while thisscore not in abscores:
            thisscore = int(input("Choose score for " + abnames[j] + ": "))
        playerabs[abnames[j]] = thisscore + thismod # assign score to ability
        thisind = abscores.index(thisscore)
        del abscores[thisind] # remove score from collection
    return playerabs

def ability_improvement(playerabs, cls, lvl):
    '''Perform ability score improvement that comes with certain level
    increases.'''
    print("\nAbility score improvements for {0} level {1}:".format(cls, lvl))
    print("Current abilitites are:")
    print(playerabs)
    abnames = ["Strength", "Dexterity", "Constitution",
               "Intelligence", "Wisdom", "Charisma"]
    d = False
    while not d:
        ab_input = input("First ability to improve: ")
        ab_match = []
        for i in abnames:
            if ab_input.lower() in i.lower():
                ab_match.append(i)
        if len(ab_match) == 1 and playerabs[ab_match[0]] < 20:
            d = True
            playerabs[ab_match[0]] += 1
    d = False
    while not d:
        ab_input = input("Second ability to improve: ")
        ab_match = []
        for i in abnames:
            if ab_input.lower() in i.lower():
                ab_match.append(i)
        if len(ab_match) == 1 and playerabs[ab_match[0]] < 20:
            d = True
            playerabs[ab_match[0]] += 1
    return playerabs

def add_hit_points(cls, level, race, tough):
    '''Determine number of hit points to add, NOT including CON modifier.'''
    choose_hit = '0'
    print("\nHit points for {0} level {1}:".format(cls, classes[cls]))
    while choose_hit not in {'1', '2'}:
        choose_hit = input(
            "\nPress 1 to add {0} hit points, or 2 to roll a d{1}: ".format(
                hitperlevel[cls], hitdice[cls]))
    if choose_hit == '1':
        hitadd = hitperlevel[cls]
    if choose_hit == '2':
        hitadd = random.randint(1, hitdice[cls])
    if race in race_with_extra_hp_per_level: # if you are a Hill Dwarf
        hitadd += 1
        print("Racial bonus included.")
    if tough: # if you have the feat "Tough"
        hitadd += 2
        print("Tough bonus included.")
    if cls == "Sorcerer" and playerpaths[cls] == "Draconic Bloodline":
        hitadd += 1
        print("Draconic Bloodline bonus included.")
    # need to include bonus for Draconic Bloodline
    print("{0} hit points added (not including CON modifier).".format(hitadd))
    return hitadd

def multiclass_check(playerabs, cls):
    '''Determine whether it is possible to multiclass into or starting
       from a given class.'''
    x = (playerabs["Strength"] < 13 and cls in {"Barbarian", "Paladin"}) or \
        (playerabs["Dexterity"] < 13 and cls in {"Monk", "Ranger", "Rogue"}) or \
        (playerabs["Intelligence"] < 13 and cls == "Wizard") or \
        (playerabs["Wisdom"] < 13 and cls in {"Cleric", "Druid", "Monk", "Ranger"}) or \
        (playerabs["Charisma"] < 13 and cls in {"Bard", "Paladin", "Sorcerer", "Warlock"}) or \
        (playerabs["Strength"] < 13 and playerabs["Dexterity"] < 13 and cls == "Fighter")
    return not x

def add_feat():
    '''Add a feat and update stats as needed.'''
    # Make a lot of variables global so they can be updated.
    global playerabs
    global hitpoints
    global tough
    global playerprofs

    if len(playerfeats) > 0:
        print("Feats already taken:")
        print(playerfeats)
    prereqok = False
    while not prereqok:
        # get user input for which feat to take
        thisfeat = choose_race(feats - playerfeats, "feat")
        # check whether the prerequisites for this feat are met
        prereqok = True
        if thisfeat in featprereq.keys(): # check against abilities
            theseabs = [playerabs[pr] for pr in featprereq[thisfeat]]
            if max(theseabs) < 13:
                print("Ability scores too low for {0}.".format(thisfeat))
                prereqok = False
        if thisfeat in featprofpr.keys(): # check against proficiencies
            if featprofpr[thisfeat] not in playerprofs:
                print("Proficiency in {0} required.".format(featprofpr[thisfeat]))
                prereqok = False
        if thisfeat == "Weapon Master" and \
           (simpleweapons | martialweapons) <= playerprofs:
            print("You are already proficient in all weapons.")
            prereqok = False
        
    # update ability scores
    if thisfeat in featabinc.keys():
        if len(featabinc[thisfeat]) == 1:
            thisabinc = featabinc[thisfeat][0]
        else:
            print("Possible abilities to increase (up to 20):")
            print(featabinc[thisfeat])
            thisabinc = choose_race(featabinc[thisfeat], "ability")
        if playerabs[thisabinc] < 20:
            playerabs[thisabinc] += 1
            print("{0} increased.".format(thisabinc))
    # update variables specific to feats
    if thisfeat == "Tough":
        tough = True
        hitpoints += 2 * comblevels
        print("Hit points updated.")
    if thisfeat == "Lightly Armored":
        playerprofs.add("light armor")
        print("Light armor proficiency added.")
    if thisfeat == "Moderately Armored":
        playerprofs.update({'medium armor', 'shield'})
        print("Medium armor and shield proficiencies added.")
    if thisfeat == "Heavily Armored":
        playerprofs.add("heavy armor")
        print("Heavy armor proficiency added.")
    if thisfeat == "Resilient":
        playerprofs.add("saving: " + thisabinc)
        print("Saving throw proficiency added.")
    if thisfeat == "Skilled":
        print("Current skills and tool proficiencies are:")
        skillsandtools = set(allskills.keys()) | artisantools | gamingsets | \
                             musicalinstruments | othertools
        print(playerprofs & skillsandtools)
        print("Choose three more among:")
        print(skillsandtools - playerprofs)
        for i in range(3):
            playerprofs.add(choose_race(skillsandtools - playerprofs,
                                        "proficiency"))
    if thisfeat == "Weapon Master":
        print("Current weapon proficiencies are:")
        print(playerprofs & (simpleweapons | martialweapons))
        print("Choose four more among:")
        print((simpleweapons | martialweapons) - playerprofs)
        for i in range(4):
            playerprofs.add(choose_race((simpleweapons | martialweapons) - playerprofs,
                                        "weapon"))
    if thisfeat == "Tavern Brawler":
        playerprofs.update({"unarmed strike", "improvised weapons"})
        print("Proficiencies added.")
            
    return thisfeat

def add_class_path(cls):
    '''Choose among different paths for a class'''
    global playerprofs
    global playerprofsdouble
    print("\nOptions for {0} at level {1} are:".format(cls, classpaths[cls][1]))
    print(classpaths[cls][0])
    path = choose_race(classpaths[cls][0], "path")

    # class-specific stuff
    if path == "College of Lore":
        print("\nSkills so far are:")
        print(set(allskills.keys()) & playerprofs)
        print("Choose three additional skills among:")
        print(set(allskills.keys()) - playerprofs)
        for i in range(3):
            playerprofs.add(choose_race(set(allskills.keys()) - playerprofs,
                                        "skill"))
    if path == "College of Valor":
        playerprofs.update({"medium armor", "shield", "flamethrower guitar"} | \
                           martialweapons)
        print("Armor and weapons proficiencies added.")
    if path == "Knowledge Domain":
        kdskills = {"Arcana", "History", "Nature", "Religion"}
        print("Choose two skills for double proficiency bonus:")
        print(kdskills)
        for i in range(2):
            p = choose_race(kdskills, "skill")
            playerprofs.add(p)
            playerprofsdouble.add(p)
    if path in {"Nature Domain", "Tempest Domain", "War Domain", "Life Domain"}:
        playerprofs.add('heavy armor')
        print("Heavy armor proficiency added.")
    if path in {"Tempest Domain", "War Domain"}:
        playerprofs.update(martialweapons)
        print("Weapons proficiencies added.")
    if path == "Battle Master":
        print("Gain proficiency in one set of artisan's tools.")
        playerprofs.add(choose_race(artisantools - playerprofs, "tool set"))
    if path == "Assassin":
        playerprofs.update({"Disguise kit", "Poisoner's kit"})
        print("Proficiencies added in disguise kit and poisoner's kit.")
    return(path)

def rogue_expertise():
    '''Double proficiency in two skills at Rogue level 1 and 6.'''
    global playerprofsdouble
    theseskills = (set(allskills.keys()) | {"Thieves' tools"}) - playerprofsdouble
    print("\nChoose two skills in which to double your proficiency bonus:")
    print(playerprofs & theseskills)
    for i in range(2):
        playerprofsdouble.add(choose_race(playerprofs & theseskills, "skill"))
    return None

def add_fighting_style(cls):
    '''Fighting styles for Fighter, Paladin, and Ranger.'''
    allstyles = ['Archery', 'Defense', 'Dueling', 'Great Weapon Fighting',
                  'Protection', 'Two-Weapon Fighting']
    if cls == "Paladin":
        allstyles = allstyles[1:5]
    if cls == "Ranger":
        allstyles = allstyles[0:3] + [allstyles[5]]
    fs = choose_race(set(allstyles) - playerfs, "fighting style")
    return(fs)

def add_level(cls):
    '''Everything for adding levels in an existing class.'''
    global hitpoints
    global playerabs
    global playerfeats
    global comblevels
    global classes
    global playerpaths
    global playerfs
    global playerprofs

    comblevels += 1 # update combined levels
    classes[cls] += 1 # update levels in this class
    # choose a path if this is the appropriate level
    if classes[cls] == classpaths[cls][1]: 
        playerpaths[cls] = add_class_path(cls)
    hitpoints += add_hit_points(cls, classes[cls], race, tough) # add hit points
    if classes[cls] in abimprovelevel[cls]: # ability score improvement or feat
        feat_or_ab = '0'
        while feat_or_ab not in {'1', '2'}:
            feat_or_ab = input(
                "\nPress 1 for ability score improvement or 2 to add a feat: ")
        if feat_or_ab == '1':
            playerabs = ability_improvement(playerabs, cls, classes[cls])
        else:
            playerfeats.add(add_feat())
    # class-specific improvements
    if cls == "Rogue" and classes[cls] in {1, 6}:
        rogue_expertise()
    if (cls == "Fighter" and classes[cls] == 1) or \
       (cls == "Paladin" and classes[cls] == 2) or \
       (cls == "Ranger" and classes[cls] == 2) or \
       (cls == "Fighter" and classes[cls] == 10 and \
        playerpaths[cls] == "Champion"):
        playerfs.add(add_fighting_style(cls))
    if cls == "Rogue" and classes[cls] == 15:
        playerprofs.add("saving: Wisdom")
        print("Wisdom saving throw proficiency added (Slippery Mind).")
    
    return None

def add_multiclass():
    '''All the updates for adding an additional class, before adding levels
       and hit points.'''
    global playerprofs
    
    newclass = choose_race(hitdice.keys(), "class")
    while newclass in [cl[0] for cl in classes] or \
            not multiclass_check(playerabs, newclass):
        if newclass in [cl[0] for cl in classes]:
            print("You are already a {0}.  Choose a new class.".format(newclass))
        if not multiclass_check(playerabs, newclass):
            print("You do not meet the ability score prerequisites to be a {0}.".format(newclass))
        newclass = choose_race(hitdice.keys(), "class")
    playerprofs.update(multiclassprof[newclass]) # add proficiencies
    if newclass == "Bard": # add one musical instrument if bard
        playerprofs.add(choose_race(musicalinstruments, "musical instrument"))
    if newclass in multiclassskill.keys(): # add skills if available
        print("\nSkills so far are:")
        print(set(allskills.keys()) & playerprofs)
        print("Choose {0} additional skill(s) among:".format(multiclassskill[newclass]))
        print(classprofopt[newclass][0] - playerprofs)
        for i in range(multiclassskill[newclass]):
            playerprofs.add(choose_race(classprofopt[newclass][0] - playerprofs,
                            "skill"))
    return newclass

def choose_armor():
    '''Get info on whether character has armor and/or shield.'''
    global playerarmor
    global playershield

    arprof = playerprofs & {'light armor', 'medium armor',
                            'heavy armor', 'shield'}
    if len(arprof) == 0:
        print("\nYou are not proficient in any armor or shields")
    else:
        print("\nYou have the following armor and shield proficiencies:")
        print(arprof)
    if new_or_level == '1':
        updatearmor = True
    else:
        print("Current armor: " + playerarmor)
        if playershield:
            print("Carrying a shield.")
        else:
            print("Not carrying a shield")
        arinpt = '0'
        while arinpt not in {'1', '2'}:
            arinpt = input("Press 1 to keep current armor and/or shield, or 2 to change: ")
        updatearmor = (arinpt == '2')
    if updatearmor:
        shieldchoice = '0'
        while shieldchoice not in {'1', '2'}:
            shieldchoice = input("Press 1 if your character is carrying a shield, or 2 if not: ")
        playershield = (shieldchoice == '1')
        print("\nEnter 'None' for no armor, or otherwise the type of armor you are wearing.")
        playerarmor = choose_race(set(armortypes.keys()) | {'None'},
                                  "type of armor")
    
    return None

def spellsavedc(pb, playermods):
    '''Generate strings for printing spell save DC and spell attack modifier.'''
    outstrings = list()
    for k in classes.keys() | playerpaths.values():
        if k in spellabs.keys():
            outstrings.append("{} spell save DC: {}\n".format(k,
                              8 + pb + playermods[spellabs[k]]))
            outstrings.append("{0} spell attack modifier: {1:+}\n\n".format(
                k, pb + playermods[spellabs[k]]))
    if "Monk" in classes.keys():
        outstrings.append("Ki save DC (Monk): {}\n\n".format(
            8 + pb + playermods["Wisdom"]))
    if "Battle Master" in classpaths.values() or "Martial Adept" in playerfeats:
        outstrings.append("Maneuver save DC (Battle Master): {}\n\n".format(
            8 + pb + max(playermods["Strength"], playermods["Dexterity"])))
    return outstrings

def choose_directory(need_write):
    '''Select a directory for file output or import, and check that it exists
       and is writeable.  need_write is a boolean indicating whether or not
       the directory must be writeable.'''
    # writeable directory on Android devices (since scripts3 directory of
    # QPython3 is not writeable from a script)
    Android_dir = "/storage/emulated/{}/Documents"
    if os.path.isdir(Android_dir.format("0")):
        mydir = Android_dir.format("0")
    elif os.path.isdir(Android_dir.format("legacy")):
        mydir = Android_dir.format("legacy")
    # for all other situations, assume we want to write to current directory
    else:
        mydir = "."

    # tell the user what the default is
    if mydir == ".":
        dirprint = "the directory where this script is saved"
    else:
        dirprint = mydir
    if need_write:
        rw = "writing"
    else:
        rw = "reading"
    print("\nDefault directory for {0} files is {1}.".format(rw, dirprint))

    # test if the default is writeable, ask user if directory should be changed
    mydir_writeable = os.access(mydir, os.W_OK | os.X_OK)
    if need_write and not mydir_writeable:
        print("Directory is not writeable.")
        change_dir = "2"
    else:
        change_dir = "0"
        while change_dir not in {'1', '2'}:
            change_dir = input("Press 1 to keep default directory or 2 to change. ")
    if change_dir == '2': # change the directory
        tries = 0
        if platform.system() == "Windows":
            print("Example directory for Windows: c:/Users/drizzt/Documents")
        while tries==0 or not os.path.isdir(mydir) or \
              (need_write and not mydir_writeable):
            tries += 1
            mydir = input("Enter new directory name: ")
            if not os.path.isdir(mydir):
                print(mydir + " is not a valid directory.")
            else:
                mydir_writeable = os.access(mydir, os.W_OK | os.X_OK)
                if need_write and not mydir_writeable:
                    print(mydir + "does not have write access.")
    return mydir

def write_charsheet():
    '''Calculate rolls and write character sheet to file.'''
    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence",
                 "Wisdom", "Charisma"]
    # Get ability modifiers
    playermods = dict()
    for a in abilities:
        playermods[a] = abmod[playerabs[a]]
    # Get proficiency bonus
    pb = profbon[comblevels]
    # Hit dice
    hdtotal = {6: 0, 8: 0, 10: 0, 12: 0}
    for k in classes.keys():
        hdtotal[hitdice[k]] += classes[k]
    hdstring = ""
    for d in hdtotal.keys():
        if hdtotal[d] > 0:
            hdstring += "{0}d{1} + ".format(hdtotal[d], d)
    hdstring = hdstring[:-3]
    # Armor class
    if playerarmor == 'None':
        armorclass = 10 + playermods["Dexterity"]
        if "Barbarian" in classes.keys():
            armorclass += playermods["Constitution"] # "Unarmored Defense"
            print("Unarmored Defense bonus added to armor class.")
    elif armortypes[playerarmor][0] == 'light armor':
        armorclass = armortypes[playerarmor][1] + playermods["Dexterity"]
    elif armortypes[playerarmor][0] == 'medium armor':
        if  playermods["Dexterity"] > 2:
            armorclass = armortypes[playerarmor][1] + 2
        else:
            armorclass = armortypes[playerarmor][1] + playermods["Dexterity"]
        if "Medium Armor Master" in playerfeats and playermods["Dexterity"] > 2:
            armorclass += 1
            print("Medium Armor Master bonus added to armor class.")
    elif armortypes[playerarmor][0] == 'heavy armor':
        armorclass = armortypes[playerarmor][1]
    if playershield: # if character has a shield
        armorclass += 2
    if "Defense" in playerfs and playerarmor != 'None':
        armorclass += 1 # "Defense" fighting style
        print("'Defense' bonus added to armor class.")
    # Initiative
    initiative = playermods["Dexterity"]
    if 'Alert' in playerfeats:
        initiative += 5
    # Saving throws
    savingthrows = dict()
    for a in abilities:
        savingthrows[a] = playermods[a]
        if "saving: " + a in playerprofs:
            savingthrows[a] += pb # proficiency bonus for saving throws
        elif "Fighter" in classes.keys() and classes["Fighter"] > 6 and \
             playerpaths["Fighter"] == "Champion" and \
             a in {"Strength", "Dexterity", "Constitution"}: # Remarkable Athelete
            rapb = pb // 2 # improve saving throw by half of proficiency bonus
            if pb % 2 == 1:
                rapb += 1
            savingthrows[a] += rapb
            print("Remarkable Athelete bonus added for {0} saving throw.".format(a))
    # Skill checks
    skillprofs = dict()
    for s in allskills.keys():
        skillprofs[s] = playermods[allskills[s]]
        if s in playerprofs:
            skillprofs[s] += pb
        if s in playerprofsdouble:
            skillprofs[s] += pb
    # Attack rolls
    meleeattackproficient = pb + playermods["Strength"]
    meleeattacknotproficient = playermods["Strength"]
    meleedamage = playermods["Strength"]
    rangedattackproficient = pb + playermods["Dexterity"]
    rangedattacknotproficient = playermods["Dexterity"]
    rangeddamage = playermods["Dexterity"]
    if 'Archery' in playerfs:
        rangedattackproficient += 2
        rangedattacknotproficient += 2
        print("Ranged attack roll bonus added for Archery.")

    # Get a directory for writing to
    thisdir = choose_directory(True)
    # Create the file
    filename = input("\nFile name for output (.txt extension recommended): ")
    with open(os.path.join(thisdir, filename), 'w') as myfile:
        myfile.write(race + "\n")
        myfile.write(playerbackground + "\n")
        myfile.write("{0: <9} level {1: >2}".format(firstclass, classes[firstclass]))
        if firstclass in playerpaths.keys():
            myfile.write(", {0}".format(playerpaths[firstclass]))
        if len(classes) > 1:
            for k in set(classes.keys()) - {firstclass}:
                myfile.write("\n{0: <9} level {1: >2}".format(k, classes[k]))
                if k in playerpaths.keys():
                    myfile.write(", {0}".format(playerpaths[k]))
        myfile.write("\n\nProficiency bonus: {0:+}\n".format(pb))
        myfile.write("\nAbility      Score Modifier")
        for a in abilities:
            myfile.write("\n{0: <12}    {1: >2}       {2: >+2}".format(a, playerabs[a], playermods[a]))        

        myfile.write("\n\nHit Points: " + str(hitpoints))
        myfile.write("\nHit Dice:   " + hdstring)

        myfile.write("\n\nArmor Class: " + str(armorclass))
        myfile.write("\nArmor: " + playerarmor)
        if playershield:
            myfile.write(", shield")

        myfile.write("\n\nModifier for initiative roll: {0:+}".format(initiative))

        myfile.write("\n\nSaving throws")
        for a in abilities:
            myfile.write("\n{0: <12} {1: >+3}".format(a, savingthrows[a]))

        myfile.write("\n\nSkill checks")
        sk = list(allskills.keys())
        sk.sort()
        for s in sk:
            myfile.write("\n{0: <15} {1: >+3}".format(s, skillprofs[s]))

        myfile.write("\n\nPassive wisdom (Perception): {0}".format(
            10 + skillprofs["Perception"]))
        myfile.write("\n\n")

        myfile.writelines(spellsavedc(pb, playermods))

        myfile.write("Feats:\n")
        if len(playerfeats) == 0:
            myfile.write("None\n\n")
        else:
            for f in playerfeats:
                myfile.write(f + "\n")
            myfile.write("\n")
        myfile.write("Fighting Styles:\n")
        if len(playerfs) == 0:
            myfile.write("None\n\n")
        else:
            for f in playerfs:
                myfile.write(f + "\n")
            myfile.write("\n")

        myfile.write("Melee attacks:\n")
        myfile.write("Attack roll modifier for weapons in which you are proficient: {:+}\n".format(
            meleeattackproficient))
        myfile.write("Attack roll modifier for weapons in which you are not proficient: {:+}\n".format(
            meleeattacknotproficient))
        myfile.write("Damage modifier: {:+}\n".format(meleedamage))
        if "Barbarian" in classes.keys():
            myfile.write("Damage modifier while raging: {:+}\n".format(
                meleedamage + barbrage[classes["Barbarian"]]))
        if "Dueling" in playerfs:
            myfile.write("Damage modifier with single one-handed weapon (Dueling): {:+}\n".format(
                meleedamage + 2))
        if "Barbarian" in classes.keys() and "Dueling" in playerfs:
            myfile.write("Damage modifier for combined Rage and Dueling: {:+}\n".format(
                meleedamage + barbrage[classes["Barbarian"]] + 2))

        myfile.write("\nRanged or finesse weapon attacks:\n")
        myfile.write("Attack roll modifier for weapons in which you are proficient: {:+}\n".format(
            rangedattackproficient))
        myfile.write("Attack roll modifier for weapons in which you are not proficient: {:+}\n".format(
            rangedattacknotproficient))
        myfile.write("Damage modifier: {:+}\n".format(rangeddamage))

        myfile.write("\nWeapons proficiencies:\n")
        weap = list(playerprofs & (simpleweapons | martialweapons | {"improvised weapons"}))
        weap.sort()
        for p in weap:
            myfile.write(p + "\n")

        myfile.write("\nArmor proficiencies:\n")
        if "light armor" in playerprofs:
            myfile.write("light armor\n")
        if "medium armor" in playerprofs:
            myfile.write("medium armor\n")
        if "heavy armor" in playerprofs:
            myfile.write("heavy armor\n")
        if "shield" in playerprofs:
            myfile.write("shield\n")
        if len(playerprofs & {"light armor", "medium armor", "heavy armor",
                              "shield"}) == 0:
            myfile.write("None\n")

        myfile.write("\nSkill proficiencies:\n")
        skp = allskills.keys() & playerprofs
        for s in sorted(skp):
            myfile.write(s + "\n")

        myfile.write("\nSaving throw proficiencies:\n")
        stp = [x for x in playerprofs if x.startswith("saving")]
        for s in sorted(stp):
            myfile.write(s + "\n")

        myfile.write("\nTool proficiencies:\n")
        tl = playerprofs & (artisantools | gamingsets | musicalinstruments | \
                             othertools | {'flamethrower guitar'})
        if len(tl) == 0:
            myfile.write("None\n")
        else:
            for t in sorted(tl):
                myfile.write(t + "\n")

        myfile.write("\nDouble proficiencies:\n")
        if len(playerprofsdouble) == 0:
            myfile.write("None\n")
        else:
            for p in sorted(playerprofsdouble):
                myfile.write(p + "\n")
                
    return None

def read_charsheet():
    '''Read a character sheet back in and extract data from it.'''
    global race
    global playerbackground
    global classes
    global playerabs
    global playerpaths
    global playerprofs
    global playerprofsdouble
    global playerarmor
    global playershield
    global playerfeats
    global playerfs
    global hitpoints
    global tough
    global comblevels
    global firstclass

    classes = dict()
    playerpaths = dict()
    playerabs = dict()
    playerfeats = set()
    playerfs = set()
    playerprofs = set()
    playerprofsdouble = set()

    thisdir = choose_directory(False)
    filename = input("\nFile name for existing character sheet (include extension): ")
    with open(os.path.join(thisdir, filename), mode='r') as myfile:
        race = myfile.readline().strip()
        assert race in racabinc.keys(), \
               "First line does not appear to be a race."
        playerbackground = myfile.readline().strip()
        assert playerbackground in background_prof.keys(), \
               "Second line does not appear to be a background."

        # get classes, levels, and paths
        classline = myfile.readline().strip()
        while classline != "":
            lvind = classline.index("level")
            thisclass = classline[:lvind].strip()
            assert thisclass in hitdice.keys(), \
                   "{} is not a known class.".format(thisclass)
            thislevel = int(classline[lvind + 6: lvind + 8])
            assert thislevel > 0 and thislevel < 21, \
                   "Level should be greater than zero and less than twenty-one."
            classes[thisclass] = thislevel
            if(len(classes) == 1):
                firstclass = thisclass # note down if this is the original class
            if "," in classline: # get path if there is one
                cmind = classline.index(',')
                playerpaths[thisclass] = classline[cmind+2:].strip()
                assert playerpaths[thisclass] in classpaths[thisclass][0]
            classline = myfile.readline().strip()
        comblevels = sum(classes.values()) # total levels across all classes
        assert comblevels < 21, "Character level shoudl be less than twenty-one."

        nextline = myfile.readline()
        while "Ability" not in nextline:
            nextline = myfile.readline()

        # get abilities
        abline = myfile.readline()
        while abline != "\n":
            thisab = abline[:12].strip()
            assert thisab in {"Strength", "Dexterity", "Constitution",
                              "Intelligence", "Wisdom", "Charisma"}, \
                    "{} is not an ability".format(thisab)
            thisscore = int(abline[16:18])
            assert thisscore > 0 and thisscore < 31, \
                "Ability score out of range."
            playerabs[thisab] = thisscore
            abline = myfile.readline()
        assert len(playerabs) == 6, "Did not find six abilities."

        # get hit points
        nextline = myfile.readline().strip()
        while "Hit Points" not in nextline:
            nextline = myfile.readline().strip()
        hitpoints = int(nextline[12:])

        # get armor
        while "Armor:" not in nextline:
            nextline = myfile.readline().strip()
        if ", shield" in nextline:
            playershield = True
            playerarmor = nextline[7:nextline.find(",")]
        else:
            playershield = False
            playerarmor = nextline[7:]
        assert playerarmor in armortypes.keys() | {'None'}, "{} not a known armor.".format(playerarmor)        

        # get feats
        while "Feats" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            if nextline != "None":
                assert nextline in feats, "{} not a known feat.".format(nextline)
                playerfeats.add(nextline)
            nextline = myfile.readline().strip()
        tough = "Tough" in playerfeats

        # get fighting styles
        while "Fighting Styles" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            if nextline != "None":
                assert nextline in {'Archery', 'Defense', 'Dueling',
                                    'Great Weapon Fighting',
                  'Protection', 'Two-Weapon Fighting'}, "{} not a known fighting style.".format(nextline)
                playerfs.add(nextline)
            nextline = myfile.readline().strip()

        # get proficiencies
        while "Weapons proficiencies" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            assert nextline in simpleweapons | martialweapons | \
                   {"improvised weapons"}, "{} not a known weapon.".format(nextline)
            playerprofs.add(nextline)
            nextline = myfile.readline().strip()
        while "Armor proficiencies" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            if nextline != "None":
                assert nextline in {"light armor", "medium armor", "heavy armor",
                        "shield"}, "{} not a known armor.".format(nextline)
                playerprofs.add(nextline)
            nextline = myfile.readline().strip()
        while "Skill proficiencies" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            assert nextline in allskills.keys(), "{} not a known skill.".format(nextline)
            playerprofs.add(nextline)
            nextline = myfile.readline().strip()
        while "Saving throw proficiencies" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            assert nextline in ["saving: " + x for x in ["Strength", "Dexterity",
                                                         "Constitution", "Intelligence",
                                                         "Wisdom", "Charisma"]], \
                            "{} not a saving throw.".format(nextline)
            playerprofs.add(nextline)
            nextline = myfile.readline().strip()
        while "Tool proficiencies" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            if nextline != "None":
                assert nextline in artisantools | gamingsets | musicalinstruments | \
                                 othertools | {'flamethrower guitar'}, \
                            "{} not a known tool".format(nextline)
                playerprofs.add(nextline)
            nextline = myfile.readline().strip()

        # get double proficiencies
        while "Double proficiencies" not in nextline:
            nextline = myfile.readline().strip()
        nextline = myfile.readline().strip()
        while nextline != "":
            if nextline != "None":
                assert nextline in allskills.keys() | {"Thieves' tools"}, \
                       "{} not allowed for double proficiencies.".format(nextline)
                playerprofsdouble.add(nextline)
            nextline = myfile.readline().strip()
            
    print(race)
    print(playerbackground)
    print("Character level {}".format(comblevels))
    print(classes)
    print(playerpaths)
    print(playerabs)
    print("Hit points: {}".format(hitpoints))
    print("Armor: " + playerarmor)
    if playershield:
        print("Carrying shield")
    print("Feats:")
    print(playerfeats)
    print("Fighting styles:")
    print(playerfs)
    print("Proficiencies:")
    print(sorted(playerprofs))
    print("Double proficiencies:")
    print(sorted(playerprofsdouble))
    print("")

    return None

### Begin script ###
# Welcome message.
print('''
*** Welcome to a D&D 5th edition character sheet generator. ***
Written by Lindsay V. Clark, released under a Creative Commons
4.0 BY-SA License, with no warranty.

This program is intended to help with the arithmetic involved in
generating and leveling a character.  Please purchase the Player's
Handbook for information on all other aspects of the game.''')

new_or_level = input('''
Press 1 to make a new character, 2 to load an existing character
sheet and add a level, or any other key to quit. ''')

if new_or_level == '1':
# script for making a new character
    race = choose_race(racabinc.keys(), "race")      # race
    if race in raceprof.keys():                      # proficiencies
        playerprofs = raceprof[race]
    else:
        playerprofs = set()
    playerprofsdouble = set() # proficiencies with double prof. bonus
    playerabs = make_ability_scores(racabinc[race])  # ability scores

    if race == "Half-Elf":
        print('''
You are a Half-Elf!  Isn't that special.  Choose two additional
ability scores to increase by +1.''')
        remaining_scores = {'Strength', 'Dexterity', 'Constitution',
                            'Intelligence', 'Wisdom'}
        while len(remaining_scores) > 3:
            print("\nChoose among:")
            print(remaining_scores)
            this_score = choose_race(remaining_scores, "ability")
            if this_score in remaining_scores:
                playerabs[this_score] += 1
            remaining_scores.discard(this_score)
        print("Choose two skills in which to be proficient.")
        playerprofs.add(choose_race(set(allskills.keys()) - playerprofs,
                                       "skill"))
        playerprofs.add(choose_race(set(allskills.keys()) - playerprofs,
                                       "skill"))
        
    if race in toolprofs.keys(): # optional tool proficiencies (Dwarf)
        print("\nOptional tool proficiencies for {0} are:".format(race))
        print(toolprofs[race][0])
        for i in range(toolprofs[race][1]):
            playerprofs.add(choose_race(toolprofs[race][0], "tool proficiency"))

    # get background
    playerbackground = choose_race(background_prof.keys(),"background")
    playerprofs.update(background_prof[playerbackground]) # background proficiencies
    if playerbackground in toolprofs.keys():
        print("Optional tool proficiencies for {0} are:".format(playerbackground))
        print(toolprofs[playerbackground][0])
        for i in range(toolprofs[playerbackground][1]):
            playerprofs.add(choose_race(toolprofs[playerbackground][0],
                                        "tool proficiency"))

    # get first class and level
    firstclass = choose_race(hitdice.keys(), "first level class")
    hitpoints = hitdice[firstclass] # add con modifier later
    tough = False # whether you have the feat "Tough"
    playerpaths = dict() # for choosing paths within a class
    playerfs = set() # fighting styles for this player (Fighter/Paladin/Ranger)
    if race in race_with_extra_hp_per_level:
        hitpoints += 1 # bonus hit point for Hill Dwarf
        print("\nRacial bonus included for hit points.")
    playerprofs.update(classprofauto[firstclass]) # add proficiencies
    print("\nSkills so far are:")
    print(set(allskills.keys()) & playerprofs)
    print("Choose {0} additional skills among:".format(classprofopt[firstclass][1]))
    print(classprofopt[firstclass][0] - playerprofs)
    for i in range(classprofopt[firstclass][1]): # add skills
        playerprofs.add(choose_race(classprofopt[firstclass][0] - playerprofs,
                                    "skill"))

    # class-specific stuff for first level
    if firstclass in toolprofs.keys(): # optional tool proficiencies (Bard, Monk)
        print("\nOptional tool proficiencies for {0} are:".format(firstclass))
        print(toolprofs[firstclass][0])
        print("You may select {0}.".format(toolprofs[firstclass][1]))
        for i in range(toolprofs[firstclass][1]):
            playerprofs.add(choose_race(toolprofs[firstclass][0],
                                        "tool proficiency"))
    if firstclass == "Rogue": # double proficiencies in two skills
        rogue_expertise()
    if classpaths[firstclass][1] == 1: # Clerics, Sorcerers, Warlocks
        playerpaths[firstclass] = add_class_path(firstclass)
        if playerpaths[firstclass] == "Draconic Bloodline":
            hitpoints += 1
            print("One hit point added.")
    if firstclass == "Fighter": # fighting style for fighter
        playerfs.add(add_fighting_style(firstclass))
        
    playerfeats = set() # set of feats for the player
    comblevels = 1 # combined levels across all classes
    classes = dict() # store classes and levels
    classes[firstclass] = 1
    
    fclevel = 0 # level for the first class
    while fclevel < 1 or fclevel > 20:
        fclevel = int(input("\nHow many levels in {0}? ".format(firstclass)))
    # go through additions level by level
    if fclevel > 1:
        for i in range(2, fclevel+1):
            add_level(firstclass)

    # do (optional) multiclassing
    addclasses = int(input('''
Enter the number of additional classes desired, or 0 if you do not want
to multiclass: '''))
    while addclasses > 0:
        if multiclass_check(playerabs, firstclass):
            addclasses -= 1
            newclass = add_multiclass()
            classes[newclass] = 0
            nclevel = 0
            while nclevel < 1 or nclevel > 20 - comblevels:
                nclevel = int(input("How many levels in {0}? ".format(newclass)))
            # go through additions level by level
            for i in range(1, nclevel+1):
                add_level(newclass)
        else: # if you can't multiclass, just add more levels in this class.
            addclasses = 0
            print("Multiclassing not possible due to low ability score(s).")
            addlvl = int(input(
                "Number of additional levels in {0}: ".format(firstclass)))
            for i in range(fclevel+1, comblevels+addlvl+1):
                add_level(firstclass)
    # end of multiclassing subroutine.

    # add armor
    choose_armor()

    print("\nFinal ability scores are:")
    print(playerabs)
    
    # add CON modifier for hit points
    hitpoints += comblevels * abmod[playerabs["Constitution"]]
    print("\nMaximum hit points (with CON modifier added): {0}.".format(
        hitpoints))

    write_charsheet()

if new_or_level == '2': # script for leveling up a character
    read_charsheet()
    if len(classes) == 1 and not multiclass_check(playerabs, list(classes.keys())[0]):
        # if multiclassing is not possible, don't give an option about which
        # class to level up in.
        print("Multiclassing not possible; adding a level in the current class.")
        
        thisclass = list(classes.keys())[0]
    else:
        clschoice = '0'
        while clschoice not in {'1', '2'}:
            clschoice = input("\nPress 1 to add a level to an existing class, or 2 to multiclass: ")
        if clschoice == '1':
            if len(classes) == 1:
                # There is just one class and we want to add a level.
                thisclass = list(classes.keys())[0]
            else:
                # Character is already multiclass, pick one class for leveling up.
                thisclass = choose_race(classes.keys(), "class in which to add a level")
        else:
            # Add a new class.
            thisclass = add_multiclass()
            classes[thisclass] = 0

    # remove CON modifier from hit points before leveling up, in case
    # CON changes with level.
    hitpoints -= comblevels * abmod[playerabs["Constitution"]]
    add_level(thisclass)
    hitpoints += comblevels * abmod[playerabs["Constitution"]]

    choose_armor()
        
    write_charsheet()

if new_or_level in {'1', '2'}:
    foo = input("\nPress enter to quit.")
    
### end script ###
#print(choose_directory(True))

#if new_or_level == '1':
#    print(classes)
#    print(playerprofs)
#    print(playerprofsdouble)



