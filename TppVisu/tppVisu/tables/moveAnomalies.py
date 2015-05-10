'''
Created on 08.05.2015

@author: Felk
'''

from enum import Enum

# also crash damage moves
recoiling = ['Take Down',
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

leeching = ['Drain Punch',
            'Leech Life',
            'Absorb',
            'Giga Drain',
            'Mega Drain']

selfdestructing = ['Explosion', 'Self-Destruct','Selfdestruct']

lasting_two_turns = ['Fly',
                     'Giga Impact',
                     'Rock Wrecker',
                     'Sky Attack',
                     'Blast Burn',
                     'Frenzy Plant',
                     'Hydro Cannon',
                     'Hyper Beam',
                     'Roar of Time',
                     'Solar Beam',
                     'Skull Bash',
                     'Shadow Force',
                     'Razor Wind']

power_doubling = ['Assurance',
                  'Avalanche',
                  'Payback',
                  'Revenge']

class MoveAnomaly(Enum):
    recoiling         = 'recoiling'
    leeching          = 'leeching'
    selfdestructing   = 'selfdestructing'
    lasting_two_turns = 'lasting 2 turns'
    power_doubling    = 'lower damage displayed'
    
def getAnomaly(move):
    if   move.name in recoiling:         return MoveAnomaly.recoiling
    elif move.name in leeching:          return MoveAnomaly.leeching
    elif move.name in selfdestructing:   return MoveAnomaly.selfdestructing
    elif move.name in lasting_two_turns: return MoveAnomaly.lasting_two_turns
    elif move.name in power_doubling:    return MoveAnomaly.power_doubling
    return None
