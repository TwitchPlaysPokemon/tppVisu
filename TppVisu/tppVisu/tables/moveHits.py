'''
Created on 28.04.2015

@author: Felk
'''

tableMoveHits = {
    'Arm Thrust'  : (2, 5),
    'Barrage'     : (2, 5),
    'Bone Rush'   : (2, 5),
    'Bonemerang'  : (2, 2),
    'Bullet Seed' : (2, 5),
    'Comet Punch' : (2, 5),
    'Double Hit'  : (2, 2),
    'Double Kick' : (2, 2),
    'Double Slap' : (2, 5),
    'Fury Attack' : (2, 5),
    'Fury Swipes' : (2, 5),
    'Double Slap' : (2, 5),
    'Icicle Spear': (2, 5),
    'Pin Missile' : (2, 5),
    'Rock Blast'  : (2, 5),
    'Spike Cannon': (2, 5),
    'Triple Kick' : (1, 3),
    'Twineedle'   : (2, 2),
}

def getMinMaxHits(move):
    try:
        return tableMoveHits[move.name]
    except KeyError:
        return (1, 1)
