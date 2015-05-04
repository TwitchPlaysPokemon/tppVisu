'''
Created on 29.04.2015

@author: Felk
'''

tableMovePriorities = {
    'Helping Hand' :  5,
    'Magic Coat'   :  4,
    'Snatch'       :  4,
    'Detect'       :  3,
    'Endure'       :  3,
    'Follow Me'    :  3,
    'Protect'      :  3,
    'Feint'        :  2,
    'Aqua Jet'     :  1,
    'Bide'         :  1,
    'Bullet Punch' :  1,
    'Extreme Speed':  1,
    'Fake Out'     :  1,
    'Ice Shard'    :  1,
    'Mach Punch'   :  1,
    'Quick Attack' :  1,
    'Shadow Sneak' :  1,
    'Sucker Punch' :  1,
    'Vacuum Wave'  :  1,
    'Vital Throw'  : -1,
    'Focus Punch'  : -3,
    'Avalanche'    : -4,
    'Revenge'      : -4,
    'Counter'      : -5,
    'Mirror Coat'  : -5,
    'Roar'         : -6,
    'Whirlwind'    : -6,
    'Trick Room'   : -7,
}

def getPriority(move):
    try:
        return tableMovePriorities[move.name]
    except KeyError:
        return 0
