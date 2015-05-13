'''
Created on 08.05.2015

@author: Felk

This module is needed to infer move-notice-strings for moves with notable anomalous behaviours at Move-object-creation.
'''
from __future__ import division

#from enum import Enum
from tppVisu.util import enum

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

health_dependend = ['Eruption',
                    'Brine',
                    'Water Spout']

special_powerrange = ['Flail',
                      'Reversal',
                      'Trump Card',
                      'Wring Out',
                      'Spit Up',
                      'Crush Grip']

round_dependend = ['Fury Cutter',
                   'Rollout']

# no special display message. Just force a highlight on this move.
others = ['Dream Eater',
          'Future Sight',
          'Present',
          'Wake-Up Slap',
          'Focus Punch',
          'Last Resort',
          'U-Turn']

MoveAnomaly = enum(recoiling          = 'recoiling',
                   leeching           = 'leeching',
                   selfdestructing    = 'selfdestructing',
                   lasting_two_turns  = 'lasting 2 turns',
                   power_doubling     = 'lower damage displayed',
                   health_dependend   = 'full health assumed.',
                   special_powerrange = 'full power range displayed',
                   round_dependend    = 'first round displayed',
                   other              = '')
#class MoveAnomaly(Enum):
#    recoiling          = 'recoiling'
#    leeching           = 'leeching'
#    selfdestructing    = 'selfdestructing'
#    lasting_two_turns  = 'lasting 2 turns'
#    power_doubling     = 'lower damage displayed'
#    health_dependend   = 'full health assumed.'
#    special_powerrange = 'full power range displayed'
#    round_dependend    = 'first round displayed'
#    other              = ''
    
def getAnomaly(move):
    if   move.name in recoiling:          return MoveAnomaly.recoiling
    elif move.name in leeching:           return MoveAnomaly.leeching
    elif move.name in selfdestructing:    return MoveAnomaly.selfdestructing
    elif move.name in lasting_two_turns:  return MoveAnomaly.lasting_two_turns
    elif move.name in power_doubling:     return MoveAnomaly.power_doubling
    elif move.name in health_dependend:   return MoveAnomaly.health_dependend
    elif move.name in special_powerrange: return MoveAnomaly.special_powerrange
    elif move.name in round_dependend:    return MoveAnomaly.round_dependend
    elif move.name in others:             return MoveAnomaly.other
    return None
