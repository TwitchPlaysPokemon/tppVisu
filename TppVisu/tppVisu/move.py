'''
Created on 29.04.2015

@author: Felk
'''
from __future__ import division, print_function

from tppVisu.tables.moveAnomalies import getAnomaly
from tppVisu.tables.moveHits import getMinMaxHits
from tppVisu.tables.movePriorities import getPriority
from tppVisu.tables.moveVisuables import isVisuable
from tppVisu.util import enum


MoveCategory = enum(physical='physical', special='special', nonDamaging='nonDamaging')

class Move(object): 
    '''class to represent a pokemon move, including all the needed data like type, category, power etc.'''
    def __init__(self, name, description, type, category, power, pp, accuracy):
        '''name, description and type are strings.
        categoryis an Enum, see above.
        power, pp and accuracy are numbers.'''
        self.name = name.title()  # First letters uppercase. Dirty fix. TODO Might not work for U-turn
        self.description = description
        self.type = type
        self.category = category
        self.power = power
        self.pp = pp
        self.accuracy = accuracy
        self.priority = getPriority(self)
        self.visuable = isVisuable(self)
        self.minMaxHits = getMinMaxHits(self)
        self.anomaly = getAnomaly(self)  # None, or a MoveAnomaly Enum, whose value is a message to be displayed.
                                        # Can also be empty string for a regular "read description" notice.
       
    def disable(self):
        self.power = -1
        
    def isDisabled(self):
        return self.power != None and self.power < 0
     
    def isPunchingMove(self):
        return self.name in ['Bullet Punch',
                             'Comet Punch',
                             'Dizzy Punch',
                             'Drain Punch',
                             'Dynamic Punch',
                             'Fire Punch',
                             'Focus Punch',
                             'Hammer Arm',
                             'Ice Punch',
                             'Mach Punch',
                             'Mega Punch',
                             'Meteor Mash',
                             'Power-Up Punch',
                             'Shadow Punch',
                             'Sky Uppercut',
                             'Thunder Punch']
    
    def isSoundMove(self):
        return self.name in ['Boomburst',
                             'Bug Buzz',
                             'Chatter',
                             'Confide',
                             'Disarming Voice',
                             'Echoed Voice',
                             'Grass Whistle',
                             'Growl',
                             'Heal Bell',
                             'Hyper Voice',
                             'Metal Sound',
                             'Noble Roar',
                             'Parting Shot',
                             'Perish Song',
                             'Relic Song',
                             'Roar',
                             'Round',
                             'Screech',
                             'Shadow Panic',
                             'Sing',
                             'Snarl',
                             'Snore',
                             'Supersonic',
                             'Uproar' ]
    
    def isOHKOMove(self):
        return self.name in ['Fissure',
                             'Guillotine',
                             'Horn Drill',
                             'Sheer Cold']

    def isSwitchMove(self):
        return self.name in ['Roar',
                             'Whirlwind',
                             'Dragon Tail',
                             'Circle Throw']

    def isSleepMove(self):
        return self.name in ['Dark Void',
                             'Grass Whistle',
                             'Hypnosis',
                             'Lovely Kiss',
                             'Sing',
                             'Sleep Powder',
                             'Spore',
                             'Yawn']
    def isRecoilMove(self):
        return self.name in ['Brave Bird',
                             'Double-Edge',
                             'Flare Blitz',
                             'Head Charge',
                             'Head Smash',
                             'High Jump Kick',
                             'Jump Kick',
                             'Submission',
                             'Take Down',
                             'Volt Tackle',
                             'Wood Hammer',
                             'Wild Charge']
        
    def isOppStatLowering(self):
        return self.name in ['Metal Sound',
                             'Captivate',
                             'Charm',
                             'Cotton Spore',
                             'Sand Attack',
                             'Scary Face',
                             'Screech',
                             'Fake Tears',
                             'Feather Dance',
                             'Smokescreen',
                             'Flash',
                             'String Shot',
                             'Growl',
                             'Sweet Scent',
                             'Tail Whip',
                             'Tickle',
                             'Kinesis',
                             'Leer',
                             'Memento']
        
    def isStatusConditionMove(self):
        return self.name in ['Glare',
                             'Poison Gas',
                             'Poison Powder',
                             'Stun Spore',
                             'Thunder Wave',
                             'Toxic',
                             'Will-O-Wisp',
                             'Yawn']
    def isWeatherChangingMove(self):
        return self.name in ['Sunny Day',
                             'Rain Dance',
                             'Sandstorm',
                             'Hail']

