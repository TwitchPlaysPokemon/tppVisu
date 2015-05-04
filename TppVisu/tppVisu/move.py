'''
Created on 29.04.2015

@author: Felk
'''
from enum import Enum

from tppVisu.tables.moveHits import getMinMaxHits
from tppVisu.tables.movePriorities import getPriority
from tppVisu.tables.moveVisuables import isVisuable


class MoveCategory(Enum):
    physical = 1
    special = 2
    nonDamaging = 3

class Move(object): 
    def __init__(self, name, description, type, category, power, pp, accuracy):
        self.name        = name
        self.description = description
        self.type        = type
        self.category    = category
        self.power       = power
        self.pp          = pp
        self.accuracy    = accuracy
        self.priority    = getPriority(self)
        self.visuable    = isVisuable(self)
        self.minHits, self.maxHits = getMinMaxHits(self)
       
    def disable(self):
        self.power = -1
        
    def isDisabled(self):
        return self.power < 0
     
    def isSelfdestructingMove(self):
        return self.name in ['Explosion',
                             'Self-Destruct']

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
    
    def isRecoilMove(self):  # also crash damage moves
        return self.name in ['Take Down',
                             'Double-Edge',
                             'Submission',
                             'Volt Tackle',
                             'Flare Blitz',
                             'Brave Bird',
                             'Wood Hammer',
                             'Head Smash',
                             'Wild Charge',
                             'Head Charge',
                             'Shadow Rush',
                             'Shadow End',
                             'Jump Kick',
                             'High Jump Kick',
                             'Hi Jump Kick']
    
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
                             'Sport',
                             'Yawn']

