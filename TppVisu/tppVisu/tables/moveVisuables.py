'''
Created on 01.05.2015

@author: Felk
'''

tableNotVisuables = ['Bide',
                     'Counter',
                     'Crush Grip',
                     'Endeavor',
                     'Hidden Power', # (for fe1k.de db) there are separate moves for each hidden power type. Use those.
                     'Mirror Coat',
                     'Nature Power',
                     'Super Fang',
                     'Sleep Talk',
                     'Me First',
                     'Beat Up',
                     'Metal Burst',
                     'Doom Desire'
                    ]

def isVisuable(move):
    return move.name not in tableNotVisuables
